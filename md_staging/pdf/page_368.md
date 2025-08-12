```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_368.jpeg
document_name: pdf
page_number: 368
page_id: pdf#page_368
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:46:41Z
fidelity: lossless
-->

### Essential PDF

```csharp
PdfDocument document = new PdfDocument();

PdfFont font = new PdfStandardFont(PdfFontFamily.Courier, 12f);
PdfBrush brush = PdfBrushes.Black;

PdfGraphics g = page.Graphics;
g.DrawString("First Name", font, brush, 10, 25);

// Create a text box
PdfTextBoxField firstNameTextBox = new PdfTextBoxField(page, "firstNameTextBox");

// Set properties
firstNameTextBox.Bounds = new RectangleF(100, 20, 200, 20);
firstNameTextBox.Font = font;
firstNameTextBox.Password = true;
firstNameTextBox.Multiline = true;

// Add the text box in document
document.Form.Fields.Add(firstNameTextBox);
g.DrawString("Last Name", font, brush, 10, 55);

PdfTextBoxField lastNameTextBox = new PdfTextBoxField(page, "lastNameTextBox");
lastNameTextBox.Bounds = new RectangleF(100, 53, 200, 20);
lastNameTextBox.Font = font;
document.Form.Fields.Add(lastNameTextBox);

g.DrawString("Company", font, brush, 10, 85);

PdfTextBoxField companyTextBox = new PdfTextBoxField(page, "companyTextBox");
companyTextBox.Bounds = new RectangleF(100, 80, 200, 20);
companyTextBox.Font = font;
document.Form.Fields.Add(companyTextBox);
g.DrawString("Position", font, brush, 10, 115);

// Create a combo box
PdfComboBoxField positionComboBox = new PdfComboBoxField(page, "positionComboBox");

// Set properties
positionComboBox.Bounds = new RectangleF(100, 115, 200, 20);
positionComboBox.Font = font;
positionComboBox.Editable = true;
```

<!-- tags: [Essential PDF, Form Fields, Syncfusion Winforms, 11.4.0.26] keywords: [PdfDocument, PdfFont, PdfTextBoxField, PdfComboBoxField, RectangleF] -->
```