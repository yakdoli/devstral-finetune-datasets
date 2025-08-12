```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_120.jpeg
document_name: grid
page_number: 120
page_id: grid#page_120
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:37:19Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates the process of exporting grid data to an Excel file using the GridExcelConverterControl.
- Includes handling modal dialogs for file selection and saving the output in a valid Excel format.
- Focuses on utilizing Syncfusion's Excel conversion utilities to streamline the export process.

## Content

### C# Example

The following code snippet illustrates how to export grid data as an Excel file. It uses the GridExcelConverterControl to convert grid data into an Excel workbook, allowing users to choose a file name and location for saving.

```csharp
private void buttonExport_Click(object sender, System.EventArgs e)
{
    SaveFileDialog saveFileDialog = new SaveFileDialog();
    saveFileDialog.Filter = "Files(*.XLS)|*.XLS";
    saveFileDialog.AddExtension = true;
    saveFileDialog.DefaultExt = ".XLS";

    if (saveFileDialog.ShowDialog() == DialogResult.OK && 
        saveFileDialog.CheckPathExists)
    {
        GridExcelConverterControl gec = new GridExcelConverterControl();
        IWorkbook workBook = ExcelUtils.CreateWorkbook(new string[] { "Sheet1", "Sheet2" });
        gec.GridToExcel(this.gridControl1.Model, workBook.Worksheets[0]);
        gec.GridToExcel(this.gridControl2.Model, workBook.Worksheets[1]);
        workBook.SaveAs(saveFileDialog.FileName);
        workBook.Close();
        ExcelUtils.ThrowNotSavedOnDestroy = false;
    }
}
```

### VB.NET Example

The following VB.NET code snippet demonstrates a similar functionality, exporting grid data to an Excel file. It also uses the GridExcelConverterControl and integrates a file dialog for user interaction.

```vb
Imports Syncfusion.XlsIO
Imports Syncfusion.GridExcelConverter

Private Sub buttonExport_Click(ByVal sender As Object, ByVal e As System.EventArgs)
    Dim saveFileDialog As SaveFileDialog = New SaveFileDialog()
    saveFileDialog.Filter = "Files(*.XLS)|*.XLS"
    saveFileDialog.AddExtension = True
    saveFileDialog.DefaultExt = ".XLS"
    If saveFileDialog.ShowDialog() = DialogResult.OK And Also saveFileDialog.CheckPathExists Then
        Dim gec As GridExcelConverterControl = New GridExcelConverterControl
        Dim workbook As IWorkbook = ExcelUtils.CreateWorkbook(New String() { "Sheet1", "Sheet2" })
        gec.GridToExcel(Me.gridControl1.Model, workBook.Worksheets(0))
        gec.GridToExcel(Me.gridDataBoundGrid1.Model, workbook.Worksheets(1))
        workbook.SaveAs(saveFileDialog.FileName)
        workBook.Close()
        ExcelUtils.ThrowNotSavedOnDestroy = False
    End If
End Sub
```

## API Reference

### Classes and Methods
- **SaveFileDialog**: A component used to display a standard dialog box that allows the user to select a file.
- **GridExcelConverterControl**: A utility class in Syncfusion for converting grid data into Excel format.
- **ExcelUtils.CreateWorkbook**: Creates a new Excel workbook with specified worksheet names.
- **GridToExcel**: Converts the model of a grid control into an Excel worksheet.
- **SaveAs**: Saves the workbook with the specified file name.
- **ThrowNotSavedOnDestroy**: A flag in ExcelUtils to suppress exceptions when a workbook is closed without being saved.

## Code Examples

The provided code examples include both C# and VB.NET implementations for exporting grid data to Excel. They demonstrate the following steps:
1. **Using SaveFileDialog**: Opens a file save dialog where users can select a file name and location.
2. **Creating an Excel Workbook**: Initializes a new Excel workbook with predefined sheet names.
3. **Converting Grid Data**: Converts the grid's model data into an Excel format using the GridExcelConverterControl.
4. **Saving the Workbook**: Saves the converted workbook with the user-specified file name.

## Cross References

- For more information on GridExcelConverterControl and ExcelUtils, refer to the Syncfusion documentation on [Excel Conversion Utilities](#).
- For handling file dialogs in Windows Forms, see the section on [File Dialogs](#).

## RAG Annotations

<!-- tags: [grid, windows-forms, syncfusion, excel-export, file-dialog, converter] keywords: [gridexcelconvertercontrol, excelfILE EXPORT, windows forms, xlsx format, worksheet names, file dialog] -->
```