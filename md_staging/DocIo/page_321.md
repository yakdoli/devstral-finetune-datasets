```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_321.jpeg
document_name: DocIo
page_number: 321
page_id: DocIo#page_321
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:49:40Z
fidelity: lossless
-->

## Overview

- This page explains how to open a document from a stream using the DocIO library.
- It demonstrates the retrieval of a document using .NET classes and provides an example code snippet.
- The example shows how to handle streams, memory operations, and document manipulation for saving the document.

## Content

### 5.7 How to open a Document from Stream by using DocIO?

DocIO provides support for opening documents from a stream. You can retrieve the document by using .NET classes, and then pass the stream to DocIO as follows.

```csharp
[C#]

HttpWebRequest request = 
    (HttpWebRequest)WebRequest.Create("http://www.nfpa.org/assets/files//PDF/Form" +
                                     "s/EvacuationGuide.doc");
HttpWebResponse response = (HttpWebResponse)request.GetResponse();
Stream stream = response.GetResponseStream();
byte[] buffer = ReadFully(stream, 32768);

// Store bytes into the memory stream
MemoryStream ms = new MemoryStream();
ms.Write(buffer, 0, buffer.Length);
ms.Seek(0, SeekOrigin.Begin);
stream.Close();

// Creating a new document.
WordDocument doc = new WordDocument();

// Open the template document from the MemoryStream.
doc.Open(ms, FormatType.Doc);
doc.Save("Sample.doc", FormatType.Doc, Response,
         HttpContentDisposition.InBrowser);

public static byte[] ReadFully(Stream stream, int initialLength)
{
    // If we've been passed an unhelpful initial length, just
    // use 32K.
    if (initialLength < 1)
    {
        initialLength = 32768;
    }
    byte[] buffer = new byte[initialLength];
    int read = 0;
    int chunk;
    while ((chunk = stream.Read(buffer, read, buffer.Length - read)) > 0)
    {
        read += chunk;
        // If we've reached the end of our buffer, check to see if there's
    }
}
```

## Code Examples

The provided code snippet demonstrates the process of:

1. Creating an HTTP request to fetch a document from a URL.
2. Reading the document into a byte array using a custom `ReadFully` method.
3. Storing the bytes in a `MemoryStream`.
4. Opening a new WordDocument from the `MemoryStream`.
5. Saving the document back to a specified format for display or download.

## RAG Annotations

<!-- tags: [DocIO, WinForms, document manipulation, document streams, Syncfusion] keywords: [open document from stream, HttpWebRequest, Memory Stream, WordDocument, FormatType, HttpContentDisposition] -->
```