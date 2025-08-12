```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_297.jpeg
document_name: DocIo
page_number: 297
page_id: DocIo#page_297
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:48:08Z
fidelity: lossless
-->

# Essential DocIO

## Content

### Supported Elements

This feature provides support for the following elements:

- Paragraph and Character Formatting
- Tables
- Bookmarks
- Headers and Footers
- Images
- List
- Page setting
- Multi column text
- Breaks
- Document properties
- Fields

#### Fields

This feature supports the preservation of fields in Rtf to Doc conversion.

#### Paragraph and Character Formatting

This feature supports almost all the paragraph and character formatting. The supported formatting features are:

- Paragraph borders
- Indentation and Pagination
- Spacing and Tabs

## Code Examples

### C#

```csharp
// Opening the RTF file
WordDocument doc = new WordDocument("Sample.rtf", FormatType.Rtf);

// Saving the RTF file as a word document
doc.Save("RtfToDoc_Res.doc", FormatType.Doc);
```

### VB.NET

```vb
' Opening the RTF file
Dim doc As New WordDocument("Sample.rtf", FormatType.Rtf)

' Saving the RTF file as a word document
doc.Save("RtfToDoc_Res.doc", FormatType.Doc)
```

## API Reference

#### Supported Elements

- **Paragraph and Character Formatting**: Handles paragraph borders, indentation, pagination, spacing, and tabs.
- **Tables**: Preservation of table structures.
- **Bookmarks**: Maintains document bookmarks.
- **Headers and Footers**: Includes headers and footers in conversions.
- **Images**: Supports image inclusion.
- **List**: Handles lists and their structures.
- **Page setting**: Maintains page settings such as margins and orientation.
- **Multi column text**: Preserves multi-column text formatting.
- **Breaks**: Supports page and section breaks.
- **Document properties**: Maintains document properties.
- **Fields**: Preserves fields in Rtf to Doc conversion.

<!-- tags: [Essential DocIO, RTF to DOC conversion, document formatting, paragraph formatting, table handling, VB.NET, C#] keywords: [DocIO, RTF, DOC, paragraph, character, table, bookmark, header, footer, image, list, page setting, multi-column, break, document properties, field, headers, footers, indentation, pagination, spacing, tabs] -->
```