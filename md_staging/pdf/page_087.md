```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_087.jpeg
document_name: pdf
page_number: 087
page_id: pdf#page_087
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:29:33Z
fidelity: lossless
-->

# Essential PDF

```csharp
PdfDocument document = new PdfDocument();
PdfPage page = document.Pages.Add();

PdfFont font = new PdfStandardFont(PdfFontFamily.Helvetica, 12f);
PdfBrush brush = PdfBrushes.Black;

PdfPageNumberField pageNumber = new PdfPageNumberField(font, brush);

for (int i = 0; i < 50; i++)
{
    page = document.Pages.Add();
    pageNumber.Draw(page.Graphics);
}
```

```vb
Dim document As PdfDocument = New PdfDocument()
Dim page As PdfPage = document.Pages.Add()

Dim font As PdfFont = New PdfStandardFont(PdfFontFamily.Helvetica, 12.0F)
Dim brush As PdfBrush = PdfBrushes.Black

Dim pageNumber As PdfPageNumberField = New PdfPageNumberField(font, brush)

For i As Integer = 0 To 49
    page = document.Pages.Add()
    pageNumber.Draw(page.Graphics)
Next i
```

## The following code example illustrates how to use a composite field.

```csharp
[C#]

PdfDocument document = new PdfDocument();
PdfPage page = document.Pages.Add();

PdfFont font = new PdfStandardFont(PdfFontFamily.Helvetica, 12f);
PdfBrush brush = PdfBrushes.Black;

PdfCompositeField compositeField = new PdfCompositeField(font, brush);

for (int i = 0; i < 50; i++)
{
```

<!-- tags: [pdf, document, page, field, essential pd] keywords: [page number field, composite field, document pages, font, brush, pdf standard font, helvetica, black] -->
```