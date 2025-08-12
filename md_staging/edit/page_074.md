```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_074.jpeg
document_name: edit
page_number: 074
page_id: edit#page_074
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:58:32Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview

This page provides an overview of essential text manipulation methods in Windows Forms using `editControl`, including deleting characters, words, selections, and all text. Code examples are provided in both C# and VB.NET.

## Content

The `editControl` class offers methods to perform various deletion operations based on cursor position or selected text. Below are the methods explained with examples in both C# and VB.NET:

### C#

```csharp
// Deletes the character to the right of the current cursor position.
this.editControl.DeleteChar();

// Deletes the character to the left of the current cursor position.
this.editControl.DeleteCharLeft();

// Deletes a word to the right of the current cursor position.
this.editControl.DeleteWord();

// Deletes a word to the left of the current cursor position.
this.editControl.DeleteWordLeft();

// Deletes all the text.
this.editControl.DeleteAll();

// Deletes a selection.
this.editControl.DeleteText(this.editControl.Selection.Top, 
                           this.editControl.Selection.Bottom);
```

### VB.NET

```vb
' Deletes the character to the right of the cursor.
Me.editControl.DeleteChar()

' Deletes the character to the left of the cursor.
Me.editControl.DeleteCharLeft()

' Deletes a word to the right of the current cursor position.
Me.editControl.DeleteWord()

' Deletes a word to the left of the current cursor position.
Me.editControl.DeleteWordLeft()

' Deletes all the text.
Me.editControl.DeleteAll()

' Deletes a selection.
Me.editControl.DeleteText(Me.editControl.Selection.Top, 
                          Me.editControl.Selection.Bottom)
```

### Key Points

- **`DeleteChar()`**: Deletes the character immediately to the right of the cursor.
- **`DeleteCharLeft()`**: Deletes the character immediately to the left of the cursor.
- **`DeleteWord()`**: Deletes the word to the right of the cursor.
- **`DeleteWordLeft()`**: Deletes the word to the left of the cursor.
- **`DeleteAll()`**: Deletes all the text in the control.
- **`DeleteText()`**: Deletes the selected text based on the top and bottom indices of the selection.

## API Reference

### Methods

- **`DeleteChar()`**  
  - **Action**: Deletes the character to the right of the cursor.

- **`DeleteCharLeft()`**  
  - **Action**: Deletes the character to the left of the cursor.

- **`DeleteWord()`**  
  - **Action**: Deletes the word to the right of the cursor.

- **`DeleteWordLeft()`**  
  - **Action**: Deletes the word to the left of the cursor.

- **`DeleteAll()`**  
  - **Action**: Deletes all the text in the control.

- **`DeleteText(startIndex, endIndex)`**  
  - **Parameters**:  
    - `startIndex`: The top index of the selection.  
    - `endIndex`: The bottom index of the selection.  
  - **Action**: Deletes the text within the specified range.

## Code Examples

### C#

```csharp
// Example: Deleting the character to the left of the cursor.
this.editControl.DeleteCharLeft();

// Example: Deleting all text in the control.
this.editControl.DeleteAll();

// Example: Deleting a selected text range.
this.editControl.DeleteText(10, 20);
```

### VB.NET

```vb
' Example: Deleting the character to the left of the cursor.
Me.editControl.DeleteCharLeft()

' Example: Deleting all text in the control.
Me.editControl.DeleteAll()

' Example: Deleting a selected text range.
Me.editControl.DeleteText(10, 20)
```

### Conclusion

The `editControl` provides various methods to handle text deletion efficiently, allowing precise control over character and word deletion, as well as handling selections and deleting all text within the control.

<!-- tags: [Syncfusion, Windows Forms, editControl, text manipulation, delete methods, C#, VB.NET] keywords: [DeleteChar, DeleteCharLeft, DeleteWord, DeleteWordLeft, DeleteAll, DeleteText, selection, cursor position] -->
```