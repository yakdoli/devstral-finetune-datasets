```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_032.jpeg
document_name: edit
page_number: 032
page_id: edit#page_032
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:55:48Z
fidelity: lossless
-->

## Essential Edit for Windows Forms

### R��etUndoInfo ResetUndolfo ResetUndolfo ResetUndo
Clear the undo buffer. Hence undo operation is not allowed on contents/actions previously added/performed up to that point.

#### Note:
The undo/redo buffer is cleared after the 'Save' operation.

### Enabling Grouping

Grouping is enabled using the below given property.

| Edit Control Property | Description |
|-----------------------|-------------|
| GroupUndo            | Specifies whether grouping should be enabled for undo/redo actions. |

#### C#
```csharp
// Accomplish Undo operation.
this.editControl1.Undo();

// Accomplish Redo operation.
this.editControl1.Redo();

// Indicates whether it is possible to Undo in the Edit Control.
bool canUndo = this.editControl1.CanUndo;

// Indicates whether it is possible to Redo in the Edit Control.
bool canRedo = this.editControl1.CanRedo;

// Clears the Undo buffer.
this.editControl1.ResetUndoInfo();

// Enable grouping for Undo / Redo actions.
this.editControl1.GroupUndo = true;
```

#### VB.NET
```vbnet
' Accomplish Undo operation.
Me.editControl1.Undo()

' Accomplish Redo operation.
Me.editControl1.Redo()

' Indicates whether it is possible to Undo in the Edit Control.
Me.editControl1.CanUndo
```

---

#### Footer:
© 2013 Syncfusion. All rights reserved. 32 | Page
<!-- tags: [Syncfusion, Winforms, Edit, Undo, Grouping, Control Property, Undo Buffer] keywords: [resetundo, resetundoinfo, undo, redo, save, grouping, edit control, canundo, canredo] -->
```