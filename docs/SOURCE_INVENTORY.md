# Source Inventory

## 1. Primary source archive

The real course transcript set is contained in the original archive:

- Source archive: `sources/original-zip/100 Days of Machine Learning _ CampusX.zip`
- Archived root folder: `100 Days of Machine Learning _ CampusX`
- Transcript folder: `100 Days of Machine Learning _ CampusX/transcripts`
- Manifest files: `manifest.csv` and `manifest.json`

The archive was inspected without modifying the original ZIP file. A temporary extraction was used for analysis only.

## 2. Reference design file

The design reference is:

- `sources/reference/java-complete-guide.html`

This file is a strong example of an educational single-page reference site with:

- dark premium UI
- sticky top search bar
- hero section with course summary
- table of contents
- sectioned learning blocks
- dense concept cards
- code blocks with copy behavior
- emphasis on clarity, reusable examples, and scan-friendly structure
- strong typography and visual hierarchy

### Observed strengths

- Excellent information density without sacrificing readability
- Fast content scanning through section headers and TOC
- Code examples are prominent and reusable
- Search and anchor-based navigation reduce friction
- The page is effectively a structured learning atlas, not a lecture transcript dump

### Observed limitations

- It is a static markdown-like reference, not a deep learning curriculum engine
- It does not model topic dependencies, lesson traceability, or progress tracking
- It is heavily content-dense, but not context-rich for project-based or interview-prep learning
- It does not provide module filters, difficulty filters, bookmarks, or persistent progress
- It lacks explicit source traceability markers for transcript-to-topic mapping
- It does not separate original course material from additional explanations and supplementary topics
- It is single-page and long, which is useful for revision but not ideal for deeper modular learning flows

## 3. Source metadata overview

The manifest data identifies a CampusX playlist titled "100 Days of Machine Learning" and contains 134 lesson entries.

### Key manifest facts

- Total entries: 134
- Fetched transcripts: 132
- No-caption lessons: 2
- Missing lesson numbers: none
- Courses are ordered by `channel_index` and published date
- Transcript files are textual, auto-generated and manually recovered from video captions

### Notable status observations

The manifest shows mixed quality sources:

- Many lessons are labeled `fetched` and have working transcripts
- Some lessons are in Hindi / bilingual / ASR transcripts
- `status = no_captions` appears for lessons 87 and 89, which must remain explicitly marked as unavailable

## 4. Transcript set structure

The extracted transcript folder contains 132 text files, each named with a lesson number and date.

The original course order is preserved in the file names and manifest ordering.

## 5. Inventory summary

| Metric | Value |
| --- | --- |
| Total lesson records | 134 |
| Available transcript files | 132 |
| No-caption / unavailable | 2 |
| Lesson numbers present | 1 to 134 |
| Missing lesson numbers | None |
| Unavailable lesson numbers | 87, 89 |

## 6. Important source-quality caveat

The source material is extremely valuable, but it is not uniformly clean or complete. Some lessons are:

- explained in Hindi, Hinglish, or mixed-language narration
- generated from ASR captions and may contain transcription noise
- not available at all where `no_captions` is recorded
- more tutorial-like than academically formal

This means the final ML Atlas must treat original CampusX content as the source-of-truth while adding separate explanatory layers, cleaner structure, better notation, diagrams, and practice work.

## 7. Recommendation for the final project

The final project should not simply convert the video transcripts into HTML. It should:

1. preserve transcript ordering and title traceability
2. separate original explanations from added educational commentary
3. add mathematical explanation, pseudocode, plots, and Python code
4. insert practice questions and interview notes
5. preserve lesson status metadata for every topic
6. mark unavailable content clearly instead of fabricating it

This makes the project a true educational guide rather than a transcript archive.
