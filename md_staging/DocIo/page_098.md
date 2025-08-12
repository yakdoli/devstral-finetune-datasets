```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_098.jpeg
document_name: DocIo
page_number: 098
page_id: DocIo#page_098
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:33:39Z
fidelity: lossless
-->

# Essential DocIO

| Property        | Description                                                               |
|-----------------|---------------------------------------------------------------------------|
| BreakCode       | Gets / sets break code.                                                  |
| ChildEntitiesx  | Gets the child entities.                                                 |
| Columns         | Gets collection of columns, which logically divide page on many printing/publishing areas. |
| EntityType      | Gets the type of the entity.                                             |
| HeadersFooters  | Gets headers/footers of current section.                                |
| PageSetup       | Gets page Setup of current section.                                     |
| Paragraphs      | Gets the paragraphs.                                                     |
| Tables          | Gets the tables.                                                         |

## Public Methods

| Name               | Description                           |
|--------------------|---------------------------------------|
| AddColumn          | Adds new column to the section.       |
| AddParagraph       | Adds the paragraph.                   |
| AddTable           | Adds the table.                      |
| Clone              | Clones itself.                       |
| MakeColumnsEqual   | Makes all columns in current section to be of equal width. |

### Example: Creating a Simple Word Document and Adding Sections and Breaks

The following example illustrates how to create a simple Word document, and add sections and breaks to it.

```csharp
// Create a new Word document
IWordDocument doc = new WordDocument();

// Add a section
IWSection section = doc.AddSection();

// Add a paragraph to the section
IWordParagraph paragraph = section.AddParagraph();

// Append text to the paragraph
paragraph.AppendText("Text Body_Text");
```

## API Reference

### Methods

- **AddColumn**: Adds a new column to the section.
- **AddParagraph**: Adds a paragraph to the section.
- **AddTable**: Adds a table to the section.
- **Clone**: Creates a deep copy of the current object.
- **MakeColumnsEqual**: Sets all columns in the section to have equal width.

## Code Examples

### Creating a Word Document with Sections and Breaks

```csharp
using Syncfusion.DocIO;
using Syncfusion.DocIO.DLS;

// Create a new Word document
IWordDocument doc = new WordDocument();

// Add a section
IWSection section = doc.AddSection();

// Add a paragraph to the section
IWordParagraph paragraph = section.AddParagraph();

// Append text to the paragraph
paragraph.AppendText("Text Body_Text");

// Save the document
doc.Save("Output.docx", FormatType.Docx);
```

<!-- tags: [DocIO, WordDocument, Section, Paragraph, Table, Column, BreakCode, PageSetup, HeadersFooters, AddColumn, AddParagraph, AddTable, Clone, MakeColumnsEqual] keywords: [section, paragraph, table, column, break, document creation, document manipulation, Word document, DocIO, API reference, example, code snippets] -->
```