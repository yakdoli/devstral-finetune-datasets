```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_168.jpeg
document_name: grid
page_number: 168
page_id: grid#page_168
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:00:16Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates the use of Push Button Cells in a grid.
- Explains how to display a PushButton in a grid cell.
- Lists GridStyleInfo properties that control the behavior of Push Button cells.
- Includes a code example for setting the cell type to PushButton.

## Content

### 4.1.4.1.13 Push Button

#### Displaying a Push Button in a Grid Cell

To display a Push Button in a grid cell, use the `PushButton` cell type. To catch and handle a user click on a button, you can add a `GridControl.CellButtonClicked` event handler. The event arguments passed into your handler will include the row and column of the click. The `GridStyleInfo` properties that control the behavior of a Push Button cell are listed in the following table:

| Property          | Description                                                                |
|-------------------|----------------------------------------------------------------------------|
| CellAppearance    | Specifies whether the button is raised, sunken, or flat.                 |
| CellType          | Set to "PushButton" for a push button control.                          |

#### Code Example to Set the Cell Type to PushButton

The following code example illustrates how to set the cell type to `PushButton`.

```csharp
// Set the cell type to PushButton
```

## API Reference

### Properties

- **CellAppearance**: Specifies the appearance of the button (raised, sunken, or flat).
- **CellType**: Specifies the type of the cell control.

## Code Examples

Here is an example of setting the cell type to `PushButton`:

```csharp
// Example code to set the cell type to PushButton
```

## Page-level Navigation/TOC

- **Push Button**: Displaying and handling a Push Button in a grid cell.
- **GridStyleInfo Properties**: Properties that control the behavior of Push Button cells.
- **Code Example**: Example of setting the cell type to PushButton.

## Cross References

- Refer to the documentation on `Progress Bar Cell Demo` for more examples.
- Additional information on event handling can be found in the `GridControl.CellButtonClicked` documentation.

### Figure: Push Button Cells

![](https://i.imgur.com/hP7Y9.png)

#### Caption: Figure 88: Push Button Cells

For other code samples, refer to the sample in the following location:

```
C:\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Windows\Samples\2.0\Cell Types\Progress Bar Cell Demo
```

## RAG Annotations

<!-- tags: [Syncfusion Winforms, GridControl, PushButton, EventHandling, GridStyleInfo, CellTypes] keywords: [PushButton, GridControl, CellButtonClicked, CellAppearance, CellType, CodingExample, Progress Bar Cell Demo] -->
```