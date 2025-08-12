```html
<!--  
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_140.jpeg
document_name: DocIo
page_number: 140
page_id: DocIo#page_140
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:36:49Z
fidelity: lossless
-->

# Essential DocIO

## Content

### Overview

WField

- **Public Constructor**

| Name                                                 | Description                                               |
|------------------------------------------------------|-----------------------------------------------------------|
| WMergeField.WMergeField (WordDocument)              | Initializes a new instance of the WMergeField class.      |

#### Public Properties

| Name       | Description                          |
|------------|--------------------------------------|
| DateFormat | Gets the date format.               |
| EntityType | Gets the type of the entity.        |
| FieldName  | Gets or sets field name.            |
| NumberFormat | Gets the number format.          |
| Prefix     | Gets the prefix of merge field.     |
| TextAfter  | Gets or sets the text after merge field. |
| TextBefore | Gets or sets the text before merge field. |

The following example illustrates how to add the a merge field to the header and footer of the document.

#### Code Example

```csharp
[C#]
IWSection section = doc.AddSection();
IWPagraph paragraph = section.AddParagraph();
paragraph.AppendText("Testing writing Merge Fields into Header");

section.PageSetup.DifferentFirstPage = true;
section.PageSetup.DifferentOddAndEvenPages = true;

paragraph = new WParagraph(doc);
paragraph.AppendText("[ FIRST PAGE Header ]");
```

## Remarks

The provided code example demonstrates the process of adding merge fields to the header and footer of a document, utilizing the `WMergeField` class from the Syncfusion DocIO library. The example showcases how to create a new section, add paragraphs, and configure page settings to accommodate different headers and footers.

## Related Topics

- [WinForms Overview](WinForms Overview)
- [DocIO Overview](DocIO Overview)
- [Merge Fields](Merge Fields)

<!-- tags: [DocIO, WinForms, WMergeField, MergeField, DocIO Documentation] keywords: [DocIO, WinForms, WMergeField, merge field, document header, document footer, code example, API reference, sample code, section, paragraph] -->
```