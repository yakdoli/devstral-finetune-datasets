```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_386.jpeg
document_name: grid
page_number: 386
page_id: grid#page_386
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:13:11Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates the use of Cross Sheet References and Named Ranges with the Grid Formula Engine.
- Explains various methods of populating a Grid control with data.

## Content

### 4.1.4.7 Populating a Grid Control

There are several ways of using Grid control to display data. For instance, you can move your data directly into an Essential Grid and let the underlying grid manage this data for you, or another way would be to set the `datasource` member of Essential Grid, thus binding the grid. Still another method is, to use the Essential Grid in a pure virtual mode, whereby you can handle certain events to provide data to the Essential Grid whenever it is in demand.

Out of these three ways, the latter two ways of providing data to an Essential Grid are discussed in more detail (in their own sections of) in this user's guide. In this section, you will learn how to get data stored directly into an Essential Grid's internal storage, so that the grid is able to maintain the data for you, and also how to populate a Grid control from a two-dimensional integer array.

#### 4.1.4.7.1 The Grid Control Indexer Technique

To place data into a grid, you need to loop through all the rows and columns, setting the `GridStyleInfo.CellValue` property for each cell. This technique is fine for small grids and is not a real drawback. It does have the overhead of firing events that are normally associated with a change in a cell's `GridStyleInfo` object. For larger grids, the overhead associated with such events is likely to be noticed by users only during population. One thing to note is that you may need to turn off the Grid's Undo/Redo support so that users cannot undo your initial population of the grid.

```csharp
// Turn off undo.
this.gridControl1.CommandStack.Enabled = false;

// Prevent the grid from redrawing for each change.
this.gridControl1.BeginUpdate();
```

## API Reference (if applicable)

```csharp
this.gridControl1.CommandStack.Enabled = false;  // Disables Undo/Redo support.
this.gridControl1.BeginUpdate();  // Prevents grid from redrawing.
```

## Code Examples

The above code snippet demonstrates how to disable Undo/Redo support and prevent the grid from redrawing for each change, which can be beneficial when populating large grids.

### Related Topics

- Using Cross Sheet References and Named Ranges with the Grid Formula Engine
- Binding a Grid to a Data Source
- Managing Data in Pure Virtual Mode

## RAG Annotations

This section is focused on providing methods and techniques for populating a Grid control with data, particularly emphasizing the Grid Control Indexer Technique. It also includes practical code examples to demonstrate disabling Undo/Redo support and preventing grid redrawing.

<!-- tags: [Syncfusion, Grid, Data Population, Undo/Redo Support, Grid Control Indexer] keywords: [Essential Grid, Cross Sheet References, Named Ranges, Grid Formula Engine, Data Source, Pure Virtual Mode, Grid Control Indexer Technique, Disable Undo Redo, Prevent Redraw] -->
```