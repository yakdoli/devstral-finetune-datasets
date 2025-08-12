```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_220.jpeg
document_name: grid
page_number: 220
page_id: grid#page_220
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:03:42Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview

- Display slider controls within grid cells.
- Implement XHTML functionality in grid cells by customizing cell types.
- Overview of GridCellModelBase and GridCellRendererBase usage.

## Content

### Slider Cell

![Slider Cell in a grid](# "[Figure 116: Slider Cell]" "Figure 116: Slider Cell")

#### 4.1.4.4.11 XHTML Cell

An XHTML page can be displayed in a grid cell by using the Xhtml Cell cell type. A custom cell type can be created and registered to provide XHTML functionality. This requires derivation of two classes:

- **GridCellModelBase**
- **GridCellRendererBase**

The CellModel (read GridCellModelBase class in this document) is responsible for handling any serialization that a cell type requires and also creates the CellRenderer (read GridCellRendererBase class in this document) class that is associated with the cell type. The **CellRenderer** class manages the UI aspects of the cell type.

The XHTML page can be displayed by using the following set of codes.

#### Using C#

```csharp
string xhtml1 = "<body style=\"font-family:Arial; line-height:1em\"> ";
xhtml1 += "<h1 style=\"text-align:center; color:#EE7A03\">XhtmlCells</h1>";
```

### Summary

- **Custom Cell Types**: Customize grid cells to display XHTML content.
- **Class Derivations**: Use GridCellModelBase and GridCellRendererBase for custom functionality.
- **Implementation**: Detailed code example in C# to display an XHTML page within a grid cell.

## Code Examples

### Displaying XHTML in a Grid Cell (C#)

```csharp
string xhtml1 = "<body style=\"font-family:Arial; line-height:1em\"> ";
xhtml1 += "<h1 style=\"text-align:center; color:#EE7A03\">XhtmlCells</h1>";
```

## Page-level Navigation/TOC

- **Sections on this page**:
  - 4.1.4.4.11 XHTML Cell
  - Usage of GridCellModelBase and GridCellRendererBase
  - Code example for displaying XHTML in a grid cell

<!-- tags: [Syncfusion Winforms, Grid, Cell Types, Customization, XHTML] keywords: [Syncfusion, Windows Forms, Grid, Cell Model, Cell Renderer, XHTML, C#] -->
```