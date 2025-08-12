```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_110.jpeg
document_name: calculate
page_number: 110
page_id: calculate#page_110
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:05:47Z
fidelity: lossless
-->

# Essential Calculate

```vb
{CalcEngine.ParseArgumentSeparator})

' Cell range
If r.IndexOf(":c") > -1 Then
    Dim s As String
    For Each s In engine.GetCellsFromArgs(r)
        ' s is a cell line a21 or c3...
        Try
            s1 = engine.GetValueFromArg(s)
            If s1 <> "" And Double.TryParse(s1, System.Globalization.NumberStyles.Number, Nothing, d) Then
                min = Math.Min(min, d)
            End If
        Catch ex As Exception
            Return ex.Message
        End Try
    Next s
Else
    Try
        s1 = engine.GetValueFromArg(r)
        If s1 <> "" And Double.TryParse(s1, System.Globalization.NumberStyles.Number, Nothing, d) Then
            min = Math.Min(min, d)
        End If
    Catch ex As Exception
        Return ex.Message
    End Try
End If
Next r
If min <> Double.MaxValue Then
    Return min.ToString()
End If
Return ""

' ComputeMymin
End Function
```

## 4.5.1.2 Step 2-Registering the Method with the CalcEngine

<!-- tags: [Syncfusion, Winforms, Calculate, CalcEngine, MethodRegistration, Version:11.4.0.26] keywords: [Calculate, CalcEngine, MethodRegistration, Step2, CellRange, TryParse, Double, VB] -->
```