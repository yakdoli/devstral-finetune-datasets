```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_293.jpeg
document_name: pdf
page_number: 293
page_id: pdf#page_293
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:41:40Z
fidelity: lossless
-->

# Essential PDF

## 4.3.1 Overview

- AcroForms are PDF files that contain form fields, allowing data entry by the end-user or the author.
- Internally, AcroForms are annotations applied to a PDF document and are loaded if available when opening an existing document.

### Creating Form

- The loaded form is represented by the `PdfLoadedForm` class, accessed via the `Form` property of `PdfLoadedDocument`.
- If no AcroForm exists, you can create it using the `CreateForm` method of `PdfLoadedDocument`.

The following code example illustrates this.

#### C#

```csharp
// Loading Existing Document
PdfLoadedDocument loadedDoc = new PdfLoadedDocument(filename);

// Creates a form
loadedDoc.CreateForm();

// Adding a new Page
PdfPageBase page = loadedDoc.Pages.Add();

// Creating a new Field
PdfButtonField bt = new PdfButtonField(page, "Submit");
bt.Bounds = new RectangleF(0, 0, 100, 100);
bt.Text = "Submit";

// Adding the Field
loadedDoc.Form.Fields.Add(bt);
```

#### VB

```vb
' Loading Existing Document
Dim loadedDoc As PdfLoadedDocument = New PdfLoadedDocument(filename)

' Creates a form
loadedDoc.CreateForm()

' Adding a new Page
```

## API Reference (if applicable)

- None provided on this page.

## Code Examples

- C# and VB examples provided above.

## See also

- None provided on this page.

<!-- tags: [product, module, control, api, version?] keywords: [Form, AcroForm, PdfLoadedDocument, PdfLoadedForm, CreateForm, Form Fields, PDF] -->
```