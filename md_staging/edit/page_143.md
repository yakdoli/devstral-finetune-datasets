```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_143.jpeg
document_name: edit
page_number: 143
page_id: edit#page_143
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:02:44Z
fidelity: lossless
-->

## Positioning Mouse Cursor on a Specified line

The Edit Control supports the "GoTo" functionality both through the use of a run time dialog box and through programmatic APIs. The `GoTo` method is used to position the mouse pointer on any specified line. The GoTo method not only positions the pointer on the appropriate line, but it also scrolls the concerned line into the view. The `linesAbove` argument can be used to specify the number of lines to be displayed above the pointer.

```csharp
// [C#]
// Places the cursor at the beginning of the given line number.
this.editControl1.GoTo(lineNumber);
this.editControl1.GoTo(lineNumber, linesAbove);
```

```vb.net
' [VB.NET]
' Places the cursor at the beginning of the given line number.
Me.editControl1.GoTo(lineNumber)
Me.editControl1.GoTo(lineNumber, linesAbove)
```

### CurrentLine Property and Goto Dialog
The `CurrentLine` property explained in the [Positions and Offsets section](positions-and-offsets), also does the same task as the `GoTo` method. The Goto dialog box is invoked using the `ShowGoToDialog` method. The keyboard shortcut to this dialog box is `Ctrl+G`.

```csharp
// [C#]
// Invoke the GoTo Dialog.
this.editControl1.ShowGoToDialog();
```

```vb.net
' [VB.NET]
' Invoke the GoTo Dialog.
Me.editControl1.ShowGoToDialog()
```

![Figure 49: GoTo Dialog Box](attachment:Edit_GoTo_Dialog_Box.png)
*Figure 49: GoTo Dialog Box*

<!-- tags: [syncfusion, winforms, edit control, goto functionality, keyboard shortcuts, API] keywords: [C#, VB.NET, programmatic APIs, mouse pointer, linesAbove, ShowGoToDialog, CurrentLine, GoTo method, line number, dialog box, Ctrl+G] -->
```