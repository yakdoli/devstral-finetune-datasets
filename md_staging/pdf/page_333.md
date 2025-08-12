```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_333.jpeg
document_name: pdf
page_number: 333
page_id: pdf#page_333
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:44:27Z
fidelity: lossless
-->

# Essential PDF

## Convert Methods

### Overview

- Converts XPS documents into PDF format using three overloaded `Convert` methods.

### Content

#### Convert Methods

The `Convert` method in the `Essential PDF` library supports three different input formats for converting XPS documents into PDF:

```vb
[VB.NET]
public PdfDocument Convert(byte[] file)
public PdfDocument Convert(String fileName)
public PdfDocument Convert(Stream file)
```

#### Converting XPS to PDF

An XPS document can be converted to PDF using the following code snippet:

```csharp
[C#]
// Create converter class.
XPSToPdfConverter converter = new XPSToPdfConverter();

// Convert the XPS to PDF
PdfDocument document = converter.Convert(fileName);

// Save and close the document
document.Save("Sample.pdf");
document.Close(true);
```

```vb
[VB.NET]
' Create converter class.
Dim converter As New XPSToPdfConverter()

' Convert the XPS to PDF
Dim document As PdfDocument = converter.Convert(fileName)

' Save and close the document
document.Save("Sample.pdf")
document.Close(True)
```

### Supported Elements

The following table shows the supported elements for conversion:

| **Element** | **Convert to PDF** |
|-------------|---------------------|
| Element     | Convert to PDF     |

## API Reference

#### `public PdfDocument Convert(byte[] file)`

Converts an XPS document from a byte array into a PDF document.

#### `public PdfDocument Convert(String fileName)`

Converts an XPS document from a file specified by its file path into a PDF document.

#### `public PdfDocument Convert(Stream file)`

Converts an XPS document from a stream into a PDF document.

### Code Examples

#### C#

```csharp
XPSToPdfConverter converter = new XPSToPdfConverter();
PdfDocument document = converter.Convert("Sample.xps");
document.Save("Sample.pdf");
document.Close(true);
```

#### VB.NET

```vb
Dim converter As New XPSToPdfConverter()
Dim document As PdfDocument = converter.Convert("Sample.xps")
document.Save("Sample.pdf")
document.Close(True)
```

<!-- tags: [syncfusion, winforms, essential pdf, xps, pdf, conversion, api, 11.4.0.26] keywords: [convert, xps, pdf, document, byte array, file name, stream, save, close] -->
```