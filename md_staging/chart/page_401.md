```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_401.jpeg
document_name: chart
page_number: 401
page_id: chart#page_401
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:39:28Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Content

### Customizing Axis Labels

#### C#

```csharp
private void chartControl1_ChartFormatAxisLabel(object sender, ChartFormatAxisLabelEventArgs e)
{
    if (e.AxisOrientation == ChartOrientation.Horizontal)
    {
        if (e.ValueAsDate.Month == 1)
            e.Label = "1st Month";
        else if (e.ValueAsDate.Month == 2)
            e.Label = "2nd Month";
        else if (e.ValueAsDate.Month == 3)
            e.Label = "3rd Month";
        else if (e.ValueAsDate.Month == 4)
            e.Label = "4th Month";
        else if (e.ValueAsDate.Month == 5)
            e.Label = "5th Month";
        else if (e.ValueAsDate.Month == 6)
            e.Label = "6th Month";
        e.Handled = true;
    }
}
```

#### VB

```vb
Private Sub chartControl1_ChartFormatAxisLabel(ByVal sender As Object, ByVal e As ChartFormatAxisLabelEventArgs)
    If e.AxisOrientation = ChartOrientation.Horizontal Then
        If e.ValueAsDate.Month = 1 Then
            e.Label = "1st Month"
        ElseIf e.ValueAsDate.Month = 2 Then
            e.Label = "2nd Month"
        ElseIf e.ValueAsDate.Month = 3 Then
            e.Label = "3rd Month"
        ElseIf e.ValueAsDate.Month = 4 Then
            e.Label = "4th Month"
        ElseIf e.ValueAsDate.Month = 5 Then
            e.Label = "5th Month"
        ElseIf e.ValueAsDate.Month = 6 Then
            e.Label = "6th Month"
        End If
        e.Handled = True
    End If
End Sub
```

## RAG Annotations

<!-- tags: [chart, axis labels, windows forms, formatting, Syncfusion] keywords: [chartControl1, ChartFormatAxisLabel, ChartOrientation, Horizontal, ValueAsDate, Month, Label, if-else, handled] -->
```