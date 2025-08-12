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