```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_138.jpeg
document_name: DocIo
page_number: 138
page_id: DocIo#page_138
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:36:31Z
fidelity: lossless
-->

# Public Constructor

| Name                            | Description                                                                 |
|---------------------------------|-----------------------------------------------------------------------------|
| WField.WField (IWordDocument)   | Initializes a new instance of the WField class.                           |

## Public Properties

| Name          | Description                                                                 |
|---------------|-----------------------------------------------------------------------------|
| EntityType    | Gets the type of the entity.                                                |
| FieldPattern  | Gets / sets field pattern.                                                 |
| FieldType     | Gets / sets field type                                                     |
| FieldValue    | Gets the field value.                                                      |
| TextFormat    | Gets/ sets regular text format.                                            |

## Code Example: C#

```csharp
IWSection section = doc.AddSection();
IWParagraph paragraph = section.AddParagraph();
paragraph.AppendText("[Testing writing Merge Fields into Header]");

section.PageSetup.DifferentFirstPage = true;
section.PageSetup.DifferentOddAndEvenPages = true;

paragraph = new WParagraph(doc);
paragraph.AppendText("[ FIRST PAGE Header ]");
section.HeadersFooters.FirstPageHeader.Paragraphs.Add(paragraph);
paragraph = new WParagraph(doc);

// Appends field
paragraph.AppendField("Field's Name", FieldType.FieldMergeField);
section.HeadersFooters.FirstPageHeader.Paragraphs.Add(paragraph);

paragraph = new WParagraph(doc);
paragraph.AppendText("[ FIRST PAGE Footer ]\r");
section.HeadersFooters.FirstPageFooter.Paragraphs.Add(paragraph);
```

## Code Example: VB.NET

```vb
Dim section As IWSection = doc.AddSection()
Dim paragraph As IWParagraph = section.AddParagraph()
paragraph.AppendText("[Testing writing Merge Fields into Header]")

section.PageSetup.DifferentFirstPage = True
section.PageSetup.DifferentOddAndEvenPages = True

paragraph = New WParagraph(doc)
paragraph.AppendText("[ FIRST PAGE Header ]")
section.HeadersFooters.FirstPageHeader.Paragraphs.Add(paragraph)
paragraph = New WParagraph(doc)

' Appends field
paragraph.AppendField("Field's Name", FieldType.FieldMergeField)
section.HeadersFooters.FirstPageHeader.Paragraphs.Add(paragraph)

paragraph = New WParagraph(doc)
paragraph.AppendText("[ FIRST PAGE Footer ]\r")
section.HeadersFooters.FirstPageFooter.Paragraphs.Add(paragraph)
```

## API Reference

- **Namespace:** The namespace containing the `WField` class.
- **Class:** WField
  - **Constructor:**
    - **WField.WField (IWordDocument):** Initializes a new instance of the WField class.

  - **Properties:**
    - **EntityType:** Gets the type of the entity.
    - **FieldPattern:** Gets / sets the field pattern.
    - **FieldType:** Gets / sets the field type.
    - **FieldValue:** Gets the field value.
    - **TextFormat:** Gets / sets regular text format.

```html
<!-- tags: [Syncfusion, Winforms, WField, Word Document, Document, Header, Footer, Text Format, Field Pattern, Field Type, Field Value, Public Properties, C#, VB.NET] keywords: [WField, IWordDocument, EntityType, FieldPattern, FieldType, FieldValue, TextFormat, Public Properties, Header, Footer, Merge Fields, AppendField, DifferentFirstPage, DifferentOddAndEvenPages, DocIo, Syncfusion, Winforms] -->
```