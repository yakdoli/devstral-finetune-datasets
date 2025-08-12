```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_444.jpeg
document_name: XlsIO
page_number: 444
page_id: XlsIO#page_444
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:18:47Z
fidelity: lossless
-->

# Essential XlsIO

```csharp
blueFont.Bold = true;
blueFont.Italic = true;
blueFont.RGBColor = Color.Blue;
rtf.SetFont(4, 7, blueFont);
```

### [VB.NET]

```vbnet
' Insert Rich Text.
Dim range As Syncfusion.XlsIO.IRange = sheet.Range("A1")
range.Text = "RichText"
Dim rtf As Syncfusion.XlsIO.IRichTextString = range.RichText

' Formatting first 4 characters.
Dim redFont As Syncfusion.XlsIO.IFont = workbook.CreateFont()
redFont.Bold = True
redFont.Italic = True
redFont.RGBColor = Color.Red
rtf.SetFont(0, 3, redFont)

' Formatting last 4 characters.
Dim blueFont As Syncfusion.XlsIO.IFont = workbook.CreateFont()
blueFont.Bold = True
blueFont.Italic = True
blueFont.RGBColor = Color.Blue
rtf.SetFont(4, 7, blueFont)
```

## 5.2.4 How to suppress the summary rows and columns using XlsIO?

You can suppress the summary rows and columns by using the **IsSummaryRowBelow** and **IsSummaryColumnRight** properties. The following code example illustrates this.

### [C#]

```csharp
// Suppress the summary rows at the bottom.
sheet.PageSetup.IsSummaryRowBelow = false;
// Suppress the summary columns to the right.
sheet.PageSetup.IsSummaryColumnRight = false;
```

### [VB.NET]

```vbnet
' Code goes here
```

<!-- tags: [XlsIO, WinForms, summary rows, columns, IsSummaryRowBelow, IsSummaryColumnRight] keywords: [XlsIO, Suppress, Summary, Rows, Columns, IsSummaryRowBelow, IsSummaryColumnRight] -->
```