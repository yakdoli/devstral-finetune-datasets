```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_338.jpeg
document_name: pdf
page_number: 338
page_id: pdf#page_338
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:45:47Z
fidelity: lossless
-->

# Handling PDF Files

## Overview
- Provides details about asynchronous PDF operations, including importing pages.
- Lists supported and unsupported Excel elements for various development frameworks.
- Highlights features like text handling, graphics, and pagination supported by Essential PDF.

## Content

### Asynchronous PDF Operations

| Method             | Description                                     | Signature                                                                 | Return Type           |
|--------------------|-------------------------------------------------|---------------------------------------------------------------------------|-----------------------|
| ImportPageAsync    | Imports a page in asynchronous mode.          | `async Task<PdfPageBase> ImportPageAsync(PdfLoadedDocument idDoc, int pageIndex)`                                   | `PdfPageBase`        |
|                    |                                                 | `async Task<PdfPageBase> ImportPageAsync(PdfLoadedDocument idDoc, PdfPageBase page)`                                | `PdfPageBase`        |
| ImportPageRangeAsync | Imports page range in asynchronous mode.   | `async Task<PdfPageBase> ImportPageRangeAsync(PdfLoadedDocument idDoc, int startIndex, int endIndex)`              | `PdfPageBase`        |
| AppendAsync        | Appends documents in asynchronous mode.       | `async Task<bool> AppendAsync(PdfLoadedDocument idDoc)`                                                             | `Boolean`            |
| MergeAsync         | Merges documents in asynchronous mode.       | `async static Task<PdfDocumentBase> MergeAsync(PdfDocumentBase dest, PdfLoadedDocument src)`                      | `PdfDocumentBase`   |

### 4.6 Supported Elements

**Description:**  
Supported and non-supported Excel elements of Essential PDF for Windows, ASP.NET, WPF, ASP.NET MVC, Silverlight, and Windows Store apps are listed in the following table.

#### Table of Supported Features

| Features                | Windows Forms/WPF | ASP.NET/ASP.NET MVC (Medium Trust) | ASP.NET/ASP.NET MVC (Full Trust) | Silverlight | Windows Store Apps |
|-------------------------|-------------------|-------------------------------------|------------------------------------|-------------|--------------------|
| Drawing Text           | Yes               | Yes                                 | Yes                                | Yes         | Yes               |
| Text Formatting        | Yes               | Yes                                 | Yes                                | Yes         | Yes               |
| Multilingual Support   | Yes               | No                                  | Yes                                | No          | No                |
| Drawing RTL text       | Yes               | No                                  | Yes                                | No          | No                |
| Text Extraction        | Yes               | Yes                                 | Yes                                | No          | No                |
| Unicode                | Yes               | No                                  | Yes                                | No          | No                |
| Pagination             | Yes               | Yes                                 | Yes                                | Yes         | Yes               |
| **Graphics**           |                   |                                     |                                    |             |                    |
| Pen and Brush          | Yes               | Yes                                 | Yes                                | Yes         | Yes               |
| Layers                 | Yes               | Yes                                 | Yes                                | Yes         | Yes               |

## Cross References
- Refer to the previous sections for more information on PDF operations and handling.

<!-- tags: [Syncfusion, Windows Forms, WPF, ASP.NET, ASP.NET MVC, Silverlight, Windows Store Apps, PDF, text handling, graphics, pagination] keywords: [ImportPageAsync, ImportPageRangeAsync, AppendAsync, MergeAsync, multilingual support, RTL text, text extraction, Unicode] -->
```