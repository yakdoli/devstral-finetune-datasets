```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_313.jpeg
document_name: pdf
page_number: 313
page_id: pdf#page_313
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:43:08Z
fidelity: lossless
-->

## Essential PDF

### Example Code

```csharp
{
    if (doc.Form.Fields[i] is PdfLoadedTextBoxField)
    {
        PdfLoadedTextBoxField textBox = (PdfLoadedTextBoxField)doc.Form.Fields[i];
        textBox.Text = "Text";
    }
}
```

```vbnet
[VB.NET]

Dim form As PdfLoadedForm = doc.Form

Dim fields As PdfLoadedFormFieldCollection = form.Fields

For i = 0 To doc.Form.Fields.Count - 1 Step i + 1
    If TypeOf doc.Form.Fields(i) Is PdfLoadedTextBoxField Then
        Dim textBox As PdfLoadedTextBoxField = CType(doc.Form.Fields(i), PdfLoadedTextBoxField)
        textBox.Text = "Text"
    End If
Next
```

### Form Fields

#### TryGetField:

Loaded field from the `PdfLoadedFormFieldCollection` provides the `TryGetField` method to obtain the form fields. It is used to get the field value from the given field name. It specifies whether the particular field is loaded or not by returning the boolean value.

#### Syntax:

```csharp
[C#]
public bool TryGetField(string fieldName, outPdfLoadedField field)
```

```vbnet
[VB.NET]
Public Function TryGetField(fieldName As String, ByRef field As PdfLoadedField) As Boolean
```

### Example:
```html
© 2013 Syncfusion. All rights reserved. 313 | Page
```
```