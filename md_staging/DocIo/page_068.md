```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_068.jpeg
document_name: DocIo
page_number: 068
page_id: DocIo#page_068
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:32:24Z
fidelity: lossless
-->

# Essential DocIO

BuiltInDocumentProperties class represents all document properties, excluding custom properties.

## Class Hierarchy

- SummaryDocumentProperties
  - BuiltInDocumentProperties

### Public Properties

| Name           | Description                                     |
|---------------|-------------------------------------------------|
| BytesCount    | Represents the number of bytes in the document. |
| Category      | Gets or sets the category of the document.      |
| Company       | Gets or sets Company property.                  |
| HiddenCount   | Gets or sets hidden count.                      |
| LinesCount    | Gets or sets the number of lines in the document. |
| Manager       | Gets or sets Manager property.                  |
| NoteCount     | Gets or sets Note count.                        |
| ParagraphCount| Gets or sets the number of paragraphs in the<br> document. |
| SlideCount    | Gets or sets slide count.                       |

### Public Methods

| Name   | Description        |
|-------|--------------------|
| Clone  | Clones itself.    |

## Example of Using BuiltInDocumentProperties

The following example illustrates how to get, set, and modify the document properties.

## Code Example

Here is an example of how to use the `BuiltInDocumentProperties` class in a C# application:

```csharp
using Syncfusion.DocIO;

// Create a new Document instance
WordDocument document = new WordDocument();

// Access the built-in document properties
BuiltInDocumentProperties bldrProperty = document.BuiltInDocumentProperties;

// Set properties
bldrProperty.LinesCount = 100;
bldrProperty.ParagraphCount = 20;
bldrProperty.Company = "Syncfusion Inc.";
bldrProperty.Category = "Technical Documentation";

// Clone the properties
BuiltInDocumentProperties clonedProperties = bldrProperty.Clone();
```

## Summary

This page provides an overview of the `BuiltInDocumentProperties` class in Syncfusion DocIO, detailing its class hierarchy, public properties, and public methods. It also includes an example demonstrating how to use these properties to manage document properties programmatically.

## API Reference

### BuiltInDocumentProperties Class

#### Properties

- **BytesCount**: Represents the number of bytes in the document.
- **Category**: Gets or sets the category of the document.
- **Company**: Gets or sets the Company property.
- **HiddenCount**: Gets or sets hidden count.
- **LinesCount**: Gets or sets the number of lines in the document.
- **Manager**: Gets or sets the Manager property.
- **NoteCount**: Gets or sets Note count.
- **ParagraphCount**: Gets or sets the number of paragraphs in the document.
- **SlideCount**: Gets or sets slide count.

#### Methods

- **Clone**: Creates a copy of the BuiltInDocumentProperties object.

## See also

- [Syncfusion DocIO Documentation](#)
- [BuiltInDocumentProperties Class](#)

<!-- tags: [DocIO, built-in document properties, document management, properties, methods, syncfusion, winforms, version: 11.4.0.26] keywords: [built-in, document properties, get, set, modify, count, category, company, hidden, line, paragraph, note, slide, clone, properties] -->
```