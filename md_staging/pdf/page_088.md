```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_088.jpeg
document_name: pdf
page_number: 088
page_id: pdf#page_088
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:28:52Z
fidelity: lossless
-->

## Essential PDF

### Composite Field Example

```csharp
PdfPage page = document.Pages.Add();
compositeField.Draw(page.Graphics);
}
```

#### [VB.NET]

```vbnet
Dim document As PdfDocument = New PdfDocument()
Dim page As PdfPage = document.Pages.Add()

Dim font As PdfFont = New PdfStandardFont(PdfFontFamily.Helvetica, 12.0F)
Dim brush As PdfBrush = PdfBrushes.Black

Dim compositeField As PdfCompositeField = New PdfCompositeField(font, brush)

For i As Integer = 0 To 49
    Dim page As PdfPage = document.Pages.Add()
    compositeField.Draw(page.Graphics)
Next i
```

When an automatic field is used as a component of the composite field, it is not necessary to specify its Font, Brush and Bounds properties. Just call its constructor without parameters.

### Note: You must specify the preceding properties for the composite field.

The following code example illustrates how to use automatic fields in templates.

#### [C#]

```csharp
PdfDocument document = new PdfDocument();
PdfPage page = document.Pages.Add();

PdfFont font = new PdfStandardFont(PdfFontFamily.Helvetica, 12f);
PdfBrush brush = PdfBrushes.Black;

PdfTemplate template = new PdfTemplate(15, 15);

PdfDateTimeField dateField = new PdfDateTimeField(font, brush);
dateField.DateFormatString = "dd/'MMMM'/'yyyy";

dateField.Draw(template.Graphics);

for (int i = 0; i < 50; i++)
{
```

## API Reference (if applicable)

### WinForms-specific Conventions
- Control names, namespaces, and types are preserved exactly (e.g., Syncfusion.Windows.Forms.Tools.TabControlAdv, Syncfusion.Windows.Forms.Grid).

## Code Examples

#### C# Example
- The example demonstrates creating a composite field and specifying its properties such as font and brush.

#### VB.NET Example
- The example shows how to iterate through multiple pages and apply a composite field to each page.

## RAG Annotations

<!-- tags: [Essential PDF, Composite Field, Automatic Field, WinForms, VB.NET, C#] keywords: [PdfDocument, PdfPage, PdfCompositeField, PdfStandardFont, PdfBrush, PdfTemplate, PdfDateTimeField, DateFormatString, Font, Brush, Bounds, Template] -->
```