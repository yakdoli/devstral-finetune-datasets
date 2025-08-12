```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_188.jpeg
document_name: pdf
page_number: 188
page_id: pdf#page_188
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:35:19Z
fidelity: lossless
-->

## Creating and Configuring a Portfolio in VB.NET

This section demonstrates how to create a new instance of the `PdfDocument` class, set up a portfolio with specific view modes, and attach multiple files to the portfolio.

```vb
' Create a new instance of the PdfDocument class.
Dim document As New PdfDocument()

' Create a new portfolio.
document.PortfolioInformation = New PdfPortfolioInformation()

' Set the view mode of the portfolio.
document.PortfolioInformation.ViewMode = PdfPortfolioViewMode.Tile

' Create the attachment.
Dim pdfFile As New PdfAttachment(GetFullTemplatePath("CorporateBrochure.pdf"))
pdfFile.FileName = "CorporateBrochure.pdf"

' Create the attachment.
Dim wordfile As New PdfAttachment(GetFullTemplatePath("Stock.docx"))
wordfile.FileName = "Stock.docx"

' Create the attachment.
Dim excelfile As New PdfAttachment(GetFullTemplatePath("Chart.xlsx"))
excelfile.FileName = "Chart.xlsx"

' Set the startup document for the Portfolio.
document.PortfolioInformation.StartupDocument = pdfFile

' Add the attachment into the document.
document.Attachments.Add(pdfFile)
document.Attachments.Add(wordfile)
document.Attachments.Add(excelfile)

' Add a new page into the document.
document.Pages.Add()
```

### Explanation

- **Creating a PdfDocument**: A new instance of the `PdfDocument` class is created to serve as the container for the portfolio.
- **Portfolio Configuration**: The `PortfolioInformation` property is utilized to configure the portfolio settings, such as specifying a view mode (e.g., Tile view).
- **Adding Attachments**: Multiple files of different types (PDF, DOCX, XLSX) are attached to the portfolio using the `PdfAttachment` class. Each attachment is assigned a filename for identification.
- **Setting the Startup Document**: Optionally, a startup document can be set to control which file opens first when the portfolio is viewed.
- **Adding a Page**: A new page is added to the document using the `Add()` method of the `Pages` collection.

This example illustrates the basic steps for working with Syncfusion’s PDF portfolio capabilities in VB.NET. It provides a foundation for creating and customizing portfolios with multiple attachments and viewer settings.

<!-- tags: [syncfusion, winforms, pdf, portfolio, vb.net] keywords: [PdfDocument, PdfPortfolioInformation, PdfAttachment, Tile view, startup document, multiple attachments] -->
```