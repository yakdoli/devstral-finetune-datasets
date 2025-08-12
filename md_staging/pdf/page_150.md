```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_150.jpeg
document_name: pdf
page_number: 150
page_id: pdf#page_150
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:33:49Z
fidelity: lossless
-->

# Essential PDF

```vb
Dim pdfGrid As New PdfGrid()

' dt is an object that can be an array (two-dimensional, one-
' dimensional or nested), a DataTable, DataColumn, DataView or DataSet.
pdfGrid.DataSource = dt
```

## Direct Rows and Columns

Alternatively, you can bind data to a PdfGrid without setting any data source. This is achieved using the PdfGridRow and PdfGridColumn classes. The following code example illustrates this.

### C#

```csharp
PdfPage pdfPage = pdfDocument.Pages.Add(); 

// Create a new PdfGrid.
PdfGrid pdfGrid = new PdfGrid();

// Add three columns.
pdfGrid.Columns.Add(3);

// Add header.
pdfGrid.Headers.Add(1);
PdfGridRow pdfGridHeader = pdfGrid.Headers[0];
pdfGridHeader.Cells[0].Value = "Employee ID";
pdfGridHeader.Cells[1].Value = "Employee Name";
pdfGridHeader.Cells[2].Value = "Salary";

// Add rows.
PdfGridRow pdfGridRow = pdfGrid.Rows.Add();
pdfGridRow.Cells[0].Value = "E01";
pdfGridRow.Cells[1].Value = "Clay";
pdfGridRow.Cells[2].Value = "$10,000";

// Draw the PdfGrid.
pdfGrid.Draw(pdfPage, PointF.Empty);
```

### VB.NET

```vb
Dim pdfPage As PdfPage = pdfDocument.Pages.Add()

' Create a new PdfGrid.
Dim pdfGrid As New PdfGrid()
```
```