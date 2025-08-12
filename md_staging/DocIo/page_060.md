<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_060.jpeg
document_name: DocIo
page_number: 060
page_id: DocIo#page_060
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:31:44Z
fidelity: lossless
-->

## Opening and Saving Documents

### Overview
- Describes various methods to open and save documents with different format types and security requirements.
- Details synchronous and asynchronous methods for document operations.

### Content

#### Synchronous Open Methods
- **Open(Stream stream, FormatType formatType)**: opens the document from the stream which has the specified format type.
- **Open(Stream stream, FormatType formatType, string password)**: opens the encrypted document from the stream that has the specified format type and the password.
- **Open(Stream stream, FormatType formatType, XHTMLValidationType validationType)**: opens the document from the stream that has the specified format type and XHTMLValidationType. Ignores validation type if the input document is not XHTML.
- **Open(Stream stream, FormatType formatType, XHTMLValidationType validationType, string baseUrl)**: opens the document from the stream that has the specified format type, XHTMLValidationType, and the baseUrl of the input document. Ignores validation type and baseUrl if the input document is not HTML.

#### Asynchronous Open Methods Specific to Windows Store Applications
- **OpenAsync(StorageFile file)**: opens the document asynchronously from the storage file.
- **OpenAsync(StorageFile file, FormatType formatType)**: opens the document asynchronously from the storage file that has the specified format type.
- **OpenAsync(Stream stream, FormatType formatType)**: opens the document asynchronously from the stream that has the specified format type.
- **OpenAsync(StorageFile file, FormatType formatType, string password)**: opens the document asynchronously from the storage file that has the specified format type and the password.
- **OpenAsync(Stream stream, FormatType formatType, string password)**: opens the document asynchronously from the stream that has the specified format type and the password.

#### Saving Documents
To save a document back to the Word document format, use the `Save` method. There are several overloads for this method.

- **Save(string fileName)**: saves to file in Microsoft Word format.
- **Save(string fileName, FormatType formatType)**: saves the document to file in .xml or Microsoft Word format.
- **Save(Stream stream, FormatType formatType)**: saves the document into stream in .xml or Microsoft Word format.
- **Save(string fileName, FormatType formatType, HttpResponse response, HttpContentDisposition contentDisposition)**: saves the document into the client browser.

#### Asynchronous Save Methods Specific to Windows Store Applications
- **SaveAsync(StorageFile file, FormatType formatType)**: saves the document asynchronously into the storage file in the specified format type.

### API Reference

#### Open Methods
- **Parameters**:
  - `Stream stream`: The input stream containing the document.
  - `FormatType formatType`: The format type of the document (e.g., Word, XML).
  - `string password`: (Optional) The password for encrypted documents.
  - `XHTMLValidationType validationType`: (Optional) The validation type for XHTML documents.
  - `string baseUrl`: (Optional) The base URL for resolving relative links in HTML documents.

#### Save Methods
- **Parameters**:
  - `string fileName`: The file path to save the document.
  - `FormatType formatType`: The format type of the document (e.g., Word, XML).
  - `HttpResponse response`: (Optional) The HTTP response object for saving to a client browser.
  - `HttpContentDisposition contentDisposition`: (Optional) The content disposition for the HTTP response.

### Code Examples
```csharp
// Opening a document
Stream documentStream = File.OpenRead("example.docx");
Document document = new Document();
document.Open(documentStream, FormatType.Word, "encryptedPassword");

// Saving a document
document.Save("output.docx", FormatType.Word);

// Asynchronous operations (Windows Store)
StorageFile file = await StorageFile.GetFileFromPathAsync("example.docx");
await document.OpenAsync(file, FormatType.Word);
await document.SaveAsync(file, FormatType.Word);
```

## Page-level Navigation/TOC
- **Synchronous Open Methods**
- **Asynchronous Open Methods Specific to Windows Store Applications**
- **Saving Documents**
- **Asynchronous Save Methods Specific to Windows Store Applications**
- **API Reference**
- **Code Examples**

## Cross References
- See also: [DocIo Documentation](https://help.syncfusion.com/dotnetoffice/docio)

<!-- tags: [syncfusion, docio, winforms, document, open, save, async, encryption, html, windows store] keywords: [DocIo, openstream, save, asynchronous, formattype, xhtmlvalidationtype, encryption, password, url, document stream, document format, windows store, httpresponse, httpcontentdisposition, storagefile, asynchronous save, document operations] -->