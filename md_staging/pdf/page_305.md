```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_305.jpeg
document_name: pdf
page_number: 305
page_id: pdf#page_305
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:42:26Z
fidelity: lossless
-->

## Overview

- Implements radio button groups in a PDF form.
- Manipulates signature fields and adds digital signatures to PDF documents.

## Content

### Creating Radio Button Groups

#### Code Example in C#

```csharp
//add the items to radio button group
employeesRadioList.Items.Add(radioItem1);
employeesRadioList.Items.Add(radioItem2);
```

#### Code Example in VB.NET

```vb
'[VB.NET]

'Create a Radio button
Dim employeesRadioList As PdfRadioButtonListField = New PdfRadioButtonListField(page, "employeesRadioList")
loadedDoc.Form.Fields.Add(employeesRadioList)

'Create radio button items
Dim radioItem1 As PdfRadioButtonListItem = New PdfRadioButtonListItem("1-9")
radioItem1.Bounds = New RectangleF(100, 140, 20, 20)
g.DrawString("1-9", font, brush, New RectangleF(150, 145, 180, 20))

Dim radioItem2 As PdfRadioButtonListItem = New PdfRadioButtonListItem("10-49")
radioItem2.Bounds = New RectangleF(100, 170, 20, 20)
g.DrawString("10-49", font, brush, New RectangleF(150, 175, 180, 20))

'add the items to radio button group
employeesRadioList.Items.Add(radioItem1)
employeesRadioList.Items.Add(radioItem2)
```

### Signature fields

A signature field is a form field that contains a digital signature. `PdfSignatureField` class is used to create signature fields in PDF forms. `PdfSignature` class enables to sign the signature field with the given certificate.

#### Code Example in C#

```csharp
[C#]

PdfSignatureField field = new PdfSignatureField(page, "Signature");
field.Bounds = new RectangleF(0, 0, 90, 20);
field.BackColor = new PdfColor(Color.Red);
field.BorderColor = new PdfColor(Color.Red);
field.Signature = new PdfSignature();
field.Signature.Certificate = certificate;
field.Signature.Reason = "Reason";
document.Form.Fields.Add(field);
```

#### Code Example in VB.NET

```vb
'[VB.NET]
```

## Page-level Navigation/TOC (if applicable)

- Creating Radio Button Groups
  - C# Code Example
  - VB.NET Code Example
- Signature fields
  - Overview of `PdfSignatureField`
  - Examples in C# and VB.NET

## Cross References

- See also: guide on form fields in PDFs, advanced PDF manipulation, certificate management.

<!-- tags: [Syncfusion, Winforms, PDF, form controls, digital signatures, radio buttons, C#, VB.NET] keywords: [PdfRadioButtonListField, PdfSignatureField, PdfSignature, certificate, digital signature] -->
```