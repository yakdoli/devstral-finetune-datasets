```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_585.jpeg
document_name: chart
page_number: 585
page_id: chart#page_585
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:51:36Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Learn how to export charts to PDF in a Windows Forms application using Syncfusion.

## Content

### Exporting Chart to PDF

Figure 357: Exporting Chart to PDF

1. **Add the Syncfusion.Pdf.Base and Syncfusion.Pdf.Windows assemblies.**
2. **Add the namespace `Syncfusion.Pdf` in your form.**

```csharp
[C#]
using Syncfusion.Pdf;
using Syncfusion.Pdf.Graphics;
```

```vbnet
[VB.NET]
Imports Syncfusion.Pdf
Imports Syncfusion.Pdf.Graphics
```

3. **Add the code snippet that is given below in your form.**

```csharp
[C#]
string fileName = Application.StartupPath + "\\chartexport";
string exportFileName = fileName + ".pdf";
string file = fileName + ".gif";
this.chartControl1.SaveImage(file);

// Create a PDF document
PdfDocument pdfDoc = new PdfDocument();

// Add a page to the empty PDF document
pdfDoc.Pages.Add();

// Draw chart image in the first page
pdfDoc.Pages[0].Graphics.DrawImage(PdfImage.FromFile(file), new PointF(10, 30));

// Save the PDF Document to disk.
pdfDoc.Save(exportFileName);

// Launches the file.
System.Diagnostics.Process.Start(exportFileName);
```

```vbnet
[VB.NET]
Dim fileName As String = Application.StartupPath & "\chartexport"
```

## Tips and Considerations
- Ensure that the necessary assemblies are referenced in your project.
- Adjust file paths and chart settings as per your application requirements.

## Cross References
- See also: Syncfusion.Pdf documentation for additional PDF features.

<!-- tags: [Syncfusion, Windows Forms, Chart, PDF Export, C#, VB.NET] keywords: [chart export, windows forms, pdf, syncfusion, csharp, vb.net] -->
```