```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_189.jpeg
document_name: pdf
page_number: 189
page_id: pdf#page_189
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:35:47Z
fidelity: lossless
-->

## Saving and Closing the Document

### Code Example

```csharp
'Save and close the document.
document.Save("Sample.pdf")
document.Close(True)
```

---

## 4.1.3.4.2 Properties

| Property         | Description                                               | Type | Data Type                |
|------------------|-----------------------------------------------------------|------|---------------------------|
| Schema           | Gets or sets the schema field of the portfolio.           | NA   | PdfPortfolioSchema       |
| ViewMode         | Gets or sets the view mode of the portfolio.              | NA   | PdfPortfolioViewMode     |
| StartupDocument   | Gets or sets the startup document of portfolio.           | NA   | PdfAttachment            |

---

## 4.1.3.4.3 Adding Custom File Fields and Attributes into a PDF Portfolio

### Overview
- Custom file fields and attributes allow you to store any type of information about the attached files.
- You can add custom file fields and attributes into a PDF Portfolio using the `PdfPortfolioSchema` and `PdfPortfolioAttributes` classes.
- The following code example demonstrates how to add custom file fields and attributes into a PDF Portfolio.

### Code Example

```csharp
// Create a PDF document.
PdfDocument document = new PdfDocument();

// Create a new PDF Portfolio.
document.PortfolioInformation = new PdfPortfolioInformation();
document.PortfolioInformation.ViewMode = PdfPortfolioViewMode.Tile;

// Create a new Portfolio Schema.
PdfPortfolioSchema schema = new PdfPortfolioSchema();

// Create custom file fields.
```

---

<!-- tags: [pdf-portfolio, custom-fields, attributes, syncfusion-winforms, pdfdocument, portfolioinformation, viewmode] keywords: [custom file fields, attributes, pdf portfolio, schema, view mode, startup document, document save, document close] -->
```