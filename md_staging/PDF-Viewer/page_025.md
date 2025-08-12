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