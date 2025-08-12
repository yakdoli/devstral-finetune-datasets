```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_085.jpeg
document_name: pdf
page_number: 085
page_id: pdf#page_085
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:28:53Z
fidelity: lossless
-->

### Essential PDF

```vb
Dim richTextElement As PdfHTMLTextElement = New PdfHTMLTextElement(longText, font, brush)
richTextElement.TextAlignment = TextAlignment.Justify

' Formatting Layout
Dim format As PdfMetafileLayoutFormat = New PdfMetafileLayoutFormat()
format.Layout = PdfLayoutType.OnePage
format.Break = PdfLayoutBreakType.FitPage

' Drawing htmlString
richTextElement.Draw(page, New RectangleF(30, 30, 600, page.GetClientSize().Height), format)
```

#### 4.1.2.1.3 Automatic Fields

**Overview**
- Automatic Fields are special objects that display information calculated automatically, just before the document is saved.
- They display fields such as page number, count of pages, author of the document, creation and current date, and other document information.
- Important properties such as Font, Brush, and Bounds must be specified to display the correct value of the field.

#### Content

##### Description of Automatic Fields

Automatic Fields are special objects that display information calculated automatically, just before the document is saved. The following are the fields displayed:

- Page number
- Count of pages
- Author of the document
- Creation and current date
- Other document information

**Note**: These fields are not always evaluated at the moment of constructing the document.

##### Important Properties for Displaying Fields

To display the correct value of the field, you should specify some important properties, which are listed below:

- **Font**: Used to display the value of the field. Exception is thrown if this property is not set.
- **Brush**: Used to print the value of the field. Exception is thrown if this property is not set.
- **Bounds**: Specifies the bounds of the field

You can also use the `Location` and `Size` properties to define the bounds of the field.

- **Location**: Represents the location of the field. Default point is (0, 0).
- **Size**: Represents the size of the field. If it is not set, the size of the field is automatically calculated to display the value.

---

<!-- tags: [syncfusion winforms, automatic fields, essential pdf, pdf html text element, field formatting] keywords: [automatic fields, page number, count of pages, author, creation date, current date] -->
```