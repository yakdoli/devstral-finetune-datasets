```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_306.jpeg
document_name: pdf
page_number: 306
page_id: pdf#page_306
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:43:41Z
fidelity: lossless
-->

# Essential PDF

```vb
Dim field As New PdfSignatureField(page, "Signature")
field.Bounds = New RectangleF(0, 0, 90, 20)
field.BackColor = New PdfColor(Color.Red)
field.BorderColor = New PdfColor(Color.Red)
field.Signature = New PdfSignature()
field.Signature.Certificate = certificate
field.Signature.Reason = "Reason"
document.Form.Fields.Add(field)
```

**Note:** For more details on public members, see class reference documentation for pdf.

## Editing Form Fields

PdfLoadedForm class contains collection of loaded fields, represented by the PdfLoadedFormFieldCollection class, and inherited from the PdfFieldCollection class. The base class for each loaded field is represented by the PdfLoadedField class and inherited from the PdfField class.

The following loaded fields are supported in the library:

- Button fields
    - Push button field, represented by PdfLoadedButtonField class
    - Check Box field, represented by PdfLoadedCheckBoxField class
    - Radio button field, represented by PdfLoadedRadioButtonListField class
- Text fields
    - Text field, represented by PdfLoadedTextBoxField class
- Choice fields
    - List Box field, represented by PdfLoadedListBoxField class
    - Combo Box field, represented by PdfLoadedComboBoxField class
- Signature fields
    - Signature field, represented by PdfLoadedSignatureField class

You can access each field by using its index or field name. The following code example illustrates this.

### Example Code

```csharp
PdfLoadedTextBoxField field = form.Fields["fieldname"] as PdfLoadedTextBoxField;
PdfLoadedTextBoxField ldField = form.Fields[0] as PdfLoadedTextBoxField;
```

### VB.NET

```
[VB.NET]
```

## API Reference (if applicable)
### Namespaces
- ```
  """Namespace: Syncfusion.Pdf.InteractiveForm

### Classes
- ``` 
  """Class: PdfLoadedField
  """Class: PdfField
  """Class: PdfSignatureField

### Methods/Properties
- ``` 
  """Method: Add(field)
  """Property: Bounds
  """Property: BackColor
  """Property: BorderColor
  """Property: Certificate
  """Property: Reason

### Returns: 
- Type: void | object

### Exceptions: 
- None explicitly mentioned in the provided text.

## Code Examples (multi-language supported)

```vb
Dim field As New PdfSignatureField(page, "Signature")
field.Bounds = New RectangleF(0, 0, 90, 20)
field.BackColor = New PdfColor(Color.Red)
field.BorderColor = New PdfColor(Color.Red)
field.Signature = New PdfSignature()
field.Signature.Certificate = certificate
field.Signature.Reason = "Reason"
document.Form.Fields.Add(field)
```

### Example Code in C#

```csharp
PdfLoadedTextBoxField field = form.Fields["fieldname"] as PdfLoadedTextBoxField;
PdfLoadedTextBoxField ldField = form.Fields[0] as PdfLoadedTextBoxField;
```

## Page-level Navigation/TOC (if applicable)
- **Editing Form Fields**
    - Button Fields
    - Text Fields
    - Choice Fields
    - Signature Fields
- **Accessing Field by Index or Name**
    - Example Code

## Cross References
See also:
- PdfLoadedForm
- PdfFieldCollection
- PdfLoadedField
- PdfField
- PdfSignatureField

## RAG Annotations
<!-- tags: [product, module, control, api, version?] keywords: [k1, k2, ...] -->
<!-- tags: [syncfusion, winforms, pdf, essentialpdf, form fields] keywords: [pdfloadedform, pdffieldcollection, pdfloadedfield, pdfsignature, edit, access, field, button, text, choice, signature, example, code] -->
```