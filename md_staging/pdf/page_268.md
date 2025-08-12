```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_268.jpeg
document_name: pdf
page_number: 268
page_id: pdf#page_268
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:40:09Z
fidelity: lossless
-->

# Essential PDF

## Overview
- Demonstrates how to use automatic fields in PDF documents, specifically the `PdfPageCountField`, `PdfDateTimeField`, and `PdfPageNumberField` as components of a composite field.
- Shows the usage of automatic fields within templates for repetitive content.

## Content

### Example of Using Automatic Fields

The following example demonstrates creating a composite field using automatic fields such as page count, date-time, and page numbering.

```vb
'Create page count field
Dim count As New PdfPageCountField(font, PdfBrushes.Black)
Dim datetimefield As New PdfDateTimeField(font, PdfBrushes.Black)
Dim compositeField As New PdfCompositeField(font, PdfBrushes.Black, "{0} {1}{2}", pageNumber, count, datetimefield)
compositeField.Bounds = New RectangleF(0, 0, 250, 100)
compositeField.Draw(doc.Pages(0).Graphics, New PointF(0, 0))

Dim datefield As New PdfCreationDateField(font, PdfBrushes.Black)
```

When an automatic field is used as a component of the composite field, it is not necessary to specify its Font, Brush, and Bounds properties. Just call its constructor without parameters.

### Note: Necessary Properties for Composite Fields

```plaintext
Note: You must specify the preceding properties for the composite field.
```

### Using Automatic Fields in Templates

The following code example illustrates how to use automatic fields in templates.

#### C#

```csharp
PdfLoadedDocument doc = new PdfLoadedDocument(@"../../Sample.pdf");

PdfFont font = new PdfStandardFont(PdfFontFamily.Helvetica, 12f);
PdfBrush brush = PdfBrushes.Black;

PdfTemplate template = new PdfTemplate(15, 15);

PdfDateTimeField dateField = new PdfDateTimeField(font, brush);
dateField.DateFormatString = "dd/'MMMM '/'yyyy";

dateField.Draw(template.Graphics);

for (int i = 0; i < 50; i++)
{
    PdfPage page = document.Pages.Add();
    page.Graphics.DrawPdfTemplate(template, new Point(50, 50));
}
```

#### VB.NET

```vb
Dim doc As PdfLoadedDocument = New PdfLoadedDocument()

Dim font As PdfFont = New PdfStandardFont(PdfFontFamily.Helvetica, 12.0F)
```

## API Reference

### Members Used
- `PdfPageCountField`
- `PdfDateTimeField`
- `PdfPageNumberField`
- `PdfCompositeField`
- `PdfCreationDateField`
- `PdfTemplate`

### Methods Used
- `Draw(Graphics, PointF)`
- `Add()`
- `DrawPdfTemplate(PdfTemplate, Point)`

## Code Examples

### C# Example
```csharp
// C# example code for using automatic fields in templates
```

### VB.NET Example
```vb
' VB.NET example code for using automatic fields in templates
```

## Cross References
- See also: PDF manipulation, templates, and automatic fields in the PDF section of the Syncfusion Winforms documentation.

<!-- tags: [PDF, WinForms, automatic fields, composite field, template] keywords: [PdfPageCountField, PdfDateTimeField, PdfCompositeField, PdfTemplate, synchronize] -->
```