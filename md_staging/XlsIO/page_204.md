```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_204.jpeg
document_name: XlsIO
page_number: 204
page_id: XlsIO#page_204
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:02:26Z
fidelity: lossless
-->

# Essential XlsIO

## Content

### Saving Excel as HTML

To save an Excel sheet or workbook as an HTML file, you can use the `SaveAsHtml` method. Below are examples in both C# and VB.NET:

#### C#

```csharp
workbook.SaveAsHtml("Sample.html", HtmlSaveOptions.Default);
```

#### VB.NET

```vbnet
' Save an Excel sheet as HTML file.
sheet.SaveAsHtml("Sample.html")

' Save a workbook as HTML file.
workbook.SaveAsHtml("Sample.html", HtmlSaveOptions.Default)
```

### Save Options

XlsIO also provides various save options to control images and text in an Excel file. It enables you to save a worksheet with the displayed text or value in the cell to an HTML file. The following code example illustrates this.

#### C#

```csharp
HtmlSaveOptions options = new HtmlSaveOptions();
options.TextMode = HtmlSaveOptions.GetText.DisplayText;
options.ImagePath = @"..\..\Output\";
sheet.SaveAsHtml("Sample.html", options);
```

#### VB.NET

```vbnet
Dim options As New HtmlSaveOptions()
options.TextMode = HtmlSaveOptions.GetText.DisplayText
options.ImagePath = "..\..\Output\"
sheet.SaveAsHtml("Sample.html", options)
```

### 4.1.3.3.4 Protection

Excel provides various options to protect worksheet and workbook elements. Protection prevents a user from accidentally or deliberately changing, moving, or deleting important data. There are various options to protect worksheets and workbooks.

Refer to the **Changes** section for more details.

This section explains how cell protection can be applied in MS Excel by using XlsIO.
```


<!-- tags: [xlsio, excel, html, save options, worksheet protection, workbook protection, c#, vb.net] keywords: [syncfusion, essential xlsio, export to html, control images, cell protection, ms excel, text mode, display text, imagePath, protection, user guide] -->
```