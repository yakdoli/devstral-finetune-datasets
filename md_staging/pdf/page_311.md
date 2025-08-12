```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_311.jpeg
document_name: pdf
page_number: 311
page_id: pdf#page_311
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:44:53Z
fidelity: lossless
-->

# Essential PDF

## Overview
- Demonstrates how to fill radio button fields in a PDF form using Syncfusion PDF toolkit.
- Explains filling list box fields by selecting an index.
- Describes filling check box fields, handling grouped and ungrouped checkboxes.

## Content

### Filling the Radio Button Field

The following code illustrates how to fill the Radio Button Field.

```csharp
// Fill radio button
PdfLoadedRadioButtonListField radio = (PdfLoadedRadioButtonListField)doc.Form.Fields[2];
radio.SelectedIndex = 1;
```

```vbnet
' Fill radio button
Dim radio As PdfLoadedRadioButtonListField = CType(doc.Form.Fields(2), PdfLoadedRadioButtonListField)
radio.SelectedIndex = 1
```

### Filling the List Box Field

The following code illustrates how to fill the List Box Field.

```csharp
// fill list box
PdfLoadedListBoxField list = (PdfLoadedListBoxField)doc.Form.Fields[3];
list.SelectedIndex = 2;
```

```vbnet
' fill list box
Dim list As PdfLoadedListBoxField = CType(doc.Form.Fields(3), PdfLoadedListBoxField)
list.SelectedIndex = 2
```

### Filling the Check Box Field

The following code illustrates how to fill the Check Box Field.

```csharp
// Fill check box
PdfLoadedCheckBoxField loadField = form.Fields[4] as PdfLoadedCheckBoxField;

// Check the first item in the checkbox group
loadField.Items[0].Checked = true;

// check the checkbox if it is not grouped.
```

## API Reference (if applicable)

### Methods

- **PdfLoadedRadioButtonListField**: Represents a radio button list field in a PDF form.
- **PdfLoadedListBoxField**: Represents a list box field in a PDF form.
- **PdfLoadedCheckBoxField**: Represents a check box field in a PDF form.

### Properties

- **Form.Fields[index]**: Accesses fields within a PDF form by index.
- **SelectedIndex**: Sets or gets the selected index of a radio button list or list box field.
- **Items[0].Checked**: Sets the checked state of an individual checkbox in a check box group.

## Code Examples (multi-language supported)
### C#
```csharp
// Example to fill a radio button field
PdfLoadedRadioButtonListField radio = (PdfLoadedRadioButtonListField)doc.Form.Fields[2];
radio.SelectedIndex = 1;

// Example to fill a list box field
PdfLoadedListBoxField list = (PdfLoadedListBoxField)doc.Form.Fields[3];
list.SelectedIndex = 2;

// Example to fill a check box field
PdfLoadedCheckBoxField loadField = form.Fields[4] as PdfLoadedCheckBoxField;
loadField.Items[0].Checked = true;
```

### VB.NET
```vbnet
' Example to fill a radio button field
Dim radio As PdfLoadedRadioButtonListField = CType(doc.Form.Fields(2), PdfLoadedRadioButtonListField)
radio.SelectedIndex = 1

' Example to fill a list box field
Dim list As PdfLoadedListBoxField = CType(doc.Form.Fields(3), PdfLoadedListBoxField)
list.SelectedIndex = 2

' Example to fill a check box field
Dim loadField As PdfLoadedCheckBoxField = form.Fields(4) As PdfLoadedCheckBoxField
loadField.Items(0).Checked = True
```

## Cross References
- Refer to the documentation on PDF form fields for more detailed information about working with different types of form elements.
- For a complete guide on handling PDF forms in WinForms applications, consult the Syncfusion WinForms documentation.

<!-- tags: [Syncfusion WinForms, PDF, PDF Form Fields, Essential PDF, Radio Buttons, List Boxes, Check Boxes, Form Fields, Filling Fields] keywords: [pdf, form fields, radio buttons, list boxes, check boxes, essential pdf, filling fields, pdf toolkit, syncfusion winforms] -->
```