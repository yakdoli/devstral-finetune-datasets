```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_369.jpeg
document_name: pdf
page_number: 369
page_id: pdf#page_369
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:46:36Z
fidelity: lossless
-->

# Essential PDF

## Overview
- Demonstrates how to add a combobox and a radio button list field to a PDF document.
- Provides code examples for adding predefined items to a combobox and radio buttons with corresponding labels.

## Content

### Adding a Combobox Field

The following code snippet shows how to add a combobox field to a PDF document and populate it with predefined items representing different job positions.

```csharp
//Add it to document
document.Form.Fields.Add(positionComboBox);

//Create the field item to be added in the combobox
PdfListFieldItem item1 = new PdfListFieldItem("Developer", "Developer");
PdfListFieldItem item2 = new PdfListFieldItem("Accountant", "Accountant");
PdfListFieldItem item3 = new PdfListFieldItem("CEO", "CEO");
PdfListFieldItem item4 = new PdfListFieldItem("Sales Manager", "Sales Manager");
PdfListFieldItem item5 = new PdfListFieldItem("Director", "Director");
PdfListFieldItem item6 = new PdfListFieldItem("HR Manager", "HR Manager");

//Add the items in combo box.
positionComboBox.Items.Add(item1);
positionComboBox.Items.Add(item2);
positionComboBox.Items.Add(item3);
positionComboBox.Items.Add(item4);
positionComboBox.Items.Add(item5);
positionComboBox.Items.Add(item6);

g.DrawString("Number of Employees", font, brush, new RectangleF(10, 145, 80, 60));
```

### Adding a Radio Button List Field

The following code snippet demonstrates how to add a radio button list field to a PDF document and populate it with options for the number of employees.

```csharp
//Create a Radio button
PdfRadioButtonListField employeesRadioList = new PdfRadioButtonListField(page, "employeesRadioList");

//Add to document
document.Form.Fields.Add(employeesRadioList);

//Create radio button items
PdfRadioButtonListItem radioItem1 = new PdfRadioButtonListItem("1-9");
radioItem1.Bounds = new RectangleF(100, 140, 20, 20);
g.DrawString("1-9", font, brush, new RectangleF(150, 145, 180, 20));

PdfRadioButtonListItem radioItem2 = new PdfRadioButtonListItem("10-49");
radioItem2.Bounds = new RectangleF(100, 170, 20, 20);
g.DrawString("10-49", font, brush, new RectangleF(150, 175, 180, 20));

PdfRadioButtonListItem radioItem3 = new PdfRadioButtonListItem("50-99");
radioItem3.Bounds = new RectangleF(100, 200, 20, 20);
g.DrawString("50-99", font, brush, new RectangleF(150, 205, 180, 20));

PdfRadioButtonListItem radioItem4 = new PdfRadioButtonListItem("100-499");
radioItem4.Bounds = new RectangleF(100, 230, 20, 20);
g.DrawString("100-499", font, brush, new RectangleF(150, 235, 180, 20));
```

## API Reference

The code utilizes the following classes and methods:
- **PdfListFieldItem**: Represents a list item for a combobox field.
- **PdfRadioButtonListField**: Represents a radio button list field.
- **PdfRadioButtonListItem**: Represents a radio button item in a radio button list field.
- **RectangleF**: Defines the bounds for radio button items.
- **Form.Fields.Add()**: Adds a field to the PDF form.
- **Graphics.DrawString()**: Draws text on the PDF page for labels.

## Code Examples

The provided examples demonstrate how to:
1. Create and add a combobox field with predefined job positions.
2. Create and add a radio button list field with options for the number of employees.

## Cross References

See also:
- [Reference to additional documentation or related sections about PDF manipulation in WinForms]

<!-- tags: [Syncfusion, WinForms, PDF, combobox, radio button, list field, job position, number of employees] keywords: [combobox, radio button list, PDF form, job position, number of employees] -->
```