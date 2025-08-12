```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_633.jpeg
document_name: grid
page_number: 633
page_id: grid#page_633
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:28:46Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Content

### Overview
- LogWindow shows optimizations for Grid Grouping control when sorting is applied.
- Both Virtual Mode and WithoutCounter optimizations are disabled as shown in the figure.

#### Figure 266: LogWindow displays Optimizations for Grid Grouping control with Sorting Applied
(Both Virtual Mode and WithoutCounter optimizations disabled)
![Figure 266: LogWindow displays Optimizations for Grid Grouping control with Sorting Applied](https://example.com/figure266.png)

#### 4.3.4.1.2 ListChanged Performance
When a ListChange is detected, the grouping engine must update the grid records accordingly. Each record change may affect its sort position, group dependency, and summaries. The engine should handle all these updates and invalidate counters related to the ListChange. The simplest approach is to invalidate the whole display and repaint all rows, but this can negatively impact performance, especially in scenarios where only a single record is changed without affecting sort order or summaries. In such cases, the engine should ideally repaint only the affected record, instead of the entire display.

GridEngine offers options to handle this by tracking which expression fields and summary columns depend on changes to specific fields. This allows it to identify fields affecting group dependency or sort position. Based on these dependencies, GridEngine can choose the most efficient method to update its internal object and manage ListChanged events.

### Example

---

## API Reference

## Code Examples

## Page-level Navigation/TOC

## Cross References

See also:
- Virtual Mode
- WithoutCounter optimizations
- Grid Grouping
- ListChanged events
- GridEngine

### RAG Annotations
<!-- tags: [grid, essential grid, windows forms, listchanged performance, grid grouping, optimizations, virtual mode, withoutcounter] keywords: [logwindow, sorting, performance, grid engine, listchanged events, grouping, expressions, summary columns] -->
```