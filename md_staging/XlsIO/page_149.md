```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_149.jpeg
document_name: XlsIO
page_number: 149
page_id: XlsIO#page_149
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:58:38Z
fidelity: lossless
-->

# XlsIO

## Overview
- [VB.NET] - Removing conditional format at the specified range.
- Removing Conditional Formats at a specified index value using the `RemoveAt` method.
- Removing Conditional Formats from the entire sheet.

## Content

### Removing Conditional Formats at the specified range
```vb
' Removing conditional format at the specified range.
sheet.Range["E5"].ConditionalFormats.Remove()
```

### Removing Conditional Formats at specified index value
XlsIO removes the conditional formats at a specified index value by using the `RemoveAt` method.

Following code example illustrates this:

#### C#
```csharp
// Removing Conditional Format at the specified Range
sheet.Range["E5"].ConditionalFormats.RemoveAt(0);
```

#### VB.NET
```vb
' Removing Conditional Format at the specified Range
sheet.Range["E5"].ConditionalFormats.RemoveAt(0)
```

### Removing Conditional Formats from entire sheet
XlsIO also provides support for removing conditional formats from the entire sheet. Following code example illustrates this.

#### C#
```csharp
// Removing Conditional Formatting Settings From Entire Sheet.
sheet.UsedRange.Clear(ExcelClearOptions.ClearConditionalFormats);
```

#### VB.NET
```vb
' [No VB.NET code provided in the image]
```

## Page-level Navigation/TOC (if applicable)
- Summary of instructions for removing conditional formats in XlsIO.

## Cross References
- Refer to additional XlsIO documentation for more detailed examples and additional functionalities.

<!-- tags: [XlsIO, Conditional Formats, RemoveAt, UsedRange, ClearConditionalFormats] keywords: [Conditional Formats, RemoveAt, ClearConditionalFormats, sheet.UsedRange, ExcelClearOptions] -->
```