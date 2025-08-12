<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_065.jpeg
document_name: DocIo
page_number: 065
page_id: DocIo#page_065
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:32:34Z
fidelity: lossless
-->

# Essential DocIO

```vb
Dim sourceDoc As WordDocument = New WordDocument()
sourceDoc.Open("SourceDocument.doc", FormatType.Doc)

'Create a new word document with one section and one paragraph
Dim doc As WordDocument = New WordDocument()
doc.EnsureMinimal()

'Clone the content of source document to the newly created document
doc = sourceDoc.Clone()

'Save the document as xml
doc.Save("Document.doc", FormatType.Doc)
```

The following code illustrates how to use the **Open** and **Save Async** methods in Windows Store applications.

```csharp
[C#]

//Open the Word document from the memory stream.
WordDocument doc = new WordDocument();
doc.OpenAsync(memoryStream, FormatType.Doc);

//Open the Word document from the storage file.
WordDocument doc = new WordDocument();
doc.OpenAsync(storageFile, FormatType.Doc);

//Save the document in the memory stream.
doc.SaveAsync(memoryStream, FormatType.Doc);

//Save the document in the storage file.
doc.SaveAsync(storageFile, FormatType.Doc);
```

```vb
[VB.NET]

'Open the Word document from the memory stream.
Dim doc As WordDocument = New WordDocument()
sourceDoc.OpenAsync(memoryStream, FormatType.Doc);

'Open the Word document from a storage file.
Dim doc As WordDocument = New WordDocument()
sourceDoc.OpenAsync(storageFile, FormatType.Doc)

'Save the document in a memory stream.
doc.SaveAsync(memoryStream, FormatType.Doc)
```

## Cross References
- See also: [DocIO Documentation](#docio-documentation)

## RAG Annotations
<!-- tags: [DocIo, WordDocument, OpenAsync, SaveAsync, WindowsStore, Streaming, StorageFile, MemoryStream] keywords: [WordDocument, OpenAsync, SaveAsync, C#, VB.NET, WindowsStore, Streaming, StorageFile, MemoryStream, DocIO] -->