```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_294.jpeg
document_name: pdf
page_number: 294
page_id: pdf#page_294
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:42:54Z
fidelity: lossless
-->

## Essential PDF

```vb
Dim page As PdfPageBase = loadedDoc.Pages.Add()

' Creating a new Field
Dim bt As PdfButtonField = New PdfButtonField(page, "Submit")
bt.Bounds = New RectangleF(0, 0, 100, 100)
bt.Text = "Submit"

' Adding the Field
loadedDoc.Form.Fields.Add(bt)
```

### Accessing Form

**PdfLoadedForm** class contains the collection of loaded fields represented by the **PdfLoadedFormFieldCollection** class, and inherited from the **PdfFieldCollection** class. The base class for each loaded field is represented by the **PdfLoadedField** class, and inherited from the **PdfField** class.

You can change the form's properties, add new fields or remove the existing fields.

The following code example illustrates how to use a loaded form.

#### [C#]

```csharp
PdfLoadedDocument ldDoc = new PdfLoadedDocument(filename);

PdfLoadedForm form = ldDoc.Form;
PdfPage page = ldDoc.Pages.Add() as PdfPage;

PdfTextBoxField textField = new PdfTextBoxField(page, "textBox");
textField.Bounds = new RectangleF(0, 0, 100, 100);
textField.Text = "New text field";
form.Fields.Add(textField);

ldDoc.Save(newFileName);
ldDoc.Close();
```

#### [VB]
```vb
Dim ldDoc As PdfLoadedDocument = New PdfLoadedDocument(filename)

Dim form As PdfLoadedForm = ldDoc.Form
Dim page As PdfPage = TryCast(ldDoc.Pages.Add(), PdfPage)
```

## API Reference (if applicable)

<!-- tags: [product, pdf, form, field, document] keywords: [pdfloadedform, pdfloadedformfieldcollection, pdfloadedfield, pdfbuttonfield, pdfloadeddocument] -->
```