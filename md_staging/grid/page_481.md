```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_481.jpeg
document_name: grid
page_number: 481
page_id: grid#page_481
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:19:20Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```vb
me.gridGroupingControl.Appearance.AnyCell.AutoSize = true;
```

AutoSize can also be applied to different cell types to resize the rows and columns to fit the contents of the cell, and the row height and column width will be resized when editing the cell contents.

## 4.1.4.14.11 Autosizing Custom Cell

Essential Grid supports automatic resizing of cells in the Grid control when custom controls are placed inside the cells.

The Grid lets you add custom controls to cells by creating a `CellModel` class and a `CellRenderer` class. These custom controls can have different sizes. When these controls are placed in the Grid, the corresponding cell is automatically resized to fit the controls. This is achieved by overriding the `OnQueryPrefferedClientSize` method in the model class. The proper size of the control can be returned by using this method. The `ResizeToFit` method will then resize the cell to the size returned by the `OnQueryPrefferedClientSize` method.

The following code examples illustrate how to implement this feature in the Grid control:

### Using C#

```csharp
// Override this method to calculate proper control size and return the same.
protected override Size OnQueryPrefferedClientSize(Graphics g, int rowIndex, int colIndex, GridStyleInfo style, GridQueryBounds queryBounds)
{
    if (Grid[rowIndex, colIndex].Tag == null)
        throw new Exception("No User Control is tagged");
    else
    {
        // Get the type of the control from Style.Tag.
        Control userControl = Grid[rowIndex, colIndex].Tag as Control;

        // Calculate the size of the control.
        Size size = userControl.Size;
        size.Height += 2;

        // Return the size.
    }
}
```
```html
<!-- tags: [grid, autosizing, custom cell, cell model, cell renderer, onqueryprefferedclientsize] keywords: [Grid control, autosizing feature, custom controls, cell resizing, cell model, cell renderer, override method, exception handling, user control, tags] -->
```