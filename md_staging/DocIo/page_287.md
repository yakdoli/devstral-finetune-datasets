```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_287.jpeg
document_name: DocIo
page_number: 287
page_id: DocIo#page_287
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:46:19Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- The document details the rendering and export properties supported by DocIO for various document elements.
- It includes information on borders, document properties, drawing objects, fields, footnotes, form fields, headers/footers, hyperlinks, images, lists, and more.
- It specifies whether each feature is fully supported, partially supported, or not supported, along with any additional notes.

## Content

### Document Rendering and Export Properties

The following table outlines the supported features and their levels of support:

| Feature    | Property                            | Supported | Notes                                                                                     |
|------------|-------------------------------------|-----------|---------------------------------------------------------------------------------------------|
| **Border** | Color                               | Yes       | -                                                                                           |
|            | Distance from text                  | Yes       | -                                                                                           |
|            | Line style                          | Partial    | Some line styles are rendered as solid.                                                      |
|            | Line width                          | Yes       | -                                                                                           |
| **Document Properties**                        | N/A        | Yes       | -                                                                                           |
| **Drawing objects** | Shapes                    | Partial    | Images and horizontal rules are exported.                                                 |
|            | Text                                | Partial    | Text from text boxes and other shapes is rendered in the main text.<br>                              |
|            | Images                              | -         | -                                                                                           |
| **Field** | N/A                                 | Yes       | Current field result is output, but the result is not recalculated.                           |
| **Footnotes and Endnotes**                     | N/A        | Yes       | -                                                                                           |
| **Form Field** | Text input                       | Yes       | -                                                                                           |
| **Header / Footer** | Different per section       | Partial    | Only primary header is output at the beginning of a section.                                |
| **Hyperlink** | External URL                      | Yes       | -                                                                                           |
|            | Local                               | Yes       | -                                                                                           |
| **Image** | Cropping                            | Yes       | -                                                                                           |
|            | Inline                              | Yes       | -                                                                                           |
|            | Scale                               | Yes       | -                                                                                           |
| **List**  | Custom bullets                      | Yes       | -                                                                                           |
|            | Multi-level                         | Yes       | -                                                                                           |
|            | Numbered                            | Yes       | -                                                                                           |

## API Reference

### Supported Features and their Export Behavior
The table above provides detailed information about the behavior of different features when rendering documents using Syncfusion DocIO. Notable points include:
- **Partial Support:** Features like line styles, shapes, and headers/footers have partial support with specific notes about their behavior.
- **Full Support:** Features such as borders, footnotes, hyperlinks, and lists are fully supported.
- **No Support:** Images within drawing objects are not currently exported.

## Code Examples

### Example: Exporting a Document with Custom Borders
```csharp
using Syncfusion.DocIO;
using Syncfusion.DocIO.DLS;

// Create a new document
WordDocument document = new WordDocument();

// Add a section
IWSection section = document.AddSection();

// Add a paragraph
IW Paragraph paragraph = section.AddParagraph();
paragraph.AppendText("Sample text with custom border.");

// Add a border
IWBorder border = paragraph.Format.Borders[KnownBorders.Box];
border.LineStyle = KnownLines.Single; // Example line style
border.Color = KnownColors.Blue; // Example color
border.Width = 1.5f; // Example width

// Save the document
document.Save("Output.docx", FormatType.Docx);
```

### Example: Managing Footnotes and Endnotes
```csharp
using Syncfusion.DocIO;
using Syncfusion.DocIO.DLS;

// Create a new document
WordDocument document = new WordDocument();

// Add a section
IWSection section = document.AddSection();

// Add a paragraph with a footnote
IW Paragraph paragraph1 = section.AddParagraph();
paragraph1.AppendText("This is a paragraph ");
paragraph1.AppendFootnote("Sample footnote text.", 1); // Add footnote

// Add another paragraph with an endnote
IW Paragraph paragraph2 = section.AddParagraph();
paragraph2.AppendText("This is another paragraph ");
paragraph2.AppendEndnote("Sample endnote text.", 1); // Add endnote

// Save the document
document.Save("Output.docx", FormatType.Docx);
```

## Cross References

- Refer to the **Hyperlink Management** section in [DocIO Hyperlink Handling Guide](#hyperlink-management) for more details on how hyperlinks are processed during export.
- The **Image Scaling and Cropping** guidelines are detailed in [DocIO Image Handling](#image-scaling-and-cropping).

<!-- tags: DocIO, document rendering, document export, borders, document properties, drawing objects, fields, footnotes, form fields, headers, footers, hyperlinks, images, lists, partial support, full support, Syncfusion Winforms, version: 11.4.0.26 keywords: borders, document properties, drawing objects, fields, footnotes, form fields, headers, footers, hyperlinks, images, lists, partial support, full support, document export, DocIO -->
```