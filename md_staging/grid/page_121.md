```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_121.jpeg
document_name: grid
page_number: 121
page_id: grid#page_121
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:36:47Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Content

### 3.1.6.6 Exporting Grid Data to Excel 2010

You can export Grid data to Excel 2010. To do this, you must explicitly set the Excel version by creating an XlsIO application, and then export the Grid data to the Excel worksheet.

You can set the `DefaultVersion` to `Excel2010` to export to this version, by default. Similarly, you can also export Grid data to other versions of Excel.

The following code example illustrates this.

```csharp
[C#]
ExcelEngine engine = new ExcelEngine();
IApplication app = engine.Excel.Application;

app.DefaultVersion = ExcelVersion.Excel2010;
IWorkbook book = app.Workbooks.Create();

GroupingGridExcelConverterControl gecc = new GroupingGridExcelConverterControl();
SaveFileDialog saveFileDialog = new SaveFileDialog();

saveFileDialog.Filter = "Files(*.xlsx)|*.xlsx";
saveFileDialog.DefaultExt = ".xlsx";

if (saveFileDialog.ShowDialog() == System.Windows.Forms.DialogResult.OK)
{
    gecc.GroupingGridToExcel(this.gridGroupingControl1, book.Worksheets(0), ConverterOptions.Visible);

    book.SaveAs(saveFileDialog.FileName());

    if (MessageBox.Show("Do you wish to open the xls file now?", "Export to Excel", MessageBoxButtons.YesNo, MessageBoxIcon.Question) == System.Windows.Forms.DialogResult.Yes)
    {
        Process proc = new Process();
        proc.StartInfo.FileName = saveFileDialog.FileName;
    }
}
```

## API Reference

This section provides additional reference materials related to exporting Grid data to Excel, including the `ExcelEngine`, `IApplication`, and `IWorkbook` classes, as well as the `GroupingGridExcelConverterControl` and `SaveFileDialog` components. For detailed API documentation, refer to the official Syncfusion documentation.

## Code Examples

```csharp
[C#]
// Complete example
using Syncfusion.ComponentModel;
using Syncfusion.Excel.IO;
using Syncfusion.Windows.Forms.Grid;

// ...

ExcelEngine engine = new ExcelEngine();
IApplication app = engine.Excel.Application;

app.DefaultVersion = ExcelVersion.Excel2010;
IWorkbook book = app.Workbooks.Create();

GroupingGridExcelConverterControl gecc = new GroupingGridExcelConverterControl();
SaveFileDialog saveFileDialog = new SaveFileDialog();

saveFileDialog.Filter = "Files(*.xlsx)|*.xlsx";
saveFileDialog.DefaultExt = ".xlsx";

if (saveFileDialog.ShowDialog() == System.Windows.Forms.DialogResult.OK)
{
    gecc.GroupingGridToExcel(this.gridGroupingControl1, book.Worksheets(0), ConverterOptions.Visible);

    book.SaveAs(saveFileDialog.FileName);

    if (MessageBox.Show("Do you wish to open the xls file now?", "Export to Excel", MessageBoxButtons.YesNo, MessageBoxIcon.Question) == System.Windows.Forms.DialogResult.Yes)
    {
        Process proc = new Process();
        proc.StartInfo.FileName = saveFileDialog.FileName;
        proc.Start();
    }
}
```

## Cross References

See also:
- `Syncfusion.Windows.Forms.Grid.GroupingGridExcelConverterControl`
- `Syncfusion.Excel.IO.ExcelEngine`
- `Syncfusion.Excel.IO.IWorkbook`

<!-- tags: [Syncfusion Winforms, Grid, Excel, Export, 11.4.0.26] keywords: [grid data, Excel 2010, export, Excel version, XlsIO, GroupingGridExcelConverterControl, SaveFileDialog, ExcelEngine, IApplication, IWorkbook, Syncfusion] -->
```
