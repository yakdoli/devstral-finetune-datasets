```html
<!--  
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_038.jpeg
document_name: PivotGrid
page_number: 038
page_id: PivotGrid#page_038
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:54:46Z
fidelity: lossless
-->

# Essential PivotGrid WindowsForms

```vb
Dim pdfExport As New PivotPdfExport(pivotGridControl1)
pdfExport.Export(savedialog.FileName)
```

The below image depicts the conversion of PivotGrid content to a PDF file:

|               | Canada                                      |                                  |                                  |                                  |                                  |                                  |                                  |                                  |                                  |                                  |                                  |                                  |                                  |                                  |                                  |
|---------------|---------------------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|
|               | **Alberta**                                 |                                  |                                  |                                  |                                  |                                  |                                  |                                  |                                  |                                  |                                  |                                  |                                  |                                  |
|               | **1**                                      | **10**                          | **11**                          | **2**                          | **3**                          | **4**                          | **5**                          |                                  |                                  |                                  |                                  |                                  |                                  |                                  |                                  |
|               | **Quantity**                               | **Year**                        | **Quantity**                    | **Year**                        | **Quantity**                    | **Year**                        | **Quantity**                    | **Year**                        | **Quantity**                    | **Year**                        | **Quantity**                    | **Year**                        | **Quantity**                    | **Year**                        |
| **Bike**      | FY 2005                                    | 25                              | 28                              | 28                              | 39                              | 39                              | 32                              | 32                              | 38                              | 38                              | 47                              | 47                              | 43                              | 43                              |
|               | FY 2006                                    | 9                               | 11                              | 11                              | 8                               | 8                               | 14                              | 14                              | 15                              | 15                              | 8                               | 8                               | 15                              | 15                              |
|               | FY 2007                                    | 4                               | 4                               | 4                               | 2                               | 2                               | 6                               | 6                               | 6                               | 6                               | 4                               | 4                               | 5                               | 5                               |
| **Bike Total**| 38                                         | 38                              | 43                              | 43                              | 49                              | 49                              | 52                              | 52                              | 59                              | 59                              | 59                              | 59                              | 63                              | 63                              |
| **Car**       | FY 2005                                    | 6                               | 6                               | 4                               | 4                               | 10                              | 10                              | 9                               | 9                               | 4                               | 4                               | 9                               | 9                               | 8                               | 8                               |
|               | FY 2006                                    | 1                               | 1                               | 1                               | 2                               | 2                               | 1                               | 1                               | 4                               | 4                               | 1                               | 1                               | 1                               | 1                               |
|               | FY 2007                                    | 1                               | 2                               | 2                               | 1                               | 1                               | 1                               | 1                               | 1                               | 1                               | 1                               | 1                               | 1                               | 1                               |
| **Car Total** | 8                                          | 8                               | 7                               | 7                               | 13                              | 13                              | 10                              | 10                              | 9                               | 9                               | 10                              | 10                              | 10                              | 10                              |
| **Grand Total**| 46                                         | 46                              | 50                              | 50                              | 62                              | 62                              | 62                              | 62                              | 68                              | 69                              | 69                              | 73                              | 73                              | 73                              |

## Sample Location
A sample is placed in the following location:

`<Installed Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\PivotGrid.Windows\Samples\2.0\Exporting\Export Demo`

### 4.10 Print Option
The print option is extended for the PivotGrid control to allow users to preview the contents before the contents are printed on paper.

This feature is used to print the PivotGrid control in landscape and portrait views. This feature has overridden the GridPrintDocumentAdv from Syncfusion.GridHelperClasses.Windows.

The pivot grid visual style color is automatically applied in the printed document based on the visual styles of the grid.

The print functionality can be invoked using the following code:

```csharp
private void button1_Click_1(object sender, EventArgs e)
{
    try
    {
        PivotGridPrintDocumentAdv pd = new PivotGridPrintDocumentAdv(this.pivotGridControl1);
    }
}
```

<!-- tags: [WinForms, PivotGrid, Exporting, Printing, GridPrintDocument, Syncfusion] keywords: [export, pdf, print, preview, landscape, portrait, visual style, color, PivotGridPrintDocument] -->
```