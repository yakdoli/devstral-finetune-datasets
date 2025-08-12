```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_182.jpeg
document_name: DocIo
page_number: 182
page_id: DocIo#page_182
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:39:15Z
fidelity: lossless
-->

## Essential DocIO

### Text Box Manipulation Example

#### Overview
This section showcases how to create and format text boxes, both within the main content area and in headers/footers, using the DocIO library. It demonstrates setting text wrapping styles, alignment, line styles, and colors to customize the appearance of the text boxes.

#### Code Example

```csharp
mainTextbox1.TextBoxFormat.TextWrappingStyle = TextWrappingStyle.Through
mainTextbox1.TextBoxFormat.TextWrappingType = TextWrappingType.Thought
mainTextbox1.TextBoxFormat.HorizontalAlignment = ShapeHorizontalAlignment.Center
mainTextbox1.TextBoxFormat.VerticalAlignment = ShapeVerticalAlignment.Bottom

' Header/footer text boxes
paragraph = New WParagraph(doc)
paragraph.AppendText("Hello textboxes")
Dim textbox As IWTextBox = paragraph.AppendTextBox(20, 50)
textbox.TextBoxBody.AddParagraph().AppendText("Header textbox")
textbox.TextBoxFormat.FillColor = System.Drawing.Color.Blue
textbox.TextBoxFormat.LineDashing = LineDashing.LongDashDotDotGEL
textbox.TextBoxFormat.LineWidth = 4.0f

Dim textbox1 As IWTextBox = paragraph.AppendTextBox(250, 50)
textbox1.TextBoxBody.AddParagraph().AppendText("Header textbox 2")
textbox1.TextBoxFormat.FillColor = System.Drawing.Color.Tomato
textbox1.TextBoxFormat.VerticalPosition = 250
textbox1.TextBoxFormat.LineStyle = TextBoxLineStyle.Triple
textbox1.TextBoxFormat.LineDashing = LineDashing.LongDashGEL
textbox1.TextBoxFormat.LineWidth = 6.0f
textbox1.TextBoxFormat.NoLine = True

section.HeadersFooters.FirstPageHeader.Paragraphs.Add(paragraph)

paragraph = New WParagraph(doc)
paragraph.AppendText("Hello footer textbox")
Dim textbox2 As IWTextBox = paragraph.AppendTextBox(120, 100)
textbox2.TextBoxFormat.VerticalPosition = 5
textbox2.TextBoxBody.AddParagraph().AppendText("Footer textbox")
textbox2.TextBoxFormat.FillColor = System.Drawing.Color.Yellow
textbox2.TextBoxFormat.LineDashing = LineDashing.DashGEL
textbox2.TextBoxFormat.LineWidth = 3.75f
textbox2.TextBoxFormat.TextWrappingStyle = TextWrappingStyle.Square
textbox2.TextBoxFormat.HorizontalAlignment = ShapeHorizontalAlignment.Left
textbox2.TextBoxFormat.VerticalAlignment = ShapeVerticalAlignment.Bottom
section.HeadersFooters.FirstPageFooter.Paragraphs.Add(paragraph)

doc.Save("Textboxes.doc")
```

### 4.4.1.4.3 Comment

## API Reference

### TextWrappingStyle Enum
- **TextWrappingStyle.Through**: Text wraps behind the text box, similar to a line break.
- **TextWrappingStyle.Square**: Text wraps within the bounds of the text box.

### ShapeHorizontalAlignment Enum
- **ShapeHorizontalAlignment.Center**: Aligns the text box horizontally to the center of the page.

### ShapeVerticalAlignment Enum
- **ShapeVerticalAlignment.Bottom**: Aligns the text box vertically to the bottom of the page.

### LineDashing Enum
- **LineDashing.LongDashDotDotGEL**: Custom line style with long dashes and dots.
- **LineDashing.LongDashGEL**: Custom line style with long dashes.
- **LineDashing.DashGEL**: Custom line style with dashed lines.

### TextBoxLineStyle Enum
- **TextBoxLineStyle.Triple**: Custom line style with triple lines.

### System.Drawing Namespace
- **Color**: Provides various color definitions for fill colors.

## Additional Notes
- The example demonstrates how to add text boxes to different sections of a document, including the main content, header, and footer, and customize their appearance using various formatting options.
- The `doc.Save` method saves the document with the specified filename, including the text boxes.

<!-- tags: [DocIO, text boxes, headers, footers, text formatting, line styles] keywords: [main textbox, header textbox, footer textbox, text wrapping, horizontal alignment, vertical alignment, line dashing, fill color, text body, paragraphs, document save] -->
```