```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_187.jpeg
document_name: pdf
page_number: 187
page_id: pdf#page_187
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:36:48Z
fidelity: lossless
-->

# Essential PDF

```csharp
// Create a new portfolio.
document.PortfolioInformation = new PdfPortfolioInformation();

// Set the view mode of the portfolio.
document.PortfolioInformation.ViewMode = PdfPortfolioViewMode.Tile;

// Create the attachment.
PdfAttachment pdfFile = new PdfAttachment(GetFullTemplatePath("CorporateBrochure.pdf"));
pdfFile.FileName = "CorporateBrochure.pdf";

// Create the attachment.
PdfAttachment wordfile = new PdfAttachment(GetFullTemplatePath("Stock.docx"));
wordfile.FileName = "Stock.docx";

// Create the attachment.
PdfAttachment excelfile = new PdfAttachment(GetFullTemplatePath("Chart.xlsx"));
excelfile.FileName = "Chart.xlsx";

// Set the startup document for the Portfolio.
document.PortfolioInformation.StartupDocument = pdfFile;

// Add the attachment into the document.
document.Attachments.Add(pdfFile);
document.Attachments.Add(wordfile);
document.Attachments.Add(excelfile);

// Add a new page into the document.
document.Pages.Add();

// Save and close the document.
document.Save("Sample.pdf");
document.Close(true);
```

## Overview
- Demonstrates creating a portfolio with multiple attachments and setting the view mode.
- Adds PDF, Word, and Excel files as attachments to a portfolio.
- Configures the portfolio to use a tiled view mode and specifies the startup document.
- Saves the portfolio to a file named `Sample.pdf`.

```bash
<!-- tags: [syncfusion, pdf, portfolio, attachments, viewmode, startupdocument] keywords: [portfolio, attachments, tiled view, startup document, save pdf, close] -->
```
```python
## Page-level Navigation/TOC (if applicable)
- **Creating a Portfolio**
  - **Setting the View Mode**
  - **Adding Attachments**
  - **Specifying the Startup Document**
  - **Saving and Closing the Portfolio**

## Cross References
- Refer to the [Essential PDF documentation](#) for more details on portfolio functionality.
- See also: [Managing PDF Attachments](#), [Portfolio View Modes](#)

```