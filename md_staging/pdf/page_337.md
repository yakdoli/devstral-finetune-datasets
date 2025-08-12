```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_337.jpeg
document_name: pdf
page_number: 337
page_id: pdf#page_337
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:44:41Z
fidelity: lossless
-->

# Essential PDF

## Overview

- Draw an image into the PDF document as a bitmap.
- Asynchronous support for reading, writing, and merging PDF files in Essential PDF.
- Overview of asynchronous methods and supported APIs in Windows Store apps.

## Content

```vb
' Draw the image into the PDF document as bitmap
Dim image As PdfImage = New PdfBitmap(img)
Dim format As PdfLayoutFormat = New PdfLayoutFormat()
format.Break = PdfLayoutBreakType.FitPage
format.Layout = PdfLayoutType.Paginate
image.Draw(page, New RectangleF(0, 0, pageSize.Width, pageSize.Height), format)
```

### 4.5 Asynchronous Support

Essential PDF can read, write, and merge PDF files using asynchronous methods. This is a new approach introduced in Visual Studio 2012 that enables applications to use asynchronous programming. The following list of public APIs in Essential PDF supports asynchronous programming.

**Note:** Asynchronous support is applicable only to Windows Store apps.

| Method      | Description                                                   | Parameters                                                                                                                                                                               | Return Type |
|-------------|---------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| **OpenAsync** | Opens an existing PDF document.                              | `- async Task<bool> OpenAsync(StorageFile stFile)`<br>`- async Task<bool> OpenAsync(StorageFile stFile, string password)`<br>`- async Task<bool> OpenAsync(byte[] bytes)`<br>`- async Task<bool> OpenAsync(byte[] bytes, string password)`<br>`- async Task<bool> OpenAsync(Stream stream)`<br>`- async Task<bool> OpenAsync(Stream stream, string password)` | Boolean      |
| **SaveAsync** | Saves the document to a stream in asynchronous mode.        | `- async Task<bool> SaveAsync(Stream stream)`                                                                                                                                           | Boolean      |
| **SaveAsync** | Saves the PDF file to a storage file.                       | `- async Task<bool> SaveAsync(StorageFile stFile)`                                                                                                                                       | Boolean      |
| **Save**      | Saves the modified document.                                | `- async Task<bool> Save()`                                                                                                                                                             | Boolean      |

### Summary of Asynchronous APIs

Essential PDF provides a comprehensive set of asynchronous APIs for handling PDF files, ensuring smooth and efficient operations in Windows Store applications.

## Cross References

- For more information on Windows Store application development with Essential PDF, see the Windows Store apps section in the documentation.
- Refer to the section on asynchronous programming in Visual Studio 2012 for additional guidance.

<!-- tags: [Essential PDF, asynchronous support, Windows Store apps, Visual Studio 2012, APIs, Windows Store] keywords: [asynchronous programming, OpenAsync, SaveAsync, async Task, PDF, Windows Store Apps, Visual Studio, PDF image, paginating, FitPage] -->
```