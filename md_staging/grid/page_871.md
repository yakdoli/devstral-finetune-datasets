```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_871.jpeg
document_name: grid
page_number: 871
page_id: grid#page_871
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:46:17Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```csharp
e.Style.Font.FontStyle = FontStyle.Italic;
}
}
}
```

### Code Example in VB.NET

```vb
' Hook up the event.
AddHandler gridGroupingControl1.QueryCellStyleInfo, AddressOf gridGroupingControl1_QueryCellStyleInfo

' QueryCellStyleInfo event : To Format Cell by Cell Basis on demand.
Private Sub gridGroupingControl1_QueryCellStyleInfo(ByVal sender As Object, ByVal e As GridTableCellStyleInfoEventArgs)
    If e.TableCellIdentity.TableCellType = GridTableCellType.RecordFieldCell Then
        If e.TableCellIdentity.ColIndex Mod 2 = 0 Then
            e.Style.BackColor = Color.FromArgb(255, 187, 111)
            e.Style.Font.FontStyle = FontStyle.Bold
        Else
            e.Style.TextColor = Color.White
            e.Style.BackColor = Color.FromArgb(55, 91, 114)
        End If
    ElseIf e.TableCellIdentity.TableCellType = GridTableCellType.AlternateRecordFieldCell Then
        If e.TableCellIdentity.ColIndex Mod 2 = 0 Then
            e.Style.BackColor = Color.FromArgb(0, 21, 84)
            e.Style.Font.FontStyle = FontStyle.Underline
            e.Style.TextColor = Color.White
        Else
            e.Style.BackColor = Color.FromArgb(255, 188, 112)
            e.Style.Font.FontStyle = FontStyle.Italic
        End If
    End If
End Sub
```

Given below is a sample screen shot.

```markdown
[Sample Screen Shot Not Shown]
```

## Footer
- Copyright: © 2013 Syncfusion. All rights reserved.
- Page Number: 871

<!-- tags: [essential-grid, windows-forms, cell-style-info, formatting, bold, italic, underline, color, background-color, text-color, gridtablecelltype, code-examples, vb-net] keywords: [cell formatting, on-demand styling, cell basis, style change, event handler, alternate record, record field, even-odd columns, bold, italic, underline, color management, visual studio] -->
```