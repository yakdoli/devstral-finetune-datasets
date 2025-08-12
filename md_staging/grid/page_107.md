```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_107.jpeg
document_name: grid
page_number: 107
page_id: grid#page_107
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:27:18Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```vb.NET
Private Sub GridQueryCellInfo(ByVal sender As Object, ByVal e As GridQueryCellInfoEventArgs)
    If (e.RowIndex > 0) AndAlso (e.ColIndex > 0) Then
        e.Style.CellValue = Me._extData(e.RowIndex - 1, e.ColIndex - 1)
        e.Handled = True
    End If
End Sub
```

Notice that all three handlers set the `Handled` property on the `EventArgs` when a value is provided. This informs the grid that no further processing is needed. Don't forget this or you'll lose some of the benefits of using a virtual grid.

### Compile and run the project. You will see something similar to the screen shot given below. The point is that the grid itself does not hold any data at all. All the data information is being provided on demand through the three events that you have added.

![Virtual Grid Holds No Internal Data](https://i.imgur.com/sS5tS4r.png)

Figure 66: Virtual Grid Holds No Internal Data

## 3.1.5.6 Saving Edited Values

```markdown
### WinForms-specific conventions
- Prefer C# samples when language is ambiguous; if VB is explicitly shown, keep both.
- Distinguish design-time vs runtime features; preserve property grids, designer steps, and menu paths as regular text or ordered lists.
- When API elements are listed (Properties/Methods/Events/Enums), keep their exact order and names, including parentheses for methods and event handler signatures if visible.

### Pages
- Keep full signatures, imports/usings, comments, region markers.
- Inline code in text should be wrapped with backticks.
```

<!-- tags: [product, module, control, api, version?] keywords: [Essential Grid, Virtual Grid, data handling, cell info, row index, column index, handled event, gridQueryCellInfo, WinForms, saving edited values] -->
```