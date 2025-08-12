```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_282.jpeg
document_name: edit
page_number: 282
page_id: edit#page_282
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:10:52Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

```csharp
// Reset the current configuration language cache to reflect these changes.
this.editControl1.Language.ResetCaches();
```

## [VB.NET]

```vb
'Removing Lexemes from the language
Me.editControl1.Language.Lexems.Remove(objConfigLex)

'Changing the lexems
objConfigLex = New ConfigLexem(Me.TextBox1.Text, "", FormatType.Custom, False)
objConfigLex.IndentationGuideline = True
objConfigLex.FormatName = "HighLight"

' Add it to the current language's Lexemes collection
Me.editControl1.Language.Lexems.Add(objConfigLex)

' Reset the current configuration language cache to reflect these changes.
Me.editControl1.Language.ResetCaches()
```

## 5.3 How To Clear the Undo Buffer In Essential Edit

You can use the `ResetUndoInfo` method to clear the undo buffer, and save the changes to the underlying stream. This is done to make sure that the changes on the contents/actions recently performed cannot be undone.

The Following code snippet illustrates this.

### [C#]

```csharp
// Code to clear the Undo buffer
this.editControl1.ResetUndoInfo();

// Code to discard all the Unsaved changes
this.editControl1.DiscardChanges();
```

### [VB.NET]

```vb
' Code to clear the Undo buffer
Me.editControl1.ResetUndoInfo()

' Code to discard all the Unsaved changes
Me.editControl1.DiscardChanges()
```
<!-- tags: [Essential Edit, Windows Forms, Undo Buffer, ResetUndoInfo, Clear Undo Buffer, Syncfusion Winforms, 11.4.0.26] keywords: [Essential Edit, Windows Forms, Undo Buffer, ResetUndoInfo, Clear Undo Buffer, Cached Language, Lexemes, Undo Buffer, Clear, Discard Unsaved Changes, VB.NET, C#] -->
```