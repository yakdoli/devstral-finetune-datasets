```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_753.jpeg
document_name: grid
page_number: 753
page_id: grid#page_753
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:37:32Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates creating summaries for both parent and child tables in a grid.
- Explains how to add summary rows using `GridSummaryColumnDescriptor` and `GridSummaryRowDescriptor`.
- Includes styling the summary rows with alignment and background color customization.
- Provides both C# and VB.NET code examples.

## Content

```csharp
scd = new GridSummaryColumnDescriptor("Sum", 
    SummaryType.Int32Aggregate, 
    "Quantity", "{Sum:?}");

srd = new GridSummaryRowDescriptor("Sum", "Total", scd);
srd.Appearance.AnyCell.HorizontalAlignment = GridHorizontalAlignment.Right;
srd.Appearance.AnyCell.BackColor = Color.FromArgb(255, 231, 162);
this.gridGroupingControl.GetTableDescriptor("Order Details").SummaryRows.Add(srd);
```

### [VB.NET]

```vb
' Adding Summaries for the Parent Table(Orders).
Dim scd As GridSummaryColumnDescriptor = New GridSummaryColumnDescriptor("Sum", SummaryType.DoubleAggregate, "Freight", "{Sum:?}")
Dim srd As GridSummaryRowDescriptor = New GridSummaryRowDescriptor("Sum", "$", scd)
srd.Appearance.AnyCell.HorizontalAlignment = GridHorizontalAlignment.Right
srd.Appearance.AnyCell.BackColor = Color.FromArgb(255, 231, 162)
Me.gridGroupingControl.TableDescriptor.SummaryRows.Add(srd)

' Adding Summaries for the Child Table(Order Details).
scd = New GridSummaryColumnDescriptor("Sum", SummaryType.Int32Aggregate, "Quantity", "{Sum:?}")
srd = New GridSummaryRowDescriptor("Sum", "Total", scd)
srd.Appearance.AnyCell.HorizontalAlignment = GridHorizontalAlignment.Right
srd.Appearance.AnyCell.BackColor = Color.FromArgb(255, 231, 162)
Me.gridGroupingControl.GetTableDescriptor("Order Details").SummaryRows.Add(srd)
```

### Explanation
- The code snippets demonstrate how to create summary rows for both parent and child tables within a grid.
- **Parent Table Summary**:
  - Uses `GridSummaryColumnDescriptor` to define a summary for the "Freight" column.
  - The `GridSummaryRowDescriptor` is used to specify the summary row details, including appearance and alignment.
- **Child Table Summary**:
  - Similarly, uses `GridSummaryColumnDescriptor` and `GridSummaryRowDescriptor` for the "Quantity" column.
  - The summary row is styled with right alignment and a specific background color.
- The examples show how to add these summary rows to the grid control, ensuring they are displayed at the appropriate level.

Here is a sample screen shot.

### WinForms-specific conventions
- The provided code adheres to the conventions of the Syncfusion Windows Forms API, including the use of `GridSummaryColumnDescriptor` and `GridSummaryRowDescriptor`.
- The examples highlight the customization options available for formatting summary rows, such as `HorizontalAlignment` and `BackColor`.
- Both C# and VB.NET versions are included to cater to different developer preferences.

### Cross References
- For more information on grid controls and their functionalities, refer to the Syncfusion documentation or related sections in the user guide.

## API Reference (if applicable)

- **Classes**
  - `GridSummaryColumnDescriptor`
  - `GridSummaryRowDescriptor`
  - `GridRowAppearance`

- **Properties**
  - `SummaryType`
  - `AnyCell.HorizontalAlignment`
  - `AnyCell.BackColor`

- **Methods**
  - `.Add()`

## Code Examples (multi-language supported)

- **C#**
  ```csharp
  scd = new GridSummaryColumnDescriptor("Sum", 
      SummaryType.Int32Aggregate, 
      "Quantity", "{Sum:?}");

  srd = new GridSummaryRowDescriptor("Sum", "Total", scd);
  srd.Appearance.AnyCell.HorizontalAlignment = GridHorizontalAlignment.Right;
  srd.Appearance.AnyCell.BackColor = Color.FromArgb(255, 231, 162);
  this.gridGroupingControl.GetTableDescriptor("Order Details").SummaryRows.Add(srd);
  ```

- **VB.NET**
  ```vb
  Dim scd As GridSummaryColumnDescriptor = New GridSummaryColumnDescriptor("Sum", SummaryType.DoubleAggregate, "Freight", "{Sum:?}")
  Dim srd As GridSummaryRowDescriptor = New GridSummaryRowDescriptor("Sum", "$", scd)
  srd.Appearance.AnyCell.HorizontalAlignment = GridHorizontalAlignment.Right
  srd.Appearance.AnyCell.BackColor = Color.FromArgb(255, 231, 162)
  Me.gridGroupingControl.TableDescriptor.SummaryRows.Add(srd)
  ```

## RAG Annotations
<!-- tags: [product, module, control, api, version?] keywords: [Essential Grid, Windows Forms, Summary Rows, GridSummaryColumnDescriptor, GridSummaryRowDescriptor, GridRowAppearance, SummaryType, HorizontalAlignment, BackColor] -->
