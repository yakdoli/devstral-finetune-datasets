```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_180.jpeg
document_name: pdf
page_number: 180
page_id: pdf#page_180
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:34:50Z
fidelity: lossless
-->

# Essential PDF

## Overview

- Explains how to create a file link annotation in a PDF document.
- Demonstrates embedding an external file using the `PdfFileLinkAnnotation` class.
- Introduces the concept of free text annotations and how they differ from standard annotations.

## Content

### File Link Annotation

```vb
Dim flAnnotation As New PdfFileLinkAnnotation(flAnnotationRectangle, filename)

' Add the Annotation to the page
Page.Annotations.Add(flAnnotation)
```

**Note:** Where `filename` = A string value specifying the full path of the file to be embedded.

#### Example for the Location of the External File

```vb
PdfFileLinkAnnotation fileLinkAnnotation = new PdfFileLinkAnnotation(fileLinkAnnotationRectangle, @"..\..\Common\Images\PDF\logo.png");
```

**Sample Location**

A sample which illustrates this feature is available in the following sample installation location:

```
<Install Location>\Windows\Pdf.Windows\Samples\2.0\User Interaction\Interactive Features
```

### Free Text Annotation

This feature enables the user to display the text directly on the page. Unlike an ordinary text annotation, a free text annotation has no open or closed state; the text is not displayed in the pop-up window. If the user wants to add a comment directly, without placing it in a pop-up window, `FreeTextAnnotation` can be used. Free Text Annotations can be included anywhere in the PDF Document by specifying the location and the CallOutLine points. While creating the project, the `Interactive` namespace has to be added in the project to enable this feature.

## Page-Level Navigation/TOC

- **4.1.3.2.3 Free Text Annotation**

## Cross References

- Refer to the previous section on file link annotations for embedding external files.
- Explore the samples provided in the installation location for practical demonstrations.

## RAG Annotations

<!-- tags: [pdf, annotation, file link, external file, free text annotation, interactive features] keywords: [PdfFileLinkAnnotation, FreeTextAnnotation, Interactive, embedding, file path, text display, pop-up window] -->
```