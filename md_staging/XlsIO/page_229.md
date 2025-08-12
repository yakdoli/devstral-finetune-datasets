```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_229.jpeg
document_name: XlsIO
page_number: 229
page_id: XlsIO#page_229
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:03:50Z
fidelity: lossless
-->

## Rich-text in Data Label

### Creating Fonts for Labels

```vb
' Create a second font with the following properties
Dim greenFont As IFont = workbook.CreateFont()
greenFont.Bold = True
greenFont.Italic = False
greenFont.Size = 18
greenFont.FontName = "Georgia"
greenFont.Color = ExcelKnownColors.Red
chart.Series(0).DataPoints(0).DataLabels.RichText.SetFont(0, 0, greenFont)
```

```vb
' Create a third font with the following properties
Dim blueFont As IFont = workbook.CreateFont()
blueFont.Bold = True
blueFont.Italic = False
blueFont.Size = 18
blueFont.FontName = "Georgia"
blueFont.Color = ExcelKnownColors.Red
chart.Series(0).DataPoints(0).DataLabels.RichText.SetFont(0, 0, blueFont)
```

### Saving and Closing the Workbook

```vb
' Save the workbook to disk
workbook.SaveAs(fileName)
' Close the workbook
workbook.Close()
excelEngine.ThrowNotSavedOnDestroy = False
excelEngine.Dispose()
```

### 3-D Chart Wall Settings

#### Overview
- Modifies side wall, back wall, and floor settings of a 3-D chart.

#### Code Example

```csharp
// Instantiate the spreadsheet creation engine
```

### Summary

This section provides guidance on customizing data labels using rich text fonts and modifying 3-D chart settings, such as the walls and floor, in Essential XlsIO for Syncfusion Winforms.

## Note: Contextual Section Title

- **4.2.2.3.3 3-D Chart Wall Settings**
  
  - Description: Explains how to adjust side wall, back wall, and floor settings of a 3-D chart.
  - Example: Code snippet demonstrates the modifications using Essential XlsIO.

### RAG Annotations
<!-- tags: [Syncfusion Winforms, XlsIO, 3-D Chart, Font Customization] keywords: [Essential XlsIO, 3-D Chart, Data Label, Rich Text, Side Wall, Back Wall, Floor Settings, Gradient Fill] -->
```