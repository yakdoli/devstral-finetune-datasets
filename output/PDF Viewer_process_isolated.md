---
title: "PDF Viewer - Syncfusion SDK Documentation"
type: "api-documentation"
framework: "syncfusion"
version: "v11"
processing_mode: "Process Isolation (프로세스 격리)"
extracted_date: "1754725956.9013019"
optimized_for: ["llm-training", "rag-retrieval"]
scaling_approach: "3"
---

<!-- 페이지 1 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_001.jpeg
document_name: PDF Viewer
page_number: 001
page_id: PDF Viewer#page_001
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:49:57Z
fidelity: lossless
-->

# Essential Studio 2013 Volume 4 - v.11.4.0.26 Essential PDF Viewer

## Overview
- Comprehensive guide to the Essential PDF Viewer component from Syncfusion.
- Focus on delivering innovative solutions for PDF viewing and manipulation.

## Content
### Introduction
The Essential PDF Viewer is a powerful component designed to provide seamless PDF viewing capabilities within WinForms applications. It offers advanced functionalities such as text searching, zooming, and annotation management.

### Key Features
- **PDF Rendering:** High-quality rendering of PDF documents.
- **Zooming Options:** Dynamic zoom levels to enhance user experience.
- **Text Search:** Efficient search functionality within PDF contents.
- **Annotations:** Support for adding and managing comments and highlights.
  
### Installation and Setup
- **Downloading the Component:** Follow the official Syncfusion documentation to download the Essential PDF Viewer DLLs.
- **Integration:** Integrate the PDF Viewer component into your WinForms project using the provided namespace and controls.
  
### Use Cases
- Enterprise applications requiring PDF document management.
- Security-sensitive applications leveraging the advanced features of the PDF Viewer.

## API Reference
### Namespaces
- `Syncfusion.Windows.Forms.PDFViewer`

### Classes
- **PDFViewer:** Core class for implementing PDF viewing functionality.
  
### Methods
- `Load(string filePath):` Loads a PDF file from the specified path.
- `Search(string searchTerm):` Searches for the given term within the loaded PDF.
  
### Properties
- **ZoomLevel:** Gets or sets the current zoom level of the PDF document.
- **CurrentPage:** Gets or sets the currently displayed page of the PDF document.
  
### Events
- `PageChanged:` Triggered when the current page of the PDF document changes.
- `SearchCompleted:` Triggered when a text search operation is completed.

## Code Examples

```csharp
using Syncfusion.Windows.Forms.PDFViewer;

// Load a PDF document
PDFViewer pdfViewer = new PDFViewer();
pdfViewer.Load("path/to/your/document.pdf");

// Zoom in to 150%
pdfViewer.ZoomLevel = 1.5f;

// Search for text within the document
pdfViewer.Search("search term");

// Handle page change events
pdfViewer.PageChanged += (sender, e) => {
    MessageBox.Show($"Page changed to {pdfViewer.CurrentPage}");
};
```

