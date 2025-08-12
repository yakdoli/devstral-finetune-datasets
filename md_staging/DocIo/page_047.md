```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_047.jpeg
document_name: DocIo
page_number: 047
page_id: DocIo#page_047
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:30:58Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- In an MVC application, a controller action returns an action result derived from the base `ActionResult` class.
- Demonstrates how to create a custom action result for non-standard content types like images, PDFs, or Excel documents.

## Content

In an MVC application, a controller action returns an action result. Specifically, it returns an action that derives from the base `ActionResult` class.

However, if you want to return content such as images, PDF files, or Microsoft Excel documents to a browser, you need to create your own action result. The following code example illustrates how to create a custom action result.

```csharp
[C#]

public class DocResult : ActionResult
{
    private string m_filename;
    private IWordDocument m_document;
    private FormatType m_formatType;
    private HttpResponse m_response;
    private HttpContentDisposition m_contentDisposition;

    public string FileName
    {
        get
        {
            return m_filename;
        }
        set
        {
            m_filename = value;
        }
    }

    public IWordDocument Document
    {
        get
        {
            if (m_document != null)
                return m_document;
            return null;
        }
    }

    public FormatType formatType
    {
        get
        {
            return m_formatType;
        }
    }
}
```

## Code Examples

### Custom ActionResult for Document Output

The provided `DocResult` class is an example of creating a custom `ActionResult` that can handle document outputs like Word documents. This class includes properties for the filename, document content, format, response, and content disposition.

### Usage Example

You can use this custom action result in your controller methods to return documents to the browser. For instance:

```csharp
public ActionResult DownloadDocument()
{
    // Create and fill the document content as needed
    var document = new WordDocument();
    document.Add("Hello, world!");

    var result = new DocResult
    {
        FileName = "Document.docx",
        Document = document,
        formatType = FormatType.Docx
    };

    return result;
}
```

This custom action result ensures that the document is properly formatted and displayed in the browser based on the specified format and disposition.

### Tags and Keywords

- **Keywords:** DocIO, MVC, custom action result, ActionResult, IWordDocument, HttpContentDisposition, FormatType
- **Tags:** DocIO, syncfusion, winforms, mvc, document_output, custom_action_result
```