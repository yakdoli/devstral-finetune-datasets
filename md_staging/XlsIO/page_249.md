```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_249.jpeg
document_name: XlsIO
page_number: 249
page_id: XlsIO#page_249
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:05:12Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Demonstrates how to create hyperlinks of various types in Excel using C# and VB.NET.
- Includes examples for website URLs, email links, file paths, UNC paths, and cell references.

## Content

### Creating Hyperlinks in Excel

#### Code Examples

##### C#

```csharp
// Creating a Hyperlink for a Website.
IHyperLink hyperlink = sheet.HyperLinks.Add(sheet.Range["C5"]);
hyperlink.Type = ExcelHyperLinkType.Url;
hyperlink.Address = "http://www.syncfusion.com";
hyperlink.ScreenTip = "To know more About SYNCFUSION PRODUCTS go through this link";

// Creating a Hyperlink for e-mail.
IHyperLink hyperlink1 = sheet.HyperLinks.Add(sheet.Range["C7"]);
hyperlink1.Type = ExcelHyperLinkType.Url;
hyperlink1.Address = "mailto:Username@syncfusion.com";
hyperlink1.ScreenTip = "Send Mail";

// Creating a Hyperlink for Opening Files using type as File.
IHyperLink hyperlink2 = sheet.HyperLinks.Add(sheet.Range["C9"]);
hyperlink2.Type = ExcelHyperLinkType.File;
hyperlink2.Address = @"C:\Program files";
hyperlink2.ScreenTip = "File path";
hyperlink2.TextToDisplay = "Hyperlink for files using File as type";

// Creating a Hyperlink for Opening Files using type as Unc.
IHyperLink hyperlink3 = sheet.HyperLinks.Add(sheet.Range["C11"]);
hyperlink3.Type = ExcelHyperLinkType.Unc;
hyperlink3.Address = @"C:\Documents and Settings";
hyperlink3.ScreenTip = "Click here for files";
hyperlink3.TextToDisplay = "Hyperlink for files using Unc as type";

// Creating a Hyperlink to another cell using type as Workbook.
IHyperLink hyperlink4 = sheet.HyperLinks.Add(sheet.Range["C13"]);
hyperlink4.Type = ExcelHyperLinkType.Workbook;
hyperlink4.Address = "Sheet1!A15";
hyperlink4.ScreenTip = "Click here";
hyperlink4.TextToDisplay = "Hyperlink to cell A15";
```

##### VB.NET

```vb
' Creating a Hyperlink for a Website.
Dim hyperlink As IHyperLink = sheet.HyperLinks.Add(sheet.Range("C5"))
hyperlink.Type = ExcelHyperLinkType.Url
hyperlink.Address = "http://www.Syncfusion.com"
hyperlink.ScreenTip = "To know more About SYNCFUSION PRODUCTS go through this link"
```

## API Reference

### Namespaces and Classes
- `ExcelHyperLinkType`: Enumerates the types of hyperlinks that can be created in Excel.
  - `Url`: Hyperlink to a web address or email.
  - `File`: Hyperlink to a file.
  - `Unc`: Hyperlink to a UNC path.
  - `Workbook`: Hyperlink to a cell within the workbook.

### Methods
- `HyperLinks.Add`: Adds a new hyperlink to the range specified.

### Properties
- `Type`: Specifies the type of hyperlink.
- `Address`: Specifies the target address for the hyperlink.
- `ScreenTip`: Specifies the tooltip text for the hyperlink.
- `TextToDisplay`: Specifies the text displayed in the hyperlink.

<!-- tags: [Essential XlsIO, Hyperlinks, C#, VB.NET, Excel, Syncfusion] keywords: [hyperlink, website, email, file, UNC, workbook, screen tip, text display, ExcelHyperLinkType, HyperLinks.Add] -->
```