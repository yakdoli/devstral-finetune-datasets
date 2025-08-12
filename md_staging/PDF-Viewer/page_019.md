```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_019.jpeg
document_name: PDF Viewer
page_number: 019
page_id: PDF Viewer#page_019
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:50:41Z
fidelity: lossless
-->

# Essential PDF Viewer

## Overview
- This page provides a detailed table of methods and their descriptions for the Essential PDF Viewer.
- It includes information about the parameters, types, and return types for each method.
- Methods covered include Load, Unload, Dispose, ExportAsImage, FindText, and GoToPageAtIndex.

## Content

### Table 2: Methods Table

| Method             | Description                                                                                                                     | Parameters                                                                                                                                    | Type | Return Type |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|------|-------------|
| Load               | This method is used to load the PDF to the viewer.                                                                         | Overloads:<br>(string filePath)<br>(string filePath, string password)<br>(PdfLoadedDocument doc)<br>(Stream file)          | N/A   | Void       |
| Unload             | Unloads the loaded PDF.                                                                                                     | -                                                                                                                                            | N/A   | Void       |
| Dispose            | Unloads the document and releases the resources used by the component.                                                    | -                                                                                                                                            | N/A   | Void       |
| ExportAsImage      | Converts the page to a raster image.                                                                                       | Overloads:<br>(int pageIndex)<br>(int startIndex, int endIndex)                                                                           | N/A   | Bitmap     |
| FindText           | Searches for the occurrence of given input text in the PDF document and returns all the occurrences and its location in all pages of the PDF document. | Overloads:<br>(String text, out Dictionary<int, List<System.Drawing.RectangleF>> matchRect)                                    | N/A   | bool       |
| GoToPageAtIndex   | Navigates to the mentioned page                                                                                             | (int index)                                                                                                                                   | N/A   | Void       |

## API Reference

### Methods
- **Load**<br>
  Overloads:
  - (`string filePath`)<br>
  - (`string filePath`, `string password`)<br>
  - (`PdfLoadedDocument doc`)<br>
  - (`Stream file`)

- **Unload**<br>
  - No parameters

- **Dispose**<br>
  - No parameters

- **ExportAsImage**<br>
  Overloads:
  - (`int pageIndex`)<br>
  - (`int startIndex`, `int endIndex`)

- **FindText**<br>
  Overloads:
  - (`String text`, `out Dictionary<int, List<System.Drawing.RectangleF>> matchRect`)

- **GoToPageAtIndex**<br>
  - (`int index`)

### Parameters
- **string filePath**: Path of the PDF file to be loaded.
- **string password**: Password for protected PDF documents.
- **PdfLoadedDocument doc**: Reference to an already loaded PDF document.
- **Stream file**: Stream containing the PDF data.
- **int pageIndex**: Index of the page to be converted to an image.
- **int startIndex**: Start index of the range to be exported as images.
- **int endIndex**: End index of the range to be exported as images.
- **String text**: The text to search for in the PDF document.
- **Dictionary<int, List<System.Drawing.RectangleF>> matchRect**: Output parameter for storing the location of text occurrences.

### Return Types
- **Void**: Methods that do not return any value.
- **Bitmap**: Returns an image of the specified page.
- **bool**: Returns a boolean value indicating whether the search was successful.

## Code Examples

Below is a sample code snippet demonstrating the use of the `Load` method:

```csharp
using Syncfusion.Pdf;
using System;

class Program
{
    static void Main(string[] args)
    {
        // Create a new instance of the PDF Viewer
        var viewer = new Syncfusion.PdfViewer.Windows.Forms.PdfViewerControl();

        // Load a PDF file
        viewer.Load("path_to_your_pdf_file.pdf");

        // Display the PDF in the viewer
        System.Windows.Forms.Application.Run(new System.Windows.Forms.Form());
    }
}
```

## Page-level Navigation/TOC
- This page covers the essential methods for interacting with the PDF Viewer in Syncfusion Winforms.

## Cross References
- Refer to the documentation for PdfLoadedDocument and other related classes for more details on working with PDF documents.

<!-- tags: [Syncfusion, PDF Viewer, Winforms, Methods, API Reference] keywords: [Load, Unload, Dispose, ExportAsImage, FindText, GoToPageAtIndex, PDF, viewer, methods, overloads] -->
```