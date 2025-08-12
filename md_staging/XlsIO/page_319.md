```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_319.jpeg
document_name: XlsIO
page_number: 319
page_id: XlsIO#page_319
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:09:34Z
fidelity: lossless
-->


### Setting Printing Range

#### Print Titles

MS Excel provides an option to repeat rows and columns, so that the labels will be displayed on every page that it takes to print the sheet. This can be selected through the Sheet tab of the Page Setup dialog box.

XlsIO allows setting these titles through the APIs discussed in the following code.

```csharp
[!#csharp]

// Sets printing range
sheet.PageSetup.PrintArea = "$G$7:$K$9,$G$11,$H$12,$I$13,$J$14";
```

```vb.net
[!#VB.NET]

' Sets printing range
sheet.PageSetup.PrintArea = "$G$7:$K$9,$G$11,$H$12,$I$13,$J$14";
```

### Print Options

There are other settings that can be used to customize the Print options. They are as follows.

#### Grid Lines

These are the gray lines that separate the cells. Checking the box will enable them to print. These can be enabled/disabled through XlsIO by using the `PrintGridlines` property of `IPageSetup` interface.

### Headings

- **Print Titles:**
  - Allows repeating rows and columns (titles) on every printed page.
- **Printing Range:**
  - Setting specific areas for printing through APIs.
- **Print Options:**
  - Customizing print settings like grid lines and headings.

<!-- tags: [XlsIO, Print Options, Print Titles, PrintGridlines, IPageSetup] keywords: [printing range, repeating rows, repeating columns, grid lines, headings, MS Excel, Page Setup, Sheet tab, Print Options, PrintGridlines, IPageSetup] -->
```