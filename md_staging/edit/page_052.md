```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_052.jpeg
document_name: edit
page_number: 052
page_id: edit#page_052
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:57:00Z
fidelity: lossless
-->

## Overview
- Describes how to use the autocomplete functionality in Windows Forms with the `IContextChoiceController`.
- Explains four cases for handling autocomplete suggestions when typing or pressing hotkeys.
- Includes code snippets in C# and VB.NET to demonstrate enabling autocomplete.

## Content

### Windows Forms Autocomplete

#### Case 1

If you type "wordr" after "this.editControl1.", such that it looks like - "this.editControl1.wordr", and press the ALT+RIGHT ARROW (or CTRL+SPACEBAR) keys, it will autocomplete it with the first matching member name. In this case, it will be autocompleted as "this.editControl1.WordRight".

#### Case 2

If you type "move" after "this.editControl1.", such that it looks like - "this.editControl1.move", and press the ALT+RIGHT ARROW (or CTRL+SPACEBAR) keys, it will autocomplete it with the first matching member name. In this case, there is no matching member name to autocomplete, and hence nothing will happen.

#### Case 3

If you type nothing after "this.editControl1.", and press the ALT+RIGHT ARROW (or CTRL+SPACEBAR) keys, it will autocomplete it with the first member name in the Context Choice list. In this case, it should be autocompleted as "this.editControl1.New".

#### Note on Case Sensitivity

Note that the searching process for the first matching member is not case sensitive. For example, "wordr" and "WordR" will be treated in the same way.

### Enabling Autocomplete

To enable this functionality while using Context Choice, set the `UseAutocomplete` property associated with the `IContextChoiceController` to `True`.

#### Code Example in C#

```csharp
private void editControl1_ContextChoiceOpen(Syncfusion.Windows.Forms.Edit.Interfaces.IContextChoiceController controller)
{
    controller.UseAutocomplete = true;
}
```

#### Code Example in VB.NET

```vb
Private Sub editControl1_ContextChoiceOpen(ByVal controller As Syncfusion.Windows.Forms.Edit.Interfaces.IContextChoiceController) Handles editControl1.ContextChoiceOpen
    controller.UseAutocomplete = True
End Sub
```

### See Also

- [AutoReplace Triggers](AutoReplace Triggers)

## Page-level Navigation/TOC
- Overview
- Content
  - Windows Forms Autocomplete
    - Case 1
    - Case 2
    - Case 3
    - Note on Case Sensitivity
  - Enabling Autocomplete
    - Code Example in C#
    - Code Example in VB.NET
- See Also

## RAG Annotations
<!-- tags: [windows forms, autocomplete, icontextchoicecontroller, useautocomplete, code examples] keywords: [winforms, contextchoice, member autocomplete, case sensitivity, hotkeys, alt+right arrow, ctrl+spacebar] -->
```