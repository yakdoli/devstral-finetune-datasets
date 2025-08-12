```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_250.jpeg
document_name: edit
page_number: 250
page_id: edit#page_250
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:09:12Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## 4.14.8 CursorPositionChanged Event

This event is raised when the current cursor position is changed.

The event handler receives an argument of type `EventArgs`.

### Code Example

```csharp
[C#]

private void editControl1_CursorPositionChanged(object sender, EventArgs e)
{
    MessageBox.Show(" CurrentCursorPosition event is raised ");
}
```

```vb
[VB.NET]

Private Sub editControl1_CursorPositionChanged(ByVal sender As Object, ByVal e As EventArgs)
    MessageBox.Show(" CursorPositionChanged event is raised ")
End Sub
```

## 4.14.9 Expand Events

This section discusses the expand events given below.

### 4.14.9.1 ExpandedAll Event

This event is raised when the `ExpandAll` method is called.

The event handler receives an argument of type `EventArgs`.

### Code Example

```csharp
[C#]
```

---
© 2013 Syncfusion. All rights reserved. 250 | Page

<!-- tags: [product, windows forms, syncfusion sdk, cursorpositionchanged event, expandedall event, eventargs, event handler, edit control] keywords: [cursor position, cursorpositionchanged, expandall, syncfusion, windows forms, eventargs, event handler] -->
```