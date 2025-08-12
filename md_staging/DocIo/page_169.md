```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_169.jpeg
document_name: DocIo
page_number: 169
page_id: DocIo#page_169
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:39:01Z
fidelity: lossless
-->

## Bookmarking and Content Retrieval in Word Documents

### Overview
- This page discusses how to extract content between bookmarks using the `GetBookmarkContent` method in the Syncfusion Word Processing API.
- It outlines restrictions associated with retrieving content based on bookmark positions, specifically involving tables and cells.
- Provides examples and visual illustrations of valid and invalid bookmark positions and structures.

### Restrictions on GetBookmarkContent Method

#### Case 1: Bookmark Starts or Ends Across Tables
- The bookmark start is positioned in the text, while the bookmark end is inside a table, or vice versa.
- **Figure 58:** Illustrates the restriction when the bookmark start is above the table and the bookmark end is inside the table.

```markdown
![GetBookmarkContent method - Restriction 1](Figure 58.png)
```

#### Case 2: Bookmarks Across Different Tables
- The bookmark start and bookmark end are positioned inside different tables.
- **Figure 59:** Shows a scenario where the bookmark spans across two separate tables.

```markdown
![GetBookmarkContent method - Restriction 2](Figure 59.png)
```

#### Case 3: Bookmarks Across Different Cells
- The bookmark start and bookmark end are positioned inside different cells.
- This case highlights the restriction when the content to be retrieved spans multiple cells within a table.

### Conclusion
This document outlines the limitations of the `GetBookmarkContent` method in handling bookmarks that overlap or span across tables and cells. It provides visual examples to illustrate the different scenarios where the method may fail or encounter restrictions.

## API Reference

### Methods

#### GetBookmarkContent
- **Description:** Retrieves the content between the bookmark start and bookmark end.
- **Parameters:**
  - `BookmarkName`: The name of the bookmark to retrieve.
- **Returns:** The content as a string or object representing the content between the bookmark start and end.
- **Restrictions:**
  - The bookmark start and end cannot span across different tables or cells.

### Code Examples
- **Example:** Extracting content between bookmarks.
```csharp
DocReader reader = new WordDocumentReader();
WordDocument document = reader.Read("document.docx");
string content = document.GetBookmarkContent("MyBookmark");
```

### Cross References
- Refer to the official Syncfusion documentation for additional details on handling bookmarks and tables in Word documents.

### RAG Annotations
<!-- tags: [Word document, bookmarks, GetBookmarkContent, table, cell, restriction] keywords: [Syncfusion, WinForms, DocIo, Word Processing API, bookmark starts, bookmark ends, table spans, cell spans] -->
```