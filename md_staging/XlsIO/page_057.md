```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_057.jpeg
document_name: XlsIO
page_number: 057
page_id: XlsIO#page_057
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:52:11Z
fidelity: lossless
-->

```csharp
}
public ExcelHttpContentType ContentType
{
    set
    {
        m_contentType = value;
    }
    get
    {
        return m_contentType;
    }
}

public ExcelResult(IWorkbook source, string fileName, HttpResponse response, ExcelDownloadType downloadType, ExcelHttpContentType contentType)
{
    this.FileName = fileName;
    this.m_source = source;
    m_response = response;
    DownloadType = downloadType;
    ContentType = contentType;
}

public override void ExecuteResult(ControllerContext context)
{
    if (context == null)
        throw new ArgumentNullException("Context");
    this.m_source.SaveAs(FileName, Response, DownloadType, ContentType);
}
```

Every action result must inherit the base `ActionResult` class. The base `ActionResult` class has one method that you must implement: the `ExecuteResult` method. The `ExecuteResult` method is called to generate the content, created by the action result. This method streams the output Excel file to the browser.

A controller action cannot return an action result directly. For example, if you want to return a view from a controller action, you don't return an object of type `ViewResult`; instead, you call the `View` method. The `View` method instantiates a new object of type `ViewResult` and returns it to the browser.

An extension method named `SaveAsActionResult` has to be created to add the `Controller` class. The `SaveAsActionResult` method returns an object of type, `ExcelResult`.

```html
<!-- tags: [XlsIO, action result, controller context, ExcelResult, controller class, extension method] keywords: [content type, download type, http response, action result, controller context, excel file, streaming, controller class, extension method, saveas, execute result] -->
```