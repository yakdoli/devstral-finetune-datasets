```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_300.jpeg
document_name: pdf
page_number: 300
page_id: pdf#page_300
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:42:08Z
fidelity: lossless
-->

## Essential PDF

### PrintButtonField Example

```csharp
PdfButtonField print = new PdfButtonField(page, "print");
print.Bounds = new RectangleF(200, 25, 90, 15);
print.Text = "Print";
print.AddPrintAction();
```

#### VB.NET

```vb
' Create a print button
Dim print As PdfButtonField = New PdfButtonField(page, "print")
print.Bounds = New RectangleF(200, 25, 90, 15)
print.Text = "Print"
print.AddPrintAction()
```

### Check Box Field

#### Overview

A check box field represents one or more check boxes that toggle between two states: ON and OFF. The check box state is manipulated by the user using the mouse or keyboard.

#### Creating a Check Box

The `PdfCheckBoxField` class is used to create a check box in PDF forms. You can customize the check box style by using properties such as `BorderStyle`, `HighlightMode`, `BorderWidth`, and more.

##### C#

```csharp
// Create a check box
PdfCheckBoxField checkBox = new PdfCheckBoxField(page, ".NET");

// Set properties
checkBox.Bounds = new RectangleF(100, 290, 20, 20);
checkBox.HighlightMode = PdfHighlightMode.Push;
checkBox.BorderStyle = PdfBorderStyle.Beveled;

// Set the value for the check box
checkBox.Checked = true;
g.DrawString(".NET", font, brush, new RectangleF(150, 290, 180, 20));
loadedDoc.Form.Fields.Add(checkBox);
```

##### VB.NET

```vb
' Create a check box
Dim checkBox As PdfCheckBoxField = New PdfCheckBoxField(page, ".NET")

' Set properties
checkBox.Bounds = New RectangleF(100, 290, 20, 20)
```

## API Reference

- **Namespace**: `Essential PDF`
- **Class**: `PdfCheckBoxField`
- **Properties**:
  - `Bounds`: Specifies the size and position of the check box.
  - `HighlightMode`: Specifies the highlight mode for the check box.
  - `BorderStyle`: Specifies the border style for the check box.
  - `Checked`: Indicates whether the check box is checked.
- **Methods**:
  - `AddPrintAction()`: Adds a print action to the check box field.

## Code Examples

### C#

```csharp
PdfCheckBoxField checkBox = new PdfCheckBoxField(page, ".NET");
checkBox.Bounds = new RectangleF(100, 290, 20, 20);
checkBox.HighlightMode = PdfHighlightMode.Push;
checkBox.BorderStyle = PdfBorderStyle.Beveled;
checkBox.Checked = true;
loadedDoc.Form.Fields.Add(checkBox);
```

### VB.NET

```vb
Dim checkBox As PdfCheckBoxField = New PdfCheckBoxField(page, ".NET")
checkBox.Bounds = New RectangleF(100, 290, 20, 20)
checkBox.HighlightMode = PdfHighlightMode.Push
checkBox.BorderStyle = PdfBorderStyle.Beveled
checkBox.Checked = True
loadedDoc.Form.Fields.Add(checkBox)
```

<!-- tags: [pdf, forms, check box, button field, essentials, Syncfusion Winforms, 11.4.0.26] keywords: [checkboxfield, printbuttonfield, highlightmode, borderstyle, checked, addprintaction] -->
```