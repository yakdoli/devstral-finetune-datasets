```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_360.jpeg
document_name: pdf
page_number: 360
page_id: pdf#page_360
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:46:08Z
fidelity: lossless
-->

## Overview
- Demonstrates how to use page templates in PDF documents.
- Explains the use of the `MeasureString` method to determine text size.
- Provides examples in both C# and VB.NET.

## Content

### Creating a Page Template and Drawing a Table

PDFPageTemplateElement is used to create a template for the PDF page, where a table is drawn. The following code examples illustrate the process of creating a template, drawing a table, and placing the template at the top of the page.

```vb
'[VB.NET]
' Create page template
Dim top As PdfPageTemplateElement = New PdfPageTemplateElement(rect)

' Create a table
Dim table As PdfLightTable = New PdfLightTable()
table.DataSource = dataTable
table.Style.CellPadding = 16

' Draw the table in template
table.Draw(top.Graphics)

' Place the template at the top.
doc.Template.Top = top
```

### How To Measure the String Whose End Position Is Not Known?

#### Overview
PDFFont provides the `MeasureString` method, which calculates the rectangle that a string will occupy on a PDF page. This information is essential for relative positioning multiple paragraphs of text.

#### Implementation

The `MeasureString` method takes parameters such as the string, a formatting object, and the size of the rectangle. It returns a `SizeF` object representing the dimensions of the string. This is then used to draw the corresponding rectangle on the PDF.

##### VB.NET

```vb
' Create a font.
Dim font As PdfStandardFont = New PdfStandardFont(PdfFontFamily.Symbol, 12, PdfFontStyle.Bold)

' Measure the size of the text based on string format and font.
Dim textSize As SizeF = pdfFont.MeasureString(text, rect.Size, format)
```

##### C# 

```csharp
// Create a font.
PdfStandardFont font = new PdfStandardFont(PdfFontFamily.Symbol, 12, PdfFontStyle.Bold);

// Measure the size of the text based on string format and font.
SizeF textSize = pdfFont.MeasureString(text, rect.Size, format);

// Draw the rectangle for the size of the text.
page.Graphics.DrawRectangle(PdfPens.Red, new RectangleF(rect.Location, textSize));
```

The `MeasureString` method provides precise sizing that can be used to structure elements on the PDF page effectively.

### Related Information

- Refer to detailed documentation on `PdfStandardFont` and `MeasureString` for additional options and parameters.
- For more advanced use cases, explore Syncfusion PDF processing capabilities, such as layout management and text formatting.

---

<!-- tags: [syncfusion, pdf, document, template, measurement, table, fontsize] keywords: [MeasureString, PdfPageTemplateElement, PdfLightTable, PdfStandardFont, text positioning, document layout] -->
```