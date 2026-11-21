# CampusX ML Atlas --- Project Handoff

**Handoff date:** 21 November 2026\
**Last confirmed audit:** 31 October 2026\
**Important:** A later Codex PDF was shared through Google Drive but
could not be retrieved in this chat. Its findings and any subsequent
fixes are therefore unverified. Claude must inspect the current
workspace before relying on this historical baseline.

## Project goal

Continue a source-traceable English machine-learning learning resource
built from CampusX lesson transcripts. The intended output is a
high-quality set of lesson Markdown files and a synchronized HTML
learning site.

The resource should preserve the instructor's actual explanations,
sequence, examples, equations, code, and emphasis while improving
clarity and organization. It should be useful for serious self-study and
revision, not merely look complete.

## Last known inventory

The 31 October 2026 audit reported: - 134 lesson records in the
manifest. - 132 available transcript text files. - Lessons 087 and 089
marked `no_captions`. - 132 numbered Markdown lessons and 132 HTML
articles, excluding 087 and 089. - Original ZIP absent during that
audit, so parity against the ZIP was not verified. - Lesson 037 had a
broken transcript reference: Markdown reportedly used
`Missing Category Imputation.txt`, while the actual manifest/transcript
filename was `Missing Category Imp.txt`.

Recount the current workspace. These are historical findings, not proof
of the current state.

## Last known content audit

The audit was a pilot, not a full audit.

### Lessons 001--010

Titles/topics and references broadly matched. Central concepts were
generally represented, but exhaustive transcript coverage was not
established.

### Lessons 081--094 --- high-risk findings to re-check

  -----------------------------------------------------------------------
  Lesson                  Topic                   Reported issue
  ----------------------- ----------------------- -----------------------
  081                     Logistic-regression     Generic regression loss
                          hyperparameters         and array-shape code

  082                     Conditional probability Source example omitted
                          / dice                  

  083                     Independent events      Confused with Naive
                                                  Bayes feature
                                                  independence

  084                     Mutually exclusive      Generic content;
                          events                  transcript reportedly
                                                  short/garbled

  085                     Bayes' theorem          Generic content instead
                                                  of lesson-specific
                                                  derivation/example

  086                     Factory/machine defect  Source example omitted
                          example                 

  088                     Naive Bayes derivation  Generic boilerplate

  090                     Numerical Naive Bayes   Generic code instead of
                                                  numerical walkthrough

  091                     K-nearest neighbours    Generic boilerplate

  092                     SVM geometry            Generic content instead
                                                  of geometric
                                                  explanation

  093                     Hard-margin             Inadequate optimization
                          optimization            treatment

  094                     Soft-margin SVM         Missing slack-variable
                                                  / C-parameter
                                                  explanation
  -----------------------------------------------------------------------

Claude must read each actual transcript and current lesson before
deciding whether these issues remain. Do not infer missing details from
this table.

### Not yet audited

Lessons 011--080 and 095--134 had not been content-audited in the pilot.
Lessons 001--010 were only broadly checked.

## Last known HTML / QA findings

The pilot reported 132 static articles/navigation links and visible
controls, but no browser execution, build/runtime, or JavaScript
interaction tests. All articles had a blanket "Source-aligned CampusX
lesson" style label, which overclaimed alignment while content review
was incomplete.

Verify the current implementation. File counts and static inspection are
not proof of runtime functionality.

## Existing documentation to locate

Prior context mentioned: - `README` - `PROJECT_PROGRESS` -
`CONTENT_COVERAGE` - `CHANGELOG` - `COMPLETE_SOURCE_INVENTORY`

Confirm actual filenames and contents. Locate the transcript directory,
manifest, Markdown lessons, HTML output, build scripts, and test
configuration. Do not guess paths.

## Source-grounding rules

1.  Treat the transcript as the primary authority for what the
    instructor said.
2.  Read the complete relevant transcript before rewriting a lesson.
3.  Preserve source examples, definitions, sequence, and important
    caveats.
4.  Separate transcript-derived material from additional clarification.
    Label additions clearly.
5.  Never fabricate instructor statements, quotes, examples, formulas,
    code, or topics.
6.  If a transcript is missing, corrupted, or unclear, document the
    limitation; do not silently fill gaps from general ML knowledge.
7.  Check all mathematics, assumptions, notation, and code for
    correctness and relevance.
8.  Avoid generic boilerplate repeated across unrelated lessons.
9.  Do not call a lesson source-aligned until it has been checked
    against its transcript.
10. Validate source filenames and paths against the real
    manifest/filesystem.

## Recommended continuation

### Phase A --- Reconnaissance

-   Map the project tree and identify canonical sources, outputs,
    scripts, and build commands.
-   Read existing project documentation and audit reports.
-   Recount transcripts, manifest records, Markdown lessons, HTML
    articles, and navigation entries.
-   Check whether the original ZIP is now available.
-   Produce a factual baseline report before edits.

### Phase B --- Priority repairs

-   Audit 081--094 transcript-by-transcript.
-   Repair only confirmed inaccuracies, omissions, generic filler, or
    unsupported material.
-   Verify and fix lesson 037's transcript reference if still incorrect.
-   Update progress, coverage, and changelog.

### Phase C --- Full content audit

-   Audit 011--080 and 095--134.
-   Re-check 001--010 and 081--094 after repairs.
-   Track per lesson: transcript availability, title/topic match,
    concept coverage, examples, equations, code, source path,
    unsupported claims, and Markdown/HTML consistency.
-   Use honest statuses: `PASS`, `NEEDS_REVISION`, `SOURCE_UNAVAILABLE`,
    or `BLOCKED`.

### Phase D --- HTML and functional QA

-   Build using the documented project process.
-   Run available lint, type, unit, and build checks.
-   Test navigation, search, filters, theme, copy controls, code blocks,
    responsive layout, and visible controls in a browser if tooling
    permits.
-   Record tests actually run. Do not claim browser QA if it was
    unavailable.

### Phase E --- Handoff

Update existing README/progress/coverage/changelog/source-inventory
files. Report counts, audited status totals, repairs, unresolved gaps,
tests and exact outcomes, files changed, and commands to reproduce the
build.

## Definition of done

-   All 132 available transcript-backed lessons have been checked
    against their sources.
-   Lessons 087 and 089 are documented as unavailable unless transcripts
    are later found.
-   Source references resolve correctly.
-   Lessons contain topic-specific, transcript-faithful explanations
    rather than generic filler.
-   Equations and code are technically checked.
-   Markdown and HTML are synchronized.
-   Build and functional QA results are honestly recorded.
-   Documentation reflects actual completion and remaining limitations.

**Prioritize source fidelity and correctness over speed or an impressive
completion report.**
