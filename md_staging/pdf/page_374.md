```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_374.jpeg
document_name: pdf
page_number: 374
page_id: pdf#page_374
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:48:09Z
fidelity: lossless
-->

# Essential PDF

## Overview
- Demonstrates how to add radio button groups, check boxes, and list boxes to a PDF document.
- Provides examples of setting properties and values for form fields.
- Explains how to integrate interactive elements within a PDF.

## Content

### Adding Radio Button Groups
```vb
' add the items to radio button group
employeesRadioList.Items.Add(radioItem1)
employeesRadioList.Items.Add(radioItem2)
employeesRadioList.Items.Add(radioItem3)
employeesRadioList.Items.Add(radioItem4)
employeesRadioList.Items.Add(radioItem5)

g.DrawString("Platform", font, brush, New RectangleF(10, 290, 80, 60))
```

### Adding Check Boxes
```vb
' Create a check box
Dim checkBox As PdfCheckBoxField = New PdfCheckBoxField(page, ".NET")

' Set properties
checkBox.Bounds = New RectangleF(100, 290, 20, 20)
document.Form.Fields.Add(checkBox)

checkBox.HighlightMode = PdfHighlightMode.Push
checkBox.BorderStyle = PdfBorderStyle.Beveled

' Set the value for the check box
checkBox.Checked = True
g.DrawString(".NET", font, brush, New RectangleF(150, 290, 180, 20))
```

```vb
' Create another check box
checkBox = New PdfCheckBoxField(page, "Java")
checkBox.Bounds = New RectangleF(100, 320, 20, 20)
document.Form.Fields.Add(checkBox)

checkBox.HighlightMode = PdfHighlightMode.Push
checkBox.BorderStyle = PdfBorderStyle.Beveled
checkBox.Checked = False
g.DrawString("Java", font, brush, New RectangleF(150, 320, 180, 20))
g.DrawString("Language known:", font, brush, New RectangleF(10, 350, 80, 60))
```

### Adding List Boxes
```vb
' Create list box
Dim listBox As PdfListBoxField = New PdfListBoxField(page, "list1")

' Add the field to listbox.
document.Form.Fields.Add(listBox)

' Set the properties.
listBox.Bounds = New RectangleF(100, 350, 100, 50)
listBox.HighlightMode = PdfHighlightMode.Outline

' Add the items to the list box
listBox.Items.Add(New PdfListBoxFieldItem("English", "English"))
listBox.Items.Add(New PdfListBoxFieldItem("French", "French"))
```

## Cross References
- See also: `PdfFormField`, `PdfRadioButtonListField`, `PdfListBoxField`, `PdfHighlightMode`, `PdfBorderStyle`.

<!-- tags: [syncfusion, winforms, pdf, form fields, check boxes, radio buttons, list boxes, pdfHighlightMode, pdfBorderStyle] keywords: [form fields, check boxes, radio buttons, list boxes] -->
```