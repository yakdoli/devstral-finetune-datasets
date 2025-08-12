<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_304.jpeg
document_name: pdf
page_number: 304
page_id: pdf#page_304
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:42:29Z
fidelity: lossless
-->

## Essential PDF

### Code Example: Adding a Text Box in a Document

#### C#
```csharp
firstNameTextBox.Multiline = true;

//Add the text box in document
loadedDoc.Form.Fields.Add(firstNameTextBox);
```

#### VB.NET
```vb
'Create a text box
Dim firstNameTextBox As PdfTextBoxField = New PdfTextBoxField(page, "firstNameTextBox")

'Set properties
firstNameTextBox.Bounds = New RectangleF(100, 20, 200, 20)
firstNameTextBox.Font = font
firstNameTextBox.Password = True
firstNameTextBox.Multiline = True

'Add the text box in document
loadedDoc.Form.Fields.Add(firstNameTextBox)
```

### RadioButton field

RadioButton fields contain a set of related buttons that can each be set to ON or OFF. Typically, at most, one radio button in a set can be ON at any given time, and selecting any one of the buttons automatically de-selects all the others. The `PdfRadioButtonListField` class is used to create a radio button in the PDF Forms. You can create the radio button list items by using the `PdfRadioButtonListItem` class.

#### Code Example: Creating Radio Buttons

```csharp
//Create a Radio button
PdfRadioButtonListField employeesRadioList = new PdfRadioButtonListField(page, "employeesRadioList");
loadedDoc.Form.Fields.Add(employeesRadioList);

//Create radio button items
PdfRadioButtonListItem radioItem1 = new PdfRadioButtonListItem("1-9");
radioItem1.Bounds = new RectangleF(100, 140, 20, 20);
g.DrawString("1-9", font, brush, new RectangleF(150, 145, 180, 20));

PdfRadioButtonListItem radioItem2 = new PdfRadioButtonListItem("10-49");
radioItem2.Bounds = new RectangleF(100, 170, 20, 20);
g.DrawString("10-49", font, brush, new RectangleF(150, 175, 180, 20));
```

## API Reference

### PdfRadioButtonListField
- **Namespace**: Syncfusion.Pdf
- **Description**: Class to create radio button fields in a PDF form.

### Methods
- **Add**
  - **Description**: Adds a field to the PDF document's form.

### Properties
- **Fields**
  - **Type**: Collection
  - **Description**: Contains the fields added to the form.

### PdfRadioButtonListItem
- **Namespace**: Syncfusion.Pdf
- **Description**: Represents a radio button item in a radio button list field.

### Methods
- **DrawString**
  - **Parameters**:
    - **String**: The text to be drawn.
    - **Font**: The font used for the text.
    - **Brush**: The brush used for the text.
    - **RectangleF**: The bounds where the text is to be drawn.

## Code Examples

The above sections provide examples for creating and manipulating text boxes and radio buttons in a PDF document using Syncfusion's Essential PDF library. The C# and VB.NET examples demonstrate how to add fields, set properties, and draw text on the PDF form.

## Cross References

See also:
- [Adding Fields to a PDF Form](#section-reference)
- [Working with Radio Buttons in PDF Forms](#section-reference)

<!-- tags: [pdf, text box, radio button, field, pdf forms, syncfusion, winforms, 11.4.0.26] keywords: [pdf, radio button, text box, add, field, document, form, property, drawstring, syncfusion, winforms, c#, vb.net] -->