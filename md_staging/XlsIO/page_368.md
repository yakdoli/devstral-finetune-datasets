```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_368.jpeg
document_name: XlsIO
page_number: 368
page_id: XlsIO#page_368
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:13:53Z
fidelity: lossless
-->

# Essential XlsIO

```csharp
// Initialize the PDF document
PdfDocument pdfDoc = new PdfDocument();

// Initialize the ExcelToPdfConverterSettings
ExcelToPdfConverterSettings settings = new ExcelToPdfConverterSettings();

// Set the Layout Options for the output PDF page.
settings.LayoutOptions = LayoutOptions.FitSheetOnOnePage;

// Assign the PDF document to the TemplateDocument property of ExcelToPdfConverterSettings
settings.TemplateDocument = pdfDoc;
settings.DisplayGridLines = GridLinesDisplayStyle.Invisible;

// Convert the Excel document to PDF document
pdfDoc = converter.Convert(settings);

// Save the PDF file
pdfDoc.Save("ExceltoPdf.pdf");
```

### [VB.NET]

```vb
'Open the Excel document you want to convert
Dim converter As New ExcelToPdfConverter("Sample.xlsx")

'Initialize the PDF document
Dim pdfDoc As New PdfDocument()

'Initialize the ExcelToPdfConverterSettings
Dim settings As New ExcelToPdfConverterSettings()

'Set the Layout Options for the output PDF page.
settings.LayoutOptions = LayoutOptions.FitSheetOnOnePage

'Assign the PDF document to the TemplateDocument property of 
```

## API Reference

- **Namespace**: Syncfusion.XlsIO
- **Class**: ExcelToPdfConverter
- **Members**:
  - **Methods**:
    - `Convert(settings)`:
      - **Parameters**:
        - `settings` - A `ExcelToPdfConverterSettings` object.
      - **Returns**: `PdfDocument` - The resulting PDF document.
  - **Properties**:
    - `DisplayGridLines` - Specifies the grid lines visibility.
    - `LayoutOptions` - Specifies the layout options for the output PDF page.
    - `TemplateDocument` - The PDF document to be used as a template.

## Code Examples

### C#

```csharp
// Initialize the PDF document
PdfDocument pdfDoc = new PdfDocument();

// Initialize the ExcelToPdfConverterSettings
ExcelToPdfConverterSettings settings = new ExcelToPdfConverterSettings();

// Set the Layout Options for the output PDF page.
settings.LayoutOptions = LayoutOptions.FitSheetOnOnePage;

// Assign the PDF document to the TemplateDocument property of ExcelToPdfConverterSettings
settings.TemplateDocument = pdfDoc;
settings.DisplayGridLines = GridLinesDisplayStyle.Invisible;

// Convert the Excel document to PDF document
pdfDoc = converter.Convert(settings);

// Save the PDF file
pdfDoc.Save("ExceltoPdf.pdf");
```

### VB.NET

```vb
Dim converter As New ExcelToPdfConverter("Sample.xlsx")
Dim pdfDoc As New PdfDocument()
Dim settings As New ExcelToPdfConverterSettings()

settings.LayoutOptions = LayoutOptions.FitSheetOnOnePage
settings.TemplateDocument = pdfDoc
settings.DisplayGridLines = GridLinesDisplayStyle.Invisible

pdfDoc = converter.Convert(settings)
pdfDoc.Save("ExceltoPdf.pdf")
```

## Page-level Navigation/TOC
- [ExcelToPdfConverter](#exceltopdfconverter)
- [ExcelToPdfConverterSettings](#exceltopdfconvertersettings)
- [PdfDocument](#pdfdocument)

## Cross References
- See also: [Syncfusion XlsIO Documentation](#syncfusion-xlsio-documentation)

<!-- tags: [XlsIO, Excel, PDF, Converter, Winforms] keywords: [ExcelToPdfConverter, ExcelToPdfConverterSettings, PdfDocument, LayoutOptions, DisplayGridLines, TemplateDocument] -->
```