```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_149.jpeg
document_name: grid
page_number: 149
page_id: grid#page_149
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:58:30Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Key Cells Property Definitions

| Description   | Definition                                                                 |
|---------------|-----------------------------------------------------------------------------|
| Description   | Text that appears next to the check box.                                   |
| TriState      | Whether or not indeterminate value is supported.                          |
| CellValue     | Boolean true or false values, or empty (null or nothing).                |

### Setting Up a CheckBox Cell in C#

The following code example illustrates how to set the cell type to CheckBox in C#.

#### C#

```csharp
// Specify display values for True/False/Indeterminate.
gridControl1.TableStyle.CheckBoxOptions = new GridCheckBoxCellInfo("True", "False", "", false);

// Set up a check box with no tristate.
gridControl1[rowIndex, colIndex].CellValue = false;
gridControl1[rowIndex, colIndex].Description = "Click Me";
gridControl1[rowIndex, colIndex].CellType = "CheckBox";
gridControl1[rowIndex, colIndex].TriState = false;

// Set up a check box with tristate.
gridControl1[rowIndex, colIndex + 1].CellValue = true;
gridControl1[rowIndex, colIndex + 1].CellType = "CheckBox";
gridControl1[rowIndex, colIndex + 1].TriState = true;
gridControl1[rowIndex, colIndex + 1].Description = "TriState";
```

### Setting Up a CheckBox Cell in VB.NET

The following code example illustrates how to set the cell type to CheckBox in VB.NET.

#### VB.NET

```vbnet
' Specify display values for True/False/Indeterminate.
gridControl1.TableStyle.CheckBoxOptions = New GridCheckBoxCellInfo("True", "False", "", False)

' Set up a check box with no tristate.
gridControl1(rowIndex, colIndex).CellValue = False
gridControl1(rowIndex, colIndex).Description = "Click Me"
gridControl1(rowIndex, colIndex).CellType = "CheckBox"
gridControl1(rowIndex, colIndex).TriState = False

' Set up a check box with tristate.
gridControl1(rowIndex, colIndex + 1).CellValue = True
gridControl1(rowIndex, colIndex + 1).CellType = "CheckBox"
gridControl1(rowIndex, colIndex + 1).TriState = True
gridControl1(rowIndex, colIndex + 1).Description = "TriState"
```

<!-- tags: [Syncfusion Winforms, Essential Grid, CheckBox, TriState, CellValue, Windows Forms] keywords: [grid, checkbox, tristate, cellvalue, celltype, description, indeterminate, true, false, null, empty] -->
```