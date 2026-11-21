import re
import zipfile
from pathlib import Path

base = Path(r"c:\Users\hp\Desktop\ML-ATLAS")
zip_path = base / "sources" / "original-zip" / "100 Days of Machine Learning _ CampusX.zip"
extract_dir = base / "sources" / "extracted" / "100 Days of Machine Learning _ CampusX"
transcript_dir = extract_dir / "transcripts"

if not zip_path.exists():
    raise FileNotFoundError(f"ZIP not found: {zip_path}")
if not extract_dir.exists():
    raise FileNotFoundError(f"Extracted directory not found: {extract_dir}")

with zipfile.ZipFile(zip_path, 'r') as zf:
    zip_names = zf.namelist()

zip_text_files = sorted(n for n in zip_names if n.lower().endswith('.txt'))
zip_other_files = sorted(n for n in zip_names if not n.lower().endswith(('.txt', '.pdf')))

transcript_files = sorted(p.name for p in transcript_dir.glob('*.txt')) if transcript_dir.exists() else []
transcript_paths = sorted(p for p in transcript_dir.glob('*.txt')) if transcript_dir.exists() else []

# parse numbers
pattern = re.compile(r"^(\d+)")
zip_lessons = []
for name in zip_text_files:
    m = pattern.search(Path(name).name)
    zip_lessons.append(int(m.group(1)) if m else None)

extract_lessons = []
for name in transcript_files:
    m = pattern.search(name)
    extract_lessons.append(int(m.group(1)) if m else None)

missing_in_zip = sorted(set(range(1, 135)) - set(n for n in zip_lessons if n is not None))
missing_in_extracted = sorted(set(range(1, 135)) - set(n for n in extract_lessons if n is not None))
zip_missing_names = [name for name in zip_text_files if pattern.search(Path(name).name) is None]
extract_missing_names = [name for name in transcript_files if pattern.search(name) is None]

# duplicate check
zip_counts = {}
for name in zip_text_files:
    key = Path(name).name
    zip_counts[key] = zip_counts.get(key, 0) + 1
zip_duplicates = sorted(k for k, v in zip_counts.items() if v > 1)

extract_counts = {}
for name in transcript_files:
    extract_counts[name] = extract_counts.get(name, 0) + 1
extract_duplicates = sorted(k for k, v in extract_counts.items() if v > 1)

# readability check
unreadable = []
for path in transcript_paths:
    try:
        data = path.read_bytes()
        if not data:
            unreadable.append((path.name, 'empty file'))
        else:
            data.decode('utf-8', errors='strict')
    except Exception as exc:
        unreadable.append((path.name, f'{type(exc).__name__}: {exc}'))

# title parse helper
name_map = {}
for name in transcript_files:
    base_name = name[:-4]
    if re.match(r'^\d+\s*-', base_name):
        title = base_name.split(' - ', 2)[2] if ' - ' in base_name else ''
    else:
        title = base_name
    name_map[name] = title

# summary
summary = {
    'zip_path': str(zip_path),
    'extract_dir': str(extract_dir),
    'zip_entry_count': len(zip_names),
    'zip_text_count': len(zip_text_files),
    'zip_other_count': len(zip_other_files),
    'extracted_transcript_count': len(transcript_files),
    'missing_lesson_numbers_in_zip': missing_in_zip,
    'missing_lesson_numbers_in_extracted': missing_in_extracted,
    'zip_duplicates': zip_duplicates,
    'extract_duplicates': extract_duplicates,
    'unreadable_transcripts': unreadable,
    'known_unavailable_lessons': [87, 89],
}

print(json := __import__('json').dumps(summary, indent=2))
print('\nZIP FILES:')
for item in zip_names:
    print(item)
print('\nEXTRACTED TRANSCRIPTS:')
for item in transcript_files:
    print(item)
