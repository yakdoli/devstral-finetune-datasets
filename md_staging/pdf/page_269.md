```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_269.jpeg
document_name: pdf
page_number: 269
page_id: pdf#page_269
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:40:07Z
fidelity: lossless
-->

## Essential PDF

### Overview
- Implements date fields and page labels in PDF documents.

### Content

Use the following code example to add a date field in a PDF document.

#### Code Example: Adding a Date Field

```vb
Dim brush As PdfBrush = PdfBrushes.Black

Dim template As PdfTemplate = New PdfTemplate(15, 15)

Dim dateField As PdfDateTimeField = New PdfDateTimeField(font, brush)
Dim dateFieldDateFormatString = "dd'/'MMMM'/'yyyy"

dateField.Draw(template.Graphics)

For i As Integer = 0 To 49
    Dim page As PdfPage = document.Pages.Add()
    page.Graphics.DrawPdfTemplate(template, New Point(50, 50))
Next i
```

#### PDF Page Label

A PdfPageLabel object specifies a new numbering range to be applied to the document sections. The following code example illustrates how to set the numbering range to the PDF document sections.

#### Code Example: Setting Page Label Numbering

```csharp
for (int k = 0, il = 0; k < ldoc.Section.Count; k++)
{
    PdfPageLabel label = new PdfPageLabel();
    label.StartNumber = 1;
    if (k == 0)
    {
        label.NumberStyle = PdfNumberStyle.Numeric;
    }
    else if (k == 1)
    {
        label.NumberStyle = PdfNumberStyle.LowerLatin;
    }
    else if (k == 2)
    {
        label.NumberStyle = PdfNumberStyle.UpperLatin;
    }

    label.Prefix = il + "-";
    ldoc.LoadedPageLabel = label;
    il++;
}
```

## API Reference

- **Classes**
  - `PdfPageLabel`
  - `PdfNumberStyle`
  - `PdfTemplate`
  - `PdfDateTimeField`
  - `PdfBrushes`

- **Methods**
  - `DrawPdfTemplate`
  - `Draw`

- **Properties**
  - `StartNumber`
  - `NumberStyle`
  - `Prefix`

- **Events**
  - None

## Code Examples (Previous)

#### Setting Page Label Numbering in C#

The code provided in the previous section demonstrates how to set different numbering styles for document sections.

## RAG Annotations

<!-- tags: [pdf, pdfpage, pagelabel, documentsection, numberstyle, datefield, codexamples] keywords: [PdfPageLabel, PdfNumberStyle, PdfTemplate, PdfDateTimeField, PdfBrushes, DrawPdfTemplate, StartNumber, NumberStyle, Prefix, documentsections, numberingrange, datefield] -->
```