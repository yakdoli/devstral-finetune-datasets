```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_307.jpeg
document_name: pdf
page_number: 307
page_id: pdf#page_307
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:44:39Z
fidelity: lossless
-->

## Essential PDF

### Overview
- Retrieves bounds and value of a field.
- Modifies field location, size, and value.
- Allows getting or setting additional properties.

### Content

```vb
Dim field As PdfLoadedTextBoxField = form.Fields["fieldname"] as PdfLoadedTextBoxField
Dim field As PdfLoadedTextBoxField = form.Fields( 0 ) as PdfLoadedTextBoxField
```

### WinForms-specific Features

Essential PDF enables retrieving the bounds and value of a field, changing its location and size, and modifying its value. Also, it can get or set additional properties.

#### Example: Changing Field Bounds and Value

```csharp
PdfLoadedDocument ldDoc = new PdfLoadedDocument(filename);
PdfLoadedForm form = ldDoc.Form;

PdfLoadedTextBoxField ldField = form.Fields[ 0 ] as PdfLoadedTextBoxField;

RectangleF newBounds = new RectangleF( 100, 100, 50, 50 );

ldField.Bounds = newBounds;
ldField.SpellCheck = true;
ldField.Text = "New text of the field.";
ldField.Password = false;

ldDoc.Save( newFileName );
ldDoc.Close();
```

```vb
Dim ldDoc As PdfLoadedDocument = New PdfLoadedDocument(filename)
Dim form As PdfLoadedForm = ldDoc.Form

Dim ldField As PdfLoadedTextBoxField = form.Fields( 0 ) as PdfLoadedTextBoxField

Dim NewBounds As RectangleF = New RectangleF(100, 100, 50, 50)

ldField.Bounds = NewBounds
ldField.SpellCheck = True
ldField.Text = "New text of the field."
ldField.Password = False

ldDoc.Save(NewFileName)
```

### API Reference

The code demonstrates modifying a field's properties and saving the changes.

### Summarized Steps

1. Load the document and form.
2. Access a specific field.
3. Modify bounds, spell check, text, and password settings.
4. Save and close the document.

## Page-level Navigation/TOC
- [Unclear]

<!-- tags: [pdf, fields, modifications, bounds, spell check, text] keywords: [Essential PDF, fields, bounds, spellCheck, text, password] -->
```