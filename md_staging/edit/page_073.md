```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_073.jpeg
document_name: edit
page_number: 073
page_id: edit#page_073
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:58:43Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

```vb.net
' Set the Insert mode.
Me.editControl1.InsertMode = True

' Inserts a string at the given line and column.
Me.editControl1.InsertText(1, 1, " text to be inserted ")

' Specifies multiple lines of text to the EditControl in the form of a string array.
Me.editControl1.Lines = New String() {" first line ", " second line ", " third line "}

' Allows text insertion only at the beginning of the readonly region at the start of a new line.
Me.editControl1.AllowInsertBeforeReadonlyNewLine = True

' Specifies whether the outer file dragged and dropped onto the editcontrol should be inserted into the current content.
Me.editControl1.InsertDroppedFileIntoText = True
```

## Deleting Text

Text can be deleted in the Edit Control by using the below given methods.

| Edit Control Method | Description |
|---------------------|-------------|
| DeleteChar         | Deletes a character to the right of the current cursor position. |
| DeleteCharLeft     | Deletes a character to the left of the current cursor position. |
| DeleteWord         | Deletes a word to the right of the current cursor position. |
| DeleteWordLeft     | Deletes a word to the left of the current cursor position. |
| DeleteAll          | Deletes all text in the document. |
| DeleteText         | Deletes the specified text. |

```csharp
// Deletes the character to the right of the cursor.
this.editControl1.DeleteChar();

// Deletes the character to the left of the cursor.
```

<!-- tags: [Syncfusion, Winforms, Edit Control, Insertion, Deletion, Version 11.4.0.26] keywords: [Syncfusion Winforms, Edit Control, text insertion, text deletion, VB.NET, C#, character deletion, word deletion, delete all text] -->
```