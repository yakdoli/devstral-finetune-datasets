```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_253.jpeg
document_name: DocIo
page_number: 253
page_id: DocIo#page_253
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:45:00Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- Describes the `TextBodySelection` class and its methods for selecting, copying, and pasting text elements in a document.
- Provides an example of how to use the `Copy` and `Paste` methods of `TextBodyPart` to manipulate text content within a document.

## Content

### TextBodySelection Class Details

#### Public Constructors

| Name | Description |
| --- | --- |
| `TextBoxSelection.TextBoxSelection(ITextBody, int, int, int, int)` | Initializes a new instance of the `TextBoxSelection` class. |
| `TextBoxSelection.TextBoxSelection(ParagraphItem, ParagraphItem)` | Initializes a new instance of the `TextBoxSelection` class. |

#### Public Properties

| Name | Description |
| --- | --- |
| `ItemEndIndex` | Gets or sets the end index of the text body item. |
| `ItemStartIndex` | Gets or sets the start index of the text body item. |
| `ParagraphItemEndIndex` | Gets or sets the end index of the paragraph item. |
| `ParagraphItemStartIndex` | Gets or sets the start index of the paragraph item. |
| `TextBody` | Gets the text body. |

### Copy and Paste Methods in `TextBoxPart`

The `Copy` and `Paste` methods of `TextBoxPart` in the `TextBoxSelection` class are used to copy and paste text and body elements at any position in the document. The following code snippet illustrates this.

```csharp
[C#]

// Create TextBoxSelection and select the items of interest.
TextBoxSelection textSel = new TextBoxSelection(sec.Body, 0,
lastItemIndex, 0, lastPItemIndex);

// Create TextBoxPart and copy the selected items.
TextBoxPart replacePart = new TextBoxPart(doc);
replacePart.Copy(textSel);

// Paste the copied content at the end of the text body.
```

## Page-level Navigation/TOC

- Public Constructors
- Public Properties
- Copy and Paste methods of TextBoxPart

## Cross References

See also:
- Fan Dashboard (for context on using document manipulation in Forms applications)
- `ITextBody` class for reference to the text body structure

<!-- tags: [syncfusion, winforms, document processing, text manipulation, copy-paste, version:11.4.0.26] keywords: [textbodyselection, textboxpart, copy, paste, document manipulation, syncfusion sdk, csharp, winforms] -->
```