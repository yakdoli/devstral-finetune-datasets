```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_122.jpeg
document_name: edit
page_number: 122
page_id: edit#page_122
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:01:38Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- Supports ASCII encoding for the edit control.
- Supports multiple newline styles based on the Syncfusion.IO.NewLineStyle enumerator.
- Handles file-saving operations with data loss events for encoding format mismatches.
- Provides text selection methods for programmatically selecting text.

## Content

### Encoding and Newline Styles

```csharp
Me.editControl1.SetEncoding(Encoding.ASCII)
```

It also supports all the new line styles supported by the `Syncfusion.IO.NewLineStyle` enumerator - `Windows`, `Mac`, `Unix`, and `Control`.

| New Line Styles | Description   |
|------------------|---------------|
| Windows          | `\r\n`        |
| Mac              | `\r`          |
| Unix             | `\n`          |
| Control          | `\n`          |

### Handling Data Loss During Saving

The `SaveFileWithDataLoss` and `SaveStreamWithDataLoss` events are fired whenever there is a data loss while saving the file by using the specified encoding format. Files or streams can be corrupted if you have some Unicode characters that cannot be saved using the specified encoding format. For example, if you have a file or stream that contains some specific characters of the German language, and if you try to save it using ASCII encoding, then data loss will occur. If the save operation is not canceled here, characters will be saved incorrectly.

### Text Selection

#### Overview

The Edit Control supports text selection operations through the use of the APIs discussed in this section.

#### Selecting Text

Edit Control provides support to select text programmatically. The `StartSelection` and `StopSelection` methods are used to programmatically specify the starting and ending bounds for the text to be selected.

| Edit Control Method | Description                                 |
|---------------------|---------------------------------------------|
| `StartSelection`    | Sets selection start at the specified position in text. |
| `StopSelection`     | Sets selection end at the specified position in text. |
| `SetSelection`      | Sets selected area of the text.             |

## API Reference

### Methods
- `StartSelection`
- `StopSelection`
- `SetSelection`

### Parameters

| Name            | Type    | Description                                   | Default | Required |
|------------------|---------|-----------------------------------------------|---------|----------|
| `Position`      | `int`   | The starting or ending position in the text. | N/A     | Yes      |

### Returns

- None. These methods modify the text selection state directly.

### Exceptions

- No specific exceptions are mentioned; standard runtime exceptions may occur based on invalid input.

## Code Examples

### C# Example

```csharp
// Selecting text using StartSelection and StopSelection
editControl1.StartSelection(5);
editControl1.StopSelection(10);

// Using SetSelection directly
editControl1.SetSelection(5, 10);
```

## Page-level Navigation/TOC (if applicable)

- Newline Styles
- Data Loss During Saving
- Text Selection

## Cross References

- For more details on Unicode and ASCII encoding, refer to the documentation on character encoding.
- For handling data loss, see the section on file-saving operations.

## RAG Annotations

<!-- tags: [edit control, text selection, newline styles, file saving, data loss] keywords: [Syncfusion.IO.NewLineStyle, StartSelection, StopSelection, SetSelection, SaveFileWithDataLoss, SaveStreamWithDataLoss, ASCII encoding, Unicode characters] -->
```