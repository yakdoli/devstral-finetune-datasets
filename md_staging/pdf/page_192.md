```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_192.jpeg
document_name: pdf
page_number: 192
page_id: pdf#page_192
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:35:33Z
fidelity: lossless
-->

### PDF Portfolio Schema Fields and File Attachments with Custom Attributes

#### Overview
- **Description**: This section demonstrates how to create and configure PDF portfolio schema fields, add custom file attributes to file attachments, and integrate them into a PDF document.
- **Steps**:
  - Define and add portfolio schema fields with specific names, types, and visibility settings.
  - Assign custom attributes to file attachments like `Price`, `Author Name`, and `Year`.
  - Add the file attachments to the document's portfolio and populate the document's attachments and pages.

#### Code Examples

```vb
' Define and add portfolio schema fields
field.Order = 2
field.Type = PdfPortfolioSchemaFieldType.String
field.Visible = True
schema.AddSchemaField(field)

field = New PdfPortfolioSchemaField()
field.Name = "Name"
field.Order = 3
field.Type = PdfPortfolioSchemaFieldType.String
field.Visible = True
schema.AddSchemaField(field)

' Add the Schema into the Portfolio.
document.PortfolioInformation.Schema = schema

' Create the file attachment with custom file attributes.
Dim pdfFile As New PdfAttachment("CorporateBrochure.pdf")
pdfFile.FileName = "CorporateBrochure.pdf"
pdfFile.PortfolioAttributes = New PdfPortfolioAttributes()
pdfFile.PortfolioAttributes.AddAttributes("Price", "250")
pdfFile.PortfolioAttributes.AddAttributes("Author Name", "Syncfusion")
pdfFile.PortfolioAttributes.AddAttributes("Year", "1981")

' Create the file attachment with custom file attributes.
Dim wordFile As New PdfAttachment("Stock.docx")
wordFile.FileName = "Stock.docx"
wordFile.PortfolioAttributes = New PdfPortfolioAttributes()
wordFile.PortfolioAttributes.AddAttributes("Price", "500")
wordFile.PortfolioAttributes.AddAttributes("Author Name", "Syncfusion")
wordFile.PortfolioAttributes.AddAttributes("Year", "1991")

document.Attachments.Add(pdfFile)
document.Attachments.Add(wordFile)
document.Pages.Add()
```

#### API Reference

- **Namespace**: `Syncfusion.Pdf.Portfolio`
- **Classes**:
  - **PdfPortfolioSchemaField**: Represents a schema field in a PDF portfolio.
    - **Properties**:
      - `Name`: Gets or sets the name of the schema field.
      - `Order`: Gets or sets the order of the schema field.
      - `Type`: Gets or sets the type of the schema field.
      - `Visible`: Gets or sets whether the schema field is visible.
  - **PdfPortfolioAttributes**: Represents attributes associated with a PDF file attachment.
    - **Method**: `AddAttributes(key, value)`
      - Adds a custom attribute to the file attachment.

#### RAG Annotations
<!-- tags: [syncfusion-sdk, winforms, pdf, portfolio, attributes, file attachments, custom fields] keywords: [portfolio schema, custom attributes, file attachments, Syncfusion, PDF attributes] -->
```