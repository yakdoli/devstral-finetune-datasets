```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_031.jpeg
document_name: edit
page_number: 031
page_id: edit#page_031
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:55:52Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Grouping Actions

To undo/redo an action group, do the following steps:

1. Invoke the `UndoGroupOpen` method to begin a new action group.
2. Perform any desired set of actions, and invoke the `UndoGroupClose` method to close the action group. All the actions performed between the `UndoGroupOpen()` and `UndoGroupClose()` method calls get grouped as one entity.
3. Now, when the `Undo` / `Redo` methods are invoked, the newly created group (or set of actions) gets undone / redone appropriately.
4. To cancel an already open action group, you have to invoke the `UndoGroupCancel` method.
5. The `CanUndo` property gets a flag that determines whether the undo operation can be performed in the Edit Control.
6. The `CanRedo` property gets a flag that determines whether the redo operation can be performed in the Edit Control.

## Unlimited Undo and Redo

Essential Edit supports multiple levels of undo / redo, whereas the default Edit Control in Windows Forms supports just one level of undo / redo. This makes Essential Edit a better choice for all your editing needs. The ability to undo and redo changes in Essential Edit improves the usability of any application that has any form of text editing.

Essential Edit allows the following methods to be invoked any number of times.

| Edit Control Method | Description |
|--------------------|-------------|
| Undo               | Performs an undo operation. (CTRL+Z) |
| Redo               | Performs a redo operation. (CTRL+Y) |
| CanUndo            | Indicates whether it is possible to undo the actions in the Edit Control. |
| CanRedo            | Indicates whether it is possible to redo the actions in the Edit Control. |
```