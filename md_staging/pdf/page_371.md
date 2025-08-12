```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_371.jpeg
document_name: pdf
page_number: 371
page_id: pdf#page_371
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:48:44Z
fidelity: lossless
-->

# Essential PDF

```csharp
listBox.HighlightMode = PdfHighlightMode.Outline;

// Add the items to the list box
listBox.Items.Add(new PdfListItem("English", "English"));
listBox.Items.Add(new PdfListItem("French", "French"));
listBox.Items.Add(new PdfListItem("German", "German"));

// Select the item
listBox.SelectedIndex = 2;

// Set the multiselect option
listBox.MultiSelect = true;

PdfSubmitAction submitAction = new PdfSubmitAction("http://stevex.net/dump.php");
submitAction.DataFormat = SubmitDataFormat.Html;

PdfResetAction resetAction = new PdfResetAction();

// Create submit button to transfer the values in the form
PdfButtonField submitButton = new PdfButtonField(page, "submitButton");
submitButton.Bounds = new RectangleF(100, 420, 90, 20);
submitButton.Font = font;
submitButton.Text = "Submit";
submitButton.Actions.MouseUp = submitAction;
document.Form.Fields.Add(submitButton);

// Create reset button to reset all the values
PdfButtonField resetButton = new PdfButtonField(page, "resetButton");
resetButton.Bounds = new RectangleF(210, 420, 90, 20);
resetButton.Font = font;
resetButton.Text = "Reset";
resetButton.Actions.MouseUp = resetAction;
document.Form.Fields.Add(resetButton);
```

## [VB]

```vb
Dim document As PdfDocument = New PdfDocument()

Dim font As PdfFont = New PdfStandardFont(PdfFontFamily.Courier, 12f)
Dim brush As PdfBrush = PdfBrushes.Black

Dim g As PdfGraphics = page.Graphics
g.DrawString("First Name", font, brush, 10, 25)

' Create a text box
```

<!-- tags: [pdf, listbox, form, submitaction, resetaction, buttonfield, document] keywords: [syncfusion, winforms, pdf, highlightmode, multiselect, submit, reset, formfields, graphics] -->
```