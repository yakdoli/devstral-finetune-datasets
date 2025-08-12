```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_397.jpeg
document_name: grid
page_number: 397
page_id: grid#page_397
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:14:31Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```csharp
// Now you can change the cell value. // Turn on Read-only checking.  
this.gridControl1.IgnoreReadOnly = false;
```

### [VB.NET]

```vbnet
Me.GridControl1(1, 1).ReadOnly = True

' Cell (1,1) has been set to Read-only.  
' To change its value, you need to use the IgnoreReadOnly property.  
Me.GridControl1.IgnoreReadOnly = True  

' Turn off Read-only checking.  
Me.GridControl1(1, 1).CellValue = 256  

' Now you can change the cell value.  
' Turn on Read-only checking.  
this.Me.GridControl1.IgnoreReadOnly = False
```

## 4.1.4.9 Using Undo/Redo

Essential Grid supports Undo/Redo functionalities similar to the one achieved with MS-Office type application. To handle this functionality, a stack is maintained internally in Essential Grid, to save the changes handled, through which the following tasks can be accomplished by the users directly.

- Allows to control the stack—when to save/unsave the changes, and when to rollback changes
- Allows to create new transactions, and control each individual transaction (like cancelling, rollback) without affecting the others

The Undo/Redo architecture is extensible thereby allowing the users to derive the base class, and add some more requirements for the Essential Grid.

<!-- tags: [windowsforms, undo/redo, grid, readonly, essentialgrid, csharp, vb.net] keywords: [undo, redo, transactions, stack, read-only, ignorereadonly, cellvalue, syncfusion, essentialgrid] -->
```