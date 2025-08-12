```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_187.jpeg
document_name: grid
page_number: 187
page_id: grid#page_187
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:01:20Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Managing Current Cell Operations

The `GridCurrentCell` class provides storage for current cell information and manages all the current cell operations such as activating, deactivating, saving, editing, and moving the current cell.

The following code examples illustrate how to set a `GridCurrentCell`:

### Using C#

```csharp
GridCurrentCell cc = this.gridControl1.CurrentCell;
```

### Using VB.NET

```vb
Dim cc As GridCurrentCell = Me.gridControl1.CurrentCell
```

## Show/Hide Current Cell Border

The `ShowCurrentCellBorderBehavior` property of the grid determines the behavior of the current cell's border. The `GridShowCurrentCellBorder` enumeration specifies the display of the current cell's frame or border.

Here is the list of options in the `GridShowCurrentCellBorder` enumeration:

- **AlwaysVisible**: Setting the `ShowCurrentCellBorderBehavior` property with this option displays the current cell borders/frame.
- **GrayWhenLostFocus**: Setting the `ShowCurrentCellBorderBehavior` property with this option shows the current cell's borders in gray when it is not focused upon.
- **HideAlways**: Setting the `ShowCurrentCellBorderBehavior` property with this option hides the borders of the current cell.
- **WhenGridActive**: Setting the `ShowCurrentCellBorderBehavior` property with this option highlights the current cell's border when the grid is under focus.

The following code examples illustrate how to set the `ShowCurrentCellBorderBehavior` property:

### Using C#
```csharp
```

``` 
<!-- tags: [Essential Grid, Windows Forms, GridCurrentCell, ShowCurrentCellBorderBehavior, GridShowCurrentCellBorder] keywords: [GridCurrentCell, ShowCurrentCellBorderBehavior, GridShowCurrentCellBorder, Current Cell Operations, Border Behavior, Code Examples, C#, VB.NET] -->
```