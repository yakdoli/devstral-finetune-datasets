```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_021.jpeg
document_name: pdf
page_number: 021
page_id: pdf#page_021
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:24:51Z
fidelity: lossless
-->

# Essential PDF

## Overview
- Introduces the Essential Studio Reporting Edition for Windows Forms.
- Demonstrates how to integrate Reporting solutions into Windows Forms applications with ease.
- Highlights high-performance libraries for manipulating Word, PDF, and Excel documents.

## Content

### Reporting for Windows Forms

Figure 7: Windows Forms Sample browser

![Windows Forms Sample browser](Windows Forms Sample browser)

- **Run Samples link:** Clicking the "Run Samples" link opens the Essential Studio Reporting Edition Windows Forms sample browser.
- **Essential Studio Features:**
  - Integrates Reporting solutions into Windows Forms applications.
  - Includes the Essential DocIO library, which can read and write Microsoft Word files.
  - Features a full-fledged object model similar to Microsoft Office COM libraries.
  - Does not use COM interop.
  - Built from scratch in C# and usable on systems without Microsoft Word installed.

Figure 8: Windows Forms Sample browser

![Windows Forms Sample browser](Windows Forms Sample browser)

- **DocIO Product Showcase:** Displays various sample functionalities such as Sales Invoices, Table Insertion, Employee Reports, Table of Contents, Forms, Clone and Merge, and Update Fields.
- **Navigating the Browser:** Click the "Pdf" form in the bottom-left pane to explore PDF-specific features.

## API Reference

### Featured Samples Overview
- **Sales Invoice:** Demonstrates generating a PDF invoice.
- **Table Insertion:** Shows how to insert tables into a PDF document.
- **Employee Report:** Illustrates creating a detailed employee report in PDF format.
- **Table of Contents:** Highlights the creation of a linked table of contents.
- **Forms:** Examples showcasing the use of different types of forms.
- **Clone and Merge:** Demonstrates cloning and merging operations in PDF documents.
- **Update Fields:** Explains how to dynamically update fields in PDF documents.

## Code Examples

### C# Example
```csharp
// Example code demonstrating the creation of a PDF invoice using Essential DocIO
using Syncfusion.DocIO;
using Syncfusion.DocIO.DLS;

public void CreatePDFInvoice()
{
    // Create a new Word document
    WordDocument document = new WordDocument();

    // Add a title
    document.Sections[0].Paragraphs[0].ParagraphText = "Sales Invoice";

    // Add some rows of data
    Table table = document.Sections[0].AddTable();
    table.Rows[0].Cells[0].Paragraphs[0].ParagraphText = "Customer Name";
    table.Rows[0].Cells[1].Paragraphs[0].ParagraphText = "Product Name";
    table.Rows[0].Cells[2].Paragraphs[0].ParagraphText = "Quantity";
    table.Rows[0].Cells[3].Paragraphs[0].ParagraphText = "Price";

    // Populate the table with data
    table.Rows.Add();
    table.Rows[1].Cells[0].Paragraphs[0].ParagraphText = "John Doe";
    table.Rows[1].Cells[1].Paragraphs[0].ParagraphText = "Laptop";
    table.Rows[1].Cells[2].Paragraphs[0].ParagraphText = "1";
    table.Rows[1].Cells[3].Paragraphs[0].ParagraphText = "$500";

    // Save the document as PDF
    document.Save("SalesInvoice.pdf", SaveFormat.PDF);
}
```

### VB.NET Example
```vbnet
' Example code demonstrating the creation of a PDF invoice using Essential DocIO
Imports Syncfusion.DocIO
Imports Syncfusion.DocIO.DLS

Public Sub CreatePDFInvoice()
    ' Create a new Word document
    Dim document As New WordDocument()

    ' Add a title
    document.Sections(0).Paragraphs(0).ParagraphText = "Sales Invoice"

    ' Add some rows of data
    Dim table As Table = document.Sections(0).AddTable()
    table.Rows(0).Cells(0).Paragraphs(0).ParagraphText = "Customer Name"
    table.Rows(0).Cells(1).Paragraphs(0).ParagraphText = "Product Name"
    table.Rows(0).Cells(2).Paragraphs(0).ParagraphText = "Quantity"
    table.Rows(0).Cells(3).Paragraphs(0).ParagraphText = "Price"

    ' Populate the table with data
    table.Rows.Add()
    table.Rows(1).Cells(0).Paragraphs(0).ParagraphText = "John Doe"
    table.Rows(1).Cells(1).Paragraphs(0).ParagraphText = "Laptop"
    table.Rows(1).Cells(2).Paragraphs(0).ParagraphText = "1"
    table.Rows(1).Cells(3).Paragraphs(0).ParagraphText = "$500"

    ' Save the document as PDF
    document.Save("SalesInvoice.pdf", SaveFormat.PDF)
End Sub
```

## Cross References
- Refer to the "Getting Started" section in the documentation for detailed setup instructions.
- For more information about Essential DocIO, consult the "Referencing" and "Formatting" sections.

<!-- tags: [syncfusion, windowsforms, reporting, pdf, essentialdocio, winforms, tableinsertion, employeereport] keywords: [sales invoice, table of contents, forms, clone and merge, update fields, pdf document, Word files, C#] -->
```