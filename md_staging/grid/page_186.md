```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_186.jpeg
document_name: grid
page_number: 186
page_id: grid#page_186
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:59:47Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

The following code examples illustrate how to set the `ActivateCurrentCellBehavior` property:

## Setting `ActivateCurrentCellBehavior` Property

### Using C#:

```csharp
this.gridControl1.ActivateCurrentCellBehavior = GridCellActivateAction.SelectAll;
```

### Using VB.NET:

```vb
Me.gridControl1.ActivateCurrentCellBehavior = GridCellActivateAction.SelectAll
```

## 4.1.4.2.6 Scroll Cell into View

You can use the `grid` method, `ScrollCellIntoView`, to scroll the specified cell or range into view. The range that should be scrolled into the visible grid view area is given as the parameter to the method. The following code examples illustrate this:

### Using C#

```csharp
// Scroll into view cell (2,2).
this.gridControl1.ScrollCellIntoView(GridRangeInfo.Cell(2, 2));

// Scroll into view range Col(2).
this.gridControl1.ScrollCellIntoView(GridRangeInfo.Col(2));
```

### Using VB.NET

```vb
' Scroll into view cell (2,2).
Me.gridControl1.ScrollCellIntoView(GridRangeInfo.Cell(2, 2))

' Scroll into view range Col(2).
Me.gridControl1.ScrollCellIntoView(GridRangeInfo.Col(2))
```

## API Reference

### Properties
- `ActivateCurrentCellBehavior`: Sets the behavior when a cell is activated.
- `ScrollCellIntoView`: Scrolls the specified cell or range into view.

### Methods
- `ScrollCellIntoView`: Scrolls the specified cell or range into view.

<!-- tags: [syncfusion, winforms, grid, control, activatecurrentcellbehavior, scrollcellintoview, c#, vb.net] keywords: [scroll cell, view, grid, range, visible, cell, activatebehavior, gridcontrol] -->
```