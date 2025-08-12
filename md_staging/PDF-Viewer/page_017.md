```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_017.jpeg
document_name: PDF Viewer
page_number: 017
page_id: PDF Viewer#page_017
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:51:04Z
fidelity: lossless
-->

## Content

### ToolStrip Structure

**Overview**
- This section details the structure and functionality of the Toolstrip in the Essential PDF Viewer application.

#### Figure 8 Structure of Toolstrip
![Figure 8 Structure of Toolstrip](https://example.com/figure8.png)

1. **File Open Dialog**
2. **Show Print Dialog**
3. **Go to first page**
4. **Go to previous page**
5. **Page Indicator**
6. **Go to next page**
7. **Go to last page**
8. **Increase magnification**
9. **Decrease magnification**
10. **Preset magnification**
11. **Fill window**
12. **Fit page to window**

### Individual Toolstrip Functions

#### Overview
- **File Open Dialog (1)**: Opens the dialog to select and load a PDF file.
- **Show Print Dialog (2)**: Displays the print options for the current PDF document.
- **Go to first page (3)**: Navigates to the beginning of the document.
- **Go to previous page (4)**: Moves to the previous page in the document.
- **Page Indicator (5)**: Indicates the current page number and total pages.
- **Go to next page (6)**: Moves to the subsequent page in the document.
- **Go to last page (7)**: Navigates to the end of the document.
- **Increase magnification (8)**: Zooms in on the current page view.
- **Decrease magnification (9)**: Zooms out on the current page view.
- **Preset magnification (10)**: Sets a predefined zoom level for the document view.
- **Fill window (11)**: Adjusts the page view to completely fill the window.
- **Fit page to window (12)**: Scales the page to fit within the window dimensions.

#### Functionality
- The Toolstrip provides essential navigation and display options for managing PDF documents effectively.

### Conclusion
- The Toolstrip is designed to enhance user interaction by offering quick access to navigation, manipulation, and display settings for PDF files.

## API Reference
- The Toolstrip leverages standard .NET and Syncfusion controls to implement functionality. Refer to the Syncfusion Winforms documentation for detailed API usage.

### Code Examples
```csharp
// Example of invoking a function to go to the first page
toolStripButton1_Click(object sender, EventArgs e) {
    pdfViewer.GoToFirstPage();
}
```

## Cross References
- See also:
  - [Syncfusion Winforms Documentation](https://www.syncfusion.com/documentation/windowsforms)

## Page-level Navigation/TOC
- [Toolstrip Structure](#Toolstrip-Structure)
- [Individual Toolstrip Functions](#Individual-Toolstrip-Functions)

<!-- tags: [Toolstrip, PDF Viewer, Syncfusion Winforms, Navigation, Display, Controls] keywords: [structure, function, navigation, Zoom, Page Indicator, Print Dialog, File Open Dialog] -->
```