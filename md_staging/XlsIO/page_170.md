```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_170.jpeg
document_name: XlsIO
page_number: 170
page_id: XlsIO#page_170
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:58:41Z
fidelity: lossless
-->

# Essential XlsIO

```csharp
txtDisplay.Text = result.DisplayText.ToString();

// Find First with Match case
IRange result = sheet.FindFirst("Simple text", ExcelFindType.Text, ExcelFindOptions.MatchCase);

// Gets the cell display text.
txtDisplay.Text = result.DisplayText.ToString();

// Find First with MatchEntireCellContent
IRange result = sheet.FindFirst("Simple text", ExcelFindType.Text, ExcelFindOptions.MatchEntireCellContent);

// Gets the cell display text
txtDisplay.Text = result.DisplayText.ToString();
```

### [VB]

```vb
' FindFirst with Number
Dim result As Range = sheet.FindFirst(1000000.00075, ExcelFindType.Number)

' Gets the cell display text
txtDisplay.Text = result.DisplayText.ToString()

' Find First with Match case
Dim result As IRange = sheet.FindFirst("Simple text", ExcelFindType.Text, ExcelFindOptions.MatchCase)

' Gets the cell display text.
txtDisplay.Text = result.DisplayText.ToString()

' Find First with MatchEntireCellContent
Dim result As IRange = sheet.FindFirst("Simple text",
```

<!-- tags: [XlsIO, Essential XlsIO, ExcelFind, Match case, MatchEntireCellContent, Text search, VB, C#] keywords: [ExcelFindType, ExcelFindOptions, IRange, txtDisplay, Simple text, MatchCase, MatchEntireCellContent, FindFirst] -->
```