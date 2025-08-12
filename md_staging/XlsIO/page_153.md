```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_153.jpeg
document_name: XlsIO
page_number: 153
page_id: XlsIO#page_153
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:58:50Z
fidelity: lossless
-->

## Conditional Formatting with Color Scales

### Overview

- This section explains how to apply **color scales** through **conditional formatting** in MS Excel.
- It demonstrates customization of criteria using the **New Formatting Rule dialog box**.

### Content

#### Figure 52: Color Scales

**Image Description:**
The image shows the Excel ribbon with the **Conditional Formatting** dropdown menu expanded. Key features include:

- **Highlight Cells Rules**, **Top/Bottom Rules**, **Data Bars**, **Color Scales**, and **Icon Sets** options.
- The **Color Scales** option is highlighted, showing predefined color scale formats applied to a range of cells (O, P, Q) in the grid.
- Predefined color scales are displayed, indicating how the color intensity varies based on values.
- The **More Rules...** option is accessible for further customization.

**Caption:**
Figure 52: Color Scales

You can customize the criteria through the **New Formatting Rule dialog box** in MS Excel.

## API Reference

### Customizing Formatting Rules

The **New Formatting Rule dialog box** provides extensive customization options for formatting rules. This includes:

- **Color Scales**: Define gradients to highlight cell values based on a pre-defined or custom color scale.
- **Icon Sets**: Use specific icons to indicate cell values.
- **Data Bars**: Visually represent cell values with horizontal bars.
- **Top/Bottom Rules**: Highlight the top or bottom 10% of values in a dataset.

### Code Examples

#### Example: Applying a Custom Color Scale in Excel

This example demonstrates how to apply a custom color scale using VBA code in MS Excel. 

```vba
Sub ApplyCustomColorScale()
    Dim ws As Worksheet
    Set ws = ThisWorkbook.Sheets("Sheet1")

    ' Select the range for formatting
    Dim rng As Range
    Set rng = ws.Range("O1:Q10")

    ' Clear any existing conditional formatting
    ws.Cells.ClearFormats

    ' Apply color scale rule
    With rng.FormatConditions.AddColorScale(ColorScaleType:=3)
        .ColorScaleCriteria(1).Type = xlConditionValueLowestValue
        .ColorScaleCriteria(1).Stop.Type = xlAutomatic
        .ColorScaleCriteria(1).FormatColor.Color = vbGreen ' Light Green

        .ColorScaleCriteria(2).Type = xlConditionValuePercent
        .ColorScaleCriteria(2).Stop.Type = 50
        .ColorScaleCriteria(2).FormatColor.Color = vbYellow ' Yellow

        .ColorScaleCriteria(3).Type = xlConditionValueHighestValue
        .ColorScaleCriteria(3).Stop.Type = xlAutomatic
        .ColorScaleCriteria(3).FormatColor.Color = vbRed ' Red (Dark Red)
    End With
End Sub
```

### See also

- [MS Excel Conditional Formatting Documentation](https://docs.microsoft.com/en-us/office/troubleshooting/excel/conditional-formatting)
- [VBA Reference: Formatting Cells and Ranges](https://docs.microsoft.com/en-us/office/vba/api/excel.range.format)

<!-- tags: XlsIO, Conditional Formatting, Excel, Color Scales, MS Excel, VBA -->
```