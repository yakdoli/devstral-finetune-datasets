```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_298.jpeg
document_name: pdf
page_number: 298
page_id: pdf#page_298
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:43:06Z
fidelity: lossless
--> 

## Authoring PDF Forms

### Overview
- Describes the classes used to create interactive form fields in PDF documents.
- Explains the usage of the `PdfButtonField` class to create interactive buttons, including submit and reset functionality.
- Provides an example code snippet in C# for creating a button field.

### Classes for Creating Form Fields

| Class                  | Description                                                                                                                                                                                                 |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PdfButtonField`       | Creates a Button (Submit Button and Reset button can be created).                                                                                                                                         |
| `PdfCheckBoxField`     | Creates a Check Box.                                                                                                                                                                                      |
| `PdfComboBoxField`     | Creates a Combo Box.                                                                                                                                                                                       |
| `PdfListItem`          | Creates list items from Combo Box and List Box.                                                                                                                                                           |
| `PdfListBoxField`      | Creates a List Box.                                                                                                                                                                                       |
| `PdfTextBoxField`      | Creates a Text Box.                                                                                                                                                                                       |
| `PdfRadioButtonListField` | Creates a Radio button list.                                                                                                                                                                          |
| `PdfRadioButtonListItem` | Creates a Radio button list item.                                                                                                                                                                      |

### Button Field

A button field represents an interactive control on the screen that the user can manipulate using the mouse. The `PdfButtonField` class is used to create Buttons fields.

The most important feature of a PDF form is the ability to send entered data to a server. To perform this action, you should create an action of `SubmitAction` type and specify a valid data processing script URL. The action must be assigned to a `MouseUp` action of the submit button.

**ResetAction** is used to restore the default values of the fields or simply clear them.

#### Code Example: Creating a Button Field

The following C# code example illustrates how to create a button field.

```csharp
// Creating a Button
PdfButtonField button = new PdfButtonField(page, "Click");
button.Bounds = new RectangleF(0, 420, 90, 20);
button.Text = "Click";
loadedDoc.Form.Fields.Add(button);

// Creating Submit action button
PdfSubmitAction submitAction = new PdfSubmitAction("http://stevex.net/dump.php");
submitAction.DataFormat = SubmitDataFormat.Html;
```

### Conclusion
This section demonstrates how to create interactive form fields, focusing specifically on the `PdfButtonField` class and the functionality of submit and reset actions within a PDF document.

### Cross References
- Refer to the `PdfButtonField` class documentation for more details on creating interactive buttons.
- See the `SubmitAction` class documentation for information on data submission.

### RAG Annotations
 <!-- tags: [pdf, form fields, interactive controls, submit action, reset action, DateTimeField, Padding, Exception, Font, Export] keywords: [pdfbuttonfield, pdfcheckboxfield, pdfcomboboxfield, pdflistfield, pdflistboxfield, pdftextboxfield, pdfradiobuttonlistfield, pdfradiobuttonlistitem, submitaction, resetaction] -->
``` 
