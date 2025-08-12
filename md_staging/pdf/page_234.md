```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_234.jpeg
document_name: pdf
page_number: 234
page_id: pdf#page_234
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:39:00Z
fidelity: lossless
-->

### Overview
- Demonstrates how to save a document to a memory stream and then write it to a file.
- Explains the steps for closing streams properly after saving.
- References asynchronous processing for Windows Store apps.
- Introduces security settings for securing PDF documents.

## Content

### Memory Stream and File Stream Operations

#### C#

```csharp
// Create a Memory Stream.
System.IO.MemoryStream memStream = new MemoryStream();

// Save the Stream to memory.
document.Save(memStream);
memStream.Seek(0, SeekOrigin.Begin);

// Create a file Stream
System.IO.FileStream fs = new FileStream("Sample.pdf", FileMode.Create);
memStream.WriteTo(fs);

// Close the Streams.
memStream.Close();
fs.Close();
```

#### VB.NET

```vb
' Create a Memory Stream.
Dim memStream As MemoryStream = New MemoryStream()

' Save the Stream to memory.
document.Save(memStream, FormatType.Doc)
memStream.Seek(0, SeekOrigin.Begin)

' Create a file Stream
Dim fs As FileStream = New FileStream("Sample.doc", FileMode.Create)
memStream.WriteTo(fs)

' Close the Streams.
memStream.Close()
fs.Close()
```

#### Note: To open or save the document asynchronously for Windows Store apps, refer to the *Asynchronous Support* section.

### 4.1.7.6 Security Settings

Adobe provides options for securing a PDF document from unauthorized access, and for restricting the access for some user. This section demonstrates various options provided by Essential PDF to secure a PDF document.

## Code Examples

### C#
The examples above demonstrate how to save documents into a memory stream and then write them to files, as well as how to properly close the streams after saving.

### VB.NET
The examples above also provide the equivalent VB.NET code for saving documents into a memory stream and then writing them to files, along with the proper closing of streams after saving.

## Page-level Navigation/TOC (if applicable)
- [unclear]

## Cross References
- See also: *Asynchronous Support* section.

## RAG Annotations
<!-- tags: [PDF, Security, MemoryStream, FileStream, WindowsStoreApps, SyncfusionWinforms, version: 11.4.0.26] keywords: [memory stream, file stream, asynchronous, security settings, document saving, unauthorized access, restriction, access control, Secure PDF document] -->
```