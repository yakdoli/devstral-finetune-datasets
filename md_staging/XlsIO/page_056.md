```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_056.jpeg
document_name: XlsIO
page_number: 056
page_id: XlsIO#page_056
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:52:05Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- This page describes a specialized class `ExcelResult` designed for handling Excel file download functionalities.
- The class extends `ActionResult` and integrates seamlessly with web applications for generating and downloading Excel files.
- Key features include setting filenames, workbook sources, download types, HTTP content types, separators, and managing HTTP responses.

## Content

### ExcelResult Class
The `ExcelResult` class is designed to manage the download of Excel files within an ASP.NET MVC environment. It provides properties to configure the download behavior, including file names, source workbooks, HTTP responses, download types, content types, and separators.

```csharp
[C#]

public class ExcelResult : ActionResult
{
    private IWorkbook m_source;
    private string m_filename;
    private HttpResponse m_response;
    private ExcelDownloadType m_downloadType;
    private ExcelHttpContentType m_contentType;
    private string m_separator;

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

    public IWorkbook Source
    {
        get
        {
            return m_source as IWorkbook;
        }
    }

    public HttpResponse Response
    {
        get
        {
            return m_response;
        }
    }

    public ExcelDownloadType DownloadType
    {
        set
        {
            m_downloadType = value;
        }
        get
        {
            return m_downloadType;
        }
    }
}
```

### Properties
- **FileName**: Gets or sets the name of the file that will be downloaded.
- **Source**: Gets the Excel workbook (IWorkbook) that is being downloaded.
- **Response**: Gets the HTTP response object used to send the Excel file to the client.
- **DownloadType**: Gets or sets the type of download for the Excel file. This can include options like immediate download, background save, or client-side processing.

### Usage
The `ExcelResult` class is typically used in combination with `ActionResults` in ASP.NET MVC controllers to dynamically generate Excel files and trigger downloads. Developers can configure various aspects of the download, such as file name, content type, and separator, based on the requirements of their application.

## API Reference

### Namespaces and Types
- **Namespace**: The class belongs to a Syncfusion XlsIO namespace (not explicitly shown in the image but can be inferred from the context).
- **Interfaces**: Implements `ActionResult` to integrate with ASP.NET MVC's action result mechanism.
- **Enums**:
  - `ExcelDownloadType`: Defines the type of download operation (e.g., Immediate, Background Save).
  - `ExcelHttpContentType`: Defines the HTTP content type for download (e.g., XLSX, CSV).

### Properties
- **FileName**: Type: `string`
- **Source**: Type: `IWorkbook`
- **Response**: Type: `HttpResponse`
- **DownloadType**: Type: `ExcelDownloadType`
- **ContentType**: Type: `ExcelHttpContentType`
- **Separator**: Type: `string`

### Methods
The class does not explicitly define any methods in the provided code segment. However, it inherits methods from `ActionResult` for executing the result.

## Code Examples

### Example: Generating an Excel File and Triggering a Download
```csharp
public ActionResult DownloadExcel()
{
    // Create a new workbook and populate it with data
    using (var workbook = new Workbook())
    {
        var excelResult = new ExcelResult
        {
            Source = workbook,
            FileName = "Report.xlsx",
            DownloadType = ExcelDownloadType.Immediate,
            ContentType = ExcelHttpContentType.XLSX
        };

        return excelResult;
    }
}
```

### Example: Using a CSV Separator
```csharp
public ActionResult DownloadCSV()
{
    // Create a new CSV file with a specific separator
    using (var workbook = new Workbook())
    {
        var excelResult = new ExcelResult
        {
            Source = workbook,
            FileName = "Report.csv",
            DownloadType = ExcelDownloadType.Immediate,
            ContentType = ExcelHttpContentType.CSV,
            Separator = ","
        };

        return excelResult;
    }
}
```

## Cross References
- For more details on handling different Excel formats and content types, refer to the "Excel Formats and Types" section.
- To understand how downloading functionality integrates with ASP.NET MVC, see the "ASP.NET MVC Integration" section.

<!-- tags: [XlsIO, Excel download, ActionResult, Syncfusion, WinForms] keywords: [ExcelResult, IWorkbook, HttpResponse, ExcelDownloadType, ExcelHttpContentType, FileName, Source, Response, DownloadType, ContentType, Separator] -->
```