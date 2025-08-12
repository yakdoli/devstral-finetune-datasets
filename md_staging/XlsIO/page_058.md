```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_058.jpeg
document_name: XlsIO
page_number: 058
page_id: XlsIO#page_058
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:51:29Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- This page illustrates the use of the `SaveAsActionResult` method from the Essential XlsIO library to save and download Excel files in various formats.

## Content

### Step 3: Controller

Add the following code in the Controller's action result:

#### Code Example: SaveAsActionResult Implementation

```csharp
public static ExcelResult SaveAsActionResult(this ExcelEngine engine, this IWorkbook _workbook, string filename, ExcelHttpContentType contentType)
{
    ExcelSaveType saveType, HttpResponse response, ExcelDownloadType downloadType;
    return new ExcelResult(_engine, _workbook, filename, response, DownloadType, contentType);
}
```

#### Code Example: Controller Action Method

```csharp
public ActionResult createsheet()
{
    return View();
}

[AcceptVerbs(HttpVerbs.Post)]
public ActionResult createsheet(string SaveOption, string Browser)
{
    // Step 1: Instantiate the spreadsheet creation engine.
    ExcelEngine excelEngine = new ExcelEngine();

    // Step 2: Instantiate the excel application object.
    IApplication application = excelEngine.Excel;

    // Creating new workbook
    IWorkbook workbook = application.Workbooks.Create(3);
    IWorksheet sheet = workbook.Worksheets[0];
    sheet.Range["A1:A5"].Text = "HelloWorld";

    return excelEngine.SaveAsActionResult(workbook, "Sample.xls", HttpContext.ApplicationInstance.Response,
        ExcelDownloadType.Open, ExcelHttpContentType.Excel97);
}
```

### Step 4: Run the Application

## API Reference

- **Namespace**: The implementation includes methods such as `SaveAsActionResult` to handle file saving and downloading.
- **Parameters**:
  - `engine`: The ExcelEngine instance.
  - `_workbook`: The workbook object to be saved.
  - `filename`: The name of the file to be saved.
  - `contentType`: The content type of the file for download, such as Excel97.
  - `DownloadType`: Specifies the behavior of the download, e.g., Open.

## Code Examples

- The provided code examples demonstrate how to create a new workbook, populate data, and return the file for download using the `SaveAsActionResult` method.

## Page-level Navigation/TOC (if applicable)

- **Introduction**
- **Step 3: Controller**
  - Code Example: SaveAsActionResult Implementation
  - Code Example: Controller Action Method
- **Step 4: Run the Application**

## Cross References

- This page specifically focuses on the `SaveAsActionResult` method and its usage within the Controller context to manage Excel file downloads in applications.

<!-- tags: [XlsIO, Essential XlsIO, Syncfusion Winforms, Action Result] keywords: [SaveAsActionResult, ExcelEngine, IWorkbook, HttpResponse, ExcelDownloadType, ExcelHttpContentType, Workbook Creation, File Download] -->
```