```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_310.jpeg
document_name: pdf
page_number: 310
page_id: pdf#page_310
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:44:01Z
fidelity: lossless
-->

# Essential PDF

```csharp
txt.Font = txtfnt;
```

## Styling TextBox Fields

### VB.NET

```vb
Dim txt As PdfLoadedTextBoxField = TryCast(frm.Fields(i), PdfLoadedTextBoxField)
txt.BorderColor = Color.SteelBlue
txt.BorderStyle = PdfBorderStyle.Solid
txt.BorderWidth = 1
txt.BackColor = New PdfColor(Color.AliceBlue)
txt.ForeColor = New PdfColor(Color.Navy)
txt.HighlightMode = PdfHighlightMode.Invert
txt.TextAlignment = PdfTextAlignment.Right
Dim f As New Font("Arial", 18.0F)
Dim txtfnt As New PdfTrueTypeFont(f, False)
txt.Font = txtfnt
```

![](https://github.com/syncfusion-docs/Essential-PDF-rendered-images/blob/main/img310.png?raw=true)  

**Figure 63:** `BorderColor = "SteelBlue"`; `BorderStyle = "Solid"`; `BorderWidth = "1"`; `BackColor = "AliceBlue"`; `ForeColor = "Navy"`

## Filling the Combo Box Field

The following code illustrates how to fill the `ComboBox` Field.

### C#

```csharp
// fill combo box
PdfLoadedComboBoxField combo = (PdfLoadedComboBoxField)doc.Form.Fields[1];
combo.SelectedIndex = 3;
```

### VB.NET

```vb
' fill combo box
Dim combo As PdfLoadedComboBoxField = CType(doc.Form.Fields(1), PdfLoadedComboBoxField)
combo.SelectedIndex = 3
```

## Filling the Radio Button Field

The following code illustrates how to fill the `RadioButton` Field.

```html
<SomeContentHere />
```

## Footer
© 2013 Syncfusion. All rights reserved. 310 | Page
```

<!-- tags: [product, Essential PDF, styling, textbox, combo box, radio button] keywords: [Syncfusion Winforms, Essential PDF, TextBoxField, ComboBoxField, RadioButtonField, Page 310] -->
```