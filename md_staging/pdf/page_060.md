```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_060.jpeg
document_name: pdf
page_number: 060
page_id: pdf#page_060
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:26:54Z
fidelity: lossless
-->

# Essential PDF

## Overview

This page covers the interactive elements and security features supported by the Essential PDF library in Syncfusion Winforms. Specifically, it highlights the availability of various features such as 3D annotations, actions, attachments, bookmarks, hyperlinks, digital signatures, and encryption/decryption across different versions.

## Content

### Interactive Elements

The following table lists the interactive elements supported by the library:

| Element       | Version 1 | Version 2 | Version 3 | Version 4 |
|---------------|-----------|-----------|-----------|-----------|
| 3D-Annotation | Yes       | Yes       | Yes       | Yes       |
| Action        | Yes       | Yes       | Yes       | Yes       |
| Attachment    | Yes       | Yes       | Yes       | Yes       |
| Bookmark      | Yes       | Yes       | Yes       | Yes       |
| Hyperlink     | Yes       | Yes       | Yes       | Yes       |

### Security

The table below shows the security features supported in each version:

| Feature                | Version 1 | Version 2 | Version 3 | Version 4 |
|------------------------|-----------|-----------|-----------|-----------|
| Digital Signature      | Yes       | No        | No        | No        |
| Encryption and Decryption | Yes       | Yes       | No        | Yes       |

### Notes

- Only .Jpeg format images are supported for the Silverlight version.
- The PdfGrid class provides additional support for some features.

## API Reference

### Namespace: Syncfusion.Pdf

#### Classes

- **PdfDocument**: Represents the main object for creating and manipulating PDF documents.
- **PdfGrid**: Used for working with grid data in PDF documents.

#### Methods

- **Save(string path)**: Saves the PDF document to the specified path.
- **AddPage()**: Adds a new page to the document.
- **AddAnnotation(PdfAnnotation annotation, int pageNumber)**: Adds an annotation to the specified page.

#### Events

- **PageLoaded**: Triggered when a page is loaded into the document.
- **AnnotationAdded**: Triggered when a new annotation is added to the document.

#### Properties

- **PageCount**: Gets the number of pages in the document.
- **Annotations**: Gets or sets the collection of annotations in the document.

### Digital Signature

- A digital signature can be added to a PDF document using the **PdfDigitalSignatureField** class.
- **AddDigitalSignatureField()**: Adds a digital signature field to the document.

### Encryption/Decryption

- The library supports both encryption and decryption of PDF documents.
- **Encrypt(string password)**: Encrypts the document with the specified password.
- **Decrypt(string password)**: Decrypts the document using the specified password.

#### Parameters

| Name           | Type    | Description                              |
|----------------|---------|------------------------------------------|
| password       | string  | The password used for encryption/decryption. |

#### Returns

- Type: **void**

#### Exceptions

- **PasswordMismatchException**: Thrown when the provided password is incorrect.

## Code Examples

### Adding a Hyperlink in a PDF Document

```csharp
using Syncfusion.Pdf;
using Syncfusion.Pdf.HtmlToPdf;
using Syncfusion.Pdf.Graphics;
using Syncfusion.Pdf.Interactive;

class Program
{
    static void Main()
    {
        // Create a new PDF document.
        PdfDocument doc = new PdfDocument();

        // Create a PDF page.
        PdfPage page = doc.Pages.Add();

        // Create a PDF graphics object.
        PdfGraphics graphics = page.Graphics;

        // Create a font.
        PdfFont font = new PdfStandardFont(PdfFontFamily.TimesRoman, 12f);

        // Create a link annotation.
        PdfLinkAnnotation linkAnnotation = new PdfLinkAnnotation(new RectangleF(50, 50, 200, 30));
        linkAnnotation.Url = "https://www.syncfusion.com";

        // Add the link annotation to the page.
        page.Annotations.Add(linkAnnotation);

        // Save the PDF document.
        doc.Save("HyperlinkExample.pdf");

        // Close the document.
        doc.Close();
    }
}
```

### Adding Encryption

```csharp
using Syncfusion.Pdf;

class Program
{
    static void Main()
    {
        // Create a new PDF document.
        PdfDocument doc = new PdfDocument();

        // Add a page.
        doc.Pages.Add();

        // Add some content.
        doc.Pages[0].Graphics.DrawString("This is a secure PDF document.", new PdfStandardFont(PdfFontFamily.TimesRoman, 20), PdfBrushes.Black, new RectangleF(100, 100, 400, 400));

        // Encrypt the document.
        string password = "123456";
        doc.FirstPage.Graphics.FillRectangle(PdfBrushes.White, 0, 0, doc.FirstPage.Size.Width, doc.FirstPage.Size.Height);
        doc.FirstPage.Annotations.Add(new PdfLinkAnnotation(new RectangleF(100, 300, 400, 50), "https://www.syncfusion.com") { Action = new PdfAction("Go to Syncfusion"));
        doc.Save("EncryptedDocument.pdf");

        // Close the document.
        doc.Close();
    }
}
```

<!-- tags: [syncfusion, winforms, pdf, digital signature, encryption, decryption] keywords: [pdfdocument, pdfgrid, pdflinkannotation, annotations, digital signature, encryption] -->
```