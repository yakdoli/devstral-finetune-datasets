```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_206.jpeg
document_name: grid
page_number: 206
page_id: grid#page_206
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:01:18Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Virtual Methods Overview

| **Method Signature**                                      | **Description**                                                                                   |
|----------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| `OnMouseDown(int rowIndex, int colIndex, MouseEventArgs e)` | Called when your cell renderer has indicated in its `OnHitTest` override that it wants to receive mouse events, and that the user has pressed a mouse button. |

These are only a few of the many virtual methods available to you. For a complete list, take a look at the Essential Grid Class Reference.

### Deriving from Essential Grid

In general, you probably will not derive directly from the base class, but instead from an existing Essential Grid derived class such as `GridStaticCellModel`.

### Sample Implementation

For a sample implementation of a derived cell control that is based on the existing Static cell control, take a look at the sample in the following path:

```
C:\Syncfusion\EssentialStudio\VersionNumber\Windows\Grid.Windows\Samples\[Version Number]\CustomCellTypes\DropDownFormAndUserControlSample
```

It shows two implementations of drop-downs. One drops a modal form by deriving `GridStaticCellModel` and `GridStaticCellRenderer`. The other drops a `UserControl` using popup architecture that handles focus issues by deriving `GridDropDownCellModel` and `GridDropDownCellRenderer`.

### 4.1.4.4 Custom Cell Types

Following are the custom cell types discussed under this section:

### 4.1.4.4.1 Button Edit

#### Button Edit Cell Type

The Button Edit cell type will allow you to add images to the button which can be embedded into the grid cells. This Button Edit cell type can be added by registering its cell model to the corresponding grid by using the `RegisterCellModel` class. There are some in-built images which will be added to the button by providing the button type, and also custom images can be added by specifying the button type as image and providing the location of the image. These Button Edit types can be used by initializing the `ButtonEditStyleProperties` class for the corresponding cell. The Button Edit types provided by grid control are listed as follows.

- Browse
- Check
- Down
- Left
- Leftend
- Redo
- Right

## Cross References

See also:

- Essential Grid Class Reference
- `RegisterCellModel` class
- `ButtonEditStyleProperties` class
- `GridStaticCellModel`, `GridStaticCellRenderer`
- `GridDropDownCellModel`, `GridDropDownCellRenderer`

## RAG Annotations

<!-- tags: [Grid, CustomCellTypes, ButtonEdit, WinForms] keywords: [Custom Cell Types, Button Edit, Grid Control, RegisterCellModel, ButtonEditStyleProperties, GridStaticCellModel, GridStaticCellRenderer, GridDropDownCellModel, GridDropDownCellRenderer] -->

```