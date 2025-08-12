```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_299.jpeg
document_name: pdf
page_number: 299
page_id: pdf#page_299
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:44:06Z
fidelity: lossless
-->


## Overview
- Enables adding a Print Button to the form.
- Clicking the print button initializes a print dialog.
- Demonstrated through code examples.

## Content

### Adding a Submit Button and Submit Action

#### C#

```csharp
// Create submit button to transfer the values in the form
PdfButtonField submitButton = new PdfButtonField(page, "submitButton");
submitButton.Bounds = new RectangleF(100, 420, 90, 20);
submitButton.Font = font;
submitButton.Text = "Submit";

// Assigning the submit action
submitButton.Actions.MouseUp = submitAction;

// Adding the Field
loadedDoc.Form.Fields.Add(submitButton);
```

#### VB.NET

```vb
' Creating a Button
Dim button As PdfButtonField = New PdfButtonField(page, "Click")
button.Bounds = New RectangleF(0, 420, 90, 20)
button.Text = "Click"
loadedDoc.Form.Fields.Add(button)

' Creating Submit action button
Dim submitAction As PdfSubmitAction = New PdfSubmitAction("http://stevex.net/dump.php")
submitAction.DataFormat = SubmitDataFormat.Html

' Create submit button to transfer the values in the form
Dim submitButton As PdfButtonField = New PdfButtonField(page, "submitButton")
submitButton.Bounds = New RectangleF(100, 420, 90, 20)
submitButton.Font = font
submitButton.Text = "Submit"

' Assigning the submit action
submitButton.Actions.MouseUp = submitAction

' Adding the Field
loadedDoc.Form.Fields.Add(submitButton)
```

### Adding a Print Button

#### C#

```csharp
// Create a print button
```

---

## Page-level Navigation/TOC (if applicable)

## Cross References

## API Reference (if applicable)

## Code Examples (multi-language supported)

### Adding a Print Button Example (C#)

```csharp
// Create a print button
```

### Adding a Print Button Example (VB.NET)

```vb
' Create a print button
```

---

<!-- tags: [syncfusion, winforms, pdfbuttonfield, printdialog, submitaction, formfield, codeexample] keywords: [submit button, submit action, print button, pdf, buttonfield, print dialog, winforms application, pdflibrary] -->
```