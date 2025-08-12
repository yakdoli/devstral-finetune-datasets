```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_406.jpeg
document_name: grid
page_number: 406
page_id: grid#page_406
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:14:41Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

Our Essential Grid control supports conversion of grid content to a PDF file. Data in Grid control can be converted to a PDF document for offline verification and/or computation. This can be achieved by making use of the GridPDFConverter class. The PDF libraries are used to support the conversion of grid content to a PDF page.

For making the control functional, the following dll files should be added along with the default dll files in the reference folder:

- Syncfusion.Pdf.Base
- Syncfusion.GridHelperClasses.Windows.

The ExportToPdf method is used to export the grid content to a PDF file. Following code example illustrates how to convert the content in grid to PDF.

### Using C#

```csharp
[C#]

GridPDFConverter pdfConverter = new GridPDFConverter(); 
pdfConverter.ExportToPdf("Sample1.pdf", this.gridControl1);
```

### Using VB.NET

```vb
[VB.NET]

Dim pdfConverter As GridPDFConverter = New GridPDFConverter()
pdfConverter.ExportToPdf("Sample1.pdf", Me.gridControl1)
```

<!-- tags: [pdf conversion, grid, windows forms, syncfusion, GridPDFConverter, exporttoPdf, dll files] keywords: [grid content, pdf document, offline verification, computation, reference folder, sample export code, C#, VB.NET] -->
```