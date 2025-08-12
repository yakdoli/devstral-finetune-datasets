```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_296.jpeg
document_name: pdf
page_number: 296
page_id: pdf#page_296
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:41:55Z
fidelity: lossless
-->

# Essential PDF

## Overview
- This property helps when filling fields in different cultures.
- A currency text field might accept numbers in various formats based on the culture in use.
- If the culture affects other inputs, the property ensures formatting consistency.

## Content

### Adding Disable AutoFormat to an Application

Adding the Disable AutoFormat feature to the application is described in the following code snippets:

```csharp
[C#]
// Disable format for the selected field
PdfLoadedTextField field = loadedDocument.Form.Fields["Price"] as PdfLoadedTextField;
field.Text = "$1,000.23";
field.DisableFormat = true;

// Disable format for all fields in the form
loadedDocument.Form.DisableFormat = true;
```

```vb
[VB]
' Disable format for the selected field
Dim field As PdfLoadedTextField = TryCast(loadedDocument.Form.Fields("Price"), PdfLoadedTextField)
field.Text = "$1,000.23"
field.DisableFormat = True

' Disable format for all fields in the form
loadedDocument.Form.DisableFormat = True
```

**Note**: XFA Form is currently supported with the following limitations:
- User rights will not be preserved.
- Only XFA static forms are supported.

### Modifying loaded form actions

Essential PDF provides support for modifying the various actions of the loaded forms. The following code example illustrates this.

```csharp
[C#]
```

## Page-level Navigation/TOC (if applicable)

* **Adding Disable AutoFormat to an Application**
* **Modifying loaded form actions**

<!-- tags: [Essential PDF, Disable AutoFormat, XFA Form] keywords: [culture, input formatting, currency text field, form fields, XFA static forms, user rights, modifying actions, loaded forms] -->
```