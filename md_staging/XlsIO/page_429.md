```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_429.jpeg
document_name: XlsIO
page_number: 429
page_id: XlsIO#page_429
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:17:59Z
fidelity: lossless
-->

## Essential XlsIO

```vb
' Save the workbook to stream.
Dim fs As FileStream = New FileStream("FileStreamSample.xls", 
    FileMode.Create, FileAccess.ReadWrite, FileShare.ReadWrite)
workbook.SaveAs(fs)
workbook.Close()
```

### 5.1.10 How to set a line break inside a cell?

In order to set a line break inside a cell, you have to enable Text Wrapping for the cell, and then break the text. The following code example illustrates how to do this.

#### C#

```csharp
sheet.Range["A1"].CellStyle.WrapText = true;
sheet.Range["A1"].Text = String.Format("Hello\nworld");
```

#### VB.NET

```vb
sheet.Range("A1").CellStyle.WrapText = True
sheet.Range("A1").Text = String.Format("Hello" & Constants.vbLf & "world")
```

### 5.1.11 How to set or format a Header/Footer?

The string that the header/footer takes is a script that you can use to format the header/footer. For more information on formatting the string, see [http://support.microsoft.com/?kbid=213618](http://support.microsoft.com/?kbid=213618).

#### C#

```csharp
mySheet.PageSetup.CenterHeader = @"&""Gothic,bold""Center Header Text";
```

#### VB.NET

```vb
mySheet.PageSetup.CenterHeader = @"&""Gothic,bold""Center Header Text"
```

### 5.1.12 How to set options to print Titles?

## Footer
© 2013 Syncfusion. All rights reserved.  
429 | Page
```

<!-- tags: [XlsIO, Syncfusion Winforms, Excel manipulation, text wrapping, header/footer formatting, line breaks, printing titles] keywords: [Essential XlsIO, line break, text wrapping, cell formatting, header, footer, print options, worksheet manipulation, Syncfusion, Excel, C#, VB.NET, line breaks inside cells] -->
```
