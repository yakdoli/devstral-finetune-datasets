```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_049.jpeg
document_name: edit
page_number: 049
page_id: edit#page_049
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:57:06Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

```csharp
// Outdents text in the specified range.
this.editControl1.OutdentText(new Point(5, 5), new Point(10, 10));
// Outdents selected text.
this.editControl1.OutdentSelection();
```

```vbnet
' Indents text in the specified range.
Me.editControl1.IndentText(New Point(5, 5), New Point(10, 10))
' Indents selected text.
Me.editControl1.IndentSelection()

' Outdents text in the specified range.
Me.editControl1.OutdentText(New Point(5, 5), New Point(10, 10))
' Outdents selected text.
Me.editControl1.OutdentSelection()
```

## 4.2.7 Right-To-Left (RTL) Support

### Right-To-Left Support for EditControl

**Right-To-Left Support for EditControl**

EditControl supports rendering content in Right-To-Left (RTL) layout.

The following features that are present in Left-To-Right layout are also supported in Right-To-Left layout:

- Line numbers, Book Marks and Selection margins
- Context Menus, ToolTips and Dialogs
- Printing and print preview
- Line borders, Underline and Text Range customization

### Use Case Scenarios

With RTL support, you can use EditControl to render content in Right-To-left layout for languages such as Arabic. This is depicted in the screenshot below:
``` 

<!-- tags: [product, windows forms, Syncfusion, edit control, text editing, RTL support] keywords: [right-to-left, layout, text rendering, indention, outdention, features] -->
``` 
```