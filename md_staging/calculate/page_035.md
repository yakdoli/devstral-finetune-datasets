```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_035.jpeg
document_name: calculate
page_number: 035
page_id: calculate#page_035
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:00:28Z
fidelity: lossless
-->

# Essential Calculate

## Overview

- Perform calculations using `Essential Calculate` with `ParseAndCompute`.
- Modify default behavior of `CalculateEngine` using the `Engine` property.
- Eliminate quotation marks in concatenated strings by setting `UseNoAmpersandQuotes`.

## Content

### Example

The default behavior of adding quotation marks to concatenated strings can be altered using the following code:

#### C#

```csharp
// Strings concatenated with the ampersand operator will return without quotation marks.
cq.Engine.UseNoAmpersandQuotes = true;
```

#### VB.NET

```vbnet
' Strings concatenated with the ampersand operator will return without quotation marks.
cq.Engine.UseNoAmpersandQuotes = True
```

**Note:** `Engine` is a class defined as a "property" in `Essential Calculate`.

`Essential Calculate` is now integrated into your WPF application.

## 3.4 Feature Summary

The features of `Essential Calculate` are summarized below:

- Includes a function library with over 150 functions and supports cross-sheet references.
- Can be used with `Essential XlsIO` to fully load, manipulate, and compute Excel spreadsheets without dependency on Excel.
- Operates independently of Microsoft Excel, enabling calculations without Excel.
- Provides extensive calculation support for custom business objects in both Windows Forms and ASP.NET applications.

<!-- tags: [essential-calculate, essential-xlsio, calculateengine, microsoft-excel, wpf, windows-forms, asp.net, calculation-library] keywords: [essential calculate, function library, cross-sheet references, excel manipulation, business objects, independence from excel, calculation support] -->
```