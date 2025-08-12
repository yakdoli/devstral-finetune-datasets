```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_142.jpeg
document_name: edit
page_number: 142
page_id: edit#page_142
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:02:45Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- The page discusses the `Find` and `Replace` dialog boxes in Windows Forms, their functionalities, and how to invoke them programmatically using C# and VB.NET.

## Content

### Find Dialog Box

- **Description**: The Find dialog box displayed in Figure 47 allows users to search for specific words or text within the current document.
- **Features**:
  - **Find what**: The text to search for is entered here.
  - **Options**: Includes choices such as `Match case`, `Match whole word`, `Search hidden text`, `Search up`, and `Use Regular Expressions`.
  - **Search Scope**: Users can choose to search the `Current Document`.

#### Figure 47: Find Dialog Box

### Replace Dialog Box

- **Description**: The Replace dialog box invoked using the `ShowReplaceDialog` method and its keyboard shortcut `Ctrl+H`.
- **Functionality**: Allows users to find and replace words within the selected text.
- **Features**:
  - **Find what**: The text to search for.
  - **Replace with**: The text to replace the found text with.
  - **Options**: Similar to the Find dialog box, including `Match case`, `Match whole word`, `Search hidden text`, `Search up`, and `Use Regular Expressions`.
  - **Search Scope**: Users can choose between `Current document` or `Selected text`.

#### Figure 48: Replace Dialog Box

### Invoking Dialogs Programmatically

#### C# Code

```csharp
// Invoke the Find Dialog.
this.editControl1.ShowFindDialog();

// Invoke the Replace Dialog.
this.editControl1.ShowReplaceDialog();
```

#### VB.NET Code

```vb
' Invoke the Find Dialog.
Me.editControl1.ShowFindDialog()

' Invoke the Replace Dialog.
Me.editControl1.ShowReplaceDialog()
```

## References
- Syncfusion, All rights reserved.

---

<!-- tags: [Syncfusion, WinForms, Find Dialog, Replace Dialog] keywords: [Find Dialog, Replace Dialog, ShowFindDialog, ShowReplaceDialog, C#, VB.NET, Edit Control, Text Search, Text Replacement] -->
```