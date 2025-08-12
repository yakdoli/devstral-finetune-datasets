```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_179.jpeg
document_name: DocIo
page_number: 179
page_id: DocIo#page_179
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:39:15Z
fidelity: lossless
-->

# Essential DocIO

TextBox is a shape. DocIO text box (WTextBox) has two properties which are as follows.

- `TextBoxFormat` – defines formatting of the text box (position, alignment, border colors, and so on)
- `TextBoxBody` – defines the text for the text box

The `TextBoxFormat` property returns the object of the `WTextBoxFormat` type. For more details, see `WTextBoxFormat`. The `TextBoxBody` property returns the object of the `WTextBoxBody` type.

You can use the `AppendTextBox` function of the `WParagraph` class to append a text box to a paragraph.

## Class Hierarchy

ParagraphItem  
|  
WTextBox

## Public Constructor

| Name | Description |
| --- | --- |
| `WTextBox.WTextBox(IWordDocument)` | Initializes a new instance of the `WTextBox` class. |

## Public Properties

| Name | Description |
| --- | --- |
| `ChildEntities` | Gets the child entities. |
| `EntityType` | Gets the type of the entity. |
| `OwnerParagraph` | Gets owner paragraph. |
| `TextBoxBody` | Get or sets `TextBoxBody` value. |
| `TextBoxFormat` | Get or sets `TextBoxFormat` value. |

The following example illustrates how to use the `WTextBox` and `TextBoxFormat` classes.

<!-- tags: [DocIO, WTextBox, WTextBoxFormat, TextBoxBody, TextBoxFormat, WParagraph, IWordDocument, class hierarchy, public constructor, public properties] keywords: [DocIO, WTextBox, WTextBoxFormat, TextBoxBody, TextBoxFormat, WParagraph, IWordDocument, class hierarchy, public constructor, public properties, text box formatting, text box properties, paragraph, text box appending, example usage] -->
```