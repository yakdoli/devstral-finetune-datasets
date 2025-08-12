```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_037.jpeg
document_name: PivotGrid
page_number: 037
page_id: PivotGrid#page_037
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:54:40Z
fidelity: lossless
-->

# Essential PivotGrid WindowsForms

```csharp
PivotWordExport wordExport = new PivotWordExport();
wordExport.pivotGridToWord(savedialog.FileName, pivotGridControl1);
```

```vb
Dim wordExport As New PivotWordExport()
wordExport.pivotGridToWord(savedialog.FileName, pivotGridControl1)
```

Merging is applied to all the cells and the exported file is as same as that of the original PivotGrid. The formatting is applied based on the visual styles of the grid.

The below image depicts the conversion of PivotGrid content to a Word file:

|             | Canada                                                                                                     |                                                                                                                       |
|-------------|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
|             | Alberta                                                                                                    |                                                                                                                       |
|             | 1                                                                                                         | 10                                                                                                                    |
|             | Quantity                                      | Year                                                                                   | Quantity                                                  | Year                |
| Bike        | FY 2005                                       | 25                                                                                   | 25                                                         | 28                  |
|             | FY 2006                                       | 9                                                                                    | 9                                                          | 11                  |
|             | FY 2007                                       | 4                                                                                    | 4                                                          | 4                   |
| Bike Total  | 38                                            | 38                                                                                   | 43                                                         | 43                  |
| Car         | FY 2005                                       | 6                                                                                    | 6                                                          | 4                   |
|             | FY 2006                                       | 1                                                                                    | 1                                                          | 1                   |
|             | FY 2007                                       | 1                                                                                    | 1                                                          | 2                   |
| Car Total   | 8                                             | 8                                                                                    | 7                                                          | 7                   |
| Grand Total | 46                                            | 46                                                                                   | 50                                                         | 50                  |

## Exporting to PDF:

Essential Grid control supports conversion of PivotGrid content to a PDF file. Data in the PivotGrid control can be converted to a PDF document for offline verification and/or computation. This can be achieved by making use of the `PivotPdfExport` class. The PDF libraries are used to support the conversion of PivotGrid content to a PDF page.

While exporting to PDF, PivotGrid is read row by row and exported into the PDF document.

The `Export` method is used to export PivotGrid content to a PDF file. The following sample code illustrates how to convert the PivotGrid content to PDF.

```csharp
PivotPdfExport pdfExport = new PivotPdfExport(pivotGridControl1);
pdfExport.Export(savedialog.FileName);
```

<!-- tags: [syncfusion, winforms, pivotgrid, pdf export, word export, essential grid, pdf, offline verification, data export, version 11.4.0.26, word document, merging, formatting, visual styles, sample code] -->
```