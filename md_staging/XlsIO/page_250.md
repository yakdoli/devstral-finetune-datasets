```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_250.jpeg
document_name: XlsIO
page_number: 250
page_id: XlsIO#page_250
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:04:17Z
fidelity: lossless
-->

## Hyperlink Creation in Excel

### Overview
- Demonstrates how to create hyperlinks for various purposes using Excel Hyperlink Objects.
- Includes examples for email, file opening, UNC paths, and internal Excel cell navigation.

### Content

#### Creating Hyperlinks for Different Purposes

' Creating a Hyperlink for e-mail.
```csharp
Dim hyperlink1 As IHyperLink = sheet.HyperLinks.Add(sheet.Range("C7"))
hyperlink1.Type = ExcelHyperLinkType.Url
hyperlink1.Address = "mailto:Username@syncfusion.com"
hyperlink1.ScreenTip = "Send Mail"
```

' Creating a Hyperlink for Opening Files using type as File.
```csharp
Dim hyperlink2 As IHyperLink = sheet.HyperLinks.Add(sheet.Range("C9"))
hyperlink2.Type = ExcelHyperLinkType.File
hyperlink2.Address = "C:\Program files"
hyperlink2.ScreenTip = "File path"
hyperlink2.TextToDisplay = "Hyperlink for files using File as type"
```

' Creating a Hyperlink for Opening Files using type as UNC.
```csharp
Dim hyperlink3 As IHyperLink = sheet.HyperLinks.Add(sheet.Range("C11"))
hyperlink3.Type = ExcelHyperLinkType.Unc
hyperlink3.Address = "C:\Documents and Settings"
hyperlink3.ScreenTip = "Click here for files"
hyperlink3.TextToDisplay = "Hyperlink for files using Unc as type"
```

' Creating a Hyperlink to another cell using type as Workbook.
```csharp
Dim hyperlink4 As IHyperLink = sheet.HyperLinks.Add(sheet.Range("C13"))
hyperlink4.Type = ExcelHyperLinkType.Workbook
hyperlink4.Address = "Sheet1!A15"
hyperlink4.ScreenTip = "Click here"
hyperlink4.TextToDisplay = "Hyperlink to cell A15"
```

### Notes
- The `ExcelHyperLinkType` enum allows specifying the type of hyperlink to be created, such as `Url`, `File`, `Unc`, or `Workbook`.
- `ScreenTip` provides a tooltip for the hyperlink.
- `TextToDisplay` specifies the text or content to display in the hyperlink location.

<!-- tags: [Syncfusion, Excel, Hyperlink, User Guide, Control, API] keywords: [Hyperlink, ExcelHyperLinkType, ScreenTip, TextToDisplay] -->
``` 
