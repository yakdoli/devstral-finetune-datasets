```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_137.jpeg
document_name: DocIo
page_number: 137
page_id: DocIo#page_137
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:36:57Z
fidelity: lossless
-->

# Essential DocIO

## WField Class Hierarchy

You can get or set the type of field by using the `FieldType` property. `WField` class also has the `TextFormat` property, which defines the text format for the field. There are four different types of text formats for fields:

- None – no text formatting
- Uppercase – uppercase text formatting
- Lowercase – lowercase text formatting
- FirstCapital – first capital text formatting
- Titlecase – title case text formatting

### Adding Field to Paragraph

You can use the `AppendField` function of the `WParagraph` class to add new fields to a paragraph. When you add a field to a paragraph, all the field markers are automatically added to the paragraph. For details, refer `WFieldMark` class description.

There are special fields like Form Field, Merge Field, Embed Field, and Seq Field. For details, refer the `WFormField`, `WMergeField`, `WEmbedField`, and `WSeqField` documentation.

### Class Hierarchy

- `WTextRange`
  - `WField`

## API Reference (if applicable)

### Namespaces and Classes

- **WField**
  - `FieldType`
  - `TextFormat` (None, Uppercase, Lowercase, FirstCapital, Titlecase)
  - `Mark` (WFieldMark)

### Methods

- **`WParagraph.AppendField`**
  - Adds a field to the paragraph.

### Properties

- **`WField.FieldType`**
  - Gets or sets the type of the field.

- **`WField.TextFormat`**
  - Defines the text format for the field.

### Notes

- For detailed information on field markers and specific field implementations, refer to the `WFieldMark`, `WFormField`, `WMergeField`, `WEmbedField`, and `WSeqField` documentation.

## See also

- [WFieldMark Documentation](#)
- [WFormField Documentation](#)
- [WMergeField Documentation](#)
- [WEmbedField Documentation](#)
- [WSeqField Documentation](#)

<!-- tags: [Syncfusion, Winforms, DocIo, WField, WFieldMark, WFormField, WMergeField, WEmbedField, WSeqField, text formatting, API reference, programming guide] keywords: [WField, FieldType, TextFormat, WParagraph.AppendField, WFieldMark, WFormField, WMergeField, WEmbedField, WSeqField, text formatting, Winforms, DocIO, documentation, API, reference] -->
```