```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_366.jpeg
document_name: pdf
page_number: 366
page_id: pdf#page_366
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:47:31Z
fidelity: lossless
-->

## Essential PDF

Essential PDF provides support for reading and writing PDF documents from / to the System.IO.Stream. You can store a PDF document stream as a binary object in the database. The following code example illustrates this.

### C#

```csharp
// Store the PDF document in Database.
// Initialize a stream.
MemoryStream stream = new MemoryStream();

// Save the document to stream.
doc.Save(stream);

// Retrieve and display the stream in PDF format.
OleDbDataReader Reader = command.ExecuteReader();
byte[] PdfFile = (byte[])Reader[1];
Stream strm = new MemoryStream(PdfFile);
using (FileStream fstream = new FileStream("sample.pdf",
FileMode.OpenOrCreate, FileAccess.ReadWrite))
{
    fstream.Write(PdfFile, 0, PdfFile.Length);
}
```

### VB.NET

```vbnet
' Store the PDF document in Database.
' Initialize a stream.
Dim stream As MemoryStream = New MemoryStream()

' Save the document to stream.
doc.Save(stream)

' Retrieve and display the stream in PDF format.
Dim Reader As OleDbDataReader = Command.ExecuteReader()
Dim PdfFile As Byte() = CType(Reader(1), Byte())
Dim strm As Stream = New MemoryStream(PdfFile)
Using fstream As FileStream = New FileStream("sample.pdf",
FileMode.OpenOrCreate, FileAccess.ReadWrite)
    fstream.Write(PdfFile, 0, PdfFile.Length)
End Using
```

### 5.2.5 How To Enable and Disable PDF Layers In a PDF document?

### Overview
- Demonstrates storing and retrieving PDF documents as binary data in a database.
- Includes code examples in both C# and VB.NET for managing PDF streams.
- Explains how to save and load PDF files to and from memory streams.

### Content

#### Stream Handling and Database Operations
- The code illustrates how to:
  - Create a `MemoryStream` to hold the PDF document.
  - Save the PDF document to the stream using the `Save` method.
  - Retrieve the PDF document from a database as a byte array.
  - Convert the byte array back into a memory stream to display or save as a PDF file.

#### C# Example Breakdown
1. Initializes a `MemoryStream` object.
2. Saves the PDF document to the `MemoryStream` using the `Save` method.
3. Retrieves the document from the database using `OleDbDataReader`.
4. Converts the byte array retrieved from the database into a `MemoryStream`.
5. Writes the streamed content to a file using `FileStream`.

#### VB.NET Example Breakdown
1. Similar to the C# example, initializes a `MemoryStream`.
2. Saves the document to the stream.
3. Uses `OleDbDataReader` to read the PDF data as a byte array from the database.
4. Creates a `MemoryStream` from the byte array.
5. Writes the data to a file using `FileStream`.

#### Conclusion
This section provides a practical example of integrating PDF document handling with database operations, demonstrating the flexibility and utility of Essential PDF in Windows Forms applications.

## API Reference (if applicable)

## Code Examples (multi-language supported)

## Page-level Navigation/TOC (if applicable)

## Cross References

## RAG Annotations
```html
<!-- tags: [Essential PDF, System.IO.Stream, MemoryStream, OleDbDataReader, FileStream, document stream, database, C#, VB.NET] keywords: [PDF stream, database storage, document handling, memory stream, file stream, stream operations, document management] -->
```
```