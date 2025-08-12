```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_501.jpeg
document_name: grid
page_number: 501
page_id: grid#page_501
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:20:32Z
fidelity: lossless
-->


# Essential Grid for Windows Forms

<table>
  <thead>
    <tr>
      <th>GridPrintOptions</th>
      <th>Used to customize the printing of a grid.</th>
      <th>enum</th>
      <th>enum</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>GridPrintOptions Name</td>
      <td>Description</td>
    </tr>
    <tr>
      <td>MultiGridPrinting</td>
      <td>
        Multiple grids are printed in a single print continuously one after another.
      </td>
    </tr>
    <tr>
      <td>PrintGridInNewPage</td>
      <td>Prints multiple grids in a new page.</td>
    </tr>
    <tr>
      <td>DefaultGridPrint</td>
      <td>
        Default grid printing without column breaks for each new page.
      </td>
    </tr>
    <tr>
      <td>ScaleColumnsToFit</td>
      <td>Multiple grid columns are scaled to fit the printed page.</td>
    </tr>
  </tbody>
</table>

## Sample Link
- Installed
- Location>\Syncfusion\EssentialStudio\<InstalledVersion>\Windows\Grid.Windows\Samples\2.0\Printing\Multi - GridPrinting

## 4.1.4.21.1 Adding Multi-Grid Printing to an Application

- The Print Preview can be enabled by using the MultipleGridPrintDocument class or by clicking the Print Preview button under the Grid Printing Options in the UI.
- Headers and footers can be added by using the DrawGridPrintHeader and DrawGridPrintFooter events or by selecting the Show Header and Footer check box under the Grid Printing Options in the UI.

```csharp
[C#]

List<Control> gridsToPrint = new List<Control>();
foreach (Control cd in this.Controls)
{
    if (cd is Control)
    {
        gridsToPrint.Add((Control)cd);
    }
}
MultiGridPrintDocument pd = new MultiGridPrintDocument(gridsToPrint);
pd.GridPrintOption = MultiGridPrintDocument.GridPrintOptions.MultipleGridPrint;
pd.ShowHeaderFooterOnAllPages = true;
PrintPreviewDialog printDialog = new PrintPreviewDialog();
printDialog.Document = pd;
```
```html
<!-- tags: [grids, multi-grid-printing, printing, windows-forms, version:] keywords: [Syncfusion, Grid, Windows Forms, printing, multi-grid printing, print preview, headers, footers] -->
```