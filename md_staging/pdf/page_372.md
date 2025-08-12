```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_372.jpeg
document_name: pdf
page_number: 372
page_id: pdf#page_372
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:46:55Z
fidelity: lossless
-->

# Essential PDF

```vb
Dim firstNameTextBox As PdfTextBoxField = New PdfTextBoxField(page, "firstNameTextBox")

' Set properties
firstNameTextBox.Bounds = New RectangleF(100, 20, 200, 20)
firstNameTextBox.Font = font
firstNameTextBox.Password = True
firstNameTextBox.Multiline = True

' Add the text box in document
document.Form.Fields.Add(firstNameTextBox)
g.DrawString("Last Name", font, brush, 10, 55)

Dim lastNameTextBox As PdfTextBoxField = New PdfTextBoxField(page, "lastNameTextBox")
lastNameTextBox.Bounds = New RectangleF(100, 53, 200, 20)
lastNameTextBox.Font = font
document.Form.Fields.Add(lastNameTextBox)

g.DrawString("Company", font, brush, 10, 85)

Dim companyTextBox As PdfTextBoxField = New PdfTextBoxField(page, "companyTextBox")
companyTextBox.Bounds = New RectangleF(100, 80, 200, 20)
companyTextBox.Font = font
document.Form.Fields.Add(companyTextBox)
g.DrawString("Position", font, brush, 10, 115)

' Create a combo box
Dim positionComboBox As PdfComboBoxField = New PdfComboBoxField(page, "positionComboBox")

' Set properties
positionComboBox.Bounds = New RectangleF(100, 115, 200, 20)
positionComboBox.Font = font
positionComboBox.Editable = True

' Add it to document
document.Form.Fields.Add(positionComboBox)

' Create the field item to be added in the combo box
Dim item1 As PdfListFieldItem = New PdfListFieldItem("Developer", "Developer")
Dim item2 As PdfListFieldItem = New PdfListFieldItem("Accountant", "Accountant")
Dim item3 As PdfListFieldItem = New PdfListFieldItem("CEO", "CEO")
Dim item4 As PdfListFieldItem = New PdfListFieldItem("Sales Manager", "Sales
```

<!-- tags: [Syncfusion, WinForms, PDF, Text, Combo Box, TextBox, Field, Font, Password, Bounds, Multiline, Document, Position, Developer, Accountant, CEO, Sales Manager] keywords: [Syncfusion Winforms, PDFTextBoxField, PdfComboBoxField, PdfListFieldItem, font, position, editable, document, DrawString, bounds, multiline, text box, combo box] -->
```