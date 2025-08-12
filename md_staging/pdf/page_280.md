```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_280.jpeg
document_name: pdf
page_number: 280
page_id: pdf#page_280
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:40:51Z
fidelity: lossless
-->

# Essential PDF

![Pages Printed and Folded into New Booklet](image.png)
*Figure 62: Pages Printed and Folded into New Booklet*

## Overview
- Illustrates the use of the `PdfBookletCreator` class for creating Booklets.
- Demonstrates the code example for creating Booklets using C# and VB.NET.
- Explains the overloads of the `CreateBooklet` method.

## Content

### Creating Booklets with PdfBookletCreator

The `PdfBookletCreator` class is used for creating Booklets. The following code example illustrates how to create the Booklet.

#### C#
```csharp
// Load a PDF document.
PdfLoadedDocument ldoc = new PdfLoadedDocument("SamplePDF.pdf");

// Create booklet with two sides.
PdfDocument doc = PdfBookletCreator.CreateBooklet(ldoc, new SizeF(500, 500), true);

// Save the document.
doc.Save("Sample.pdf");
```

#### VB.NET
```vbnet
' Load a PDF document.
Dim ldoc As PdfLoadedDocument = New PdfLoadedDocument("SamplePDF.pdf")

' Create booklet with two sides.
Dim doc As PdfDocument = PdfBookletCreator.CreateBooklet(ldoc, New SizeF(500, 500), True)

' Save the document.
doc.Save("Sample.pdf")
```

### Overloads of the CreateBooklet Method

The following code example illustrates the overloads of the `CreateBooklet` method.

#### C#
```csharp
CreateBooklet(PdfLoadedDocument, SizeF)
CreateBooklet(PdfLoadedDocument, SizeF, Boolean)
```

## API Reference

### Methods

- **CreateBooklet**
  - **Parameters:**
    - `PdfLoadedDocument`: The PDF document to be transformed into a booklet.
    - `SizeF`: The size of the booklet pages.
    - `Boolean`: Determines if the booklet should have two sides.

## Code Examples

The provided code examples demonstrate the usage of the `CreateBooklet` method in both C# and VB.NET. The method takes a `PdfLoadedDocument` object as input and generates a new `PdfDocument` object representing the booklet. The size of the booklet pages is specified using the `SizeF` structure. The `Boolean` parameter indicates whether the booklet should have two sides.

### C# Example
```csharp
// Load and create a booklet
PdfDocument booklet = PdfBookletCreator.CreateBooklet(pdfDocument, new SizeF(500, 500), true);
```

### VB.NET Example
```vbnet
' Load and create a booklet
Dim booklet As PdfDocument = PdfBookletCreator.CreateBooklet(pdfDocument, New SizeF(500, 500), True)
```

## RAG Annotations
<!-- tags: [pdf, booklet, pdf-booklet-creator, create-booklet, winforms, syncfusion-sdk] keywords: [create booklet, pdf document, booklet pages, size, two sides, overloads, pdfloadeddocument, sizef] -->
```