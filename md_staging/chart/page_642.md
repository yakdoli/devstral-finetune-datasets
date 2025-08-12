```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_642.jpeg
document_name: chart
page_number: 642
page_id: chart#page_642
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:57:58Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

```vb
Me.chartControl1.Series(i).Style.Interior = New BrushInfo(DirectCast(ps.GetValue(i Mod ps.Length), PatternStyle), Color.White, Color.Black)

If Me.chartControl1.Series3D OrElse Me.chartControl1.ChartInterior.BackColor = Color.Black Then
    Me.chartControl1.Series(i).Style.Interior = New BrushInfo(DirectCast(ps.GetValue(i Mod ps.Length), PatternStyle), Color.Black, Color.White)
    Me.chartControl1.Series(i).Style.Border.Color = Color.Black
End If
End If
Next

Dim container As GraphicsContainer = BeginTransform(e.Graphics)
e.Graphics.ResetTransform()

Using img As Image = New Bitmap(e.MarginBounds.Width, e.MarginBounds.Height)
    Using g As Graphics = Graphics.FromImage(img)
        ''' ' Assigning the initial values of max and min to chartcontrol maximum and ''' / minimum values

        Me.chartControl1.ChartArea.PrimaryXAxis.Range.Min = mi
        Me.chartControl1.ChartArea.PrimaryXAxis.Range.Max = mx
        Me.chartControl1.ChartArea.PrimaryXAxis.Range.Interval = (Me.chartControl1.ChartArea.PrimaryXAxis.Range.Max - Me.chartControl1.ChartArea.PrimaryXAxis.Range.Min) / Me.chartControl1.ChartArea.PrimaryXAxis.Range.NumberOfIntervals

        ''' ' Modifying the maximum and minimum values

        mi = mx
        mx = mx + Convert.ToDouble(textBox1.Text)
        Dim hdc As IntPtr = g.GetHdc()
        Dim stream As Stream = New MemoryStream()
        Dim mf As New Metafile(stream, hdc)

        ''' ' Call the Draw method to draw the chart
        Me.chartControl1.Draw(mf, img.Size)
        DrawingUtils.DrawGrayedImage(e.Graphics, mf, e.MarginBounds, New
```

## Footer
© 2013 Syncfusion. All rights reserved.
```