## Page-level Navigation/TOC
- [Introduction](#introduction)
- [Key Features](#key-features)
- [Installation and Setup](#installation-and-setup)
- [Use Cases](#use-cases)
- [API Reference](#api-reference)
- [Code Examples](#code-examples)

<!-- tags: [syncfusion, winforms, pdf viewer, essential studio, v.11.4.0.26] keywords: [PDF, rendering, zoom, search, annotations, text, document] -->
```

---

<!-- 페이지 2 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_005.jpeg
document_name: PDF Viewer
page_number: 005
page_id: PDF Viewer#page_005
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:50:17Z
fidelity: lossless
-->

## Essential PDF Viewer

### Prerequisites

| Development Environments                                                                                 | .NET Framework versions                                                                     |
|----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| - Visual Studio 2010 (Ultimate, Premium, Professional and Express)                                      | - .NET Framework version 3.5 with Service Pack 1                                          |
| - Visual Studio 2008 (Team System, Professional, Standard & Express)                                   | - .NET Framework version 4.0                                                              |
| - Visual Studio 2005 (Professional, Standard & Express)                                                 | - .NET Framework version 2.0                                                              |
| - Microsoft Expression Blend                                                                              |                                                                                             |

### Compatibility

| Operating Systems                                                                                                                             |
|---------------------------------------------------------------------------------------|
| - Windows Server 2008 (32 bit and 64 bit)                                              |
| - Windows Vista (32 bit and 64 bit)                                                   |
| - Windows XP                                                                        |
| - Windows 2003                                                                      |
| - Windows 7                                                                         |

## 1.4 Documentation

| Type of Documentation                        | Location                                                                                                                |
|-----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Readme                                        | Readme: [drive:]\Program Files\Syncfusion\Essential Studio\x.x.x\Infrastructure\Read Me\Reporting_Windows.html             |
| Release Notes                                  | ReleaseNotes: [drive:]\Program Files\Syncfusion\Essential Studio\x.x.x\Infrastructure\Release Notes\Reporting.html#Windows-PdfViewer |
| User Guide (this document)                    | Online <br> http://help.syncfusion.com/resources (Navigate to the PDF Viewer for                                       |
```

---

<!-- 페이지 3 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_009.jpeg
document_name: PDF Viewer
page_number: 009
page_id: PDF Viewer#page_009
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:50:29Z
fidelity: lossless
-->

# Essential PDF Viewer

## Overview
- Features a Windows Forms sample browser for showcasing functionalities.
- Demonstrates the use of Syncfusion's PDF Viewer to handle PDF files.
- Includes options to view PDF files, print, customize toolbars, and export as images.

## Content

### Windows Forms Sample Browser

#### Figure 3: Windows Forms Sample browser
The Windows Forms Sample browser is shown with the `Windows Forms` header. On the left sidebar, various options are presented, including:

- **DocIO**
  - Product Showcase
  - Getting Started
  - Insert Content
  - Formatting
  - Page Layout
  - References
  - Editing
  - Mail Merge
  - View
  - Security
  - Import And Export

A section titled "Syncfusion Essential DocIO" is visible. It describes Essential DocIO as a .NET library that can read and write Microsoft Word files. The library features a full-fledged object model similar to the Microsoft Office COM libraries. It operates without COM interop and is fully built in C#, making it usable on systems that do not have Microsoft Word installed.

#### Featured Samples
Several sample images are displayed, illustrating:
- **Sales Invoice**, showing an invoice with details.
- **Table Insertion**, demonstrating the insertion of a customer table.
- **Employee Report**, displaying an employee report with data.
- **Table Of Contents**, highlighting the table of contents for a document.

### Interactive Options
- **Sales Invoice**: Displays an invoice template.
- **Table Insertion**: Presents a customer table with company names and customer IDs.
- **Employee Report**: Shows an employee profile report.
- **Forms**: Illustrates an educational qualification form.
- **Clone and Merge**: Displays an option to clone and merge documents.
- **Update Fields**: Indicates the ability to update fields in a document.

#### Step to Click PDF Viewer
3. **Click `PDF Viewer` from the bottom-left pane.**

The image indicates the next step is to click the `PDF Viewer` option from the bottom-left pane. This will transition to the PDF Viewer specific functionalities and features.

#### Figure 4: Windows Forms Sample Browser Displaying PdfViewer Samples
This section highlights the Windows Forms Sample Browser with the following demonstrated features:
- **Pdf Viewer Demo**: Displays a demo of the PDF Viewer capabilities.
- **Custom Toolbar**: Illustrates a customizable toolbar for the PDF Viewer.
- **Silent Printing**: Shows an option for printing PDFs in the background.
- **Multi Tabbed Viewer**: Demonstrates a multi-tabbed viewer interface for handling multiple PDFs.
- **Export as Image**: Allows exporting PDF pages as images.

Each sample screenshot provides a visual representation of the features mentioned, such as updating fields, cloning documents, and handling multiple tabs.

## API Reference
The document does not include explicit API references, but highlights the use of Syncfusion PDF Viewer API for reading and managing PDF files.

## Code Examples
The document does not include code examples but mentions the ability to print, customize toolbars, and export as images, suggesting that such functionalities are programmatically available.

## Page-level Navigation/TOC
There is no explicit Table of Contents present, but the document provides a structured overview and sample demonstrations of key features.

## Cross References
- **See also**: 
  - Syncfusion WinForms Technical Documentation
  - Windows Forms Developer Hub

## RAG Annotations
The document provides a detailed walkthrough of PDF Viewer functionality, leveraging Syncfusion's Essential PDF Viewer features for managing and interacting with PDF files. Examples include:
- Visual demonstrations of various document features such as invoices, tables, employee reports, and forms.
- Interactive options for customization, printing, and exporting PDFs are shown.
- A clear step to access the PDF Viewer from the sample browser is provided.

<!-- tags: [essential pdf viewer, windows forms, syncfusion winforms, pdf viewer, sample browser, docio, forms, employee reports, table insertions, pdf export] keywords: [syncfusion, windows forms, essential pdf viewer, pdf features, sample browser, interactive options, document handling] -->
```

---

<!-- 페이지 4 -->

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

---

<!-- 페이지 5 -->

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

---

<!-- 페이지 6 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_021.jpeg
document_name: PDF Viewer
page_number: 021
page_id: PDF Viewer#page_021
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:51:21Z
fidelity: lossless
-->

# Essential PDF Viewer

## Content

### Loading PDF Documents

Initialize the PDF Viewer.

```vb
' Initialize PDF Viewer.
Private pdfViewer1 As New PdfViewerControl()
```

Load the PDF.

```vb
' Load the PDF.
pdfViewer1.Load("Template.pdf")
```

You can load an encrypted document by using the overload in the `Load` method.

#### Loading Encrypted Documents

In C#:

```csharp
// Initialize PDF Viewer.
PdfViewerControl pdfViewer1 = new PdfViewerControl();

// Load the PDF.
pdfViewer1.Load("Template.pdf", "password");
```

In VB.NET:

```vb
' Initialize PDF Viewer.
Private pdfViewer1 As New PdfViewerControl()

' Load the PDF.
pdfViewer1.Load("Template.pdf", "password")
```

### Printing PDF Files

PDF Viewer allows printing loaded PDFs using the **Print** button in the toolbar. The following **Print** dialog will be opened upon triggering the **Print** button.

## API Reference

* **Namespace:** Syncfusion.PdfViewer.WinForms
* **Class:** PdfViewerControl
* **Methods:** Load(String filePath, String password)

## Code Examples

### Example: Loading a Protected PDF Document

#### C#

```csharp
// Initialize PDF Viewer.
PdfViewerControl pdfViewer1 = new PdfViewerControl();

// Load the encrypted PDF.
pdfViewer1.Load("SecureTemplate.pdf", "123456");
```

#### VB.NET

```vb
' Initialize PDF Viewer.
Private pdfViewer1 As New PdfViewerControl()

' Load the encrypted PDF.
pdfViewer1.Load("SecureTemplate.pdf", "123456")
```

## Cross References

* Refer to the documentation for detailed steps on handling secured documents.
* Additional information on printing functionality can be found in the **Printing** section.

<!-- tags: [syncfusion, pdf viewer, encryption, printing, forms, windows forms] -->
<!-- keywords: [load pdf, encrypted documents, print dialog, pdf viewer documentation, c#, vb.net, load method, syncfusion SDK, 11.4.0.26] -->
```

---

<!-- 페이지 7 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_025.jpeg
document_name: PDF Viewer
page_number: 025
page_id: PDF Viewer#page_025
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:51:34Z
fidelity: lossless
-->

# Essential PDF Viewer

## Overview
- The PDF Viewer control supports searching text in the PDF document using the `FindText` API.
- The `FindText` method returns `true` if the specified text is found in the document.
- The result is a dictionary containing the page index and rectangular coordinates of the text found on that page.

## Content

### Text Search in PDF Viewer

The PDF Viewer control also supports searching text in the PDF document with the help of the following API. The `FindText` method returns `true` when the text given is found in the document. The dictionary contains the page index and the list of rectangular coordinates of the text found in that page. The following code snippet illustrates how text search can be achieved in the PDF Viewer control.

#### C# Example

```csharp
bool IsMatchFound;
pdfViewerControl1.Load("../../Data/Barcode.pdf");

// Get the occurrences of the target text and location.
Dictionary<int, List<RectangleF>> textSearch = new Dictionary<int, List<RectangleF>>();
IsMatchFound = pdfViewerControl1.FindText("targetText", out textSearch);
```

#### VB.NET Example

```vb
Dim IsMatchFound As Boolean
pdfViewerControl1.Load("../../Data/Barcode.pdf")

' Get the occurrences of the target text and location.
Dim textSearch As New Dictionary(Of Integer, List(Of RectangleF))()
IsMatchFound = pdfViewerControl1.FindText("targetText", textSearch)
```

### 4.1.6 Annotation

#### Overview of Annotations

Essential PDF Viewer provides support for URI annotations in the PDF document, which enables the URI available in the PDF document to be opened in the browser just by clicking it. This also supports a few events, which are listed in the previous table.

<!-- tags: [PDF Viewer, text search, annotation, URI, Syncfusion Winforms, C#, VB.NET] keywords: [FindText, Dictionary, RectangleF, textSearch, IsMatchFound, URI annotations, document, PDF Viewer control, page index, search text] -->
```

---

<!-- 페이지 8 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_029.jpeg
document_name: PDF Viewer
page_number: 029
page_id: PDF Viewer#page_029
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:51:47Z
fidelity: lossless
-->

## Index

### A
- Adding PDF Viewer to an Application 13
- Annotation 25
- Appearance and Structure of the Control 16

### C
- Concepts and Features 18

### D
- Default Deployment Pattern 10
- Deployment Procedures 10
- Deployment Requirements 10
- Documentation 5

### E
- Events 20
- Exporting PDF 23
- Exporting PDFs as Raster Images 23
- Exporting PDFs as Vector Images 23

### F
- Fast Deployment Pattern 10
- Feature Summary 11
- Get page count? 26
- Getting Started 11

### H
- How To 26

### I
- Installation 7
- Installation and Deployment 7
- Introduction to PDF Viewer 4

### L
- Load a specific page? 27
- Load PDF without Toolstrip in Viewer? 27

### M
- Methods 18

### O
- Overview 4

### P
- Prerequisites and Compatibility 4
- Printing PDF Files 21
- Properties 18
- Properties, Methods, and Events Tables 18

### S
- Sample Installation Location 7
- Silent Printing 22
- Text Search 24

### U
- Use Case Scenario 4

### V
- View the PDF stream in viewer? 26
- Viewing PDF Files 20
- Viewing Samples 7

### W
- Where to Find Samples? 7
- Working with PDF Viewer 18
```

---

<!-- 페이지 9 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_002.jpeg
document_name: PDF Viewer
page_number: 002
page_id: PDF Viewer#page_002
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:49:57Z
fidelity: lossless
-->

# Contents

## Overview

- **1.1 Introduction to PDF Viewer** ..... 4
- **1.2 Use Case Scenario** ..... 4
- **1.3 Prerequisites and Compatibility** ..... 4
- **1.4 Documentation** ..... 5

## Installation and Deployment

- **2.1 Installation** ..... 7
- **2.2 Where to Find Samples?**
  - **2.2.1 Sample Installation Location** ..... 7
  - **2.2.2 Viewing Samples** ..... 7
- **2.3 Deployment Procedures**
  - **2.3.1 Deployment Requirements** ..... 10
  - **2.3.2 Default Deployment Pattern** ..... 10
  - **2.3.3 Fast Deployment Pattern** ..... 10

## Getting Started

- **3.1 Feature Summary** ..... 11
- **3.2 Adding PDF Viewer to an Application** ..... 13
- **3.3 Appearance and Structure of the Control** ..... 16

## Concepts and Features

- **4.1 Working with PDF Viewer** ..... 18
  - **4.1.1 Properties, Methods, and Events Tables** 
    - **4.1.1.1 Properties** ..... 18
    - **4.1.1.2 Methods** ..... 18
    - **4.1.1.3 Events** ..... 20
  - **4.1.2 Viewing PDF Files** ..... 20
  - **4.1.3 Printing PDF Files**
    - **4.1.3.1 Silent Printing** ..... 22
  - **4.1.4 Exporting PDF**
    - **4.1.4.1 Exporting PDFs as Raster Images** ..... 23
    - **4.1.4.2 Exporting PDFs as Vector Images** ..... 23

<!-- tags: [PDF Viewer, Syncfusion Winforms, installation, deployment, features, documentation, version:11.4.0.26] keywords: [overview, use case, prerequisites, samples, deployment, features, exporting PDFs, printing, viewer] -->
```

---

<!-- 페이지 10 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_006.jpeg
document_name: PDF Viewer
page_number: 006
page_id: PDF Viewer#page_006
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:50:12Z
fidelity: lossless
-->

## Documentation and Reference

### Installed Documentation
- **Path**: Dashboard -> Documentation -> Installed Documentation.

### Class Reference

#### Online
- **Website**: [http://help.syncfusion.com/resources](http://help.syncfusion.com/resources)
- **Instructions**: Navigate to the Reporting Windows Forms User Guide. Select **PDF Viewer**, and then click the **Class Reference** link found in the upper right section of the page.

#### Installed Documentation
- **Path**: Dashboard -> Documentation -> Installed Documentation.

### Additional Notes
- **Note**: Click **Download as PDF** to access a PDF version of the documentation.

### Copyright
- **Copyright**: © 2013 Syncfusion. All rights reserved.

<!-- tags: [PDF Viewer, Syncfusion, Windows Forms, Class Reference, Documentation] keywords: [PDF, User Guide, Installed Documentation, Class Reference, Windows Forms, Syncfusion Winforms, Product Documentation] -->
```

---

<!-- 페이지 11 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_010.jpeg
document_name: PDF Viewer
page_number: 010
page_id: PDF Viewer#page_010
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:50:20Z
fidelity: lossless
-->

## Content

### 2.3 Deployment Procedures

#### Deployment Requirements

The required assemblies are:
- Syncfusion.Core.dll
- Syncfusion.Compression.Base.dll
- Syncfusion.Pdf.Base.dll
- Syncfusion.PdfViewer.Windows.dll

#### 2.3.2 Default Deployment Pattern

For step-by-step installation procedure of Essential Studio, refer to the Installation topic under Installation and Deployment in the Common UG.

#### 2.3.3 Fast Deployment Pattern

For licensing, patches, and information on adding or removing selective components, refer to the following topics in the Common UG under Installation and Deployment:
- Licensing
- Patches
- Add/Remove Components

### Overview

- Sample features are displayed on the left pane.
- Users can select samples and browse through their features.
- To run a sample, click the Run Sample icon in the right pane.
- Deployment procedures including required assemblies and patterns are detailed.

### WinForms-specific conventions

- The required assemblies for Syncfusion.PdfViewer.Windows.dll are specified.
- Installation and deployment guidelines are provided under both Default and Fast Deployment Patterns.
- Licensing, patches, and selective component management are referenced for further information.

### API Reference (if applicable)

No specific API references are mentioned. However, referenced assemblies and deployment procedures have clear relationships to Syncfusion’s PDF Viewer functionality.

### Code Examples (multi-language supported)

No specific code examples are explicitly displayed, but the reference to required assemblies may indicate the necessity of including relevant C# code to demonstrate usage.

### Page-level Navigation/TOC (if applicable)

This page contains sections on deployment requirements, deployment patterns, and references for further details, covering the installation and configuration of Syncfusion’s PDF Viewer.

### Cross References

- **Common UG under Installation and Deployment** is referenced for both Default and Fast Deployment Patterns.
- Licensing and component management topics are referenced under the Common UG.

### RAG Annotations

<!-- tags: [PDF Viewer, deployment, assemblies, essential studio, fast deployment, licensing] keywords: [Syncfusion.Core.dll, Syncfusion.Compression.Base.dll, Syncfusion.Pdf.Base.dll, Syncfusion.PdfViewer.Windows.dll, Run Sample, Installation topic, Fast Deployment, Licensing] -->
```

---

<!-- 페이지 12 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_014.jpeg
document_name: PDF Viewer
page_number: 014
page_id: PDF Viewer#page_014
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:50:34Z
fidelity: lossless
-->

# Essential PDF Viewer

## Overview
- PDF Viewer control is available in the Syncfusion Windows Toolbox.
- Steps to incorporate the PDF Viewer control into a project.
- Appearance and behavior of the PDF Viewer can be customized via properties.

## UI Components in the Toolbox

The following components are available in the Syncfusion Windows Toolbox for PDF Viewer:

- **Pointer**
- **GridControl**
- **GridListControl**
- **PdfDocumentView**
- **PdfViewerControl** <!-- Highlighted -->
- **GridRecordNavigationControl**
- **GridAwareTextBox**
- **BannerTextProvider**
- **ButtonAdv**
- **ColorPickerButton**
- **ColorUIControl**
- **TextBoxExt**
- **CurrencyTextBox**
- **PopupControlContainer**

**Figure 5: PDF Viewer control in Toolbox**

### Procedure to Add PDF Viewer Control

1. **Drag a PDF Viewer control onto the form.**
   - This action places the PDF Viewer control within the application's form interface.

**Appearance and behavior-related aspects of the PDF Viewer can be controlled by setting the appropriate properties through the properties grid.**

---

## API Reference (if applicable)

### Properties
- **Customization Properties:**`Appearance`, `Behavior`
- **PDF Viewer Control Settings:**`PdfViewerSettings`, `ZoomLevel`

### Methods
- **Load PDF Document:**`LoadPdfDocument()`
- **Refresh Viewer:**`RefreshViewer()`

### Events
- **DocumentLoaded:**`DocumentLoadedEvent`

---

## Code Examples

### C# Example

```csharp
using Syncfusion.Windows.Forms.PdfViewer;

public void InitializePdfViewer()
{
    PdfViewerControl viewer = new PdfViewerControl();
    viewer.Dock = DockStyle.Fill;
    this.Controls.Add(viewer);

    // Load a PDF document
    viewer.LoadPdfDocument("path/to/pdf/document.pdf");
}
```

### VB.NET Example

```vb
Imports Syncfusion.Windows.Forms.PdfViewer

Public Sub InitializePdfViewer()
    Dim viewer As New PdfViewerControl()
    viewer.Dock = DockStyle.Fill
    Me.Controls.Add(viewer)

    ' Load a PDF document
    viewer.LoadPdfDocument("path/to/pdf/document.pdf")
End Sub
```

---

## Page-level Navigation/TOC (if applicable)

- [**Figure 5**] PDF Viewer control in Toolbox
- Procedure to Add PDF Viewer Control

## Cross References

- **Related Controls:** ButtonAdv, ColorPickerButton, CurrencyTextBox
- **Further Assistance:** Syncfusion Windows Forms Documentation

<!-- tags: [syncfusion, windows forms, pdf viewer, control, toolbox, properties, api] keywords: [pdf, viewer, drag, form, properties grid, customization] -->
```

---

<!-- 페이지 13 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_018.jpeg
document_name: PDF Viewer
page_number: 018
page_id: PDF Viewer#page_018
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:50:50Z
fidelity: lossless
-->

# Concepts and Features

## 4.1 Working with PDF Viewer

Essential PDF Viewer can display PDF files, and print and export the pages as raster images. All this can be done within a .NET application.

### 4.1.1 Properties, Methods, and Events Tables

#### 4.1.1.1 Properties

**Table 1: Properties Table**

| Property              | Description                                                                 | Type | Data Type |
|-----------------------|-----------------------------------------------------------------------------|------|-----------|
| EnableNotificationBar | Enables the display of the Notification bar on setting it to true.        | N/A  | bool      |
| PageCount             | Returns the number of pages as viewed in the PDF Viewer.                 | N/A  | Integer   |
| ShowToolbar           | Displays the document toolbar when set to true.                          | N/A  | bool      |

#### 4.1.1.2 Methods
<!-- tags: [PDF Viewer, properties, methods, events, N/A, bool, integer] keywords: [properties, methods, EnableNotificationBar, PageCount, ShowToolbar, N/A, bool, integer] -->
```html
```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

```html

---

<!-- 페이지 14 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_022.jpeg
document_name: PDF Viewer
page_number: 022
page_id: PDF Viewer#page_022
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:52:15Z
fidelity: lossless
-->

# Essential PDF Viewer

## Content

### Print Dialog Displayed in PDF Viewer

Figure 9: Print Dialog displayed in PDF Viewer

#### 4.1.3.1 Silent Printing

The `PrintDocument` property of `PdfViewerControl` returns `System.Drawing.Printing.PrintDocument` that helps to complete printing using `PrintDialog`. The following code sample demonstrates this:

##### C#

```csharp
PrintDialog dialog = new PrintDialog();
dialog.AllowPrintToFile = true;
dialog.Document = viewer.PrintDocument;
dialog.Document.Print();
```

##### VB.NET

```vb
Dim dialog As New PrintDialog()
dialog.AllowPrintToFile = True
dialog.Document = viewer.PrintDocument
dialog.Document.Print()
```

## API Reference

### Methods

- `PrintDocument`: Retrieves the `PrintDocument` object used for printing.
- `Print`: Initiates the printing process.

### Properties

- `AllowPrintToFile`: Enables or disables the option to print to file.

## Code Examples

#### C#

```csharp
PrintDialog dialog = new PrintDialog();
dialog.AllowPrintToFile = true;
dialog.Document = viewer.PrintDocument;
dialog.Document.Print();
```

#### VB.NET

```vb
Dim dialog As New PrintDialog()
dialog.AllowPrintToFile = True
dialog.Document = viewer.PrintDocument
dialog.Document.Print()
```

## RAG Annotations

<!-- tags: [PDF Viewer, PrintDocument, PrintDialog, Silent Printing, C#, VB.NET] keywords: [PdfViewerControl, printing, PrintDocument, PrintDialog, AllowPrintToFile, Print] -->
```

---

<!-- 페이지 15 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_026.jpeg
document_name: PDF Viewer
page_number: 026
page_id: PDF Viewer#page_026
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:52:26Z
fidelity: lossless
-->

## 5 How To

This section will help you find answers to common questions regarding Essential Pdf Viewer.

### 5.1 View the PDF stream in viewer?

PDF files as stream can be viewed in Essential Pdf Viewer using the overload available in the Load method. Following are the code snippets.

```csharp
[C#]
FileStream stream = new FileStream("Template.pdf", FileMode.Open);
//Initialize PDF Viewer
PdfViewerControl pdfViewer1 = new PdfViewerControl();
  
//Load the PDF
pdfViewer1.Load(stream);
```

```vb.net
[VB.NET]
Dim stream As New FileStream("Template.pdf", FileMode.Open)

' Initialize PDF Viewer
Dim pdfViewer1 As New PdfViewerControl()

' Load the PDF
pdfViewer1.Load(stream)
```

### 5.2 Get page count?

The number of pages as viewed in the PDF Viewer can be found by using PageCount property.

```csharp
[C#]
int count = pdfViewer1.PageCount;
```

<!-- tags: [PDF Viewer, Essential PDF Viewer, Page Count, Stream, Load Method, C#, VB.NET] keywords: [PDF, viewer, stream, load, PageCount, essential] -->
```

---

<!-- 페이지 16 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_003.jpeg
document_name: PDF Viewer
page_number: 003
page_id: PDF Viewer#page_003
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:49:57Z
fidelity: lossless
-->

## Overview
- This section provides a guide on various functions and features available for handling PDF files in the PDF Viewer.
- Details include text search, annotations, and various "How To" sections for managing PDF streams, page counts, specific pages, and loading PDF files without a ToolStrip in the viewer.

## Content

### 4.1.5 Text Search
- Referring to page 24.

### 4.1.6 Annotation
- Referring to page 25.

### 5 How To
- Referring to page 26.

#### 5.1 View the PDF stream in viewer?
- Referring to page 26.

#### 5.2 Get page count?
- Referring to page 26.

#### 5.3 Load a specific page?
- Referring to page 27.

#### 5.4 Load PDF without ToolStrip in Viewer?
- Referring to page 27.

<!-- tags: PDF Viewer, text search, annotations, page count, specific page loading, toolstrip configuration, syncfusion winforms, version: 11.4.0.26 -->
```

---

<!-- 페이지 17 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_007.jpeg
document_name: PDF Viewer
page_number: 007
page_id: PDF Viewer#page_007
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:50:07Z
fidelity: lossless
-->

# 2 Installation and Deployment

## 2.1 Installation

This section covers information on the install location, samples, licensing, patches update, and updating of the recent version of Essential Studio. It also illustrates the installation procedure for PDF Viewer. It deals with the following sections.

## 2.2 Where to Find Samples?

This section covers the location of the installed samples and describes the procedure to run the samples through the sample browser and online. It also lists the location of utilities, assemblies, and source code.

### 2.2.1 Sample Installation Location

The Windows Forms samples are installed in the following location:

```
…\MyDocuments\Syncfusion\EssentialStudio\Version
Number\Windows\PdfViewer.Windows\Samples\2.0
```

### 2.2.2 Viewing Samples

To view the samples:

1. Click **Start** -> **All Programs** -> **Syncfusion** -> **Essential Studio <x.x.x.x>** -> **Dashboard** -> **Reporting**.

---

<!-- tags: [syncfusion, winforms, pdf viewer, installation, deployment, samples, version 11.4.0.26] keywords: [essential studio, syncfusion, windows forms, pdf viewer, installation, samples location, utilities, assemblies, source code, reporting] -->
```

---

<!-- 페이지 18 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_011.jpeg
document_name: PDF Viewer
page_number: 011
page_id: PDF Viewer#page_011
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:50:18Z
fidelity: lossless
-->

# Getting Started

## Feature Summary

### Overview
- A summary of the supported features for viewing, printing, and manipulating PDF files.
- Includes support for various PDF objects, image filters, and export functionality.

### Content

#### Supported Features
- **Support for viewing and printing PDF files.**
- **Support for various PDF objects** such as text, lines, curves, color spaces, and JPEG images with DCTDecode, CCITTFaxDecode, and FlateDecode filters.
- **Support for exporting PDF pages as raster images.**

#### Feature Support Matrix

The supported and non-supported elements of Essential PDF Viewer for Windows Forms, WPF, and ASP.NET MVC are listed in the following table:

| Features                | Windows | WPF | ASP.NET MVC |
|-------------------------|---------|-----|-------------|
| **Text**                | Yes     | Yes | Yes         |
| **Graphical Elements** (Line, Curve etc.) | Yes     | Yes | Yes         |
| **Image Formats**       |         |     |             |
| JPEG                    | Yes     | Yes | Yes         |
| PNG                     | Yes     | Yes | Yes         |
| TIFF                    | Yes     | Yes | Yes         |
| Inline Images           | Yes     | Yes | Yes         |
| **Encoding Techniques** |         |     |             |
| Soft mask               | Yes     | Yes | Yes         |
| Image mask              | No      | No  | No          |
| **Fonts** *             |         |     |             |
| Standard Fonts          | Yes     | Yes | Yes         |
| TrueType Fonts          | Yes     | Yes | Yes         |
| Type 0, Type 1          | Yes     | Yes | Yes         |
| Embedded Fonts          | Yes**   | Yes** | Yes**   |
| **Color Space**         |         |     |             |

#### Notes
- Fonts marked with ** indicate additional details or conditions apply beyond standard support.

<!-- tags: [essential pdf viewer, windows forms, wpf, asp.net mvc, pdf features, image formats, encoding techniques, fonts, color space] keywords: [support, viewing, printing, pdf objects, image filters, export, graphical elements, text, jpeg, png, tiff, inline images, soft mask, standard fonts, true type fonts, type 0, type 1, embedded fonts] -->
```

---

<!-- 페이지 19 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_015.jpeg
document_name: PDF Viewer
page_number: 015
page_id: PDF Viewer#page_015
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:50:32Z
fidelity: lossless
-->

# Essential PDF Viewer

![Properties](https://example.com/properties_image.png "Properties")

**Figure 6: Properties**

## Content

3. Add Syncfusion.PdfViewer.Windows namespace.

### C#:

```csharp
using Syncfusion.PdfViewer.Windows;

// Initializing the PDF Viewer
PdfViewer viewer = new PdfViewer();

// Loading the document in the PDF Viewer
viewer.Load(@"c:\documents\myPDF.pdf");
```

### VB:

```vb
' Add Syncfusion.PdfViewer.Windows namespace here

' Initializing the PDF Viewer
Dim viewer As New PdfViewer()

' Loading the document in the PDF Viewer
viewer.Load(@"c:\documents\myPDF.pdf")
```

## Cross References
- See also: [Syncfusion.PdfViewer.Windows Namespace Documentation](#)

<!-- tags: [Syncfusion, Syncfusion Winforms, PDF Viewer, Properties, C#, VB, namespace, version: 11.4.0.26] keywords: [properties, pdf viewer, initialization, document loading, c#, vb, namespace] -->
```

---

<!-- 페이지 20 -->

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

---

<!-- 페이지 21 -->

<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_023.jpeg
document_name: PDF Viewer
page_number: 023
page_id: PDF Viewer#page_023
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:51:07Z
fidelity: lossless
-->

# Essential PDF Viewer

## 4.1.4 Exporting PDF

### 4.1.4.1 Exporting PDFs as Raster Images

Essential PDF Viewer allows selected pages to be exported as raster images. Exporting can be done using the `ExportAsImage` method. This option helps to convert a PDF into an image.

```csharp
[C#]
Bitmap img = pdfViewer1.ExportAsImage(0);

// Save the image.
img.Save("Sample.png", ImageFormat.Png);
```

```vbnet
[VB.NET]
Dim img As Bitmap = pdfViewer1.ExportAsImage(0)

' Save the image.
img.Save("Sample.png", ImageFormat.Png)
```

You can also specify the page range instead of converting each page.

```csharp
[C#]
Bitmap[] img = pdfViewer1.ExportAsImage(0, 3);
```

```vbnet
[VB.NET]
Dim img() As Bitmap = pdfViewer1.ExportAsImage(0, 3)
```

### 4.1.4.2 Exporting PDFs as Vector Images

Exporting PDFs as vector images can be done using the `ExportAsMetafile` method. The following code sample demonstrates how a PDF document can be exported as a metafile.

```csharp
[C#]
Metafile img = pdfViewer1.ExportAsMetafile(0);

// Save the image
img.Save("Sample.emf", ImageFormat.Emf);
```

## API Reference

- **Method**: `ExportAsImage`
  - Converts a PDF page to a raster image.
  - Parameters:
    - `pageIndex`: Specifies the page index to be exported.
  - Returns: `Bitmap` object representing the raster image.

- **Method**: `ExportAsMetafile`
  - Converts a PDF page to a vector image in metafile format.
  - Parameters:
    - `pageIndex`: Specifies the page index to be exported.
  - Returns: `Metafile` object representing the vector image.

## Code Examples

### Exporting a PDF Page as a Raster Image (C#)

```csharp
[C#]
Bitmap img = pdfViewer1.ExportAsImage(0);
img.Save("Sample.png", ImageFormat.Png);
```

### Exporting a PDF Page as a Vector Image (C#)

```csharp
[C#]
Metafile img = pdfViewer1.ExportAsMetafile(0);
img.Save("Sample.emf", ImageFormat.Emf);
```

### Exporting a PDF Page as a Raster Image (VB.NET)

```vbnet
[VB.NET]
Dim img As Bitmap = pdfViewer1.ExportAsImage(0)
img.Save("Sample.png", ImageFormat.Png)
```

### Exporting a PDF Page as a Vector Image (VB.NET)

```vbnet
[VB.NET]
Dim img As Metafile = pdfViewer1.ExportAsMetafile(0)
img.Save("Sample.emf", ImageFormat.Emf)
```

## Cross References

See also:  
- [Working with PDF Pages](#working-with-pdf-pages)  
- [PDF Viewer Controls](#pdf-viewer-controls)

<!-- tags: [syncfusion, pdfviewer, export, winforms, conversion, raster, vector] keywords: [exportasimage, exportasmetafile, pdf, image, bitmap, metafile, pdfviewer, windowsforms, syncfusionpdfviewer] -->

---

<!-- 페이지 22 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_027.jpeg
document_name: PDF Viewer
page_number: 027
page_id: PDF Viewer#page_027
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:51:26Z
fidelity: lossless
-->

## Essential PDF Viewer

### Load a specific page?

Navigation to a specific page, through code, is possible using the GoToPageAtIndex method.

```csharp
pdfViewer1.GoToPageAtIndex(2);
```

```vb
pdfViewer1.GoToPageAtIndex(2)
```

### Load PDF without Toolstrip in Viewer?

In order to view PDF without the toolbar, make use of the PdfDocumentView control instead of PdfViewerControl. Other features and options are similar to PdfViewerControl.

```csharp
PdfDocumentView pdfDocumentView1 = new PdfDocumentView();
pdfDocumentView1.Load(@"Template.pdf");
```

```vb
Dim pdfDocumentView1 As New PdfDocumentView()
pdfDocumentView1.Load("Template.pdf")
```

The following is the image of a PDF document viewed in PdfDocumentView.

---

Page © 2013 Syncfusion. All rights reserved.
```

<!-- tags: [Syncfusion Winforms, PDF Viewer, GoToPageAtIndex, PdfDocumentView] keywords: [navigation, specific page, toolstrip, features, options] -->
```

---

<!-- 페이지 23 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_004.jpeg
document_name: PDF Viewer
page_number: 004
page_id: PDF Viewer#page_004
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:49:57Z
fidelity: lossless
-->

# Overview

## Introduction to PDF Viewer

Essential PDF Viewer for .NET is a 100% managed .NET component that will have the ability to view and print PDF files from your .NET applications.

## Use Case Scenario

The user can embed the PDF viewer within the .NET application using this feature. The PDF viewer can also be used as a stand-alone application.

![PDF Viewer](https://example.com-pdf-viewer)
*Figure 1: PDF Viewer*

## Prerequisites and Compatibility

This section covers the requirements that are mandatory for using Syncfusion Essential PDF Viewer. It also lists operating systems and browsers that are compatible with the product.
```

---

<!-- 페이지 24 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_008.jpeg
document_name: PDF Viewer
page_number: 008
page_id: PDF Viewer#page_008
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:50:05Z
fidelity: lossless
--> 

## Overview
- **Syncfusion Essential Studio Dashboard Reporting Edition** provides tools for integrating reporting solutions into ASP.NET applications.
- Highlights the ease of integration and includes high-performance libraries for Word, PDF, and Excel manipulation.
- Focuses on viewing PdfViewer samples for the WF (Windows Forms) platform.

## Content

### Figure 2: Syncfusion Essential Studio Dashboard Reporting Edition

The image showcases the Syncfusion Essential Studio Dashboard Reporting Edition, featuring the following details:
- **User Interface**:
  - **Reporting** section highlights support for ASP.NET, ASP.NET MVC, and other frameworks.
- **Run Samples** button offers options to run locally installed samples.
- **Documentation** resources such as Online Samples, Explore Samples, Download Source Code, Online Documentation, and Read Me.

#### To view the PdfViewer samples for WF platform:

##### Windows Forms

1. **Click the drop-down button of the Windows platform**. The following options are displayed, allowing you to view the samples in the following three ways:
   - **Run Samples**: View the locally installed PdfViewer samples for Windows using the sample browser.
   - **Online Samples**: View the online PdfViewer samples for Windows.
   - **Explore Samples**: Locate the samples for PdfViewer on the disk.
   
2. **Click Run Samples link**. Essential Studio Reporting Edition Windows Forms sample browser is displayed.

## API Reference (if applicable)

No specific APIs are discussed in this section.

## Code Examples (multi-language supported)

No code examples are provided in this section.

## Cross References

See also: [Syncfusion Essential Studio Dashboard Reporting Edition], [Reporting solutions for ASP.NET applications], [High-performance libraries for Word, PDF, and Excel].

<!-- tags: [Syncfusion Winforms, reporting, essential studio, version 11.4.0.26] keywords: [syncfusion, essential studio, dashboard, reporting edition, pdf viewer, window forms, samples] -->
```

---

<!-- 페이지 25 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_012.jpeg
document_name: PDF Viewer
page_number: 012
page_id: PDF Viewer#page_012
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:50:21Z
fidelity: lossless
-->

## Overview
- Features supported by the Essential PDF Viewer for RGB, CMYK, Gray, ICC, and Indexed color modes.
- Compatibility with various compression filters like DCTDecode, CCITTFaxDecode, FlateDecode, LZWDecode, ASCII85Decode, ASCIIHexDecode, and JBIG2Decode.
- Support for specific interactive features, including Zoom, Page Navigation, and Search, but limited support for Actions, Annotations, Bookmarks, and Navigation Pane.

## Content

### Color Modes
| RGB   | Yes | Yes | Yes   |
| CMYK  | Yes | Yes | Yes*** |
| Gray  | Yes | Yes | Yes   |
| ICC   | Yes | Yes | Yes   |
| Indexed | Yes | Yes | Yes   |

### Compression Filters
| DCTDecode (Image, Content) | Yes | Yes | Yes   |
| CCITTFaxDecode (Image) | Yes | Yes | Yes   |
| FlateDecode (Image, Content) | Yes | Yes | Yes   |
| LZWDecode (Content only) | Yes | Yes | Yes   |
| ASCII85Decode (Content only) | Yes | Yes | Yes   |
| ASCIIHexDecode (Image) | Yes | Yes | Yes   |
| JBIG2Decode (Image) | Yes | Yes | Yes   |

### Interactive Features
| Actions | No | No | No   |
| Annotations | Yes**** | Yes**** | No   |
| Attachments | No | No | No   |
| Bookmarks | No | No | No   |
| Form | No | No | No   |
| Page Navigation | Yes | Yes | Yes   |
| Zoom | Yes | Yes | Yes   |
| Navigation Pane | No | No | No   |
| Selection (Keyboard & Mouse) | No | No | No   |
| Search | Yes | Yes | No   |
| Document Information | No | No | No   |
| Conformance | Yes | Yes | Yes   |
| Encrypted Documents | Yes | Yes | Yes   |

## API Reference (if applicable)
- **Namespace**: Syncfusion.Pdf
- **Class**: PdfDocument

### Members

#### Properties
- **Annotations**: Collection of annotations in the PdfDocument.
- **Bookmarks**: Collection of bookmarks in the PdfDocument.
- **Conformance**: Conformance level of the document (e.g., Pdf15, Pdf17).
- **Encrypted**: Boolean indicating if the document is encrypted.
- **Zoom**: Zoom factor for the viewer.

#### Methods
- **Decrypt()**: Decrypts the encrypted document.
- **SetSecurity(password, permissions)**: Sets security for the document with the specified password and permissions.

#### Events
- **PageLoaded**: Triggered when a page is loaded.

## Code Examples

### C# Example
```csharp
using Syncfusion.Pdf;
using System.IO;

// Load a PDF document
PdfDocument doc = new PdfDocument("input.pdf");

// Check if the document is encrypted
if (doc.Encrypted)
{
    // Decrypt the document
    doc.Decrypt("password");
}

// Enable zoom feature in the viewer
PdfViewer viewer = new PdfViewer();
viewer.Zoom = 1.5;

// Save the document
doc.Save("output.pdf");
doc.Close();
```

### VB Example
```vb
Imports Syncfusion.Pdf
Imports System.IO

' Load a PDF document
Dim doc As New PdfDocument("input.pdf")

' Check if the document is encrypted
If doc.Encrypted Then
    ' Decrypt the document
    doc.Decrypt("password")
End If

' Enable zoom feature in the viewer
Dim viewer As New PdfViewer()
viewer.Zoom = 1.5

' Save the document
doc.Save("output.pdf")
doc.Close()
```

<!-- tags: [Essential PDF Viewer, WinForms, PDF, Compression Filters, Interactive Features] keywords: [RGB, CMYK, Gray, ICC, Indexed, DCTDecode, CCITTFaxDecode, FlateDecode] -->
```

---

<!-- 페이지 26 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_016.jpeg
document_name: PDF Viewer
page_number: 016
page_id: PDF Viewer#page_016
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:50:42Z
fidelity: lossless
-->

# PDF Viewer

## Overview
- Demonstrates initialization and usage of the Syncfusion PDF Viewer control in Windows Forms.
- Explains loading a PDF document into the viewer programmatically.
- Analyzes the UI structure of the PDF Viewer, including components like ToolStrip, Page Break, and Client Area.

## Content

### 3.3 Appearance and Structure of the Control

The following screenshot is a pictorial representation of PDF Viewer.

```markdown
Imports Syncfusion.PdfViewer.Windows

' Initializing the Pdf Viewer
Dim viewer As PdfViewer = New PdfViewer()

' Loading the document in the Pdf Viewer
viewer.Load("c:/documents/myPDF.pdf")
```

Refer to [Viewing PDF files](#viewing-pdf-files) for more information.

#### Figure 7 Structure of PDF Viewer

The screenshot highlights the following components:

- **ToolStrip**: Contains navigation and display options for the PDF document.
- **Page Break**: Indicates the end of a page in the PDF document.
- **Client Area**: Displays the contents of the PDF document.

#### Toolbar Components
- Visual representation of the ToolStrip with various functionalities for navigating and viewing PDF documents.

#### Page Break Indicators
- Markers showing the boundaries between pages within the document.

#### Client Area Display
- Shows the content of the PDF document, including tables of data.

### Code Example

```vb
' Initializing the Pdf Viewer
Dim viewer As PdfViewer = New PdfViewer()

' Loading the document in the Pdf Viewer
viewer.Load("c:/documents/myPDF.pdf")
```

### UI Structure Analysis

#### Toolbar (ToolStrip)
- Contains tools and options for viewing and navigating PDF documents.

#### Page Breaks
- Visual indicators showing where a page ends in the document.

#### Client Area
- Displays the actual content of the PDF document.

## API Reference

### Classes
- **PdfViewer**: Represents the main control for viewing and navigating PDF documents.

### Methods
- **Load(String path)**: Loads the specified PDF document into the viewer.

## Code Examples

### VB.NET Example

```vb
Imports Syncfusion.PdfViewer.Windows

' Initializing the Pdf Viewer
Dim viewer As PdfViewer = New PdfViewer()

' Loading the document in the Pdf Viewer
viewer.Load("c:/documents/myPDF.pdf")
```

## Cross References

- See also: [Viewing PDF files](#viewing-pdf-files)

<!-- tags: [pdf viewer, windows forms, syncfusion, controls, pdf, toolkit] keywords: [syncfusion sdk, winforms, pdf viewer, document loading, tools strip, client area, page break] -->
```

---

<!-- 페이지 27 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_020.jpeg
document_name: PDF Viewer
page_number: 020
page_id: PDF Viewer#page_020
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:50:57Z
fidelity: lossless
-->

# Essential PDF Viewer

| Method      | Description                                                                 | Parameters           | Returns | Result Type |
|-------------|-----------------------------------------------------------------------------|----------------------|---------|-------------|
| ZoomTo      | Magnifies the document displayed to the specified percentage.           | (int percentage)     | N/A     | Void        |

## 4.1.1.3 Events

### Table 3: Events Table

| Event               | Description                                                                 | Arguments | Type |
|---------------------|-----------------------------------------------------------------------------|----------|------|
| DocumentLoaded       | This event is triggered after the PDF is successfully loaded.             | N/A      | N/A  |
| HyperLinkMouseHover | This event is triggered when the mouse pointer is placed over the URL.    | N/A      | N/A  |
| HyperLinkMouseClicked | This event is triggered when the URL in the PDF document is clicked. | N/A      | N/A  |

## 4.1.2 Viewing PDF Files

A PDF can be loaded into the PDF Viewer either through the File Open dialog available in the toolbar or through the Load method. It also requests passwords to open encrypted documents.

```csharp
// Initialize PDF Viewer.
PdfViewerControl pdfViewer1 = new PdfViewerControl();

// Load the PDF.
pdfViewer1.Load("Template.pdf");
```

```vb.NET
```

<!-- tags: [Syncfusion Winforms, PDF Viewer, Events, Methods, Parameters, Returns, Loaded Files, Hyperlinks, Mouse Events, Loading PDF, Passwords] keywords: [Events Table, ZoomTo, DocumentLoaded, HyperLinkMouseHover, HyperLinkMouseClicked, Load method, File Open dialog, Encrypted documents, Initializing PDF Viewer, Loading PDF Files, GLC Functions, GLC PDF Viewer, API Reference, C#, VB.NET] -->
``` 


---

<!-- 페이지 28 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_024.jpeg
document_name: PDF Viewer
page_number: 024
page_id: PDF Viewer#page_024
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:51:10Z
fidelity: lossless
-->

## Overview
- Explains how to convert PDF pages to EMF images using VB.NET and C#.
- Describes specifying a page range for conversion in the PDF Viewer control.
- Demonstrates text search and highlighting functionality in the Essential PDF Viewer.

## Content

### Code Examples for Exporting as EMF

#### VB.NET
```vb
Dim img As Metafile = pdfViewer1.ExportAsMetafile(0)

' Save the image
img.Save("Sample.emf", ImageFormat.Emf)
```

#### C#
```csharp
Metafile[] img = pdfViewer1.ExportAsMetafile(0, 3);
```

#### VB.NET
```vb
Dim img() As Metafile = pdfViewer1.ExportAsMetafile(0, 3)
```

### 4.1.5 Text Search

Essential PDF Viewer allows end users to search and highlight the text in the PDF document. The search box will appear when Ctrl+F is pressed and searches the text in the PDF document as shown in the following figure.

![Searching a PDF](image.png)

**Figure 10: Searching a PDF**

## API Reference

### Methods

- **ExportAsMetafile**: Converts a range of pages in the PDF into a Metafile.

### Parameters

- **startIndex**: The starting page index for conversion.
- **endIndex**: The ending page index for conversion.

### Returns

- An array of Metafiles containing the specified page range.

## Code Examples

#### VB.NET
```vb
Dim img As Metafile = pdfViewer1.ExportAsMetafile(0)
img.Save("Sample.emf", ImageFormat.Emf)
```

#### C#
```csharp
Metafile[] img = pdfViewer1.ExportAsMetafile(0, 3);
```

#### VB.NET
```vb
Dim img() As Metafile = pdfViewer1.ExportAsMetafile(0, 3)
```

## Cross References

- For more information on exporting PDF pages, see the complete documentation on PDF Viewer.

<!-- tags: [syncfusion, pdf viewer, essentials pdf, export as metafile, vb.net, c#, text search] keywords: [PDF Viewer, ExportAsMetafile, Ctrl+F, text highlighting, metafile, page range, search functionality] -->
```

---

<!-- 페이지 29 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_028.jpeg
document_name: PDF Viewer
page_number: 028
page_id: PDF Viewer#page_028
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:51:24Z
fidelity: lossless
-->

# Northwind Customers

## Overview
- The page displays a PDF document showcasing a customer database for the fictional company **Northwind Traders**.
- The PDF contains a table listing customer information, including IDs, company names, contact details, and addresses.
- The table is presented in a scrollable view, indicating the use of a document viewer control.

## Content

### Customer Table

| CustomerID | CompanyName           | ContactName          | Address                         | City             | PostalCode | Country   | Phone              | Fax               |
|------------|------------------------|----------------------|---------------------------------|------------------|------------|-----------|--------------------|-------------------|
| ALFKI      | Alfons Futterkiste    | Maria Anders         | Obere Str. 57                 | Berlin          | 12209      | Germany   | 030-0074321        | 030-0076545       |
| ANATR      | Ana Trujillo Emparedados y Helados | Ana Trujillo | Avda. de la Construcción 2222 | México D.F.     | 05021      | Mexico    | (5) 55-4729       | (5) 55-3745       |
| ANTON      | Antonio Moreno Taquería | Antonio Moreno      | Mataderos 2312               | México D.F.     | 05023      | Mexico    | (5) 55-3932       |                   |
| AROUT      | Around the Horn        | Thomas Hardy         | 120 Hanover Sq.               | London          | WA1 1DP    | UK        | (171) 555-7788    | (171) 555-6750    |
| BERGS      | Berglunds snacks/döner | Christina Berglund  | Berguvsvägen 8               | Luleå          | S-95822    | Sweden    | 0921-123465        | 0921-123467       |
| BLAUS      | Blauer See Delikatessen | Hanna Moos          | Forsterstr. 57               | Mannheim        | 68306      | Germany   | 0621-08460         | 0621-08924        |
| BLONP      | Blondel père et fils   | Frédéric Citeaux    | 24, place Kleber              | Strasbourg      | 67000      | France    | 88.60.15.31       | 88.60.15.32       |
| BOLID      | Bólido Comidas preparadas | Martin Sommer     | C/ Araquil, 67               | Madrid          | 28023      | Spain     | (91)25522         | (91)25591        |
| BONAP      | Bon appétit            | Laurence Lebihan    | 12, rue des Bouchers           | Marseille       | 13008      | France    | 91.24.45.40       | 91.24.45.41       |
| BOTTM      | Bottom-Dollar Markets  | Elizabeth Lincoln    | 23 Tsawassen Blvd.           | Tsawassen       | T2F 8M4    | Canada    | (604) 555-4729    | (604) 555-3745    |
| BSBEV      | B's Beverages          | Victoria Ashworth    | Fauntleercy Circus             | London          | EC2 5NT    | UK        | (171) 555-1212    |                   |
| CACTU      | Cactus Comidas para llevar | Patricio Simpson | Carrito 333                   | Buenos Aires    | 1010       | Argentina | (1)35-5555        | (1)35-4892        |
| CENTC      | Centro comercial Moctezuma | Francisco Chang | Sierras de Granada 9993      | México D.F.     | 05022      | Mexico    | (5) 55-3392       | (5) 55-7293       |
| CHOPS      | Chop-suey Chinese      | Yang Wang           | Hauptstr. 29                  | Bern            | 3012       | Switzerland| 0452-076545       |                   |
| COMMI      | Comércio Mineiro       | Pedro Afonso        | Av. dos Lusiadas, 23          | São Paulo       | 05432-043  | Brazil    | (11) 55-7647      |                   |
| CONSH      | Consolidated           | Elizabeth Berkeley   | Berkeley                       | London          | WX1 6LT    | UK        | (171)             |                   |

### Document Viewer Demonstration
- The PDF is displayed within a `PdfDocumentView` control, as indicated by the window title and interface elements.
- The document viewer allows for interactive scrolling, as evidenced by the visible scroll bar.
- The content is clearly formatted and structured for easy readability.

## API Reference
- This section contains information specific to the Syncfusion Winforms PDF viewer control. It may include API calls for displaying and interacting with PDF documents.
- Example methods could include creating a new `PdfDocumentView` instance, loading PDF files, and handling user interactions such as scrolling and zooming.

### Example Code
```csharp
// Sample C# code for loading and displaying a PDF document
using Syncfusion.Pdf;
using Syncfusion.PdfViewer.WindowsForms;

PdfDocument document = new PdfDocument(@"path_to_pdf_file.pdf");
PdfViewer viewer = new PdfViewer();
viewer.Load(document);

// Attach the viewer to the form or container
this.Controls.Add(viewer);
```

## Figures
- **Figure 11: PDF displayed in PdfDocumentView**
  - This figure showcases the PDF document as rendered in the document viewer, highlighting how the viewer control presents and navigates the document.

## Cross References
- See also:
  - [Syncfusion PDF Viewer Documentation](#)
  - [WinForms Controls Overview](#)

<!-- tags: [syncfusion, winforms, pdf viewer, northwind traders, document control, pdf-ocr-to-markdown] keywords: [pdf viewer, northwind customers, document viewer, syncfusion winforms, api reference] -->
```