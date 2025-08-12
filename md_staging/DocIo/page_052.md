<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_052.jpeg
document_name: DocIo
page_number: 052
page_id: DocIo#page_052
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:31:18Z
fidelity: lossless
-->

# Essential DocIO

Essential DocIO is a Non-UI component that is used in Web applications. To use DocIO in an ASP.NET application, you must stream the created document to the client browser.

## Overview
- Demonstrates how to stream a document to the browser in an ASP.NET application.
- Illustrates saving a document to the disk in a Silverlight application.

## Content

### Streaming the Document to the Browser in ASP.NET

The following code example illustrates how to stream the document to the browser.

```csharp
[C#]

// Streaming the document to the Browser.
doc.Save("Sample.doc", FormatType.Doc, Response,
HttpContentDisposition.InBrowser);

// Streaming the document to the Browser.
doc.Save("Sample.docx", FormatType.Docx, Response,
HttpContentDisposition.InBrowser);
```

```vb.net
[VB.NET]

' Streaming the document to the Browser.
doc.Save("Sample.doc", FormatType.Doc, Response,
HttpContentDisposition.InBrowser)

' For .docx format
doc.Save("Sample.docx", FormatType.Docx, Response,
HttpContentDisposition.InBrowser)
```

### Saving the Word document in Silverlight Application

To use DocIO in a Silverlight application, you must save the created document to the disk. The following code example illustrates how to do this.

```csharp
[C#]

SaveFileDialog sfd = new SaveFileDialog()
{
    DefaultExt = "doc",
    FilterIndex = 1
};
if (sfd.ShowDialog() == true)
{
    using (Stream stream = sfd.OpenFile())
    {
        document.Save(stream, FormatType.Doc);
    }
}
```

## API Reference

### Methods
- `Save(string fileName, FormatType formatType, HttpResponseBase response, HttpContentDisposition disposition)`: Streams the document to the browser.
- `Save(Stream stream, FormatType formatType)`: Saves the document to the disk.

## Code Examples

The code examples provided show how to stream a document to the browser in C# and VB.NET and how to save a document to the disk in a Silverlight application.

## Cross References

See also:
- [Essential DocIO Documentation](#)

<!-- tags: [DocIO, ASP.NET, Silverlight, stream, save, document] keywords: [Essential DocIO, ASP.NET, Silverlight, streaming, saving, document, format] -->