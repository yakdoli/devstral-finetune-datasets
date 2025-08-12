```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_405.jpeg
document_name: XlsIO
page_number: 405
page_id: XlsIO#page_405
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:16:23Z
fidelity: lossless
-->

**Essential XlsIO**

```csharp
IWorksheet sheet = book.Worksheets[0];

sheet.FirstVisibleColumn = 5;
sheet.FirstVisibleRow = 11;
sheet.VerticalSplit = 110;
sheet.HorizontalSplit = 100;
sheet.ActivePane = 1;

book.SaveAs(WORKSHEETS_PANE);
```

**[VB.NET]**

```vb
Dim sheet As IWorksheet = book.Worksheets(0)

sheet.FirstVisibleColumn = 5
sheet.FirstVisibleRow = 11
sheet.VerticalSplit = 110
sheet.HorizontalSplit = 100
sheet.ActivePane = 1

book.SaveAs(WORKSHEETS_PANE)
```

<!-- tags: [XlsIO, Syncfusion Winforms, IWorksheet, FirstVisibleColumn, FirstVisibleRow, VerticalSplit, HorizontalSplit, ActivePane, SaveAs] keywords: [Excel, Split, Pane, Save, Workbook, Sheet] -->
```