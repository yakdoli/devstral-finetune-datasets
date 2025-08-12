```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_048.jpeg
document_name: DocIo
page_number: 048
page_id: DocIo#page_048
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:31:04Z
fidelity: lossless
-->

```csharp
set
{
    m_formatType = value;
}
}
public HttpContentDisposition ContentDisposition
{
    get
    {
        return m_contentDisposition;
    }
    set
    {
        m_contentDisposition = value;
    }
}
public HttpResponse Response
{
    get
    {
        return m_response;
    }
}

public DocResult(IWordDocument document, string filename, FormatType formatType, HttpResponse response, HttpContentDisposition contentDisposition)
{
    FileName = filename;
    m_document = document;
    this.formatType = formatType;
    m_response = response;
    this.ContentDisposition = contentDisposition;
}
public override void ExecuteResult(ControllerContext context)
{
    if (context == null)
        throw new ArgumentNullException("Context");
    this.Document.Save(FileName, formatType, Response, ContentDisposition);
}
}
```

## Overview
- Every action result must inherit from the base ActionResult class.
- The base ActionResult class has one method that you must implement: the `ExecuteResult` method.
- The `ExecuteResult` method is called to generate the content created by the action result.
- This method streams the output Word document file to the browser.

## Code Examples
The provided code demonstrates how to create a custom `DocResult` class that inherits from the base `ActionResult` class. The `ExecuteResult` method is implemented to save a Word document to the browser using the provided parameters such as filename, document format type, HttpResponse, and HttpContentDisposition.

## API Reference
### Class: DocResult
#### Properties
- `ContentDisposition`: Returns or sets the content disposition for the response.
- `Response`: Returns or sets the HttpResponse object.
- `FileName`: Property to store the file name of the document.
- `Document`: Property to store the IWordDocument object.

#### Methods
- `ExecuteResult(ControllerContext context)`: Overrides the base method to generate the content and stream the Word document file to the browser.

## RAG Annotations
<!-- tags: [actionresult, docresult, executeresult, worddocument, httpresponse, httpcontentdisposition] keywords: [ActionResult, DocResult, ExecuteResult, IWordDocument, HttpResponse, HttpContentDisposition, streaming, output Word document, browser, controllercontext] -->
```