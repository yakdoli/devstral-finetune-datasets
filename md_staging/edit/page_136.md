```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_136.jpeg
document_name: edit
page_number: 136
page_id: edit#page_136
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:01:50Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- The mode of the INSERT key in the Edit Control is controlled programmatically via the InsertMode property.
- Toggling the InsertMode property mimics pressing the INSERT key on the keyboard.
- When InsertMode is True, new characters insert into the control; when False, characters overwrite existing text.
- Default InsertMode setting is True.

## Content

The mode of the INSERT key in the Edit Control can be controlled programmatically by using the InsertMode property. Toggling the value of this property is equivalent to pressing the INSERT key on the keyboard. When InsertMode is set to True, the characters typed get inserted into the Edit Control, without overwriting the existing text. When set to False, the characters typed overwrite the existing text of the Edit Control. By default, this property is set to True.

The mode of the INSERT key can also be toggled by using the ToggleInsertMode method of the Edit Control.

### Code Examples

#### C#
```csharp
// Enable the insert key mode in Edit Control.
this.editControl1.InsertMode = true;

// Toggle the insert mode.
this.editControl1.ToggleInsertMode();
```

#### VB.NET
```vb
' Enable the insert key mode in Edit Control.
Me.editControl1.InsertMode = True

' Toggle the insert mode.
Me.editControl1.ToggleInsertMode()
```

### 4.6.2 Keyboard Shortcuts

The keyboard shortcuts for the commands in the Edit Control are listed below.

#### Keyboard Shortcuts Table

| Command     | Shortcut              |
|-------------|------------------------|
| Clipboard    |                        |
| Copy         | CTRL+C, CTRL+INSERT   |
| Paste        | CTRL+V, SHIFT+INSERT  |
| Cut          | CTRL+X, SHIFT+DEL     |
| SelectAll    | CTRL+A                 |
| File Operation |                      |

## Page-level Navigation/TOC (if applicable)
- 4.6.2 Keyboard Shortcuts

## RAG Annotations
<!-- tags: [syncfusion, windowsforms, insertmode, toggleinsertmode, keyboard shortcuts, edit control] keywords: [insert mode, toggle, append, overwrite, ctrl+c, ctrl+v, shift+insert, clipboard commands, select all] -->
```