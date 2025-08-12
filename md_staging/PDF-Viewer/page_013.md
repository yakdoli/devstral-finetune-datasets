```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_013.jpeg
document_name: PDF Viewer
page_number: 013
page_id: PDF Viewer#page_013
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:50:53Z
fidelity: lossless
-->

### PDF Viewer

| Feature        | No      | Yes*****     | No      |
|----------------|---------|--------------|---------|
| Edit           | No      | No           | No      |
| Touch Support  | No      | Yes*****     | No      |
| Printing Options |        |              |         |
| Silent Printing | Yes    | Yes          | Yes     |
| Send to Printer | Yes    | Yes          | Yes     |
| Export Options |        |              |         |
| Image Export | Yes (raster and vector formats) | Yes (raster format only) | No      |

* If the font is not available in the machine or is embedded within the PDF, it will be substituted by MS Sans Serif in Windows Forms and ASP.NET MVC. In WPF, Times New Roman will be the substitute font.
* *** Only embedded fonts of TrueType and Identity-H encoding are supported.
* **** Supports only images in MVC platform.
* *****Supports only URI annotation.
* *****Supported only in the 4.0 framework.

## 3.2 Adding PDF Viewer to an Application

To add a PDF Viewer control to your application:

1. Open your form in the designer. Add the Syncfusion controls to your VS.NET toolbox if you haven't done so already (the install would have automatically done this unless you selected not to complete toolbox integration during installation).

<!-- tags: [syncfusion, winforms, pdf viewer, control, integration, application] keywords: [pdf viewer, syncfusion controls, windows forms, wpf, mvc, uri annotation, designer, toolbox] -->
```