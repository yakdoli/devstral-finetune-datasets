```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_302.jpeg
document_name: pdf
page_number: 302
page_id: pdf#page_302
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:43:26Z
fidelity: lossless
-->

## Combo Box Field

### Overview
- This section explains how to create and configure a **positionComboBox** in a PDF form using C#. It covers setting properties like bounds and font, making the combobox editable, adding it to the document, and populating it with items such as "Developer" and "Accountant."

### Content

```vb
'positionComboBox"

'Set properties
positionComboBox.Bounds = New RectangleF(100, 115, 200, 20)
positionComboBox.Font = font

' Setting the combobox as editable
positionComboBox.Editable = True

'Add combobox to document
loadedDoc.Form.Fields.Add(positionComboBox)

'Create the field item to be added in the combobox
Dim item1 As PdfListItem = New PdfListItem("Developer", "Developer")
Dim item2 As PdfListItem = New PdfListItem("Accountant", "Accountant")

'Add the items in combbox.
positionComboBox.Items.Add(item1)
positionComboBox.Items.Add(item2)
```

### PdfListBoxField

A scrollable List Box contains several text items, one or more of which may be selected as the field value. `PdfListBoxField` is used to create the ListBox field in PDF forms.

#### Overview
- This section demonstrates how to create and configure a **listBox** field in a PDF form using C#. It covers creating the list box, setting properties such as bounds and highlight mode, adding items to the list, selecting an item, and enabling multi-select functionality.

#### Content

```csharp
[C#]

//Create list box
PdfListBoxField listBox = new PdfListBoxField(page, "list1");

//Set the properties.
listBox.Bounds = new RectangleF(100, 350, 100, 50);
listBox.HighlightMode = PdfHighlightMode.Outline;

//Add the items to the list box
listBox.Items.Add(new PdfListItem("English", "English"));
listBox.Items.Add(new PdfListItem("French", "French"));
listBox.Items.Add(new PdfListItem("German", "German"));

//Select the item
listBox.SelectedIndex = 2;

//Set the multiselect option
listBox.MultiSelect = true;
```

<!-- tags: [syncfusion-sdk, winforms, pdf, combobox, listbox, field, properties, editable, multi-select, version:11.4.0.26] keywords: [combobox, positionComboBox, editable, PdfListBoxField, items, select, highlightMode, MultiSelect, listbox, properties, bounds, font] -->
```