```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_087.jpeg
document_name: DocIo
page_number: 087
page_id: DocIo#page_087
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:33:24Z
fidelity: lossless
-->

# Essential DocIO

Essential DocIO can be used to read and write Microsoft Word documents of Word 97-2003, Word 2007, and Word 2010 format. It is compatible with both 32 and 64-bit machines and has no external dependencies.

## Application

Essential DocIO provides a rich set of APIs to create and manipulate the word document and its elements. Word 2010 format documents can be created using the same APIs that were used for Word 97-2003 and Word 2007 format documents, except the format type.

To open/save the word 2010 format document, you have to specify the format type as "Automatic" or "Word2010".

## 4.2.4 Stream Support

Essential DocIO provides support to open or save the created Word document into the **Memory Stream** and **File Stream**. Using this, you can open or save the document in the database or make changes to the document without saving to disk.

### C#

```csharp
// Create a Memory Stream.
MemoryStream memStream = new MemoryStream();

// Save the document into memory stream.
document.Save(memStream);

// Move the pointer to the first position
memStream.Seek(0, SeekOrigin.Begin);

// Create a file Stream
FileStream fs = new FileStream("Sample.doc", FileMode.Create);
memStream.WriteTo(fs);

// Open the Word document from stream
WordDocument sourceDoc = new WordDocument(memStream, FormatType.Doc);

// Close the Streams.
memStream.Close();
fs.Close();
```

## API Reference (if applicable)
- [Namespace] `Syncfusion.DocIO`
- [Class] `WordDocument`
  - [Method] `Save(Stream)`
  - [Method] `Seek(Int64, SeekOrigin)`
  - [Method] `WriteTo(Stream)`
  - [Enum] `FormatType` (e.g., `Doc`, `Docx`, `Dot`, `Dotx`)

## Code Examples (multi-language supported)
The example above demonstrates how to:
1. Create a `MemoryStream` and save a Word document into it.
2. Create a `FileStream` to save the document to a file.
3. Open the document from the `MemoryStream`.

## Page-level Navigation/TOC (if applicable)
- [Section] Application
- [Section] Stream Support

## Cross References
- See also:
  - [API Documentation for DocIO](#)
  - [Handling Word Documents](#)

<!-- tags: essentialdocio, worddocument, memorystream, filestream, csharp, api, stream, synchronization, readingwriting, version11.4.0.26 -->
```
