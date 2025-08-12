```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_071.jpeg
document_name: edit
page_number: 071
page_id: edit#page_071
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:57:58Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- Provides support for appending, deleting, and inserting multiple lines of text in an Edit Control.
- Utilizes specific APIs and properties for text manipulation.
- Includes examples in C# and VB.NET for clarity.

## Content

### 4.4.5.1 Appending, Deleting, and Inserting Multiple Lines of Text
Edit Control offers support for text manipulation operations like append, delete, and insertion of multiple lines of text, through the use of the following APIs.

#### Appending Text
Text can be appended to the Edit Control by using the below given method.

| Edit Control Method | Description                                             |
|--------------------|-------------------------------------------------------|
| AppendText         | Appends the specified text to the end of the existing contents of the Edit Control. |

#### Code Examples

**C#**
```csharp
// Appends the given string to the end of the text in Edit Control.
this.editControl1.AppendText(" text to be appended ");
```

**VB.NET**
```vb.net
' Appends the given string to the end of the text in the Edit Control.
Me.editControl1.AppendText(" text to be appended ")
```

#### Inserting Text
The Insert mode can be enabled in the Edit Control by setting the `InsertMode` property to `True`.

Text can be inserted anywhere inside the Edit Control by using the `InsertText` method given below.

| Edit Control Method | Description                                   |
|--------------------|---------------------------------------------|
| InsertText         | Inserts a piece of text at any desired position in the Edit Control. |

#### Inserting Multiple Lines
Collection of text lines can be inserted by using the property given below.

| Edit Control Property | Description                                 |
|--------------------|---------------------------------------------|
| [Property Name]       | [Description for the property.]             |

### Page-level Navigation/TOC (if applicable)
- [4.4.5.1 Appending, Deleting, and Inserting Multiple Lines of Text]
  - Appending Text
  - Inserting Text
  - Inserting Multiple Lines

## API Reference (if applicable)
- `AppendText`: Appends the specified text to the end of the existing contents of the Edit Control.
- `InsertText`: Inserts a piece of text at any desired position in the Edit Control.
- `InsertMode`: A boolean property to enable or disable the Insert mode.

## Code Examples (multi-language supported)
- C# and VB.NET examples provided above for `AppendText` and `InsertText`.

## Cross References
See also:
- [Previous section: Working with Text Control](#page_ref)
- [Related topic: Editing Modes](#page_ref)

<!-- tags: [Edit Control, AppendText, InsertText, InsertMode, Windows Forms] keywords: [text manipulation, append, insert, delete, multiple lines, edit control] -->
```