```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_101.jpeg
document_name: calculate
page_number: 101
page_id: calculate#page_101
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:05:06Z
fidelity: lossless
-->

# Essential Calculate

```csharp
double d;
if (double.TryParse(calcWB["Outputs"][1, 1].ToString(), NumberStyles.Any, null, out d))
{
    this.labelPrice.Text = string.Format("{0:C2}", d);
}
else
    this.labelPrice.Text = "----";

// Allows the label to update.
this.labelPrice.Refresh();

this.calcWB.Engine.CalculatingSuspended = false;
this.Cursor = Cursors.Default;
this.labelPrice.Text = string.Format("{0} updates in {1} seconds", num, (TimeSpan)(DateTime.Now - start));
}
```

## [VB]

```vb
Private Sub button2_Click(sender As Object, e As System.EventArgs)

    ' Runs 1000 iterations
    Dim num As Integer = 1000

    Me.Cursor = Cursors.WaitCursor
    Dim start As DateTime = DateTime.Now
    Dim inputSheet As CalcSheet = Me.calcWB("Inputs")
    Dim r As New Random()

    Me.calcWB.Engine.CalculatingSuspended = True

    Dim i As Integer = 0
    While i < num

        ' 1) Sets random values into the Inputs sheet.
        inputSheet(ageRow, 2) = (r.Next(74) + 15).ToString()
        If r.Next(2) = 1 Then
            inputSheet(sexRow, 2) = "M"
        Else
            inputSheet(sexRow, 2) = "F"
        End If
        inputSheet(stateRow, 2) = Me.comboBoxState.Items(r.Next(50))
        inputSheet(pointsRow, 2) = r.Next(15).ToString()
        inputSheet(modelRow, 2) = r.Next(11).ToString()
        inputSheet(modelYearRow, 2) = (33 + r.Next(1972)).ToString()
    End While

End Sub
```

## Page-level Navigation/TOC (if applicable)
- If this page contains a local Table of Contents, include it here.

## Cross References
- See also: relevant links or references to other sections.

<!-- tags: [Syncfusion, Winforms, Essential Calculate] keywords: [calculate, label update, random values, inputs sheet, stateRow, pointsRow, modelRow, modelYearRow] -->
```