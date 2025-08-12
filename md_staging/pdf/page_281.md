```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_281.jpeg
document_name: pdf
page_number: 281
page_id: pdf#page_281
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:40:53Z
fidelity: lossless
-->

# Essential PDF

## Overview
- Learn how to create booklets with margins using specified overloads.
- Understand the process of loading, specifying margins, creating booklets, and saving the document in both C# and VB.NET.

## Content

### Booklet Creation Methods

The following methods are available for creating booklets:

```plaintext
CreateBooklet(String, String, SizeF)
CreateBooklet(PdfLoadedDocument, SizeF, Boolean, PdfMargins)
CreateBooklet(String, String, SizeF, Boolean)
```

### Applying Margins to Booklets

You can also apply margins to the booklets at the time of creating the booklet by using one of the preceding overloads.

### Example: Creating a Booklet with Margins

The following code example illustrates how to create a booklet with the following overload: **CreateBooklet(PdfLoadedDocument, SizeF, Boolean, PdfMargins)**.

#### C# Example

```csharp
// Load a PDF document.
PdfLoadedDocument ldoc = new PdfLoadedDocument("SamplePDF.pdf");

// Specify the margin.
PdfMargins margin = new PdfMargins();
margin.All = 10;

// Create booklet with two sides.
PdfDocument doc = PdfBookletCreator.CreateBooklet(ldoc, new SizeF(500, 500), true, margin);

// Save the document.
doc.Save("Sample.pdf");
```

#### VB.NET Example

```vb
' Load a PDF document.
Dim ldoc As PdfLoadedDocument = New PdfLoadedDocument("SamplePDF.pdf")

' Specify the margin.
Dim margin As PdfMargins = New PdfMargins()
margin.All = 10

' Create booklet with two sides.
Dim doc As PdfDocument = PdfBookletCreator.CreateBooklet(ldoc, New SizeF(500, 500), True, margin)

' Save the document.
doc.Save("Sample.pdf")
```

## API Reference

### Methods

- **CreateBooklet(String, String, SizeF)**: Creates a booklet from a PDF file with the specified dimensions.
- **CreateBooklet(PdfLoadedDocument, SizeF, Boolean, PdfMargins)**: Creates a booklet from a loaded PDF document with specified dimensions, binding orientation, and margins.
- **CreateBooklet(String, String, SizeF, Boolean)**: Creates a booklet from a PDF file with specified dimensions and binding orientation.

#### Parameters

- **String**: The file path of the PDF to load.
- **PdfLoadedDocument**: A loaded PDF document.
- **SizeF**: The size of each page in the booklet.
- **Boolean**: A flag indicating whether the booklet has a two-side binding (True) or single-side binding.
- **PdfMargins**: An object representing the margins to be applied to the booklet.

#### Return Type

- **PdfDocument**: A new PDF document object representing the created booklet.

### Exceptions

- Thrown if the input PDF file is invalid or inaccessible.
- Thrown if the provided dimensions are invalid.
- Thrown if the margin settings are not applied correctly.

## Code Examples

### Full Example in C#

```csharp
using Syncfusion.Pdf.Conversion;
using Syncfusion.Pdf.Interactive;
using Syncfusion.Pdf;

// Load a PDF document.
PdfLoadedDocument ldoc = new PdfLoadedDocument("SamplePDF.pdf");

// Specify the margin.
PdfMargins margin = new PdfMargins();
margin.All = 10;

// Create booklet with two sides.
PdfDocument doc = PdfBookletCreator.CreateBooklet(ldoc, new SizeF(500, 500), true, margin);

// Save the document.
doc.Save("BookletOutput.pdf");
doc.Close(true);
```

### Full Example in VB.NET

```vb
Imports Syncfusion.Pdf.Conversion
Imports Syncfusion.Pdf.Interactive
Imports Syncfusion.Pdf

' Load a PDF document.
Dim ldoc As PdfLoadedDocument = New PdfLoadedDocument("SamplePDF.pdf")

' Specify the margin.
Dim margin As PdfMargins = New PdfMargins()
margin.All = 10

' Create booklet with two sides.
Dim doc As PdfDocument = PdfBookletCreator.CreateBooklet(ldoc, New SizeF(500, 500), True, margin)

' Save the document.
doc.Save("BookletOutput.pdf")
doc.Close(True)
```

## Cross References

Refer to the documentation on [PdfBookletCreator](#pdfbookletcreator) for more detailed information.

<!-- tags: [pdf, booklet, margins, pdfloadeddocument, syncfusion winforms] keywords: [Syncfusion, WinForms, PDF, Booklet, Margins, Overloads, C#, VB.NET] -->
```