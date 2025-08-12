```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_201.jpeg
document_name: grid
page_number: 201
page_id: grid#page_201
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:02:11Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- 1. Learn how to make the Grid non-editable by setting the `BrowseOnly` property to `true`.
- 2. Explore the process of deriving custom cell controls for special functionalities.
- 3. Understand the two base classes, `GridCellModelBase` and `GridCellRendererBase`, involved in defining cell controls.

## Content

### 4.1.4.2.12.2 Making a Grid Browse-Only

To make the Grid non-editable, the following property must be set to true:

```csharp
this.gridControl1.BrowseOnly = true;
```

```vb
Me.gridControl1.BrowseOnly = true
```

### 4.1.4.3 Deriving a Cell Control

Derived cell controls can be used to add cells that have a special functionality. You can employ such controls to produce special behavior like a masked edit control, a draggable button, or a tree node within a grid cell. Being able to extend a cell behavior through the derived cell controls makes Essential Grid very adaptable.

There are two classes involved in defining the cell architecture within Essential Grid. `GridCellModelBase` serves as the base class for the first class which is involved in the cell model. `GridCellRendererBase` is the base class for the second class which is involved in defining a cell control, the cell renderer. For example, the Static cell control is defined in the `GridStaticCellModel` and `GridStaticCellRenderer` classes which are derived from these base classes. So, whether the cell control is a text box, a combo box, or a NumericUp/Down cell, the behavior is accomplished through these two classes which are derived from `GridCellModelBase` and `GridCellRendererBase`.

In the next sections, you will learn how to derive a cell control from the

`C:\Syncfusion\EssentialStudio\VersionNumber\Windows\Grid.Windows\Samples\[Version Number]\CustomCellTypes\DerivedCellControlTutorial` sample.

Also,

`C:\Syncfusion\EssentialStudio\VersionNumber\Windows\Grid.Windows\Samples\[Version Number]\CustomCellTypes\DropDownFormAndUserControlSample` sample illustrates how to add your own cell controls. It has two derived cell controls, one drops a modal form when a cell button is pressed, and the other is displays a pop-up `UserControl` when a cell button is pressed.

Among the samples shipped with Grid control, there are several that provide custom cell types. The following table lists some of the samples.

## API Reference (if applicable)

Not applicable for this page.

## Code Examples (multi-language supported)
- The code examples provided demonstrate setting the `BrowseOnly` property in both C# and VB.
- The examples are minimal, focused on individual components of the Grid control.

## Page-level Navigation/TOC (if applicable)

Not applicable for this page.

## Cross References

- Refer to the Microsoft Docs for more information on cell controls and their implementations.
- Explore the Microsoft WinForms documentation for details on UI controls and their behavior.

## RAG Annotations
<!-- tags: [Grid, Windows Forms, Cell Control, ReadOnly, Derive Cell Control] keywords: [BrowseOnly, GridCellModelBase, GridCellRendererBase, StaticCellControl, DerivedCellControl, ModalForm] -->
```