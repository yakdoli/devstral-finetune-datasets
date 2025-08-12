```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_295.jpeg
document_name: pdf
page_number: 295
page_id: pdf#page_295
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:43:54Z
fidelity: lossless
-->

# Essential PDF

```csharp
Dim textField As PdfTextBoxField = New PdfTextBoxField(page, "textBox")
textField.Bounds = New RectangleF(0, 0, 100, 100)
textField.Text = "New text field"
form.Fields.Add(textField)

ldDoc.Save(newFileName)
ldDoc.Close()
```

## Flattening

The library enables to flatten the loaded field by using the Flatten property of the PdfLoadedField class. A particular field or the whole form can be flattened using this class. The following code snippet illustrates this.

### [C#]

```csharp
// For Whole form flattening
PdfLoadedDocument ldDoc = new PdfLoadedDocument(filename);
PdfLoadedForm form = ldDoc.Form;
form.Flatten = true;
ldDoc.Save(newFileName);
ldDoc.Close();

// Flattening the first field
form.Fields[0].Flatten = true;
```

### [VB.NET]

```vb
' For Whole form flattening
Dim ldDoc As New PdfLoadedDocument(filename)
Dim form As PdfLoadedForm = ldDoc.Form
form.Flatten = True
ldDoc.Save(newFileName)
ldDoc.Close()

' Flattening the first field
form.Fields(0).Flatten = True
```

## Disable AutoFormat

This property allows you to disable the formatting applied to form fields. Formats can be disabled for either selected fields or for the complete form.

## Use Case Scenarios

<!-- tags: [product, module, control, api, version?] keywords: [flattening, disable autoformat, pdf, form fields, text box, disable formatting, format, field, whole form] -->
```