```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_652.jpeg
document_name: grid
page_number: 652
page_id: grid#page_652
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:31:16Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview

- Illustration of ListChange Performance with Syncfusion Essential Grid interface.
- Focus on High Frequency Updates and mechanisms for managing data changes dynamically.
- Details on sorting, insertion, deletion, and highlighting in response to data changes.

## Content

### 4.3.4.1.3 High Frequency Updates

This section discusses an example that lets you make high frequency updates in an efficient manner. It shows sort position changes, inserting and removing of records from a timer event. At start up, the grid grouping control is sorted by Column "1" and changes to fields in that column affect the sort position of a record. Also, the background colors of the cells in records are dependent on the value in column "1". This dependency is specified with the `ReferencedFields` property. The changes are highlighted for a short period of time after a change was detected.

#### ReferencedFields Property

The `ReferencedFields` property, as the name implies, saves a list of field names referred by a given field. The engine will use these fields in the `ListChanged` event to determine which cells to update when a change was made in an underlying field.

## Figure: ListChange Performance

**Figure 267: ListChange Performance**

The figure demonstrates the functionality of the Syncfusion Essential Grid, showing how caption bars with total summaries are updated manually upon `ListChanges`, as indicated by the annotations. Additionally, it highlights how column values can dynamically change, visualized by the dynamic changes in background colors and the highlighting of modified fields.

## API Reference (if applicable)

- **ReferencedFields Property**  
  - **Description**: Saves a list of field names referred by a given field.
  - **Usage**: Used by the engine in the `ListChanged` event to determine which cells need updating when a change occurs in an underlying field.
  - **Parameters**:
    - None.
  - **Returns**: A list of field names as a dependency.
  - **Exceptions**:
    - None specifically noted.

## RAG Annotations
<!-- tags: [Syncfusion, Winforms, grid, EssentialGrid, ReferencedFields, listchange, highfrequencyupdates] keywords: [ListChange Performance, CaptionBars, ManualTotalSummaries, TotalSummaries, HighFrequencyUpdates, ReferencedFields Property, ListChanged event, Sorted Columns, Dynamic Highlighting] -->
```