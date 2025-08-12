```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_191.jpeg
document_name: pdf
page_number: 191
page_id: pdf#page_191
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:37:01Z
fidelity: lossless
-->

# Essential PDF

```csharp
    wordFile.FileName = "Stock.docx";
    wordFile.PortfolioAttributes = new PdfPortfolioAttributes();
    wordFile.PortfolioAttributes.AddAttributes("Price", "500");
    wordFile.PortfolioAttributes.AddAttributes("Author Name", "Syncfusion");
    wordFile.PortfolioAttributes.AddAttributes("Year", "1991");

    document.Attachments.Add(pdfFile);
    document.Attachments.Add(wordFile);
    document.Pages.Add();

    document.Save("sample.pdf");
```

### [VB.NET]

```vb
    ' Create a PDF document.
    Dim document As New PdfDocument()

    ' Create a new PDF Portfolio.
    document.PortfolioInformation = New PdfPortfolioInformation()
    document.PortfolioInformation.ViewMode = PdfPortfolioViewMode.Tile

    ' Create a new Portfolio Schema.
    Dim schema As New PdfPortfolioSchema()

    ' Create custom file fields.
    Dim field As New PdfPortfolioSchemaField()
    field.Name = "Price"
    field.Order = 1
    field.Type = PdfPortfolioSchemaFieldType.String
    field.Visible = True
    schema.AddSchemaField(field)

    field = New PdfPortfolioSchemaField()
    field.Name = "Author Name"
```
```