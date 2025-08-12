```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_421.jpeg
document_name: XlsIO
page_number: 421
page_id: XlsIO#page_421
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:17:32Z
fidelity: lossless
-->

# XlsIO

## Overview
- Covers Excel and custom Add-Ins support in XlsIO.
- Illustrates how to register and use Add-Ins in Excel.
- Includes code examples for add-in integration and usage.

## Content

### Registering and Using Add-Ins in XlsIO

#### Introduction
XlsIO provides support for Excel and custom Add-Ins. They can be accessed by first registering, and then using the Add-In's custom functions through XlsIO formulas.

#### Figure References
- **Figure 161: Add-Ins**
  - Displays the Add-Ins dialog in Excel, showing available add-ins like Analysis ToolPak, Bloomberg Excel Tools, Blip, and others.
- **Figure 162: Add-Ins in Excel**
  - Shows the Excel ribbon with the Add-Ins tab active, highlighting tools like Function Builder, Formula Conversion Tool, Real-Time Updates, and more.

#### Example Code for Registering and Using Add-Ins

[C#]
```csharp
IAddInFunctions unknownFunctions = workbook.AddInFunctions;
unknownFunctions.Add("c:\\blp\\api\\dde\\blp.xla", "blp");

// Use the Function.
sheet.Range[ "A3" ].Formula = "blp(A1+\" CORP\",\"PX_LAST\")";
```

### Explanation of Code Example
- `IAddInFunctions unknownFunctions = workbook.AddInFunctions;`: Initializes an object to handle Add-In functions.
- `unknownFunctions.Add("c:\\blp\\api\\dde\\blp.xla", "blp");`: Registers the Bloomberg add-in (blp) from the specified location.
- `sheet.Range[ "A3" ].Formula = "blp(A1+\" CORP\",\"PX_LAST\")";`: Sets a formula in cell A3 that uses the registered Bloomberg function to retrieve the last price for a specified corporation.

## Page-Level Navigation/TOC
- **Add-Ins in Excel**
  - Registration and Usage
  - Code Examples

## Cross References
- Relevant sections or features within XlsIO for further details.

## RAG Annotations
<!-- tags: [xlsio, excel, add-ins, custom functions, code examples] keywords: [xsl-io, integration, blp, bloomberg, formula, add-in, csharp, add-in functions] -->
```