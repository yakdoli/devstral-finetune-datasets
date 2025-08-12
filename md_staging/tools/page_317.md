```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_317.jpeg
document_name: tools
page_number: 317
page_id: tools#page_317
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:05:04Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

```csharp
this.autoCompletel.AllowListDelete = true;
```

```vb
Me.autoCompletel.AllowListDelete = True
```

## Overview
- Explains how to configure and manage the `AutoCompleteControl` in Windows Forms using essential tools.
- Demonstrates enabling and resetting history items in the AutoComplete control.
- Includes implementation examples in both C# and VB.NET.
- Shows how to use AutoComplete with custom `UserControl` and `RichTextBox` controls.

## Content

### 3.5.1.1.5.5 How to delete the history items persisted by an AutoComplete control?

We can delete the history items persisted by an `AutoCompleteControl` by calling the `AutoComplete.ResetHistory()` method.

```csharp
this.autoCompletel.ResetHistory();
```

```vb
Me.autoCompletel.ResetHistory()
```

### 3.5.1.1.5.6 How to implement an AutoComplete Control in an User Control?

AutoComplete control can be used in an `UserControl` by setting the parent form of the User Control to the parent form property of the `AutoComplete Control`.

```csharp
private void UserControll_Load(object sender, System.EventArgs e)
{
    this.autoCompletel.ParentForm = this.ParentForm;
    this.autoCompletel.DataSource = this.items;
}
```

```vb
Private Sub UserControll_Load(ByVal sender As Object, ByVal e As System.EventArgs)
    Me.autoCompletel.ParentForm = Me.ParentForm
    Me.autoCompletel.DataSource = Me.items
End Sub
```

### 3.5.1.1.5.7 How to implement AutoComplete with RichTextBox control?

Follow the below steps to implement AutoComplete feature with `RichTextBox` control.

## API Reference (if applicable)

## Code Examples (multi-language supported)

## RAG Annotations
<!-- tags: [Syncfusion, WinForms, AutoCompleteControl, WindowsForms, UserControls, RichTextBox] keywords: [allowlistdelete, resethistory, auto-complete, user control, rich text box, history items, AutocompleteDataSource, ParentForm] -->
```