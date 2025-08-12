```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_373.jpeg
document_name: pdf
page_number: 373
page_id: pdf#page_373
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:47:01Z
fidelity: lossless
-->

### Creating ComboBox and RadioButtonListFields in PDF Forms

#### Overview
- Demonstrates how to create and populate a ComboBox with items.
- Implements RadioButtonListFields with options for employee numbers.

#### Content

The following sample demonstrates adding a `ComboBox` and radio buttons ("`RadioButtonListFields`") to a PDF form.

- **ComboBox Items**: Adds a list of positions to the `ComboBox`.
- **RadioButtonListFields**: Adds options for selecting the number of employees.

```vb
Dim item1 As PdfListItem = New PdfListItem("CEO", "CEO")
Dim item2 As PdfListItem = New PdfListItem("Vice President", "Vice President")
Dim item3 As PdfListItem = New PdfListItem("Finance Manager", "Finance Manager")
Dim item4 As PdfListItem = New PdfListItem("Sales Manager", "Sales Manager")
Dim item5 As PdfListItem = New PdfListItem("Director", "Director")
Dim item6 As PdfListItem = New PdfListItem("HR Manager", "HR Manager")

' Add the items in combo box.
positionComboBox.Items.Add(item1)
positionComboBox.Items.Add(item2)
positionComboBox.Items.Add(item3)
positionComboBox.Items.Add(item4)
positionComboBox.Items.Add(item5)
positionComboBox.Items.Add(item6)

g.DrawString("Number of Employees", font, brush, New RectangleF(10, 145, 80, 60))

' Create a Radio button
Dim employeesRadioList As PdfRadioButtonListField = New PdfRadioButtonListField(page, "employeesRadioList")

' Add to document
document.Form.Fields.Add(employeesRadioList)

' Create radio button items
Dim radioItem1 As PdfRadioButtonListItem = New PdfRadioButtonListItem("1-9")
radioItem1.Bounds = New RectangleF(100, 140, 20, 20)
g.DrawString("1-9", font, brush, New RectangleF(150, 145, 180, 20))

Dim radioItem2 As PdfRadioButtonListItem = New PdfRadioButtonListItem("10-49")
radioItem2.Bounds = New RectangleF(100, 170, 20, 20)
g.DrawString("10-49", font, brush, New RectangleF(150, 175, 180, 20))

Dim radioItem3 As PdfRadioButtonListItem = New PdfRadioButtonListItem("50-99")
radioItem3.Bounds = New RectangleF(100, 200, 20, 20)
g.DrawString("50-99", font, brush, New RectangleF(150, 205, 180, 20))

Dim radioItem4 As PdfRadioButtonListItem = New PdfRadioButtonListItem("100-499")
radioItem4.Bounds = New RectangleF(100, 230, 20, 20)
g.DrawString("100-499", font, brush, New RectangleF(150, 235, 180, 20))

Dim radioItem5 As PdfRadioButtonListItem = New PdfRadioButtonListItem("500+")
radioItem5.Bounds = New RectangleF(100, 260, 20, 20)
g.DrawString("500+", font, brush, New RectangleF(150, 265, 180, 20))
```

This code example shows how to dynamically add interactive controls to a PDF using the `PdfListItem`, `PdfComboBox`, `PdfRadioButtonListField`, and `PdfRadioButtonListItem` classes.

<!-- tags: [pdf, combobox, radiobuttonlist, pdf Kardashians, listbox, form fields] keywords: [Syncfusion Winforms, ComboBox, RadioButtons, PDF Forms, fields, AddCombobox, AddField, Buttons] -->
```