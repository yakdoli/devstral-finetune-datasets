```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_312.jpeg
document_name: pdf
page_number: 312
page_id: pdf#page_312
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:43:01Z
fidelity: lossless
-->

## Essential PDF

```csharp
loadField.Checked = true;
```

### [VB.NET]

' Fill check box
```vbnet
Dim loadField As PdfLoadedCheckBoxField = form.Fields(4) as PdfLoadedCheckBoxField
```

' Check the first item in the checkbox group
```vbnet
loadField.Items(0).Checked = True
```

' Check the checkbox if it is not grouped.
```vbnet
loadField.Checked = True
```

### Filling the Signature Field

The following code illustrates how to fill the Signature Field.

#### [C#]

```csharp
PdfLoadedSignatureField sigField = ldoc.Form.Fields[0] as PdfLoadedSignatureField;
sigField.Signature = new PdfSignature();
sigField.Signature.Certificate = certificate;
sigField.Signature.Reason = "Reason";
```

#### [VB.NET]

```vbnet
Dim sigField As PdfLoadedSignatureField = TryCast(ldoc.Form.Fields(0), PdfLoadedSignatureField)
sigField.Signature = New PdfSignature()
sigField.Signature.Certificate = certificate
sigField.Signature.Reason = "Reason"
```

### Enumerating and Filling Fields

You can also enumerate the fields and fill them. The following code example illustrates how to enumerate the text fields.

#### [C#]

```csharp
PdfLoadedForm form = doc.Form;
PdfLoadedFormFieldCollection fields = form.Fields;
for (i = 0; i < doc.Form.Fields.Count; i++)
```

---

<!-- tags: [Syncfusion, Winforms, PDF, SignatureField, CheckBoxField, EnumerateFields] keywords: [signature field, checkbox field, enumerate fields, fill fields, pdf form] -->
```