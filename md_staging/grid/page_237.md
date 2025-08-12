```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_237.jpeg
document_name: grid
page_number: 237
page_id: grid#page_237
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:04:49Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Overview
- Essential Grid provides flexible support for **Multilevel Undo/Redo**.
- Allows users to undo history for most actions performed.
- Enabled by setting the `CommandStack.Enabled` property to `true`.
- Utilizes the `GridModelCommandManager` class for tasks like undo and redo.

### Main Content

#### Multilevel Undo/Redo Feature
Essential Grid has flexible support for **Multilevel Undo/Redo**. This feature enables the user to undo history for most actions that are performed. This feature can be enabled by setting the `CommandStack.Enabled` property to `true`. Using the functions of the `GridModelCommandManager` class, various tasks like undo and redo can be done. You can access this class from a Grid with the `CommandStack` property of a GridModel instance.

##### Enabling the Multilevel Undo/Redo Feature

The Multilevel Undo/Redo feature can be enabled for Essential Grid by using the following code:

1. **Using C#**

```csharp
this.gridControl1.CommandStack.Enabled = true;
this.gridControl1.CommandStack.Undo();
this.gridControl1.CommandStack.Redo();
```

2. **Using VB.NET**

```vb
Me.gridControl1.CommandStack.Enabled = True
Me.gridControl1.CommandStack.Undo()
Me.gridControl1.CommandStack.Redo()
```

## API Reference

- **CommandStack.Enabled**: Property to enable the undo/redo stack.
- **CommandStack.Undo()**: Method to perform an undo operation.
- **CommandStack.Redo()**: Method to perform a redo operation.

## Code Examples

### Example: Enabling Undo/Redo in C#

```csharp
this.gridControl1.CommandStack.Enabled = true;

// Undo the last action
this.gridControl1.CommandStack.Undo();

// Redo the last action
this.gridControl1.CommandStack.Redo();
```

### Example: Enabling Undo/Redo in VB.NET

```vb
Me.gridControl1.CommandStack.Enabled = True

' Undo the last action
Me.gridControl1.CommandStack.Undo()

' Redo the last action
Me.gridControl1.CommandStack.Redo()
```

## Related Topics

- **GridModelCommandManager**
- **CommandStack**
- **Undo and Redo Operations in Grid**

<!-- tags: [essential-grid, windows-forms, undo-redo, gridmodelcommandmanager, commandstack, syncfusion, winforms] keywords: [multilevel undo, redo, gridcontrol, essential grid, windows forms, undo redo stack, grid model command manager] -->
```