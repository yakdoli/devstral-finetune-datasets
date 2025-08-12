```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_262.jpeg
document_name: pdf
page_number: 262
page_id: pdf#page_262
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:41:04Z
fidelity: lossless
-->

# Essential PDF

## Overview
- Steps to create and manipulate PDF pages.
- Demonstrates adding a new page in a PDF document using C# and VB.NET.

## Content

### Adding a Page

1. **Call the `doc.Pages.Add` method.**
   This will create an empty page with the default parameters.

    **Note:** You can also specify the size and margins for the new page.

    The following code snippet illustrates how to create a new page in the PDF document.

    #### [C#]
    ```csharp
    PdfLoadedDocument lDoc = new PdfLoadedDocument(filename);
    page = lDoc.Pages.Add() as PdfPage;

    g = page.Graphics;
    text = "Page 2";
    g.DrawString(text, font, PdfBrushes.Black, PointF.Empty);

    filename = OutputPath + "AddNewPages.pdf";
    lDoc.Save(filename);
    lDoc.Close();
    ```

    #### [VB.NET]
    ```vb
    Dim lDoc As New PdfLoadedDocument(filename)
    page = TryCast(lDoc.Pages.Add(), PdfPage)

    g = page.Graphics
    text = "Page 2"
    g.DrawString(text, font, PdfBrushes.Black, PointF.Empty)

    filename = OutputPath + "AddNewPages.pdf"
    lDoc.Save(filename)
    lDoc.Close()
    ```

    **Note:** You can use the page’s `Graphics`, but should not use the graphics objects that require the page to layout.

    A new page is added to the PDF document.

### Removing a Page

## API Reference (if applicable)

## Code Examples (multi-language supported)

## Page-level Navigation/TOC (if applicable)

## Cross References

See also:
- Related section on manipulating PDF documents

## RAG Annotations

<!-- tags: [PDF, document manipulation, page addition, C#, VB.NET] keywords: [Syncfusion, PDF, add page, manipulate, graphics, documentation] -->
```