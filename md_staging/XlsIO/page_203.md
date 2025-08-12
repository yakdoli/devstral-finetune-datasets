```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_203.jpeg
document_name: XlsIO
page_number: 203
page_id: XlsIO#page_203
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:01:31Z
fidelity: lossless
-->

# Essentia XlsIO

## Overview
- Demonstrates setting and clearing tab colors in Excel sheets.
- Shows how to clear data and formatting in a sheet.
- Provides an example for converting an Excel sheet or workbook to HTML format.

## Content

### Tab Color

Tab Colors are set to highlight a particular sheet that has some important data. This is done in Excel by selecting the "Tab Color" option in the sheet context menu. You can set the tab color through the `TabColor` property, as given below.

```vb.net
sheet.Name = "Result"
```

```csharp
sheet.TabColor = ExcelKnownColors.Blue;
```

```vb.net
sheet.TabColor = ExcelKnownColors.Blue
```

---

### Clear

You can clear all data/data with formatting in a sheet by using the `Clear` and `ClearData` methods of the `IWorksheet`.

```csharp
sheet.Clear();
```

```vb.net
sheet.Clear()
```

---

### 4.1.3.3.3.4 Sheet to HTML

XlsIO provides support to convert a worksheet or workbook to HTML with basic formatting preserved. The following code example illustrates how to do this.

```csharp
// Save an Excel sheet as HTML file.
sheet.SaveAsHtml("Sample.html");
// Save a workbook as HTML file.
```

## API Reference

### Methods

- **SaveAsHtml(string filename)**  
  Saves the sheet or workbook as an HTML file.

## Code Examples

### Clearing a Sheet

```csharp
IWorksheet sheet = workbook.Worksheets[0];
sheet.Clear();
```

### Converting to HTML

```csharp
IWorksheet sheet = workbook.Worksheets[0];
sheet.SaveAsHtml("Sample.html");
```

## Page-level Navigation/TOC

- [Tab Color](#tab-color)
- [Clear](#clear)
- [Sheet to HTML](#sheet-to-html)

<!-- tags: [Syncfusion, XlsIO, TabColor, Clear, ConvertToHTML] keywords: [Excel, TabColor, Clear, Sheet, Workbook, HTML, WinForms, C#, VB.NET, IWorksheet, SaveAsHtml] -->
```