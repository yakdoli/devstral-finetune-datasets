```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_398.jpeg
document_name: grid
page_number: 398
page_id: grid#page_398
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:14:08Z
fidelity: lossless
-->

## Overview

- This page discusses the GridCommandStack class in Essential Grid for Windows Forms, focusing on its Undo/Redo functionality.
- It explains how the command stack tracks changes made to a grid and provides methods for managingUndo and Redo operations.
- Code samples in C# and VB.NET are provided to demonstrate how to control the Undo/Redo buffer using the CommandStack property.

## Content

### 4.1.4.9.1 The Basics

Essential Grid has a **GridCommandStack** class that implements support for the Undo/Redo commands in a grid. Depending upon the grid settings, as a user makes changes to the grid, these changes will be tracked in stack structures which, will be found in the **GridCommandStack** class. This class has methods that will allow you to undo the last action, redo the last undone action, and batch transactions so that a series of actions can be undone or redone in a single step.

The **CommandStack** property of the **GridControl** class will return a reference to the **GridCommandStack** object that is associated with a grid. It is through this property that you can access the Undo/Redo support in an Essential Grid. For example, you can use the `Enabled` property of the CommandStack to control whether or not the grid is supporting an Undo/Redo at any given moment. Here are the code samples that show you some **CommandStack** properties.

#### C#

```csharp
// Turn off the Undo buffer.
this.gridControl1.CommandStack.Enabled = false;

// Turn on the Undo buffer.
this.gridControl1.CommandStack.Enabled = true;

// Clear the Undo buffer.
this.gridControl1.CommandStack.UndoStack.Clear();

// Clear the Redo buffer.
this.gridControl1.CommandStack.RedoStack.Clear();

// Clear both the Undo and Redo buffers.
this.gridControl1.CommandStack.Clear();
```

#### VB.NET

```vb
' Turn off the Undo buffer.
Me.gridControl1.CommandStack.Enabled = False

' Turn on the Undo buffer.
Me.gridControl1.CommandStack.Enabled = True

' Clear the Undo buffer.
Me.gridControl1.CommandStack.UndoStack.Clear()
```

## API Reference

### Members of GridCommandStack

- **Enabled**: A property to enable or disable Undo/Redo support.
- **UndoStack.Clear()**: Clears the Undo buffer.
- **RedoStack.Clear()**: Clears the Redo buffer.
- **Clear()**: Clears both the Undo and Redo buffers.

## Code Examples

### C# Example

```csharp
this.gridControl1.CommandStack.Enabled = false;  // Disable Undo/Redo
this.gridControl1.CommandStack.UndoStack.Clear();  // Clear Undo buffer
this.gridControl1.CommandStack.RedoStack.Clear();  // Clear Redo buffer
this.gridControl1.CommandStack.Clear();  // Clear both Undo and Redo buffers
```

### VB.NET Example

```vb
Me.gridControl1.CommandStack.Enabled = False  ' Disable Undo/Redo
Me.gridControl1.CommandStack.UndoStack.Clear()  ' Clear Undo buffer
```

## See Also

- [Unclear]

<!-- tags: [Essential Grid, Undo/Redo, GridCommandStack, C#, VB.NET, Windows Forms] keywords: [GridCommandStack, Undo, Redo, CommandStack, GridControl, C#, VB.NET, Windows Forms] -->
```