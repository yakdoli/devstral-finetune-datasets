```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_113.jpeg
document_name: XlsIO
page_number: 113
page_id: XlsIO#page_113
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:56:01Z
fidelity: lossless
-->

## Editing Rich Text

XlsIO provides support for reading and writing rich text by using the **IRichTextString** interface. It enables to format each character in the cell with different font styles.

---

### Note: Currently XlsIO cannot write formatted rich text.

#### [C#]

```csharp
// Insert Rich Text.
IRange range = sheet.Range["A1"];
range.Text = "RichText";
IRichTextString rtf = range.RichText;

// Formatting first 4 characters.
IFont redFont = workbook.CreateFont();
redFont.Bold = true;
redFont.Italic = true;
redFont.RGBColor = Color.Red;
rtf.SetFont(0, 3, redFont);

// Formatting last 4 characters.
IFont blueFont = workbook.CreateFont();
blueFont.Bold = true;
blueFont.Italic = true;
blueFont.RGBColor = Color.Blue;
rtf.SetFont(4, 7, blueFont);
```

#### [VB.NET]

```vb
' Insert Rich Text.
Dim range As IRange = sheet.Range("A1")
range.Text = "RichText"
Dim rtf As IRichTextString = range.RichText

' Formatting first 4 characters.
Dim redFont As IFont = workbook.CreateFont()
redFont.Bold = True
redFont.Italic = True
redFont.RGBColor = Color.Red
rtf.SetFont(0, 3, redFont)
```

---

<!-- tags: [XlsIO, rich text formatting, IRichTextString, Syncfusion Winforms, 11.4.0.26] keywords: [rich text, font styles, IRichTextString, XlsIO, formatting, C#, VB.NET] -->
```