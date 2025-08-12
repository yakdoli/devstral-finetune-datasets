```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_367.jpeg
document_name: XlsIO
page_number: 367
page_id: XlsIO#page_367
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:12:50Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Demonstrates the process of generating an MS Excel file from Grid data using XlsIO.
- Explains how to export Excel documents into PDF format using Essential XlsIO.

## Content

### Exporting Excel to PDF

Essential XlsIO allows exporting an Excel document into PDF format. Use the Convert method of the ExcelToPdfConverter class to convert the Excel spreadsheet and save the PDF output.

#### Note:
You need to have both Essential PDF and Essential XlsIO installed in your system since Syncfusion.ExceltoPDFConverter.Base.dll is conditionally shipped when both XlsIO.Base and Pdf.Base is installed.

#### Example Code: Exporting Excel to PDF

[C#]

```csharp
// Open the Excel document you want to convert
ExcelToPdfConverter converter = new ExcelToPdfConverter("Sample.xlsx");
```

### Figure: MS Excel file generated from the Grid data by using XlsIO
![Figure 134: MS Excel file generated from the Grid data by using XlsIO](https://example.com/image_url)

#### Caption:
Figure 134: MS Excel file generated from the Grid data by using XlsIO

## API Reference

### ExcelToPdfConverter Class
- **Convert Method**: Used to convert an Excel document to PDF format.

## Code Examples

### C#
```csharp
// Example of converting an Excel document to PDF
ExcelToPdfConverter converter = new ExcelToPdfConverter("Sample.xlsx");
```

## Page-level Navigation/TOC (if applicable)
- Exporting Excel to PDF
- Note on Dependencies
- Example Code

## Cross References
- See also: Exporting PDF in Essential PDF User Guide

## RAG Annotations
<!-- tags: [xlsio, pdf, export, conversion, essential pdf] keywords: [xlsio, pdf, export, essential pdf, essential xlsio] -->
```