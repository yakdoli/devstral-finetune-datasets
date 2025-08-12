```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_102.jpeg
document_name: DocIo
page_number: 102
page_id: DocIo#page_102
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:33:55Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- Use the ImportContent method to transfer content and styles between documents.
- Understand how to handle conflicting styles and preserve unique style names.
- Explore various ImportOptions for importing contents with specific formatting rules.

## Content

### ImportContent Methods

#### ImportContent(WordDocument doc)
Use this method to import contents and styles from the source document to the destination document.

#### ImportContent(WordDocument doc, bool importStyles)
Use this method to import contents from the source document to the destination document by specifying whether to import styles which have the same name between the source and destination document.

- **If importStyles is true**:
  - All the contents and styles of the source document will be imported to the destination document.
  - If a style in the source document has the same name as a style in the destination document, "Guid" is added as a suffix to the name of the imported style to preserve unique style name.

- **If importStyles is false**:
  - All the contents will be imported, but only the styles that are not present in the destination document will be preserved.
  - If a style with the same name exists in the destination document, the destination style is applied to the imported contents.

#### Note:
If source and destination documents have styles with the same names, then "Guid" is added as a suffix to the name of the imported styles in the destination document.

### ImportContent(WordDocument doc, ImportOptions importOptions)
Use this method to import contents from the source document to the destination document with various import options similar to MS Word copy and paste options.

Below are the import options supported by Essential DocIO:

- **KeepSourceFormatting**:
  - Imports all the contents of the source document to the destination document and preserves the entire source document formatting of the content as direct formatting.
  - Header and footer contents will be imported similar to the UseDestinationStyles option.

- **MergeFormatting**:
  - Imports all the contents of the source document to the destination document and applies the formatting of surrounding content in the destination document.
  - Merges the formatting of the contents surrounding it by preserving some of the source formatting (such as bold, italic, underline, etc.).
  - Header and footer contents will be imported similar to the UseDestinationStyles option.

- **KeepTextOnly**:
  - Imports only the text from the source document to the destination document (tables, textboxes, pictures, headers, footers, etc., will be removed).
  - Similar to content copied from a text file (.txt).

- **UseDestinationStyles**:
  - Imports all the content of the source document to the destination document and applies the styles present in the destination document.
  - Imports the source style to the destination document if no style with the same name exists in the destination document.

### Example
The following example illustrates how to import contents from one document to another with various import options.

## API Reference

- **Namespace**: Syncfusion.DocIO
- **Class**: WordDocument
- **Methods**: ImportContent
  - Parameters:
    - `doc`: The source WordDocument from which contents are imported.
    - `importStyles`: A boolean indicating whether to import styles.
    - `importOptions`: An ImportOptions object specifying import rules.

### Code Examples

```csharp
// Example of using ImportContent with importStyles set to true
WordDocument sourceDoc = new WordDocument("source.docx");
WordDocument destinationDoc = new WordDocument("destination.docx");
destinationDoc.ImportContent(sourceDoc, true);
```

## Page-level Navigation/TOC (if applicable)
N/A

## Cross References
N/A

## RAG Annotations
<!-- tags: [docio, worddocument, importcontent, importoptions, syncfusion winforms, 11.4.0.26] keywords: [import, styles, formatting, merge, keep text, use destination styles, source document, destination document] -->
```