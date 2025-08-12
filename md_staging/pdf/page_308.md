```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_308.jpeg
document_name: pdf
page_number: 308
page_id: pdf#page_308
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:42:49Z
fidelity: lossless
-->

# Essential PDF

## Content

### 4.3.3 Form Filling

Essential PDF provides support to fill AcroForm fields. You can fill the form field value either by using its field name or field index.

The following code example illustrates how to fill various loaded fields by using Essential PDF.

#### Filling the Text Box Field

The following code illustrates how to fill the Text Box Field.

##### Code Example in C#

```csharp
PdfLoadedTextBoxField ldField = form.Fields[0] as PdfLoadedTextBoxField;
RectangleF newBounds = new RectangleF(100, 100, 50, 50);
ldField.Bounds = newBounds;
ldField.SpellCheck = true;
ldField.Text = "New text of the field.";
ldField.Password = false;
ldField.BorderStyle = PdfBorderStyle.Dashed;
```

##### Code Example in VB.NET

```vbnet
Dim ldField As PdfLoadedTextBoxField = form.Fields(0) as PdfLoadedTextBoxField

Dim NewBounds As RectangleF = New RectangleF(100, 100, 50, 50)

ldField.Bounds = NewBounds
ldField.SpellCheck = True
ldField.Text = "New text of the field."
ldField.Password = False
ldField.BorderStyle = PdfBorderStyle.Dashed
```

#### Formatting the text box

The following table lists some of the properties of the `TextBoxField`.

<!-- tags: [form filling, acroform, text box field, pdf, essential pdf] keywords: [Essential PDF, form fields, AcroForm, Text Box Field, SpellCheck, Password, BorderStyle] -->
```