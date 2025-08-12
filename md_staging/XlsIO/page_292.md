```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_292.jpeg
document_name: XlsIO
page_number: 292
page_id: XlsIO#page_292
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:09:06Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Demonstrates how to manipulate combo box controls in Excel spreadsheets using code.
- Explains methods for reading, creating, and selecting combo box items.
- Provides examples in both C# and VB.NET.

## Content

### Manipulating Combo Boxes in Excel Spreadsheets

```csharp
// Select an item.
comboBox1.SelectedIndex = 6;

// Read a Combo Box.
IComboBoxShape comboBox2 = sheet.ComboBoxes[0];
comboBox2.SelectedIndex = 3;
```

#### VB.NET Example

```vb
' Create a Combo Box.
Dim comboBox1 As IComboBoxShape = sheet.ComboBoxes.AddComboBox(27, 5, 20, 100)

' Assign a value to the Combo Box.
comboBox1.ListFillRange = sheet("A1:A12")
comboBox1.LinkedCell = sheet("C3")

' Select an item.
comboBox1.SelectedIndex = 6

' Read a Combo Box.
Dim comboBox2 As IComboBoxShape = sheet.ComboBoxes(0)
comboBox2.SelectedIndex = 3
```

### Visual Representation

![Figure 98: Combo Box control added to the Spreadsheet by using Essential XlsIO](https://i.imgur.com/V5zrZ9O.png)

### Explanation
- **Creating a Combo Box**: The code demonstrates how to add a combo box to an Excel spreadsheet using `AddComboBox` with specified parameters for position, size, and other properties.
- **Assigning Values**: The `ListFillRange` property links the combo box to a range of cells to populate its dropdown list. The `LinkedCell` property ensures changes in the combo box are reflected in the specified linked cell.
- **Selecting an Item**: The `SelectedIndex` property is used to set or retrieve the currently selected item in the combo box.

## API Reference

### Classes and Methods
- **XlsIO**: The main library for manipulating Excel files.
- **IComboBoxShape**: Interface for working with combo box controls in Excel.
  - **AddComboBox(x, y, width, height)**: Creates a new combo box at the specified coordinates and dimensions.
  - **ListFillRange**: Sets the range of cells that populate the combo box's dropdown list.
  - **LinkedCell**: Links the selected item in the combo box to a specific cell.
  - **SelectedIndex**: Gets or sets the index of the currently selected item in the combo box.

## Code Examples

### C#

```csharp
using Syncfusion.XlsIO;
// Create a new instance of the Excel engine.
var excelEngine = new ExcelEngine();
// Access the XlsIO application instance.
IApplication application = excelEngine.Excel;
IWorkbook workbook = application.Workbooks.Create();

// Access the first worksheet.
IWorksheet sheet = workbook.Worksheets[0];

// Add a combo box to the worksheet.
IComboBoxShape comboBox1 = sheet.ComboBoxes.AddComboBox(200, 50, 100, 30);

// Populate the combo box from a range of cells.
comboBox1.ListFillRange = sheet.Range["A1:A10"];
comboBox1.LinkedCell = sheet.Range["C1"];
comboBox1.SelectedIndex = 3;

// Save the workbook and dispose of resources.
workbook.SaveAs("ComboBoxExample.xlsx");
workbook.Close();
exceEngine.Dispose();
```

### VB.NET

```vb
Imports Syncfusion.XlsIO
' Create a new instance of the Excel engine.
Dim excelEngine As New ExcelEngine()
' Access the XlsIO application instance.
Dim application As IApplication = excelEngine.Excel
Dim workbook As IWorkbook = application.Workbooks.Create()

' Access the first worksheet.
Dim sheet As IWorksheet = workbook.Worksheets(0)

' Add a combo box to the worksheet.
Dim comboBox1 As IComboBoxShape = sheet.ComboBoxes.AddComboBox(200, 50, 100, 30)

' Populate the combo box from a range of cells.
comboBox1.ListFillRange = sheet.Range("A1:A10")
comboBox1.LinkedCell = sheet.Range("C1")
comboBox1.SelectedIndex = 3

' Save the workbook and dispose of resources.
workbook.SaveAs("ComboBoxExample.xlsx")
workbook.Close()
exceEngine.Dispose()
```

## Conclusion
The above sections illustrate how to effectively use the XlsIO library to work with combo box controls in Excel spreadsheets, providing both C# and VB.NET examples for clarity.

<!-- tags: [xlsio, combo box, excel, syncfusion winforms, creating controls, linked cell, list fill range] keywords: [xlsio, combo box, excel, add combo box, linkedcell, listfillrange, selectedindex] -->
```