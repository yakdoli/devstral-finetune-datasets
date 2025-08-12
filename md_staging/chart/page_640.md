```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_640.jpeg
document_name: chart
page_number: 640
page_id: chart#page_640
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:54:37Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

### Code Example

```vb
Private Sub PrintDocument_PrintPage(ByVal sender As Object, ByVal e As System.Drawing.Printing.PrintPageEventArgs)
    If textBox1.Text = "" Then
        textBox1.Text = "20"
    End If

    ' Set the HasMorePages property to true for dividing the chart into Multiple pages
    e.HasMorePages = True

    Me.chartControl1.PrimaryXAxis.LabelIntersectAction = ChartLabelIntersectAction.Wrap

    ' Initializing max and min range values
    If mx = 0.0 AndAlso mi = 0.0 Then
        mx = Convert.ToDouble(textBox1.Text)
        mi = 0
    End If

    ' Get the Color mode
    Dim grayScale As Boolean = Me.chartControl1.PrintDocument.ColorMode = ChartPrintColorMode.GrayScale
    Dim toolBarVisibility As Boolean = Me.chartControl1.ShowToolbar
    If Not Me.chartControl1.PrintDocument.PrintToolBar Then
        Me.chartControl1.ShowToolbar = False
    End If

    If m_correctAction.Value = PrintAction.PrintToPrinter AndAlso Me.chartControl1.PrintDocument.ColorMode = ChartPrintColorMode.CheckPrinter Then
        grayScale = Me.chartControl1.PrintDocument.PrinterSettings.SupportsColor
    End If

    ' Check the color mode of print
    If Not grayScale Then
        ' Assigning the initial values of max and min to chartcontrol maximum and minum values
    End If
End Sub
```

## API Reference

### Namespaces & Classes

- `System.Drawing.Printing.PrintPageEventArgs`
- `Syncfusion.Windows.Forms.Chart.ChartControl`
- `Syncfusion.Windows.Forms.Chart.ChartPrintColorMode`
- `Syncfusion.Windows.Forms.Grid.GridPrintDocument`

### Methods & Properties

- `Convert.ToDouble(text)`
- `Me.chartControl1.PrimaryXAxis.LabelIntersectAction`
- `Me.chartControl1.PrintDocument.ColorMode`
- `Me.chartControl1.PrintDocument.PrinterSettings.SupportsColor`
- `Me.chartControl1.ShowToolbar`
- `Me.chartControl1.PrintDocument.PrintToolBar`

### Events

- `PrintDocument_PrintPage`

## Code Examples

Visual Basic Example:
```vb
' Example usage of PrintDocument_PrintPage event handler
Private Sub PrintDocument_PrintPage(ByVal sender As Object, ByVal e As System.Drawing.Printing.PrintPageEventArgs)
    ' Implementation details as shown above
End Sub
```

## Cross References

See also:
- [Printing Data Grid](#printing-data-grid)
- [Customizing Chart Features](#customizing-chart-features)

<!-- tags: [windows forms, chart control, printing, color modes, VB.NET] keywords: [Syncfusion, PrintDocument, PrintPageEventArgs, ChartLabelIntersectAction, ChartPrintColorMode, PrintAction, PrintToolBar, Max and Min values] -->
```