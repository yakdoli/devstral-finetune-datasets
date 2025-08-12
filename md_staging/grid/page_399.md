```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_399.jpeg
document_name: grid
page_number: 399
page_id: grid#page_399
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:14:41Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```vb
' Clear the Redo buffer.
Me.gridControl1.CommandStack.RedoStack.Clear()

' Clear both the Undo and Redo buffers.
Me.gridControl1.CommandStack.Clear()
```

## 4.1.4.9.2 Transactions

A transaction is a series of steps that should be treated as a single action in the Undo / Redo architecture. For example, you may have a record-oriented grid where you may want to group any changes in the current row as one transaction. This way, when the user wants to undo the last change, all the changes in the row are undone. It is possible to group a series of actions into a single Undo / Redo step through the use of these three `GridCommandStack` methods: `BeginTrans`, `CommitTrans`, and `RollBack`.

A call to `BeginTrans` will mark the start of a series of actions that are to be treated as a single Undo / Redo step. Once `BeginTrans` has begun, all the changes are marked as being a member of a single transaction until either `CommitTrans` or `RollBack` is called. `CommitTrans` signals a successful end to the transaction. A call to `RollBack` will cause all the changes in the current transaction to be undone and will end the transaction processing. A `RollBack` call will return the grid in the same state that it was in, immediately prior to the call to `BeginTrans`.

It is possible to nest transactions. If you are in the middle of a transaction, it is OK to call `BeginTrans` again. But, when such nested transactions are undone, they are treated as part of a single parent transaction.

## 4.1.4.9.3 Derived Commands

The Undo / Redo architecture of the Essential Grid is complete as shipped with the product. If, for some reason, you need to handle special grid requirements that cannot be performed with the standard implementation, the Undo / Redo architecture is extensible. To extend it, you need to derive custom command classes from either the abstract class `SyncfusionCommand` or the abstract class `GridModelCommand`. In your derived class, you will need to add whatever members you need in order to track enough state information that will allow you to Undo / Redo the action that is being done. Then you have to implement an execute method and other abstract members of the base class. If you do a search in the Essential Grid source code for `GridModelCommand`, you will see many examples of the derived command classes.

<!-- tags: [syncfusion, windows forms, grid, command stack, undo, redo, transactions, derived commands] keywords: [transaction, grid, command stack, undo, redo, BeginTrans, CommitTrans, RollBack, SyncfusionCommand, GridModelCommand] -->
```