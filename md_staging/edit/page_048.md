```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_048.jpeg
document_name: edit
page_number: 048
page_id: edit#page_048
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:56:43Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- Edit Control supports VS.NET-like Block Indent and Outdent features.
- Allows text selection and manipulation using TAB, SPACE, and SHIFT+TAB keys.
- Programmatically sets the tab size using the TabSize property.
- Methods are available to indent and outdent text programmatically.
- Examples are provided in C# and VB.NET.

## Content

### Block Indent and Outdent

Edit Control supports VS.NET-like Block Indent and Outdent. When a block of text is selected, pressing the TAB or SPACE keys adds an appropriate number of tabs or spaces to the beginning of each line in the selected block. This moves the selected section of the code to the right by the specified number of tabs or spaces. Pressing the SHIFT+TAB keys combination removes the tabs or spaces previously added, effectively undoing the last action.

### Setting the Tab Size

You can set the tab size to the desired number of spaces using the `TabSize` property of the Edit Control, as shown below. By default, the `TabSize` property value is set to `2`.

#### Code Example: Setting Tab Size

**C#**
```csharp
// "n" is the integer value specifying the number of spaces.
this.editControl1.TabSize = n;
```

**VB.NET**
```vbnet
' "n" is the integer value specifying the number of spaces.
Me.editControl1.TabSize = n
```

### Indent and Outdent Text Programmatically

The following methods are used to indent and outdent text in the Edit Control.

| Edit Control Method        | Description                       |
|----------------------------|-----------------------------------|
| IndentText                 | Indents text in the specified range. |
| IndentSelection            | Indents selected text.           |
| OutdentText                | Outdents text in the specified range. |
| OutdentSelection           | Outdents selected text.         |

#### Code Example: Indenting and Outdenting Text

**C#**
```csharp
// Indents text in the specified range.
this.editControl1.IndentText(new Point(5, 5), new Point(10, 10));
// Indents selected text.
this.editControl1.IndentSelection();
```

## API Reference

### Methods

- **IndentText**: Indents text in the specified range.
- **IndentSelection**: Indents selected text.
- **OutdentText**: Outdents text in the specified range.
- **OutdentSelection**: Outdents selected text.

## Code Examples

The above section demonstrates how to use the methods to manipulate text indentation programmatically in C# and VB.NET.

<!-- tags: [Syncfusion Winforms, Edit Control, TabSize, Indent, Outdent, C#, VB.NET] keywords: [indentation, text manipulation, programmatically, selected text, tab size] -->
```