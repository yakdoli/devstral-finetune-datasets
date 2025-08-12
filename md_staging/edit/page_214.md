```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_214.jpeg
document_name: edit
page_number: 214
page_id: edit#page_214
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:07:12Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

```csharp
' Set text font.
e.Font = New Font("Garamond", 11)
If e.Line.LineIndex Mod 2 = 0 Then
    ' Set color of the text.
    e.Color = Color.Blue
End If
End Sub
```

Refer to the User Margin Demo sample in the following sample installation location for more information in this regard.

```
..My Documents\Syncfusion\EssentialStudio\Version
Number\Windows\Edit.Windows\Samples\2.0\Advanced Editor Functions\UserMarginDemo
```

## 4.9.3 Background Settings

Edit Control can be displayed with a gradient background by setting the `BackgroundColor` property to the desired `BrushInfo` object. The following table lists some properties of the `EditControl` and their corresponding descriptions.

| Edit Control Property | Description |
|------------------------|-------------|
| `BackgroundColor`      | Specifies background fill style and color. |
| `Style`                | Specifies the brush style. The options provided are as follows: <br> <br> - Solid<br> - Pattern<br> - Gradient |
| `BackColor`            | Specifies the backcolor of the control. |
| `ForeColor`            | Specifies the forecolor of the control. |
| `PatternStyle`         | Specifies the pattern style. The options provided are as follows: <br> <br> - Horizontal<br> - Vertical<br> - ForwardDiagonal<br> - BackwardDiagonal<br> - Cross |

<!-- tags: [product, syncfusion, windows forms, edit control, background settings, brushinfo, style, backcolor, forecolor, patternstyle, version 11.4.0.26] keywords: [backgroundcolor, style, backcolor, forecolor, patternstyle, gradient, brush, editcontrol, usermargin, syncfusionstudio] -->
```