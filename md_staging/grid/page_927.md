```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_927.jpeg
document_name: grid
page_number: 927
page_id: grid#page_927
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:50:10Z
fidelity: lossless
-->

## Overview
- Demonstrates cell highlighting using `SystemColors.HIGHLIGHT` and bold font in Windows Forms Grid.
- Enables `ListBoxSelection` mode to expose default selection behavior.

### Content

```vb
' Highlight the current cell with SystemColors.Highlight and Bold font.
If e.RowIndex > grid.Model.Rows.HeaderCount AndAlso e.ColIndex > grid.Model.Cols.HeaderCount AndAlso cc.HasCurrentCellAt(e.RowIndex, e.ColIndex) Then
    e.Style.Interior = New BrushInfo(SystemColors.Highlight)
    e.Style.TextColor = SystemColors.HighlightText
    e.Style.Font.Bold = True
End If

' Code for ColumnOnly.
ElseIf radioButton4.Checked Then

' Highlight the current column with SystemColors.Highlight and Bold font.
If e.RowIndex > grid.Model.Rows.HeaderCount AndAlso e.ColIndex > grid.Model.Cols.HeaderCount AndAlso cc.ColIndex = e.ColIndex Then
    e.Style.Interior = New BrushInfo(SystemColors.Highlight)
    e.Style.TextColor = SystemColors.HighlightText
    e.Style.Font.Bold = True
End If

' Code for Row and Column.
ElseIf radioButton5.Checked Then

' Highlight the current row and column with SystemColors.Highlight and Bold font.
If e.RowIndex > grid.Model.Rows.HeaderCount AndAlso e.ColIndex > grid.Model.Cols.HeaderCount AndAlso (cc.RowIndex = e.RowIndex OrElse cc.ColIndex = e.ColIndex) Then
    e.Style.Interior = New BrushInfo(SystemColors.Highlight)
    e.Style.TextColor = SystemColors.HighlightText
    e.Style.Font.Bold = True
End If
End If
End Sub
```

#### Enable ListBoxSelection mode to expose the default selection.

```csharp
// Code for Default option.
private void radioButton1_CheckedChanged(object sender, System.EventArgs e)
{
    if (this.radioButton1.Checked)
}
```

---

## API Reference (if applicable)
- **Namespace**: Unspecified
- **Class**: Not explicitly named
- **Methods**:
  - `radioButton1_CheckedChanged`: Event handler for default option.

## Code Examples
- **VB.NET**: Demonstrates cell highlighting based on selection mode.
- **C#**: Demonstrates enabling of `ListBoxSelection` mode.

## RAG Annotations
<!-- tags: grid, windows-forms, cell-highlighting, bold-font, listboxselection, defaults-exposure, systemcolors keywords: Model, Rows, HeaderCount, Cols, HeaderCount, HasCurrentCellAt, BrushInfo, TextColor, Font, Bold, CurrentCellAt, ListBoxSelection -->
```