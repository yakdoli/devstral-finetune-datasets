```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_072.jpeg
document_name: edit
page_number: 072
page_id: edit#page_072
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:58:21Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- Allows specification of multiple lines of text to the Edit Control in the form of a string array.
- Provides properties to insert text based on conditions.
- Demonstrates control over text insertion, drag-and-drop file handling, and尊重tab stops.

## Content

### Lines
| Lines | Description |
| --- | --- |
|  | Lets you specify multiple lines of text to the Edit Control in the form of a string array. This feature is similar to the one in .NET RichTextBox control. |

### Inserting Text based on Conditions

The below given properties can be used to insert text based on conditions which have been described below.

| Edit Control Property | Description |
| --- | --- |
| AllowInsertBeforeReadOnlyNewLine | Specifies whether inserting text should be allowed at the beginning of readonly region at the start of a new line. |
| InsertDroppedFileIntoText | Specifies whether the outer file dragged and dropped onto the Edit Control should be inserted into the current content.<br/><br/>When this property is set to 'False', the current file is closed, and the dropped outer file is opened. |
| RespectTabStopsOnInsertingText | Specifies whether tab stops should be respected on inserting blocks of text. |

### Code Examples (C#)

```csharp
// Set the Insert mode.
this.editControl1.InsertMode = true;

// Inserts a string at the given line and column.
this.editControl1.InsertText(1, 1, " text to be inserted ");

// Specifies multiple lines of text to the EditControl in the form of a string array.
this.editControl1.Lines = new string[] { " first line ", " second line ", " third line " };

// Allows text insertion only at the beginning of the readonly region at the start of a new line.
this.editControl1.AllowInsertBeforeReadOnlyNewLine = true;

// Specifies whether the outer file dragged and dropped onto the editcontrol should be inserted into the current content.
this.editControl1.InsertDroppedFileIntoText = true;
```

## API Reference

This section references the properties and methods used in the code examples.

### Properties
- `InsertMode`
- `Lines`
- `AllowInsertBeforeReadOnlyNewLine`
- `InsertDroppedFileIntoText`
- `RespectTabStopsOnInsertingText`

## RAG Annotations
<!-- tags: [Syncfusion Winforms, edit control, text insertion, drag-and-drop, tab stops] keywords: [AllowInsertBeforeReadOnlyNewLine, InsertDroppedFileIntoText, RespectTabStopsOnInsertingText, Lines, InsertText] -->
```
