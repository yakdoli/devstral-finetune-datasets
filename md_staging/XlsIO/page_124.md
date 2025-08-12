```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_124.jpeg
document_name: XlsIO
page_number: 124
page_id: XlsIO#page_124
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:57:09Z
fidelity: lossless
-->

# Essential XlsIO

```csharp
sheet.Range["B5"].Text = "0.00";
sheet.Range["C5"].NumberFormat = "0.00";

sheet.Range["C6"].Number = -500;
sheet.Range["B6"].Text = "[Blue]#,##0";
sheet.Range["C6"].NumberFormat = "[Blue]#,##0";

sheet.Range["C7"].Number = 0.000000000000000000000000001234567890;
sheet.Range["B7"].Text = "0.0000000000000000000000000000000000000";
sheet.Range["C7"].NumberFormat = "0.0000000000000000000000000000000000000";

sheet.Range["C9"].Number = 1.20;
sheet.Range["B9"].Text = "0.00E+00";
sheet.Range["C9"].NumberFormat = "0.00E+00";
```

### [VB.NET]
```vb
' Applying Number Format.
sheet.Range("C2").Number = 1000000.00075
sheet.Range("B2").Text = "0.00"
sheet.Range("C2").NumberFormat = "0.00"

sheet.Range("C3").Number = 1000000.5
sheet.Range("B3").Text = "###,##"
sheet.Range("C3").NumberFormat = "###,##"

sheet.Range("C5").Number = 10000
sheet.Range("B5").Text = "0.00"
sheet.Range("C5").NumberFormat = "0.00"

sheet.Range("C6").Number = -500
sheet.Range("B6").Text = "[Blue]#,##0"
sheet.Range("C6").NumberFormat = "[Blue]#,##0"

sheet.Range("C7").Number = 1.23456789E-21
sheet.Range("B7").Text = "0.0000000000000000000000000000000000000"
sheet.Range("C7").NumberFormat = "0.0000000000000000000000000000000000000"

sheet.Range("C9").Number = 1.2
sheet.Range("B9").Text = "0.00E+00"
sheet.Range("C9").NumberFormat = "0.00E+00"
```

The following code example illustrates how to set the format for Percentage.

```html
<!-- tags: XlsIO, number formatting, percentage, decimal formatting, Excel, WinForms, Syncfusion, API, version:11.4.0.26 -->
```