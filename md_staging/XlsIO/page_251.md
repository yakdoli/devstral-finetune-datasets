```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_251.jpeg
document_name: XlsIO
page_number: 251
page_id: XlsIO#page_251
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:05:00Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Demonstrates the use of hyperlinks in XlsIO.
- Explains how to add header/footer to print sheets in MS Excel.

## Content

### 4.2.4 Header/Footer

#### Overview
Often, there is a need to include some information about your document at the top (the header), or the bottom (the footer) of each printed sheet. Spreadsheets often need several pages to print. It is important to put the right information on the header or footer, so you can tell which pages go together.

![Figure 85: XlsIO with Hyperlinks](https://placeholder.com/image.png)

#### Key Points
- Headers and footers provide crucial information for printed sheets.
- MS Excel offers an option to insert headers and footers through the **View** menu and a handy dialog box.

#### Instructions
- **Process**: 
  1. Access the **View** menu.
  2. Locate and select the option to insert headers and footers.
  3. Use the dialog box provided to customize header/footer content.

## Code Examples

### Sample Code for Adding Headers and Footers
```csharp
// Import necessary namespaces
using Syncfusion.XlsIO;

// Initialize workbook
IWorkbook workbook = new Workbook();
IWorksheet sheet = workbook.Worksheets[0];

// Add header/footer
sheet.BuiltInHeadersFooters.AddHeaderFooter("&C &D", BuiltInHeaderFooterSection.Header);
sheet.BuiltInHeadersFooters.AddHeaderFooter("&L &P/&N", BuiltInHeaderFooterSection.Footer);

// Save workbook
workbook.Save("DocumentWithHeadersFooters.xlsx");
// Dispose objects
workbook.Dispose();
```

## Cross References
- **Related Topics**: 
  - Hyperlinks
  - Print Settings
  - Document Layout

## RAG Annotations
<!-- tags: [XlsIO, header/footer, syncingfusion, print-sheets, ms-excel, document-information, versions] keywords: [hyperlinks, header, footer, printed sheets, ms excel, built-in, dialog box, workbook, worksheet, document layout] -->
```