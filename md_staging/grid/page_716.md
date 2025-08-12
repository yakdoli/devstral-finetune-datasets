```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_716.jpeg
document_name: grid
page_number: 716
page_id: grid#page_716
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:35:55Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Code Sample

```vb
e.Style.BackColor = Color.YellowGreen
e.Style.TextColor = Color.Yellow
e.Style.CellType = "Static"
e.Style.HorizontalAlignment = GridHorizontalAlignment.Left
e.Style.Enabled = False

' Setting color to the drop area.
ElseIf e.Style.Text.StartsWith("Drag a") Then
    e.Style.Text = "Drag and Drop Parent Table Column headers"
    e.Style.BackColor = Color.Orange
    e.Style.TextColor = Color.White

' Setting color to the dropped columns.
ElseIf e.Style.Text.StartsWith("Child") Then
    e.Style.BackColor = Color.Orange
    e.Style.TextColor = Color.White
    e.Style.Themed = False

' Setting color to the remaining part.
Else
    e.Style.BackColor = Color.YellowGreen
End If
End Sub
```

## Sample Output

Here is a sample output.

![Group Drop Panel with Two Drop Areas](https://i.imgur.com/<image_token>.png)

**Figure 287**: Formatting the Group Drop Area by using the PreviewViewStyleInfo Event

## API Reference

### Namespaces and Classes
- `Color`
- `GridHorizontalAlignment`
- `Event e`

### Properties
- `BackColor`
- `TextColor`
- `CellType`
- `Enabled`
- `Themed`
- `Text`

## Code Examples

The provided code demonstrates how to set different styles for various parts of a grid, including the drop area, dropped columns, and the remaining part of the grid.

## Cross References

- See also: Example of dynamic cell handling in Syncfusion Grid.

<!-- tags: [syncfusion-winforms, grid, cell-styling, drop-area, drop-columns, enabled-property, color, text-color, horizontal-alignment, static-cell-type, previewviewstyleinfo-event] keywords: [grid, winforms, cell-styling, drop-area, dropped-columns, enabled, color, text-color, horizontal-alignment, static-cell, previewviewstyleinfo, dynamic-cell] -->
```