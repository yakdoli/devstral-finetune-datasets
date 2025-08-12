```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_159.jpeg
document_name: diagram
page_number: 159
page_id: diagram#page_159
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:16:56Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Demonstrates the Default Handle Edit Mode and its functionality when resizing a shape.
- Explains the editing behavior of shapes within the Diagram control.
- Illustrates how to manipulate and resize shapes using the built-in handles.

## Content

### Default Handle Edit Mode

#### Figure 91: Default Handle Edit Mode

<p align="center">
  ![Default Handle Edit Mode](<FIGURE-IMAGE-URL>)
</p>

The figure illustrates the Default Handle Edit Mode, where a shape is selected and displayed with resizing handles. These handles allow the user to resize the shape by dragging the handles.

### Default Handle Edit Mode with Resize

#### Figure 92: Default Handle Edit mode with Resize

<p align="center">
  ![Default Handle Edit mode with Resize](<FIGURE-IMAGE-URL>)
</p>

This figure shows the shape after it has been resized using the handles. The resizing maintains the aspect ratio, as demonstrated in the figure.

### Explanation of Handle Functionality

- **Handles**: The yellow square around the shape and the green circles represent the resizing handles.
- **Resize Operation**: Users can resize the shape by dragging any of the handles. The central handle allows uniform resizing.
- **Behavior During Resize**: The shape maintains its integrity, ensuring that the resizing is predictable and controlled.

## API Reference

This section provides a reference to the APIs and functions related to handling shape resizing in the Diagram control.

## Code Examples

### Example: Enabling Default Handle Edit Mode
```csharp
// Enabling Default Handle Edit Mode
diagram.DefaultHandleEditMode = true;

// Adding a shape
Shape shape = new Shape();
shape.Bounds = new RectangleF(100, 100, 200, 200);
diagram.Shapes.Add(shape);
```

### Example: Handling Resize Events
```csharp
// Handling Resize Events
diagram.Resize += (sender, e) =>
{
    MessageBox.Show("Shape is being resized.");
};
```

## Page-level Navigation/TOC (if applicable)

- **Default Handle Edit Mode**
  - Figure 91: Default Handle Edit Mode
  - Figure 92: Default Handle Edit mode with Resize
- **Explanation of Handle Functionality**
- **API Reference**
- **Code Examples**

## Cross References

See also:
- [Syncfusion Diagram User Guide](link)
- [Shape Manipulation Techniques](link)
- [Diagram Control Documentation](link)

## RAG Annotations

<!-- tags: [syncfusion, windowsforms, diagram, handleeditmode, resize, shapes] keywords: [Syncfusion, WinForms, Diagram, handles, resize, shape manipulation, edit mode, default mode] -->
```