```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_190.jpeg
document_name: pdf
page_number: 190
page_id: pdf#page_190
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:36:33Z
fidelity: lossless
-->

# Essential PDF

PdfPortfolioSchemaField field = new PdfPortfolioSchemaField();
field.Name = "Price";
field.Order = 1;
field.Type = PdfPortfolioSchemaFieldType.String;
field.Visible = true;
schema.AddSchemaField(field);

field = new PdfPortfolioSchemaField();
field.Name = "Author Name";
field.Order = 2;
field.Type = PdfPortfolioSchemaFieldType.String;
field.Visible = true;
schema.AddSchemaField(field);

field = new PdfPortfolioSchemaField();
field.Name = "Year";
field.Order = 3;
field.Type = PdfPortfolioSchemaFieldType.String;
field.Visible = true;
schema.AddSchemaField(field);

// Add the Schema into the Portfolio.
document.PortfolioInformation.Schema = schema;

// Create the file attachment with custom file attributes.
PdfAttachment pdfFile = new PdfAttachment("CorporateBrochure.pdf");
pdfFile.FileName = "CorporateBrochure.pdf";
pdfFile.PortfolioAttributes = new PdfPortfolioAttributes();
pdfFile.PortfolioAttributes.AddAttributes("Price", "250");
pdfFile.PortfolioAttributes.AddAttributes("Author Name", "Syncfusion");
pdfFile.PortfolioAttributes.AddAttributes("Year", "1981");

// Create the file attachment with custom file attributes.
PdfAttachment wordFile = new PdfAttachment("Stock.docx");
```

<!-- tags: [Essential PDF, PdfPortfolioSchemaField, PdfPortfolioSchemaFieldType, PdfPortfolioAttributes, Portfolio Information] keywords: [essentialpdf, pdfattachment, custom attributes, portfolio, schema, file attributes, author name, year, price] -->