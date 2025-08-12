```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_976.jpeg
document_name: grid
page_number: 976
page_id: grid#page_976
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:53:32Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Summaries

### Overview
- Explains how to add summaries in the designer using the `TableDescriptor.SummaryRows` property.
- Describes the customization options for summary rows and columns, including summary type, format, and calculation based on column values.

### Content

Summaries can be added in the designer itself by accessing the property, `TableDescriptor.SummaryRows` property. You can add as many summary rows as you need, each with a desired number of summary columns where you can specify the type of summary, summary format, the column based on whose values the summary has to be calculated, and the like for each of the summary columns.

#### Figure 368: Sorted Grid showing the SortedColumns Editor
This section introduces the SortedColumns Editor and its features for managing summary rows and columns in the grid.

#### Figure 369: Adding Summary Rows
This figure demonstrates the interface for adding summary rows, where users can customize properties such as `Name`, `Summary Type`, `DataMember`, `Display Column`, and `IgnoreRecordFit`.

##### GridSummaryColumnDescriptor Collection Editor
- **Members**: Lists the summary columns under `Summary 1`.
- **Summary 1 properties**:
  - **Look And Feel**:
    - *Format*: `(Count) Record`
    - *Style*: `FillRow`
    - *Appearance*: `Appearance`
  - **Misc**:
    - *Summary Type*: `Count`
    - *DataMember*: `(Record)`
    - *Display Column*:
    - *IgnoreRecordFit*: `False`
    - *MaxLength*: `23`

##### GridSummaryRowDescriptor Collection Editor
- **Members**: Lists the summary rows under `Row 1`.
- **Row 1 properties**:
  - **Misc**:
    - *Name*: `Row 1`
    - *Visible*: `True`
    - *Title*: `Title`
    - *TitleColumnCount*: `0`
    - *SummaryColumns*: `Count = 1`
    - *Appearance*: `Appearance`

### Related Features
- **Sorted Columns Editor**: Provides an interface to manage the sort order and aggregation settings for the grid's columns.
- **TableDescriptor**: Controls the behavior and appearance of the grid's data table.
- **Child Group Options**: Allows configuration of child groups within the grid.

### Summary Rows Configuration
- **Customizable Summary Types**: Supports various summary calculations, such as count, sum, average, minimum, and maximum.
- **Column Binding**: Enables association of summary columns with specific data members for aggregation.
- **Appearance Control**: Offers styling options for summary rows and columns.

#### See also:
- `TableDescriptor`
- `GridSummaryRowDescriptor`
- `GridSummaryColumnDescriptor`

<!-- tags: [windows forms, grid, summaries, editor, design-time customization, version 11.4.0.26] keywords: [summary rows, summary types, summary format, GridSummaryRowDescriptor, GridSummaryColumnDescriptor, TableDescriptor, SortedColumns Editor] -->
```
