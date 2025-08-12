```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_255.jpeg
document_name: XlsIO
page_number: 255
page_id: XlsIO#page_255
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:05:14Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Describes how to set up page numbers in headers.
- Provides Header and Footer options for page setup.

## Content

### Setting the Page Number in the Center Header

```csharp
// Setting the page number in the Center Header.
sheet.PageSetup.CenterHeader = "&P";
```

```vb
' Setting the page number in the Center Header.
sheet.PageSetup.CenterHeader = "&P"
```

### Header Footer options

| Property                        | Description                                                                 |
|----------------------------------|-----------------------------------------------------------------------------|
| DifferentOddAndEvenPagesHF      | If true, the headers and footers on odd-numbered pages will be different from those on even-numbered pages. |
| DifferentFirstPageHF            | When set to true, this property specifies a separate header and footer for the first page.                  |
| HFScaleWithDoc                  | If true, the headers and footers will use the same font size and scaling as in the worksheet. If false, the headers and footers will not shrink or expand with document scaling. |
| AlignHFWithPageMargins          | If true, the header and footer margin is aligned with the left and right margins of the worksheet. If false, the header and footer margin is aligned with paper edges.              |

### Example Code for Header and Footer Options

```csharp
// Setting the header footer page setup options.
sheet.PageSetup.DifferentOddAndEvenPagesHF = false;
sheet.PageSetup.DifferentFirstPageHF = false;
sheet.PageSetup.HFScaleWithDoc = true;
sheet.PageSetup.AlignHFWithPageMargins = true;
```

```vb
' Setting the header footer page setup options.
```

## Code Examples

```csharp
// Example demonstrating how to configure header and footer options in C#.
sheet.PageSetup.DifferentOddAndEvenPagesHF = false;
sheet.PageSetup.DifferentFirstPageHF = false;
sheet.PageSetup.HFScaleWithDoc = true;
sheet.PageSetup.AlignHFWithPageMargins = true;
```

```vb
' Example demonstrating how to configure header and footer options in VB.NET.
sheet.PageSetup.DifferentOddAndEvenPagesHF = false
sheet.PageSetup.DifferentFirstPageHF = false
sheet.PageSetup.HFScaleWithDoc = true
sheet.PageSetup.AlignHFWithPageMargins = true
```

## Page-level Navigation/TOC
- **Header** - Setting the Page Number in the Center Header.
- **Content** - Header Footer options.
- **Example Code** - Demonstration of configuring header and footer options.

<!-- tags: [xlsio, page setup, header footer, page numbers] keywords: [different odd and even pages, different first page, header footer scaling, align with page margins] -->
```