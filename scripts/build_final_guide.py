from __future__ import annotations

from dataclasses import dataclass
from html import escape
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
CONTENT_DIR = ROOT / "content"
DIST_DIR = ROOT / "dist"
OUTPUT_FILE = DIST_DIR / "ML-Atlas.html"

LESSON_PATTERN = re.compile(r"^(\d{3})-(.+)\.md$")
INLINE_MATH_PATTERN = re.compile(r"\$(.+?)\$")


@dataclass
class Lesson:
    number: int
    slug: str
    title: str
    module: str
    markdown: str
    html: str


def module_for_lesson(number: int) -> str:
    if 1 <= number <= 16:
        return "Foundations"
    if 17 <= number <= 46:
        return "Data and Feature Engineering"
    if 47 <= number <= 60:
        return "PCA and Regression Core"
    if 61 <= number <= 80:
        return "Regularization and Logistic Regression"
    if 81 <= number <= 100:
        return "Naive Bayes, KNN, SVM, Trees"
    if 101 <= number <= 120:
        return "Ensemble Methods"
    return "Advanced Ensemble, Clustering, Tuning"


def apply_inline_markup(text: str) -> str:
    out = escape(text)
    out = re.sub(r"`([^`]+)`", lambda m: f"<code>{escape(m.group(1))}</code>", out)
    out = INLINE_MATH_PATTERN.sub(lambda m: f"<span class=\"math-inline\">{escape(m.group(1))}</span>", out)
    return out


def markdown_to_html(md: str) -> str:
    lines = md.splitlines()
    html_parts: list[str] = []

    in_code = False
    code_lang = ""
    code_buffer: list[str] = []
    in_ul = False
    in_ol = False
    in_math_block = False
    math_buffer: list[str] = []
    expect_output_block = False

    def close_lists() -> None:
        nonlocal in_ul, in_ol
        if in_ul:
            html_parts.append("</ul>")
            in_ul = False
        if in_ol:
            html_parts.append("</ol>")
            in_ol = False

    def close_code() -> None:
        nonlocal in_code, code_buffer, code_lang, expect_output_block
        block = "\n".join(code_buffer)
        cls = "code-block expected-output" if expect_output_block else "code-block"
        language_attr = f' data-language="{escape(code_lang)}"' if code_lang else ""
        html_parts.append(
            f'<div class="{cls}">'
            f'<button class="copy-btn" type="button">Copy</button>'
            f'<pre><code{language_attr}>{escape(block)}</code></pre>'
            "</div>"
        )
        in_code = False
        code_buffer = []
        code_lang = ""
        expect_output_block = False

    def normalize_math_text(text: str) -> str:
        # Some earlier generated markdown used \t escapes in LaTeX, which became tab characters.
        return text.replace("\t", "\\t")

    for raw in lines:
        line = raw.rstrip("\n")
        stripped = line.strip()

        if stripped == "$$":
            close_lists()
            if in_code:
                code_buffer.append(line)
                continue
            if in_math_block:
                math_content = normalize_math_text("\n".join(math_buffer))
                html_parts.append(f'<div class="math-block">{escape(math_content)}</div>')
                in_math_block = False
                math_buffer = []
            else:
                in_math_block = True
                math_buffer = []
            continue

        if in_math_block:
            math_buffer.append(line)
            continue

        if stripped.startswith("```"):
            close_lists()
            if in_code:
                close_code()
            else:
                in_code = True
                code_lang = stripped[3:].strip()
            continue

        if in_code:
            code_buffer.append(line)
            continue

        if not stripped:
            close_lists()
            continue

        if stripped.lower().startswith("expected output:"):
            close_lists()
            expect_output_block = True
            html_parts.append('<p class="expected-output-label">Expected output:</p>')
            continue

        if stripped.startswith("#"):
            close_lists()
            level = len(stripped) - len(stripped.lstrip("#"))
            level = min(max(level, 1), 6)
            content = stripped[level:].strip()
            html_parts.append(f"<h{level}>{apply_inline_markup(content)}</h{level}>")
            continue

        if stripped.startswith("- "):
            if not in_ul:
                close_lists()
                in_ul = True
                html_parts.append("<ul>")
            html_parts.append(f"<li>{apply_inline_markup(stripped[2:])}</li>")
            continue

        if re.match(r"^\d+\.\s+", stripped):
            if not in_ol:
                close_lists()
                in_ol = True
                html_parts.append("<ol>")
            item = re.sub(r"^\d+\.\s+", "", stripped)
            html_parts.append(f"<li>{apply_inline_markup(item)}</li>")
            continue

        close_lists()
        html_parts.append(f"<p>{apply_inline_markup(stripped)}</p>")

    close_lists()
    if in_code:
        close_code()
    if in_math_block and math_buffer:
      math_content = normalize_math_text("\n".join(math_buffer))
      html_parts.append(f'<div class="math-block">{escape(math_content)}</div>')

    return "\n".join(html_parts)


