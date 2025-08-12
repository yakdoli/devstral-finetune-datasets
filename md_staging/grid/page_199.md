```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_199.jpeg
document_name: grid
page_number: 199
page_id: grid#page_199
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:02:15Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates the use of cell comment tips in the Essential Grid.
- Explains the `ShowCurrentCellBorderBehavior` property and its behavior.
- Lists the options available in the `GridShowCurrentCellBorder` enumeration.

## Content

### Figure 106: Cell Comment Tips
![Image Description: A sample grid displaying a cell comment tip in cell 4,4. The comment contains multiple lines of sample text.]()

A sample demonstrating this feature is available under the following sample installation path:

```
C:\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Windows\Samples\2.0\Appearance\Cell Comment Tip Demo
```

#### 4.1.4.2.11 Grid New Feature

The `ShowCurrentCellBorderBehavior` property of the grid determines the behavior of the current cell's border. The `GridShowCurrentCellBorder` enumeration specifies the display of the current cell's frame or border.

Here is the list of options in the `GridShowCurrentCellBorder` enumeration:

- **AlwaysVisible**: Setting `ShowCurrentCellBorderBehavior` property with this option displays the current cell borders/frame.
- **GrayWhenLostFocus**: Setting `ShowCurrentCellBorderBehavior` property with this option shows the current cell's borders in gray when it is not focused upon.
- **HideAlways**: Setting `ShowCurrentCellBorderBehavior` property with this option hides the borders of the current cell.
- **WhenGridActive**: Setting `ShowCurrentCellBorderBehavior` property with this option highlights the current cell's border when the grid is under focus.

The following code examples illustrate how to set the `ShowCurrentCellBorderBehavior` property:

#### Using C#

### References
- Documentation and examples provided by Syncfusion for their Windows Forms controls.
- Sample path for cell comment tip demonstration.

## API Reference

### Properties
- **ShowCurrentCellBorderBehavior**: Determines the behavior of the current cell's border.
  - **Type**: `GridShowCurrentCellBorder`
  - **Possible Values**:
    - `AlwaysVisible`
    - `GrayWhenLostFocus`
    - `HideAlways`
    - `WhenGridActive`

## Code Examples

### Example: Setting the ShowCurrentCellBorderBehavior Property in C#

```csharp
grid.ShowCurrentCellBorderBehavior = GridShowCurrentCellBorder.AlwaysVisible;
```

## Cross References
- [4.1.4.2.11 Grid New Feature](#)
- Cell Comment Tips documentation
- GridShowCurrentCellBorder enumeration

## RAG Annotations
<!-- tags: Grid, Windows Forms, Cell Comments, Cell Border, GridShowCurrentCellBorder, ShowCurrentCellBorderBehavior keywords: cell comment tips, current cell border, GridShowCurrentCellBorder, ShowCurrentCellBorderBehavior, C# example, always visible, gray when lost focus, hide always, when grid active -->
```