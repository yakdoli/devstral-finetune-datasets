```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_099.jpeg
document_name: calculate
page_number: 099
page_id: calculate#page_099
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:04:49Z
fidelity: lossless
-->

## Content

### Overview
This section explains the process of setting input values into a CalcSheet in a Windows Forms application using VB.NET. The code snippet shows how to populate various fields in the CalcSheet based on user inputs from controls on the form. 

#### Code Example

```vb
Private ageRow As Integer = 3
Private sexRow As Integer = 4
Private stateRow As Integer = 5
Private pointsRow As Integer = 6
Private modelRow As Integer = 7
Private modelYearRow As Integer = 8
Private multipleDiscountRow As Integer = 9

Private Sub SetSheetInputs()
    Dim inputSheet As CalcSheet = Me.calcWB("Inputs")
    inputSheet(ageRow, 2) = Me.numericUpDownAge.Value.ToString()
    inputSheet(sexRow, 2) = Me.comboSex.Text(0).ToString()
    inputSheet(stateRow, 2) = Me.comboState.Text
    inputSheet(pointsRow, 2) = Me.numericUpDownPoints.Value.ToString()
    inputSheet(modelRow, 2) = Me.comboModel.Text
    inputSheet(modelYearRow, 2) = Me.numericUpDownModelYear.Value.ToString()
    If Me.checkBoxMultipleDiscounts.Checked Then
        inputSheet(multipleDiscountRow, 2) = "Yes"
    Else
        inputSheet(multipleDiscountRow, 2) = "No"
    End If
    inputSheet(3, 5) = Me.textBoxBaseAmount.Text
End Sub
```

#### Explanation of the Code

1. **Calls a method to take the values from the controls on the form and move them into the Inputs sheet of the workbook.**
   - The `SetSheetInputs` subroutine transfers values from various form controls (like textbox, combobox, numeric updown, and checkbox) into specific cells of the `Inputs` sheet in a CalcWorkbook.

2. **Commented Code for Compatibility with CalculatingSuspended Property**
   - If the `CalculatingSuspended` property is set to `True`, this ensures that the value in cell A1 of the Outputs sheet is current. However, since calculations are suspended, this code is not needed in the current context.
   
3. **Retrieving the Computed Value from the Output Sheet**
   - The calculated value is stored in cell A1 of the `Outputs` sheet. To retrieve this value, you need to index the workbook with the sheet name and then index the sheet to return the value. This is represented as `calcWB["Outputs"][1,1]`.

## API Reference

### Members
- `ageRow`: Integer, initialized to 3.
- `sexRow`: Integer, initialized to 4.
- `stateRow`: Integer, initialized to 5.
- `pointsRow`: Integer, initialized to 6.
- `modelRow`: Integer, initialized to 7.
- `modelYearRow`: Integer, initialized to 8.
- `multipleDiscountRow`: Integer, initialized to 9.
- `SetSheetInputs`: Subroutine that sets the input values from the form controls into the `Inputs` sheet of the workbook.

## Code Examples

The example provided demonstrates the integration of form controls with a CalcSheet, enabling dynamic updating of the worksheet based on user inputs.

## Cross References

- See also:
  - [Calculation Engine Overview](#calculation-engine-overview)
  - [Working with CalcSheets](#working-with-calcsheets)

<!-- tags: [calculation, sheet, form, windows forms, vb.net, syncfusion] keywords: [input, output, worksheet, control integration, syncfusion,winforms] -->
```