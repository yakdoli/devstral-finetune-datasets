```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_756.jpeg
document_name: grid
page_number: 756
page_id: grid#page_756
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:38:26Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- **Creating summaries in caption rows**.
- Enabling caption summaries by configuring the grid grouping control.
- Displaying summary rows in captions with customized text.

## Content

### Example Code: Adding a Summary Row

```csharp
GridSummaryRowDescriptor("Sum", "$", scd)
srd.Appearance.AnyCell.HorizontalAlignment = GridHorizontalAlignment.Right
srd.Appearance.AnyCell.BackColor = Color.Cornsilk
Me.gridGroupingControl.GetTableDescriptor("Orders").SummaryRows.Add(srd)
Me.gridGroupingControl.ShowGroupDropArea = True
Me.gridGroupingControl.TableDescriptor.GroupedColumns.Add("RequiredDate")
```

### Enabling Caption Summaries

To enable Caption Summaries, set `ShowCaptionSummaryCells` to `True` and turn off the `ShowSummaries` property, which disables the creation of additional summary rows.

- **C#**
  
  ```csharp
  // Creating summaries in caption.
  this.gridGroupingControl.ChildGroupOptions.ShowCaptionSummaryCells = true;
  this.gridGroupingControl.ChildGroupOptions.ShowSummaries = false;
  ```

- **VB.NET**
  
  ```vb
  ' Creating summaries in caption.
  Me.gridGroupingControl.ChildGroupOptions.ShowCaptionSummaryCells = True
  Me.gridGroupingControl.ChildGroupOptions.ShowSummaries = False
  ```

### Specifying Summary Rows in Caption

Once caption summaries are enabled, you can specify a summary to be displayed in the Caption Rows by assigning the summary name to the `CaptionSummaryRow` property. Optionally, you can customize the caption text as needed.

- **C#**
  
  ```csharp
  this.gridGroupingControl.ChildGroupOptions.CaptionSummaryRow = "Sum";
  this.gridGroupingControl.ChildGroupOptions.CaptionText = "{RecordCount} Items";
  ```

- **VB.NET**
  
  ```vb
  Me.gridGroupingControl.ChildGroupOptions.CaptionSummaryRow = "Sum"
  Me.gridGroupingControl.ChildGroupOptions.CaptionText = "{RecordCount} Items"
  ```

## RAG Annotations
<!-- tags: [grid, summary rows, caption summaries, WinForms] keywords: [GridSummaryRowDescriptor, ShowCaptionSummaryCells, ShowSummaries, CaptionSummaryRow, CaptionText] -->
```