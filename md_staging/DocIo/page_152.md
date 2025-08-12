```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_152.jpeg
document_name: DocIo
page_number: 152
page_id: DocIo#page_152
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:37:28Z
fidelity: lossless
-->

## WFormField

### Public Constructor

| Name                                     | Description                                      |
|------------------------------------------|--------------------------------------------------|
| WTextField.WTextField(IWordDocument)     | Initializes a new instance of the WTextField class. |

### Public Properties

| Name           | Description                                |
|----------------|--------------------------------------------|
| DefaultText    | Gets/sets default text for text form field. |
| MaximumLength  | Gets/sets maximum text length.            |
| StringFormat   | Gets/sets string text format (text, date/time, number) directly. |
| TextRange      | Gets/sets form field text range.          |
| Type           | Gets/sets text form field type.           |

The following three examples illustrate the different variants of text form field usage.

```csharp
[C#]

Example 1

IWordDocument doc = new WordDocument(true);
IWordParagraph par = doc.LastParagraph;

// Append text form field to the paragraph.
WTextField textFormField = par.AppendTextFormField("Hello");
textField.TextFormat = TextFormat.Uppercase;
textField.Enabled = false;
textField.Help = "Help2";
```
```