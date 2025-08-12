```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_307.jpeg
document_name: XlsIO
page_number: 307
page_id: XlsIO#page_307
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:08:51Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Explains how to define page margins using APIs in XlsIO.
- Demonstrates setting margins in a sheet through the properties of `IPageSetup`.

## Content

### Page Setup - Margins

![Figure 107: Page Setup - Margins](#)

XlsIO has APIs to define the margins in a sheet through the properties of `IPageSetup`. It sets the value in terms of inches.

### Code Example: Setting Margins

Following code example illustrates how to set the margin.

```csharp
// C#
// Page Setup Using Margins.
sheet.PageSetup.LeftMargin = 2;
sheet.PageSetup.RightMargin = 2;
sheet.PageSetup.TopMargin = 2;
sheet.PageSetup.BottomMargin = 2;
```

```vbnet
' VB.NET
' Page Setup Using Margins.
sheet.PageSetup.LeftMargin = 2
sheet.PageSetup.RightMargin = 2
sheet.PageSetup.TopMargin = 2
sheet.PageSetup.BottomMargin = 2
```

## API Reference

- **Namespace**: `Syncfusion.XlsIO`
- **Class**: `IPageSetup`
- **Methods/Properties**:
  - `LeftMargin`
  - `RightMargin`
  - `TopMargin`
  - `BottomMargin`

### Parameters

| Name          | Description                                     |
|---------------|-------------------------------------------------|
| `LeftMargin`  | Sets the left margin of the page.              |
| `RightMargin` | Sets the right margin of the page.             |
| `TopMargin`   | Sets the top margin of the page.               |
| `BottomMargin`| Sets the bottom margin of the page.            |

## Code Examples

### C# Example

```csharp
// C#
// Page Setup Using Margins.
sheet.PageSetup.LeftMargin = 2;
sheet.PageSetup.RightMargin = 2;
sheet.PageSetup.TopMargin = 2;
sheet.PageSetup.BottomMargin = 2;
```

### VB.NET Example

```vbnet
' VB.NET
' Page Setup Using Margins.
sheet.PageSetup.LeftMargin = 2
sheet.PageSetup.RightMargin = 2
sheet.PageSetup.TopMargin = 2
sheet.PageSetup.BottomMargin = 2
```

<!-- tags: [xlsio, page setup, margins, iPageSetup, syncfusion winforms, api] keywords: [margins, xlsio, api, iPageSetup, c#, vb.net, set margins, top margin, bottom margin, left margin, right margin] -->
```