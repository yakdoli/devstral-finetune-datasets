```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_102.jpeg
document_name: calculate
page_number: 102
page_id: calculate#page_102
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:05:22Z
fidelity: lossless
-->

## Essential Calculate

```vb
If Me.checkBoxMultipleCars.Checked Then
    inputSheet(multipleDiscountRow, 2) = "Yes"
Else
    inputSheet(multipleDiscountRow, 2) = "No"
End If
inputSheet(3, 5) = Me.textBoxBaseAmount.Text

' 2) Calculations are suspended so need to pull the computed value
' to make sure it has been calculated with the latest changes.
Me.calcWB.Engine.UpdateCalcID()
calcWB.Engine.PullUpdatedValue(Me.calcWB.GetSheetID("Outputs"), 1, 1)

' 3) Gets the value from cell 1,1 on the output sheet.
Dim d As Double
If Double.TryParse(calcWB("Outputs")(1, 1).ToString(), NumberStyles.Any, Nothing, d) Then
    Me.labelPrice.Text = String.Format("{0:C2}", d)
Else
    Me.labelPrice.Text = "---"
End If

' Allows the label to update.
Me.labelPrice.Refresh()
End While
Me.calcWB.Engine.CalculatingSuspended = False
Me.Cursor = Cursors.Default
Me.labelPrice.Text = String.Format("{0} updates in {1} seconds", num, CType(DateTime.Now - start, TimeSpan))

' Button2_Click
End Sub
```

### Overview
- Sets random values into the Inputs sheet using the proper row and column indexers.
- Calls `UpdateCalcID` and `PullUpdatedValue` to ensure the value in the Outputs sheet at cell (1,1) reflects the current values in the workbook.
- Retrieves the value on the Output sheet at cell (1,1).

## Content

### 4.4 Supported Algebra

<!-- tags: [syncfusion, winforms, calculation, algebra, inputs, outputs] keywords: [CheckBox, TextBox, Label, Format, Parse, SheetID, Calculate Suspension, TimeSpan, Floats, Algebra]. -->
```