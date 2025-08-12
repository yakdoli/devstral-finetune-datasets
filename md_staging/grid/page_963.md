```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_963.jpeg
document_name: grid
page_number: 963
page_id: grid#page_963
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:52:50Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Essential Grid Grouping control supports the conversion of grid contents to a PDF file.
- Users can convert data from the Grid Grouping control into a PDF document using the GridPDFConverter class.
- PDF libraries are used to support the conversion of grid content to a PDF page.
- Requires specific DLL files to ensure the conversion of grid data to a PDF document.

## Content

### Conversion to PDF
To ensure the conversion of grid data to a PDF document, the following dll files should be added, along with the default dll files in the reference folder:

- Syncfusion.Pdf.Base
- Syncfusion.GridHelperClasses.Windows

The `ExportToPdf` method should be used to export the grid to a PDF file.

### Code Example for Conversion

The following code example illustrates the conversion of grid data to a PDF document.

#### C#
```csharp
GridPDFConverter pdfConvertor = new GridPDFConverter();
pdfConvertor.ExportToPdf("Sample.pdf", this.gridGroupingControl1.TableControl);

// Launching the PDF file by using the default Application [Acrobat Reader].
System.Diagnostics.Process.Start("Sample.pdf");
```

#### VB.NET
```vb
Dim pdfConvertor As GridPDFConverter = New GridPDFConverter()
pdfConvertor.ExportToPdf("Sample.pdf", Me.gridGroupingControl1.TableControl)

' Launching the PDF file by using the default Application [Acrobat Reader].
System.Diagnostics.Process.Start("Sample.pdf")
```

### Summary
- The `ExportToPdf` method is used to convert the grid data into a PDF file.
- Ensure that the necessary DLL files are included in the project to support the conversion process.

## Cross References
See also:
- [GridPDFConverter](#GridPDFConverter)
- [Sample.pdf](#Sample.pdf)
- [GridGroupingControl](#GridGroupingControl)

<!-- tags: [Essential Grid, Grid Grouping, PDF Conversion, Windows Forms, GridPDFConverter, Sample.pdf, GridGroupingControl, ExportToPdf] keywords: [grid, pdf, conversion, windows forms, export, dll files, Acrobat Reader, Syncfusion Winforms] -->
```