def extract_title(markdown_text: str, fallback_slug: str, number: int) -> str:
    for line in markdown_text.splitlines():
        if line.strip().startswith("#"):
            heading = line.strip().lstrip("#").strip()
            heading = re.sub(r"^\d+\s+[\-–—]\s*", "", heading).strip()
            return heading if heading else fallback_slug.replace("-", " ").title()
    return fallback_slug.replace("-", " ").title()


def collect_lessons() -> list[Lesson]:
    lessons: list[Lesson] = []
    for path in sorted(CONTENT_DIR.glob("batch-*/*.md")):
        m = LESSON_PATTERN.match(path.name)
        if not m:
            continue
        number = int(m.group(1))
        slug = m.group(2)
        markdown_text = path.read_text(encoding="utf-8")
        title = extract_title(markdown_text, slug, number)
        module = module_for_lesson(number)
        html = markdown_to_html(markdown_text)
        lessons.append(
            Lesson(
                number=number,
                slug=slug,
                title=title,
                module=module,
                markdown=markdown_text,
                html=html,
            )
        )
    lessons.sort(key=lambda x: x.number)
    return lessons


def build_html(lessons: list[Lesson]) -> str:
    available_count = len(lessons)
    unavailable = [87, 89]

    modules: dict[str, list[Lesson]] = {}
    for lesson in lessons:
        modules.setdefault(lesson.module, []).append(lesson)

    sidebar_parts: list[str] = []
    for module_name, module_lessons in modules.items():
        sidebar_parts.append(f'<section class="module-group" data-module="{escape(module_name)}">')
        sidebar_parts.append(f"<h3>{escape(module_name)}</h3>")
        sidebar_parts.append('<ul class="lesson-list">')
        for lesson in module_lessons:
            lesson_id = f"lesson-{lesson.number:03d}"
            search_blob = f"{lesson.number:03d} {lesson.title} {lesson.markdown}".lower()
            sidebar_parts.append(
                "<li "
                f'data-number="{lesson.number:03d}" '
                f'data-module="{escape(module_name.lower())}" '
                f'data-search="{escape(search_blob)}">'
                f'<a href="#{lesson_id}" data-target="{lesson_id}">{lesson.number:03d} - {escape(lesson.title)}</a>'
                "</li>"
            )
        sidebar_parts.append("</ul>")
        sidebar_parts.append("</section>")

    lesson_parts: list[str] = []
    for idx, lesson in enumerate(lessons):
        lesson_id = f"lesson-{lesson.number:03d}"
        active_class = " lesson-active" if idx == 0 else ""
        lesson_parts.append(
            f'<article id="{lesson_id}" class="lesson{active_class}" '
            f'data-number="{lesson.number:03d}" data-module="{escape(lesson.module.lower())}">'
            f'<header class="lesson-header"><h2>{lesson.number:03d} - {escape(lesson.title)}</h2>'
            f'<p class="lesson-meta">Module: {escape(lesson.module)} | Source-aligned CampusX lesson</p></header>'
            f"{lesson.html}</article>"
        )

    module_options = [
        '<option value="all">All Modules</option>'
    ] + [f'<option value="{escape(name.lower())}">{escape(name)}</option>' for name in modules.keys()]

    html = """<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>ML Atlas - CampusX Transcript Guide</title>
  <style>
    :root {{
      --bg: #0f1418;
      --panel: #192229;
      --panel-alt: #22303a;
      --text: #e6edf3;
      --muted: #9bb0be;
      --accent: #3ecf8e;
      --accent-2: #ffb84d;
      --border: #2f3e49;
      --code-bg: #0c1115;
      --print-text: #111;
      --font-ui: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
      --font-code: Consolas, "Courier New", monospace;
    }}

    * {{ box-sizing: border-box; }}

    body {{
      margin: 0;
      background: radial-gradient(circle at 10% 10%, #1b2a33 0%, var(--bg) 55%);
      color: var(--text);
      font-family: var(--font-ui);
      line-height: 1.6;
    }}

    .shell {{
      display: grid;
      grid-template-columns: 320px 1fr;
      min-height: 100vh;
    }}

    .sidebar {{
      border-right: 1px solid var(--border);
      background: linear-gradient(180deg, var(--panel) 0%, #121a20 100%);
      padding: 1rem;
      position: sticky;
      top: 0;
      height: 100vh;
      overflow: auto;
    }}

    .brand h1 {{
      margin: 0;
      font-size: 1.35rem;
      letter-spacing: 0.2px;
    }}

    .brand p {{
      margin: 0.35rem 0 1rem;
      color: var(--muted);
      font-size: 0.9rem;
    }}

    .stats {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 0.5rem;
      margin-bottom: 1rem;
    }}

    .stat {{
      background: var(--panel-alt);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 0.55rem;
      font-size: 0.84rem;
    }}

    .stat strong {{ display: block; font-size: 1rem; color: var(--accent); }}

    .controls {{
      display: grid;
      gap: 0.6rem;
      margin-bottom: 0.8rem;
    }}

    .controls input,
    .controls select {{
      width: 100%;
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 0.6rem 0.7rem;
      background: #0d141a;
      color: var(--text);
      font: inherit;
    }}

    .filter-note {{
      color: var(--muted);
      font-size: 0.82rem;
      margin: 0 0 0.6rem;
    }}

    .module-group {{ margin-bottom: 1rem; }}
    .module-group h3 {{
      margin: 0 0 0.45rem;
      font-size: 0.92rem;
      color: var(--accent-2);
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }}

    .lesson-list {{ list-style: none; margin: 0; padding: 0; display: grid; gap: 0.25rem; }}

    .lesson-list li a {{
      color: var(--text);
      text-decoration: none;
      display: block;
      padding: 0.38rem 0.48rem;
      border-radius: 7px;
      border: 1px solid transparent;
      font-size: 0.9rem;
    }}

    .lesson-list li a:hover,
    .lesson-list li a.active {{
      background: rgba(62, 207, 142, 0.14);
      border-color: rgba(62, 207, 142, 0.35);
    }}

    .lesson-list li.hidden {{ display: none; }}

    .main {{
      min-width: 0;
      padding: 1.25rem clamp(1rem, 2vw, 2rem);
    }}

    .hero {{
      border: 1px solid var(--border);
      border-radius: 16px;
      background: linear-gradient(135deg, #17303d, #1c252d);
      padding: 1.1rem 1.2rem;
      margin-bottom: 1rem;
    }}

    .hero h2 {{ margin: 0 0 0.35rem; font-size: clamp(1.1rem, 2.5vw, 1.65rem); }}
    .hero p {{ margin: 0; color: var(--muted); }}

    .lesson {{
      display: none;
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 1rem;
      background: rgba(16, 24, 30, 0.92);
      margin-bottom: 1rem;
    }}

    .lesson.lesson-active {{ display: block; }}

    .lesson-header h2 {{ margin: 0; font-size: 1.2rem; }}
    .lesson-meta {{ margin: 0.25rem 0 0.9rem; color: var(--muted); font-size: 0.88rem; }}

    h1, h2, h3, h4 {{ line-height: 1.3; margin-top: 1.05rem; margin-bottom: 0.4rem; }}
    p, li {{ font-size: 0.97rem; }}

    ul, ol {{ padding-left: 1.2rem; }}

    .math-inline {{
      font-family: var(--font-code);
      background: rgba(255, 184, 77, 0.14);
      border: 1px solid rgba(255, 184, 77, 0.28);
      border-radius: 4px;
      padding: 0.05rem 0.25rem;
      white-space: nowrap;
    }}

    .math-block {{
      font-family: var(--font-code);
      white-space: pre-wrap;
      background: rgba(255, 184, 77, 0.1);
      border: 1px solid rgba(255, 184, 77, 0.35);
      border-radius: 8px;
      padding: 0.7rem;
      margin: 0.6rem 0;
      overflow-x: auto;
    }}

    .expected-output-label {{
      margin: 0.55rem 0 0.3rem;
      color: var(--accent-2);
      font-weight: 600;
    }}

    .code-block {{
      position: relative;
      margin: 0.6rem 0;
      border: 1px solid var(--border);
      border-radius: 10px;
      background: var(--code-bg);
      overflow: hidden;
    }}

    .code-block pre {{
      margin: 0;
      padding: 0.9rem 0.85rem;
      overflow-x: auto;
      font-family: var(--font-code);
      font-size: 0.86rem;
      line-height: 1.5;
    }}

    .expected-output pre {{
      background: rgba(62, 207, 142, 0.08);
    }}

    .copy-btn {{
      position: absolute;
      top: 0.35rem;
      right: 0.35rem;
      border: 1px solid var(--border);
      border-radius: 6px;
      font-size: 0.75rem;
      padding: 0.18rem 0.42rem;
      background: #1a232c;
      color: var(--text);
      cursor: pointer;
    }}

    .copy-btn:hover {{ border-color: var(--accent); }}

    @media (max-width: 980px) {{
      .shell {{ grid-template-columns: 1fr; }}
      .sidebar {{
        position: static;
        height: auto;
        border-right: none;
        border-bottom: 1px solid var(--border);
      }}
    }}

    @media print {{
      body {{ background: #fff; color: var(--print-text); }}
      .sidebar, .hero, .copy-btn {{ display: none !important; }}
      .shell {{ display: block; }}
      .main {{ padding: 0; }}
      .lesson {{
        display: block !important;
        page-break-inside: avoid;
        border: none;
        background: #fff;
        margin-bottom: 1rem;
      }}
      .math-block, .math-inline {{
        background: #f5f5f5;
        border-color: #ddd;
      }}
    }}
  </style>
</head>
<body>
  <div class="shell">
    <aside class="sidebar">
      <div class="brand">
        <h1>ML Atlas</h1>
        <p>CampusX transcript-backed guide in original lesson order</p>
      </div>

      <div class="stats">
        <div class="stat"><strong>{available_count}</strong>Available lessons</div>
        <div class="stat"><strong>{", ".join(str(x) for x in unavailable)}</strong>Unavailable</div>
      </div>

      <div class="controls">
        <input id="searchInput" type="search" placeholder="Search lesson title or content" aria-label="Search lessons" />
        <select id="moduleFilter" aria-label="Filter lessons by module">
          {''.join(module_options)}
        </select>
      </div>

      <p id="filterNote" class="filter-note">Showing all lessons</p>
      {''.join(sidebar_parts)}
    </aside>

    <main class="main">
      <section class="hero">
        <h2>Machine Learning Atlas Final Guide</h2>
        <p>This standalone file includes every available CampusX lesson draft from 001 to 134, excluding unavailable no-caption lessons 087 and 089.</p>
      </section>

      {''.join(lesson_parts)}
    </main>
  </div>

  <script>
    const links = Array.from(document.querySelectorAll('.lesson-list a'));
    const items = Array.from(document.querySelectorAll('.lesson-list li'));
    const lessons = Array.from(document.querySelectorAll('.lesson'));
    const searchInput = document.getElementById('searchInput');
    const moduleFilter = document.getElementById('moduleFilter');
    const filterNote = document.getElementById('filterNote');

    function activateLesson(id) {
      lessons.forEach((article) => {
        article.classList.toggle('lesson-active', article.id === id);
      });
      links.forEach((link) => {
        link.classList.toggle('active', link.dataset.target === id);
      });
    }

    function firstVisibleLessonId() {
      const visible = items.find((item) => !item.classList.contains('hidden'));
      if (!visible) return null;
      const link = visible.querySelector('a');
      return link ? link.dataset.target : null;
    }

    function applyFilters() {
      const query = searchInput.value.trim().toLowerCase();
      const moduleValue = moduleFilter.value;
      let shown = 0;

      items.forEach((item) => {
        const hay = item.dataset.search || '';
        const itemModule = item.dataset.module || '';
        const matchSearch = !query || hay.includes(query);
        const matchModule = moduleValue === 'all' || itemModule === moduleValue;
        const visible = matchSearch && matchModule;
        item.classList.toggle('hidden', !visible);
        if (visible) shown += 1;
      });

      if (shown === 0) {
        filterNote.textContent = 'No lessons match the current search/filter.';
        lessons.forEach((article) => article.classList.remove('lesson-active'));
        links.forEach((link) => link.classList.remove('active'));
      } else {
        filterNote.textContent = `Showing ${shown} lesson${shown === 1 ? '' : 's'}`;
        const active = document.querySelector('.lesson.lesson-active');
        if (!active) {
          const fallback = firstVisibleLessonId();
          if (fallback) activateLesson(fallback);
        } else {
          const activeLink = links.find((l) => l.dataset.target === active.id);
          const hidden = activeLink ? activeLink.closest('li').classList.contains('hidden') : true;
          if (hidden) {
            const fallback = firstVisibleLessonId();
            if (fallback) activateLesson(fallback);
          }
        }
      }
    }

    links.forEach((link) => {
      link.addEventListener('click', (event) => {
        event.preventDefault();
        activateLesson(link.dataset.target);
        if (window.innerWidth <= 980) {
          window.scrollTo({ top: 0, behavior: 'smooth' });
        }
      });
    });

    document.querySelectorAll('.copy-btn').forEach((btn) => {
      btn.addEventListener('click', async () => {
        const code = btn.parentElement.querySelector('code');
        if (!code) return;
        const text = code.textContent || '';
        try {
          if (navigator.clipboard && navigator.clipboard.writeText) {
            await navigator.clipboard.writeText(text);
          } else {
            throw new Error('Clipboard API unavailable');
          }
          const prev = btn.textContent;
          btn.textContent = 'Copied';
          setTimeout(() => { btn.textContent = prev; }, 1200);
        } catch (err) {
          try {
            const temp = document.createElement('textarea');
            temp.value = text;
            temp.setAttribute('readonly', '');
            temp.style.position = 'absolute';
            temp.style.left = '-9999px';
            document.body.appendChild(temp);
            temp.select();
            const ok = document.execCommand('copy');
            document.body.removeChild(temp);
            btn.textContent = ok ? 'Copied' : 'Failed';
            setTimeout(() => { btn.textContent = 'Copy'; }, 1200);
          } catch (fallbackErr) {
            btn.textContent = 'Failed';
            setTimeout(() => { btn.textContent = 'Copy'; }, 1200);
          }
        }
      });
    });

    searchInput.addEventListener('input', applyFilters);
    moduleFilter.addEventListener('change', applyFilters);

    const fromHash = location.hash.replace('#', '').trim();
    if (fromHash && document.getElementById(fromHash)) {
      activateLesson(fromHash);
    } else if (lessons.length > 0) {
      activateLesson(lessons[0].id);
    }

    applyFilters();
  </script>
</body>
</html>
"""
    html = html.replace("{available_count}", str(available_count))
    html = html.replace("{\", \".join(str(x) for x in unavailable)}", ", ".join(str(x) for x in unavailable))
    html = html.replace("{''.join(module_options)}", "".join(module_options))
    html = html.replace("{''.join(sidebar_parts)}", "".join(sidebar_parts))
    html = html.replace("{''.join(lesson_parts)}", "".join(lesson_parts))
    html = html.replace("{{", "{").replace("}}", "}")
    return html


def main() -> None:
    lessons = collect_lessons()

    expected_numbers = [n for n in range(1, 135) if n not in (87, 89)]
    found_numbers = [lesson.number for lesson in lessons]
    missing = [n for n in expected_numbers if n not in found_numbers]
    duplicates = sorted({n for n in found_numbers if found_numbers.count(n) > 1})

    if missing:
        raise RuntimeError(f"Missing available lessons: {missing}")
    if duplicates:
        raise RuntimeError(f"Duplicate lesson numbers: {duplicates}")

    html = build_html(lessons)
    DIST_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(html, encoding="utf-8")

    print(f"Wrote {OUTPUT_FILE}")
    print(f"Included lessons: {len(lessons)}")


if __name__ == "__main__":
    main()
