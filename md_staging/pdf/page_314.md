<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_314.jpeg
document_name: pdf
page_number: 314
page_id: pdf#page_314
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:44:15Z
fidelity: lossless
-->

# Essential PDF

## Overview

- Illustrates how to get the form field with the given field name using code examples in C# and VB.NET.
- Highlights the `TryGetValue` method for retrieving field values.

## Content

### Getting the Form Field

The following code example demonstrates how to get the form field with the given field name.

#### C#

```csharp
// Load the document.
PdfLoadedDocument doc = new PdfLoadedDocument(@"..\..\Data\Form.pdf");
// Load the form from the loaded document.
PdfLoadedForm form = doc.Form;
// Load the form field collections from the form.
PdfLoadedFormFieldCollection field = new PdfLoadedFormFieldCollection(form);
PdfLoadedField m_field = null;
string fieldValue = string.Empty;
// TryGetField Method.
if (field.TryGetField("f1-1", out m_field))
{
    (m_field as PdfLoadedTextBoxField).Text = "1";
}
```

#### VB.NET

```vb
' Load the document.
Dim doc As New PdfLoadedDocument("..\..\Data\Form.pdf")
' Load the form from the loaded document.
Dim form As PdfLoadedForm = doc.Form
' Load the form field collections from the form.
Dim field As New PdfLoadedFormFieldCollection(form)
Dim m_field As PdfLoadedField = Nothing
Dim fieldValue As String = String.Empty
' TryGetField Method.
If field.TryGetField("f1-1", m_field) Then
    TryCast(m_field, PdfLoadedTextBoxField).Text = "1"
End If
```

### TryGetValue

**TryGetValue:**

Loaded field from the `PdfLoadedFormFieldCollection` provides the `TryGetValue` method to obtain the field values. It is used to get the field value from the given field name. It specifies whether the particular field returns true or false value.

**Example:** For a check box field, it returns a value whether it is checked or not.

## Page-level Navigation/TOC (if applicable)
- Getting the Form Field
- TryGetValue

## Cross References
- See also: Form field manipulation, document loading, form retrieval, field collections

<!-- tags: [pdf, form manipulation, trygetfield, windowsforms, syncfusion] keywords: [pdfdocument, formfield, trygetfield, form retrieval, check box, document loading] -->