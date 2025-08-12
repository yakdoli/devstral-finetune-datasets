```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_035.jpeg
document_name: pdf
page_number: 035
page_id: pdf#page_035
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:26:01Z
fidelity: lossless
-->

# Essential PDF

## Overview
- This section demonstrates the creation of a new PDF document and the addition of a page with the text "Hello World."

## Content

### Creating a New PDF Document

#### C#
```csharp
// Create a new PDF document. This object represents the PDF document.  
// This document has one page, by default. Additional pages have to be added.  
PdfDocument pdfDoc = new PdfDocument();
```

#### VB.NET
```vbnet
' Create a new PDF document. This object represents the PDF document.  
' This document has one page, by default. Additional pages have to be added.  
Dim pdfDoc As Syncfusion.Pdf.PdfDocument = New Syncfusion.Pdf.PdfDocument()
```

**\[i]** The PDF document represents the document that is created in the memory. It is only the memory representation of the PDF document that is written to the disk.

- A new PDF document is created.

### Adding a New Page to the Document

#### C#
```csharp
// Add a page to the document  
PdfPage page = doc.Pages.Add();
```

#### VB.NET
```vbnet
' Add a page to the document  
Dim firstPage As Syncfusion.Pdf.PdfPage = doc.Pages.Add()
```

- A PDF page is added to the document (doc).

### Writing the String "Hello World" on the First Page

2. Write the string "Hello World" on the first page in the PDF document. This task is further subdivided into the following tasks:
   - Create the font object to be used for writing the "Hello World" string. You can set the font size and style in the same statement.
   - Write the text using the `DrawString` method of the Graphics object.

#### C#
```csharp
// Create the font object to be used for writing the "Hello World" string. You can set the font size and style in the same statement.  
// Write the text using the DrawString method of the Graphics object.  
```

## API Reference

### Namespaces and Classes
- `Syncfusion.Pdf.PdfDocument`
- `Syncfusion.Pdf.PdfPage`
- `Syncfusion.Pdf.Graphics`

### Methods
- `PdfDocument()`  
  Initializes a new instance of the `PdfDocument` class.
- `PdfDocument.Pages.Add()`  
  Adds a new page to the document.
- `Graphics.DrawString()`  
  Writes text using the specified font and drawing parameters.

### Parameters
- `string`  
  The text to be written.
- `Font`  
  The font to be used for writing the text.
- `Brush`  
  The brush that defines the characteristics of the text.

### Returns
- `PdfPage`  
  Returns the newly added page.
- `void`  
  Returns nothing when writing the text.

## Code Examples

#### C#
```csharp
PdfDocument pdfDoc = new PdfDocument();
PdfPage page = pdfDoc.Pages.Add();

// Create font and brush objects  
Font font = new Font("Arial", 14, FontStyle.Regular);  
SolidBrush brush = new SolidBrush(Color.Black);

// Create graphics object from the page  
Graphics graphics = page.Graphics;

// Draw string on the page  
// graphics.DrawString("Hello World", font, brush, new PointF(100, 100)); // Insert actual DrawString call
```

#### VB.NET
```vbnet
Dim pdfDoc As New PdfDocument()
Dim firstPage As PdfPage = pdfDoc.Pages.Add()

' Create font and brush objects  
Dim font As New Font("Arial", 14, FontStyle.Regular)  
Dim brush As New SolidBrush(Color.Black)

' Create graphics object from the page  
Dim graphics As Graphics = firstPage.Graphics

' Draw string on the page  
' graphics.DrawString("Hello World", font, brush, New PointF(100, 100)) ' Insert actual DrawString call
```

## Cross References
- For more information on working with fonts and rendering text, refer to the section on "PDF Text Rendering."

### Tags and Keywords
```markdown
<!-- tags: Essential PDF, Syncfusion Winforms, PdfDocument, PdfPage, Graphics, DrawString keywords: Create PDF, Add Page, Write Text, Font, Brush, DrawString, Graphics -->
```
```