```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_098.jpeg
document_name: calculate
page_number: 098
page_id: calculate#page_098
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:05:07Z
fidelity: lossless
-->

## Content

### Essential Calculate

```csharp
private int ageRow = 3;
private int sexRow = 4;
private int stateRow = 5;
private int pointsRow = 6;
private int modelRow = 7;
private int modelYearRow = 8;
private int multipleDiscountRow = 9;

// 4) Set the input values into the CalcSheets.
private void SetSheetInputs()
{
    CalcSheet inputSheet = this.calcWB["Inputs"];
    inputSheet[ageRow, 2] = this.numericUpDownAge.Value.ToString();
    inputSheet[sexRow, 2] = this.comboBoxSex.Text[0].ToString();
    inputSheet[stateRow, 2] = this.comboBoxState.Text;
    inputSheet[pointsRow, 2] = this.numericUpDownPoints.Value.ToString();
    inputSheet[modelRow, 2] = this.comboBoxModel.Text;
    inputSheet[modelYearRow, 2] = numericUpDownModelYear.Value.ToString();
    inputSheet[multipleDiscountRow, 2] = checkBoxMCars.Checked ? "Yes" : "No";
    inputSheet[3, 5] = this.textBoxBaseAmount.Text;
}
```

### [VB]

```vb
Private Sub button1_Click(sender As Object, e As System.EventArgs)

    ' 1) Moves input values from the form into the CalcSheet.
    SetSheetInputs()

    ' 2) Calculations not suspended, so just getting the value triggers
    '    the computation. So these two lines are not needed.....
    '    Me.calcWB.Engine.UpdateCalcID()
    '    Me.calcWB.Engine.PullUpdatedValue(this.calcWB.GetSheetID("Outputs"), 1, 1)

    ' 3) Get the value from cell 1,1 on the output sheet.
    Dim d As Double
    If Double.TryParse(calcWB("Outputs")(1, 1).ToString(), NumberStyles.Any, Nothing, d) Then

        ' Cell 1,1 on the outputs sheet has the result.
        Me.labelPrice.Text = String.Format("{0:C2}", d)
    Else
        Me.labelPrice.Text = "----"
    End If
End Sub
```

## RAG Annotations

<!-- tags: [Syncfusion Winforms, essential Calculate, calcSheets, inputs, outputs, forms] keywords: [calculate, essential, calcSheets, input values, output sheet, cell, Trigger computation, Parse, Format, NumberStyles] -->
```