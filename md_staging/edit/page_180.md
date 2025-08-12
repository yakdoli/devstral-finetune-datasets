```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_180.jpeg
document_name: edit
page_number: 180
page_id: edit#page_180
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:04:20Z
fidelity: lossless
-->

## Essential Edit for Windows Forms

### Overview
- Demonstrates the customization of tooltips in the Syncfusion Windows Forms Editor control.
- Provides both C# (`editControl_UpdateContextToolTip`) and VB.NET (`editControl_UpdateContextToolTip`) implementations for updating the context tooltip.

### Content

#### ToolTip Customization

```csharp
// Get tokens from the current line
ILexem lexem = line.FindLexemByColumn(pointVirtual.X);

if (lexem != null)
{
    // Set the desired information tooltip
    e.Text = "This is additional information on " + lexem.Text;
}
```

```vb
Private Sub editControl_UpdateContextToolTip(ByVal sender As Object, ByVal e As Syncfusion.Windows.Forms.Edit.Dialogs.UpdateTooltipEventArgs) Handles EditControl.UpdateContextToolTip
    If e.Text = String.Empty Then
        Dim pointVirtual As Point = editControl.PointToVirtualPosition(New Point(e.X, e.Y))

        If pointVirtual.Y > 0 Then
            ' Get the current line
            Dim line As ILexemLine = editControl.GetLine(pointVirtual.Y)

            If Not (line Is Nothing) Then
                ' Get tokens from the current line
                Dim lexem As ILexem = line.FindLexemByColumn(pointVirtual.X)

                If Not (lexem Is Nothing) Then
                    ' Set the desired information tooltip
                    e.Text = "This is additional information on " + lexem.Text
                End If
            End If
        End If
    End If
End Sub
```

#### Background Brush

### Customization

### Background Brush

## Page-Level Navigation/TOC
- [unclear]

### Cross References
- See also: `editControl_UpdateContextToolTip`, `ILexem`, `ILexemLine`, `Point`, `Syncfusion.Windows.Forms.Edit.Dialogs.UpdateTooltipEventArgs`

<!-- tags: [Syncfusion, WinForms, Editor Control, Tooltip, Customization, Background Brush] keywords: [EditControl, UpdateContextToolTip, ILexem, ILexemLine, Point, UpdateTooltipEventArgs] -->
```
