```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_303.jpeg
document_name: pdf
page_number: 303
page_id: pdf#page_303
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:44:21Z
fidelity: lossless
-->

# Essential PDF

```csharp
loadedDoc.Form.Fields.Add(listBox);
```

### [VB.NET]

```vbnet
' Create list box
Dim listBox As PdfListBoxField = New PdfListBoxField(page, "list1")

' Set the properties.
listBox.Bounds = New RectangleF(100, 350, 100, 50)
listBox.HighlightMode = PdfHighlightMode.Outline

' Add the items to the list box
listBox.Items.Add(New PdfListItem("English","English"))
listBox.Items.Add(New PdfListItem("French","French"))
listBox.Items.Add(New PdfListItem("German","German"))

' Select the item
listBox.SelectedIndex = 2

' Set the multiselect option
listBox.MultiSelect = True
loadedDoc.Form.Fields.Add(listBox)
```

> **Note:** You can create multiple options from the ListBox by setting the MultiSelect option to True.

## TextBox field

A text field is a box or space in which the user can enter text through the keyboard. The text can be restricted to a single line or permitted to span multiple lines, depending on the setting of the Multiline flag. `PdfTextBoxField` class is used to create a textbox field in PDF forms. This class also provides support to create password and multilined text boxes.

The following code example illustrates this.

### [C#]

```csharp
// Create a text box
PdfTextBoxField firstNameTextBox = new PdfTextBoxField(page, "firstNameTextBox");

// Set properties
firstNameTextBox.Bounds = new RectangleF(100, 20, 200, 20);
firstNameTextBox.Font = font;
firstNameTextBox.Password = true;
```

## API Reference (if applicable)
- **Namespace:** Syncfusion.Pdf
- **Class:** PdfTextBoxField
- **Properties:**
  - Bounds: RectangleF
  - Font: Font
  - Password: Boolean
  - Multiline: Boolean

### Methods
- Add(): Adds the text box to the PDF form.

## Code Examples (multi-language supported)

### [C#]

```csharp
// Example of creating a password-protected textbox
PdfTextBoxField passwordBox = new PdfTextBoxField(page, "passwordBox");
passwordBox.Bounds = new RectangleF(100, 450, 200, 20);
passwordBox.Font = font;
passwordBox.Password = true;
pdfForm.Fields.Add(passwordBox);
```

### [VB.NET]

```vbnet
' Example of creating a password-protected textbox
Dim passwordBox As PdfTextBoxField = New PdfTextBoxField(page, "passwordBox")
passwordBox.Bounds = New RectangleF(100, 450, 200, 20)
passwordBox.Font = font
passwordBox.Password = True
pdfForm.Fields.Add(passwordBox)
```

<!-- tags: [pdf, textfield, textboxfield, listboxfield, passwordbox, textentry, syncfusion, winforms, document, pdfreader, pdfwriter] keywords: [pdf, Syncfusion, textbox, listbox, password, multiline, textfield, font, bounds, highlightmode, multiselect, properties, methods, codeexample, csharp, vb.net, api, pdfform, control, example, textfield, documentprocessing] -->
```