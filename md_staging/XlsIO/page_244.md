```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_244.jpeg
document_name: XlsIO
page_number: 244
page_id: XlsIO#page_244
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:05:54Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- This page explains how to create and customize Sparklines using XlsIO in Excel documents.
- Focuses on the API support for Sparklines, including creation, customization, and integration into Excel spreadsheets.
- Demonstrates code examples in C# and VB for adding and configuring Sparklines.

## Content

### Sparkline Creation Using XlsIO

The Sparklines appear once you select the data range and the location range. Now you can customize the appearance of Sparklines in terms of color, style, etc. A group of Sparkline tools are available on the ribbon to change the high point, low point, color, edit the sparkline data, etc.

XlsIO provides support for creation of Sparklines by using simple APIs.

- **ISparklineGroups** interface caches the SparklineGroup that needs to be added to the Spreadsheet.
- **ISparklineGroup** represents Sparklines in an object and has properties that allow customization.
- **ISparklines** interface returns the collection of Sparkline present in a Worksheet.
- **ISparkline** represents a sparkline in the Sparklines. Currently, XlsIO supports all the three types of sparklines - Line, Column, Win/Loss which are supported in Excel 2010.

The following code example illustrates how to create Sparklines by using XlsIO.

#### Code Examples

**C#**
```csharp
ISparklineGroup sparklineGroup = sheet.SparklineGroups.Add();
sparklineGroup.SparklineType = SparklineType.Line;

ISparklines sparklines = sparklineGroup.Add();

IRange dataRange = sheet.Range["D6:G17"];
IRange referenceRange = sheet.Range["H6:H17"];

sparklines.Add(dataRange, referenceRange);
```

**VB**
```vb
Dim sparklineGroup As ISparklineGroup = sheet.SparklineGroups.Add()
sparklineGroup.SparklineType = SparklineType.Line

Dim sparklines As ISparklines = sparklineGroup.Add()

Dim dataRange As IRange = sheet.Range("D6:G17")
Dim referenceRange As IRange = sheet.Range("H6:H17")

sparklines.Add(dataRange, referenceRange)
```

## Cross References
- See also: Sparkline customization tools, Excel Spreadsheet manipulation in XlsIO.

<!-- tags: [Syncfusion, XlsIO, Sparklines, Excel, WinForms, C#, VB, API, 11.4.0.26] keywords: [Sparkline, XlsIO, Excel, WinForms, C#, VB, API, creation, customization, data range, reference range] -->
```