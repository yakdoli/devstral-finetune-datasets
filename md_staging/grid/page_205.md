```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_205.jpeg
document_name: grid
page_number: 205
page_id: grid#page_205
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:02:32Z
fidelity: lossless
-->

## Cell Editing and Rendering Methods in Grid

### Overview
- Methods that handle active editing and drawing of cells in Grid controls.
- Event handling for mouse and keyboard interactions.
- Customization of cell rendering and state management.

### Content

#### Methods Overview

| Method Name                                                                                                   | Description                                                                                                                                                                                                                                                                                                                                 |
|--------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ◦ Handles active editing of the cell. For example, if your custom control is a checked list box control, you will use this method to check the selected items in the embedded checked list box from information stored in the cell's style object.                                                                                                   |                                                                                                                                                                                                                                                                                                                                         |
| **OnDraw(Graphics g, Rectangle clientRectangle, int rowIndex, int colIndex, GridStyleInfo style)**          | Called to draw the contents of the client bounds for the cell, for example, the text for a static cell. If your cell has an active state, then normally there are two paths through OnDraw. One path draws the active cell and the other handles the drawing of the cell when it is not active. Override it when you want to draw the content of your cell.                                                                                                                |
| **OnKeyDown(KeyEventArgs e)**                                                                                | Called when the user presses a key.                                                                                                                                                                                                                                                                                                      |
| **OnKeyUp(KeyEventArgs e)**                                                                                  | Called when the user releases a key.                                                                                                                                                                                                                                                                                                     |
| **OnKeyPress(KeyPressEventArgs e)**                                                                          | Called for a user key press.                                                                                                                                                                                                                                                                                                              |
| **OnHitTest(int rowIndex, int colIndex, MouseEventArgs mouseEventArgs, IMouseController controller)**        | Override the OnHitTest in your derived cell renderer if you want to catch mouse events. If you want your renderer class to handle mouse actions like OnMouseDown or OnMouseMove, this OnHitTest should return a non-zero value. Otherwise, your mouse methods will not be called.                                                                                                                         |
| **OnMouseHoverLeave(int rowIndex, int colIndex, EventArgs e)**                                               | Called when your cell renderer has indicated in its OnHitTest override that it wants to receive mouse events, and that the user is moving the mouse out of the cell.                                                                                                                                                                                                                                |
| **OnMouseHover(int rowIndex, int colIndex, MouseEventArgs e)**                                               | Called when your cell renderer has indicated in its OnHitTest override that it wants to receive mouse events, and that the user is moving the mouse over the cell.                                                                                                                                                                                                                                 |
| **OnMouseHoverEnter(int rowIndex, int colIndex)**                                                             | Called when your cell renderer has indicated in its OnHitTest override that it wants to receive mouse events, and that the user has moved the mouse into the cell.                                                                                                                                                                                                                                  |

### API Reference

#### Methods

| Method Name                          | Parameters                                                                                                                     | Description                                                                                                                                  |
|--------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| **OnDraw**                           | `Graphics g`, `Rectangle clientRectangle`, `int rowIndex`, `int colIndex`, `GridStyleInfo style`                         | Draws the cell contents, handling both active and non-active states.                                              |
| **OnKeyDown**                       | `KeyEventArgs e`                                                                                                              | Handles key down events for the cell.                                                                                                      |
| **OnKeyUp**                         | `KeyEventArgs e`                                                                                                              | Handles key up events for the cell.                                                                                                        |
| **OnKeyPress**                      | `KeyPressEventArgs e`                                                                                                         | Handles user key press events.                                                                                                             |
| **OnHitTest**                       | `int rowIndex`, `int colIndex`, `MouseEventArgs mouseEventArgs`, `IMouseController controller`                            | Determines whether the cell should receive mouse events. Returns a non-zero value if handling mouse actions is desired. |
| **OnMouseHoverLeave**               | `int rowIndex`, `int colIndex`, `EventArgs e`                                                                                 | Called when the mouse leaves the cell if mouse events are being handled.                                                          |
| **OnMouseHover**                    | `int rowIndex`, `int colIndex`, `MouseEventArgs e`                                                                            | Called when the mouse hovers over the cell if mouse events are being handled.                                                          |
| **OnMouseHoverEnter**               | `int rowIndex`, `int colIndex`                                                                                               | Called when the mouse enters the cell if mouse events are being handled.                                                           |

### Code Examples

#### OnDraw Method Example
```csharp
protected override void OnDraw(Graphics g, Rectangle clientRectangle, int rowIndex, int colIndex, GridStyleInfo style)
{
    // Custom drawing logic for the cell
    g.DrawString("Custom Text", new Font("Arial", 10), Brushes.Black, clientRectangle);
}
```

### Cross References
- See also: Grid Editing and CellStyleInfo documentation for more details on cell styling and state management.

<!-- tags: [grid, cell editing, rendering, mouse events, keyboard events, winforms] keywords: [OnDraw, OnKeyDown, OnKeyUp, OnKeyPress, OnHitTest, OnMouseHoverLeave, OnMouseHover, OnMouseHoverEnter] -->
``` 
