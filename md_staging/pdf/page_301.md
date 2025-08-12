```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_301.jpeg
document_name: pdf
page_number: 301
page_id: pdf#page_301
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:42:13Z
fidelity: lossless
-->

# Essential PDF

```csharp
checkBox.HighlightMode = PdfHighlightMode.Push
checkBox.BorderStyle = PdfBorderStyle.Beveled

//'Set the value for the check box
checkBox.Checked = True
g.DrawString(".NET", font, brush, New RectangleF(150, 290, 180, 20))
loadedDoc.Form.Fields.Add(checkBox)
```

## PdfComboBox Field

A combo box represents a drop-down list, optionally accompanied by an editable text box in which the user can type a value other than the predefined choices. PdfComboBoxField class is used to create a combo box field in PDF forms. You can add list of items to the combo box by using the PdfListFieldItem class.

The following code example illustrates this.

### Code Example in C#

```csharp
//[C#]

//Create a combo box
PdfComboBoxField positionComboBox = new PdfComboBoxField(page, "positionComboBox");

//Set properties
positionComboBox.Bounds = new RectangleF(100, 115, 200, 20);
positionComboBox.Font = font;

// Setting the combobox as editable
positionComboBox.Editable = true;

//Add combobox to document
loadedDoc.Form.Fields.Add(positionComboBox);

//Create the field item to be added in the combobox
PdfListFieldItem item1 = new PdfListFieldItem("Developer", "Developer");
PdfListFieldItem item2 = new PdfListFieldItem("Accountant", "Accountant");

//Add the items in combo box.
positionComboBox.Items.Add(item1);
positionComboBox.Items.Add(item2);
```

### Code Example in VB.NET

```vb
'[VB.NET]

'Create a combo box
Dim positionComboBox As PdfComboBoxField = New PdfComboBoxField(page, 
```
```