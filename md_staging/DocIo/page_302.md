```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_302.jpeg
document_name: DocIo
page_number: 302
page_id: DocIo#page_302
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:47:05Z
fidelity: lossless
-->

# Essential DocIO

## Overview

- Demonstrates how to embed font files in an EPub document for consistent formatting.
- Includes C# and VB.NET code examples to save a Word document as an EPub file with embedded fonts.
- Provides a sample output image of the EPub document for reference.

## Content

### Code Examples

#### C#

```csharp
// Load any .doc or .docx file
WordDocument document = new WordDocument(filename);

// Turn on embedding font files
document.SaveOptions.EPubExportFont = true;

// Save the EPub file
document.Save("Sample.epub", FormatType.EPub);
```

#### VB.NET

```vb
' Load any .doc or .docx file
Dim document As WordDocument = New WordDocument(filename)

' Turn on embedding font files
document.SaveOptions.EPubExportFont = True

' Save the EPub file
document.Save("Sample.epub", FormatType.EPub)
```

#### Sample Output EPub

The following is the sample image of output EPub document when converted using the above code.

---

## API Reference

### Methods

- **load(filename)**:
  - **Parameters**:
    - `filename`: String - The path to the .doc or .docx file to load.
  - **Returns**: `WordDocument` - An object representing the loaded document.

- **save(filename, formatType)**:
  - **Parameters**:
    - `filename`: String - The path to save the EPub file.
    - `formatType`: FormatType - The format type, in this case, `EPub`.
  - **Returns**: Void - Saves the document in the specified format.

- **SaveOptions**:
  - Property `EpubExportFont`:
    - **Description**: A boolean property that determines whether font files should be embedded in the EPub file.
    - **Default**: `false`
    - **Required**: Yes

---

## Code Examples (Repeated)

### C#

```csharp
// Load any .doc or .docx file
WordDocument document = new WordDocument(filename);

// Turn on embedding font files
document.SaveOptions.EPubExportFont = true;

// Save the EPub file
document.Save("Sample.epub", FormatType.EPub);
```

### VB.NET

```vb
' Load any .doc or .docx file
Dim document As WordDocument = New WordDocument(filename)

' Turn on embedding font files
document.SaveOptions.EPubExportFont = True

' Save the EPub file
document.Save("Sample.epub", FormatType.EPub)
```

---

## Page-level Navigation/TOC

- [Introduction to DocIO]
- [Working with EPub Files]
  - Embedding Fonts in EPub Files

---

## Cross References

- See also: [DocIO Features Overview]
- See also: [EPub Conversion Guidelines]

---

<!-- tags: [DocIO, EPub, WordDocument, font embedding, WinForms] keywords: [DocIO, EPub, font, embedding, export, SaveOptions, WordDocument] -->
```