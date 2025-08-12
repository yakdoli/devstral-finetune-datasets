```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_315.jpeg
document_name: pdf
page_number: 315
page_id: pdf#page_315
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:45:16Z
fidelity: lossless
-->

# Essential PDF

## Overview
- Explains how to use the `TryGetValue` method to retrieve form field values from a PDF document.
- Demonstrates `C#` and `VB.NET` code examples to illustrate the functionality.
- Provides an example of updating a form field based on its retrieved value.

## Content

### Syntax
#### C#
```csharp
public bool TryGetValue(string fieldName, out string fieldValue)
```

#### VB.NET
```vbnet
Public Function TryGetValue(fieldName As String, ByRef fieldValue As String) As Boolean
```

### Example
The following code example illustrates how to get the form field with the given field name.

#### C#
```csharp
// Load the document.
PdfLoadedDocument doc = new PdfLoadedDocument(@"Form.pdf");
// Load the form from the loaded document.
PdfLoadedForm form = doc.Form;
// Load the form field collections from the form.
PdfLoadedFormFieldCollection field = new
    PdfLoadedFormFieldCollection(form);
PdfLoadedField m_field = null;
string fieldValue = string.Empty;
// TryGetValue Method.
if (field.TryGetValue("fl-2", out fieldValue) && fieldValue == "")
{
    (form.Fields["fl-2"] as PdfLoadedTextBoxField).Text = "2";
}
```

#### VB.NET
```vbnet
' Load the document.
Dim doc As New PdfLoadedDocument("Form.pdf")
' Load the form from the loaded document.
Dim form As PdfLoadedForm = doc.Form
' Load the form field collections from the form.
Dim field As New PdfLoadedFormFieldCollection(Form)
Dim m_field As PdfLoadedField = Nothing
Dim fieldValue As String = String.Empty
```

## API Reference
### `TryGetValue` Method
- **Parameters**:
  - `fieldName`: The name of the form field to retrieve.
  - `fieldValue`: The output parameter to hold the retrieved value.
- **Returns**: `bool`, indicating whether the retrieval was successful.
- **Description**: Attempts to retrieve the value of the specified form field. If successful, the value is stored in `fieldValue`, and the method returns `true`. Otherwise, it returns `false`.

## Code Examples
The provided examples demonstrate the usage of the `TryGetValue` method in both `C#` and `VB.NET` to interact with PDF form fields.

## See also
- [Syncfusion Winforms Documentation](https://www.syncfusion.com/documentation/windows-forms)
- [Essential PDF API Reference](https://www.syncfusion.com/documentation/e-pdf/api)

<!-- tags: [Syncfusion, Winforms, PDF, TryGetValue, API, 11.4.0.26] keywords: [Syncfusion Winforms, C#, VB.NET, PDF, TryGetValue, form field, document] -->
```