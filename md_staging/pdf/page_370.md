```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_370.jpeg
document_name: pdf
page_number: 370
page_id: pdf#page_370
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:47:49Z
fidelity: lossless
-->

# Essential PDF

## Overview
- Demonstrates how to create various interactive form elements such as radio buttons, check boxes, and list boxes in a PDF document using Syncfusion's PDF functionalities.
- Explains the process of adding radio button groups, setting their properties, and integrating them into the PDF document.
- Showcases the creation of clear boxes with specified properties and values.
- Includes an example of creating a list box and adding fields to it.

## Content

### Creating Interactive Form Elements in PDF

#### Radio Button Group
- **Radio Button Items Creation**:
  ```csharp
  PdfRadioButtonListItem radioItem5 = new PdfRadioButtonListItem("500-more");
  radioItem5.Bounds = new RectangleF(100, 260, 20, 20);
  g.DrawString("500-more", font, brush, new RectangleF(150, 265, 180, 20));
  ```
- **Adding to the Radio Button Group**:
  ```csharp
  employeesRadioList.Items.Add(radioItem1);
  employeesRadioList.Items.Add(radioItem2);
  employeesRadioList.Items.Add(radioItem3);
  employeesRadioList.Items.Add(radioItem4);
  employeesRadioList.Items.Add(radioItem5);
  ```

#### Check Box Creation
- **Creating a Check Box**:
  ```csharp
  PdfCheckBoxField checkBox = new PdfCheckBoxField(page, ".NET");
  checkBox.Bounds = new RectangleF(100, 290, 20, 20);
  document.Form.Fields.Add(checkBox);
  ```
- **Setting Properties**:
  ```csharp
  checkBox.HighlightMode = PdfHighlightMode.Push;
  checkBox.BorderStyle = PdfBorderStyle.Beveled;
  ```
- **Setting the Value for the Check Box**:
  ```csharp
  checkBox.Checked = true;
  g.DrawString(".NET", font, brush, new RectangleF(150, 290, 180, 20));
  ```
- **Another Check Box Example**:
  ```csharp
  checkBox = new PdfCheckBoxField(page, "Java");
  checkBox.Bounds = new RectangleF(100, 320, 20, 20);
  document.Form.Fields.Add(checkBox);
  checkBox.HighlightMode = PdfHighlightMode.Push;
  checkBox.BorderStyle = PdfBorderStyle.Beveled;
  checkBox.Checked = false;
  g.DrawString("Java", font, brush, new RectangleF(150, 320, 180, 20));
  g.DrawString("Language known:", font, brush, new RectangleF(10, 350, 80, 60));
  ```

#### List Box Creation
- **Creating a List Box**:
  ```csharp
  PdfListBoxField listBox = new PdfListBoxField(page, "list1");
  ```
- **Adding the Field to the List Box**:
  ```csharp
  document.Form.Fields.Add(listBox);
  ```
- **Setting the Properties**:
  ```csharp
  listBox.Bounds = new RectangleF(100, 350, 100, 50);
  ```

<!-- tags: [pdf, form elements, radio buttons, check boxes, list boxes, Syncfusion, PDF functionalities] -->
<!-- keywords: [PdfRadioButtonListItem, PdfCheckBoxField, PdfListBoxField, properties, bounds, highlight mode, border style, checked, document.form.fields, interactive form elements] -->
```