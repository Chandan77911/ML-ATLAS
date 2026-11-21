# Changelog

## 2026-10-30

### Added

- Batch 1 content for lessons 001-008 under `content/batch-1/`
- Lesson-level source traceability for each CampusX transcript
- Beginner, technical, and supplementary explanations for the first 8 lessons
- Practice prompts and small Python examples aligned to the original course flow
- Coverage snapshot in `docs/CONTENT_COVERAGE.md`
- Detailed quality audit at `docs/BATCH_01_AUDIT.md`

### Improved

- Strengthened explanation depth for all lessons 001-008
- Clarified foundational terms such as features, labels, generalization, model, and policy
- Added mathematical intuition for distance-based learning in lesson 006
- Separated lesson 004 and lesson 005 more clearly to avoid conceptual redundancy
- Expanded business-context explanations, misconceptions, and interview questions

### Verified

- Batch 1 covers the original sequence from lessons 001 to 008
- Transcript files used for source traceability are present in the extracted source archive
- No-caption lessons 87 and 89 remain explicitly marked unavailable and are not reconstructed
- The detailed educational audit has been completed and saved in `docs/BATCH_01_AUDIT.md`

### Added

- Batch 2 content for lessons 009-016 under `content/batch-2/`
- Project progress checkpoint at `docs/PROJECT_PROGRESS.md`
- Batch 2 summary file at `content/batch-2/README.md`

### Improved

- Expanded the project workflow and data-ingestion material for lessons 009-016
- Added environment setup guidance and tensor foundations
- Reinforced the practical understanding of real ML project framing and CSV/JSON/SQL workflows

### Verified

- Batch 2 continues in the original transcript order after lesson 008
- Batch 2 files were created and checked for educational consistency
- The next lesson target is 017: Fetching Data From an API

### Added

- Batch 3 extension covering lessons 022-060 under `content/batch-3/`
- Source-aware lesson files for Pandas Profiling, feature engineering, missing-data handling, outliers, PCA, and regression foundations
- Continuation status updates in `docs/PROJECT_PROGRESS.md` and `docs/CONTENT_COVERAGE.md`

### Improved

- Kept the transcript sequence focused on real ML-data work and analysis methods
- Added mathematical intuition, code examples, and practice questions for the extended preprocessing and regression sections
- Continued to preserve source traceability and avoid reconstructing unavailable lessons 87 and 89

### Verified

- Lessons 022-060 were created in the original sequence and aligned to the extracted CampusX transcripts
- The project remains source-traceable and does not invent content for unavailable lessons
- The next target is lesson 061 and beyond in the original transcript order

### Notes

- This batch intentionally stops before final HTML generation, as requested
- The project remains in modular content-development mode
- Work is actively continuing in the original transcript order

## 2026-10-30 (continuation batches 4-7)

### Added

- Batch 4 lesson files for lessons 061-080 under `content/batch-4/`
- Batch 5 lesson files for lessons 081-100 under `content/batch-5/`
- Batch 6 lesson files for lessons 101-120 under `content/batch-6/`
- Batch 7 lesson files for lessons 121-134 under `content/batch-7/`
- Numbered naming for all continuation lessons so they map cleanly to the original transcript sequence

### Improved

- Kept the continuation in source order and preserved the explicit unavailable status for lessons 087 and 089
- Unified the lesson numbering for all post-060 batches to match the CampusX archive from 061 onward
- Updated project coverage notes to reflect the remaining available lesson coverage across all continuation batches

### Verified

- The generated continuation files cover lessons 061-134 excluding 087 and 089
- The lesson set is grouped in consistent batch folders and remains traceable to the transcript titles and file names
- The project remains source-first and does not invent missing/no-caption lessons

### Notes

- This marks the end of the transcript-backed content generation phase for the available CampusX archive
- Final HTML build, browser validation, and site QA remain as the last project milestone

## 2026-10-31 (final assembly and validation)

### Added

- Final standalone guide assembled at `dist/ML-Atlas.html`
- Responsive layout, print stylesheet, lesson navigation, search/filter controls, and code-copy buttons in the final output

### Improved

- Normalized equation rendering artifacts caused by escaped tab sequences in generated markdown
- Added robust clipboard copy fallback for code blocks in the standalone guide

### Verified

- Every available transcript lesson is represented in the final guide: 132 lessons included
- Lessons 087 and 089 remain explicitly unavailable due to missing captions and are not reconstructed
- Lesson ordering and link-target integrity validated across all rendered lesson sections
- Search and module filtering validated directly in browser on the generated HTML file

### Notes

- Final browser checks were run on the local file build using the integrated browser tooling
- This milestone completes final assembly for the transcript-backed lesson set
