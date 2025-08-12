```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_170.jpeg
document_name: DocIo
page_number: 170
page_id: DocIo#page_170
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:38:27Z
fidelity: lossless
--> 

# Essential DocIO

## Overview
- Explains the restrictions for the GetBookmarkContent method.
- Discusses exceptional cases where the method raises an error.
- Provides illustrative examples using figures to represent bookmark behavior.

## Content

### Restriction 3

#### Example Scenario
The following diagram illustrates the placement of bookmarks within a document:

```plaintext
Figure 60: GetBookmarkContent method - Restriction 3
```
The bookmark starts and ends are placed as follows:
- **Bookmark Start** is located within the table.
- **Bookmark End** is also within the same table.

#### Exception
The following exception is raised by the GetBookmarkContent method for all the preceding cases:
- "Bookmark Start and Bookmark End located inside different contents".

### Restriction 4

#### Example Scenario
The following diagram illustrates a more complex scenario involving multiple bookmarks:

```plaintext
Figure 61: GetBookmarkContent method - Restriction 4
```
The diagram shows two bookmarks:
- **Start Bookmark1** and **End Bookmark1**, placed within the same content.
- **Start Bookmark2** and **End Bookmark2**, placed in separate content areas.

The diagram also includes text placed before and after the bookmarks for context.

#### Exception
For such cases, the GetBookmarkContent method may raise exceptions based on the placement of bookmarks.

## API Reference
- **Namespace**: Likely related to `EssentialDocIO` or a similar SDK namespace.
- **Members Involved**: GetBookmarkContent method.
- **Parameters**:
  - Start Bookmark
  - End Bookmark
- **Returns**: Content between the specified bookmarks.
- **Exceptions**:
  - "Bookmark Start and Bookmark End located inside different contents".

## Figures

### Figure 60: GetBookmarkContent method - Restriction 3
This figure illustrates a basic case of bookmark placement within a table structure:
```plaintext
- Text above the table
- Text inside cell
- Text inside the cell of second row
```
The bookmark start and end are located within the same table, ensuring consistent content placement.

### Figure 61: GetBookmarkContent method - Restriction 4
This figure depicts a more intricate case involving overlapping or disjoint bookmark placements:
```plaintext
- Start Bookmark1 and End Bookmark1 within the same content area.
- Start Bookmark2 and End Bookmark2 across different content areas.
```
This demonstrates the complexity in handling bookmarks that span or overlap different content sections.

<!-- tags: [docio, bookmarks, getbookmarkcontent, exceptions, syncfusion, winforms] keywords: [bookmark placement, content overlap, method restrictions, exception handling] -->
```