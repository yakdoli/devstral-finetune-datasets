```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_255.jpeg
document_name: edit
page_number: 255
page_id: edit#page_255
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:09:06Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

```vb
Private Sub editControl1_DrawLineMark(ByVal sender As Object, ByVal e As Syncfusion.Windows.Forms.Edit.DrawLineMarkEventArgs)
    If e.VirtualLine Mod 2 = 0 Then
        Dim brush As Brush = New Drawing2D.LinearGradientBrush(e.MarkRect, Color.Red, Color.Yellow, LinearGradientMode.Vertical)
        e.Graphics.FillRectangle(brush, e.MarkRect)
        e.Graphics.DrawRectangle(Pens.IndianRed, e.MarkRect)
    End If
End Sub
```

Figure 82: Custom Indicators in the Indicator Margin

## 4.14.11 InsertModeChanged Event

This event is fired when the value of the `InsertMode` property changes. The `InsertMode` property specifies the insert mode state.

The event handler receives an argument of type `EventArgs`.

```csharp
[C#]

// Handle the InsertModeChanged event.
this.editControl.InsertModeChanged += new EventHandler(editControl_InsertModeChanged);

// Set the value of the InsertMode property.
this.editControl.InsertMode = false;

private void editControl_InsertModeChanged(object sender, EventArgs e)
```

## Page-level Navigation/TOC (if applicable)

- [Overview]
- [Content]
  - [4.14.11 InsertModeChanged Event]
- [API Reference (if applicable)]
- [Code Examples (multi-language supported)]
- [Cross References]
- [RAG Annotations]

<!-- tags: [syncfusion, windows forms, edit, insertmodechanged, event, property, insertmode, eventargs] keywords: [insertmode, insertmodechanged, event, property, edit, windowsforms, syncfusion, eventhandler, args] -->
```