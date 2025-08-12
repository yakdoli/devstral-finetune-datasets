```html
<!--  
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_096.jpeg
document_name: calculate
page_number: 096
page_id: calculate#page_096
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:05:33Z
fidelity: lossless
--> 

## Overview
- Indicates a technical guide for creating and managing an Excel workbook object using the Syncfusion Essential Calculate library in a WinForms application.
- Demonstrates the instantiation and setup of a workbook object from an Excel file and performing preliminary calculations to establish dependencies.
- Shows the initial setup of a form with combo boxes and how they relate to the instantiated Excel workbook.
- Provides both C# and VB.NET code examples for the same functionality.

## Content

### WinForms Workbook Initialization Code

```csharp
private void Form1_Load(object sender, System.EventArgs e)
{
    // 1) Instantiates the workbook object from the spreadsheet file.
    calcWB = ExcelRWCalcWorkbook.CreateFromXLS(@"CarIns.xls");

    // 2) Do all calculations so that dependencies are known.
    this.calcWB.Engine.LockDependencies = false;
    this.calcWB.CalculateAll();

    // this.calcWB.Engine.CalculatingSuspended = true;
    this.calcWB.Engine.LockDependencies = true;

    // 3) Set some initial values on the form.
    this.comboBoxSex.SelectedIndex = 0;
    this.comboBoxState.SelectedIndex = 0;
    this.comboBoxModel.SelectedIndex = 0;
}
```

```vb
[VB]

Private calcWB As ExcelRWCalcWorkbook

Private Sub Form1_Load(sender As Object, e As System.EventArgs)
    ' 1) Instantiate the workbook object from the spreadsheet file.
    calcWB = ExcelRWCalcWorkbook.CreateFromXLS("CarIns.xls")

    ' 2) Do all calculations so that dependencies are known.
    Me.calcWB.Engine.LockDependencies = False
    Me.calcWB.CalculateAll()

    ' Me.calcWB.Engine.CalculatingSuspended = True
    Me.calcWB.Engine.LockDependencies = True

    ' 3) Set some initial values on the form.
    Me.comboBoxSex.SelectedIndex = 0
    Me.comboBoxState.SelectedIndex = 0
    Me.comboBoxModel.SelectedIndex = 0
End Sub
```

### Explanation of the Code

The following is an explanation of the preceding code.

1. **Workbook Instantiation**: 
   - **Usage**: Uses a static member, `ExcelRWWorkbook.CreateFromXLS`, to read and instantiate an `ExcelRWWorkbook` object from the given XLS file. (The `CreateFromXLS` method relies on Essential XlsIO to actually do this work.)
   - **Description**: This step involves loading an existing Excel file (`CarIns.xls`) into memory as a workbook object. This enables further interaction with the Excel workbook's data and formulas via the Essentia Action Calculate library.

---

<!-- tags: [Syncfusion, WinForms, Essential Calculate, ExcelRWWorkbook, CalculateFromXLS, CarIns.xls, Version: 11.4.0.26] keywords: [workbook object, calculate dependencies, form initialization, combo boxes, Excel file loading] -->
```