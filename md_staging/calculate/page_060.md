```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_060.jpeg
document_name: calculate
page_number: 060
page_id: calculate#page_060
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:01:48Z
fidelity: lossless
-->

## Essential Calculate

```vb
' / </summary>
' / <param name="sender"></param>
' / <param name="e"></param>
Private Sub button1_Click(ByVal sender As Object, ByVal e As
System.EventArgs) _
                                              Handles Button1.Click
    ' Creates some sample data.
    Me.nRows = r.Next(10) + 2
    Me.nCols = r.Next(3) + 1
    Dim a(nRows, nCols) As Double
    Dim row As Integer
    For row = 0 To nRows - 1
        Dim col As Integer
        For col = 0 To nCols - 1
            a(row, col) = CDbl(r.Next(100)) / 10
        Next
    Next

    ' Creates an ArrayCalcData object and passes it in this array.
    Me.data = New ArrayCalcData(a)

    ' Creates a CalcEngine object using this ArrayCalcData object.
    Dim engine As New CalcEngine(Me.data)

    ' Turns on dependency tracking so that values set with the Set button
    ' take effect immediately.
    engine.UseDependencies = True

    ' Calls the RecalculateRange so any formulas in the data can be
    ' initially computed.
    engine.RecalculateRange(RangeInfo.Cells(1, 1, nRows + 1, nCols + 1), data)

    ShowObject()

    ' Button1_Click
End Sub
' / <summary>
' / Displays the ArrayCalcData values in a text box.
' / </summary>
Private Sub ShowObject()
    Me.TextBox1.Text = ""
    Dim i As Integer
    For i = 0 To Me.nRows
```

## Page-level Navigation/TOC (if applicable)
- [Previous Section](#previous-section-label)
- [Next Section](#next-section-label)

## Cross References
- Related Topic: [Dependency Tracking](#dependency-tracking)
- Related API: [ArrayCalcData](#arraycalcdatadoc), [CalcEngine](#calcenginedoc)

## RAG Annotations
<!-- tags: [Syncfusion Winforms, Essential Calculate, dependency tracking, ArrayCalcData, CalcEngine, version: 11.4.0.26] keywords: [calculate, dependency, tracking, recalculate, arraycalcdata, calcengine] -->
```