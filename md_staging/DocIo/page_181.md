```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_181.jpeg
document_name: DocIo
page_number: 181
page_id: DocIo#page_181
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:39:52Z
fidelity: lossless
 -->

# Essential DocIO

```csharp
textbox1.TextBoxFormat.LineWidth = 6.0f;
textbox1.TextBoxFormat.NoLine = true;

section.HeadersFooters.FirstPageHeader.Paragraphs.Add(paragraph);

paragraph = new WParagraph(doc);
paragraph.AppendText("Hello footer textbox");
IWTextBox textbox2 = paragraph.AppendTextBox(120, 100);
textbox2.TextBoxFormat.VerticalPosition = 5;
textbox2.TextBoxBody.AddParagraph().AppendText("Footer textbox");
textbox2.TextBoxFormat.FillColor = System.Drawing.Color.Yellow;
textbox2.TextBoxFormat.LineDashing = LineDashing.DashGEL;
textbox2.TextBoxFormat.LineWidth = 3.75f;
textbox2.TextBoxFormat.TextWrappingStyle = TextWrappingStyle.Square;
textbox2.TextBoxFormat.HorizontalAlignment = ShapeHorizontalAlignment.Left;
textbox2.TextBoxFormat.VerticalAlignment = ShapeVerticalAlignment.Bottom;
section.HeadersFooters.FirstPageFooter.Paragraphs.Add(paragraph);

doc.Save("Textboxes.doc");
```

### VB.NET
```vb
Dim doc As IWordDocument = New WordDocument()
Dim section As IWSection = doc.AddSection()
Dim paragraph As IParagraph = section.AddParagraph()
section.PageSetup.DifferentFirstPage = True
section.PageSetup.DifferentOddAndEvenPages = True

' Main doc text boxes
paragraph.AppendText("Testing textboxes")

' 1st text box
Dim mainTextBox As IWTextBox = paragraph.AppendTextBox(150, 110)
mainTextBox.TextBoxBody.AddParagraph().AppendText("Textbox text 1")
mainTextBox.TextBoxFormat.FillColor = System.Drawing.Color.Blue
mainTextBox.TextBoxFormat.LineDashing = LineDashing.LongDashDotDotGEL
mainTextBox.TextBoxFormat.LineWidth = 4.0f

' 2nd text box
Dim mainTextBox1 As IWTextBox = paragraph.AppendTextBox(150, 100)
mainTextBox1.TextBoxFormat.VerticalPosition = 500
mainTextBox1.TextBoxBody.AddParagraph().AppendText("Another textbox")
mainTextBox1.TextBoxFormat.FillColor = System.Drawing.Color.Yellow
mainTextBox1.TextBoxFormat.LineDashing = LineDashing.DashGEL
mainTextBox1.TextBoxFormat.LineWidth = 3.75f
```

## Page-level Navigation/TOC
- **Main Section**: Explanation of the `Essential DocIO` features.
- **Code Examples**: Demonstrations for both C# and VB.NET.

## Cross References
- See also: Other sections related to working with headers, footers, and text formatting in `Essential DocIO`.

<!-- tags: [Essential DocIO, text formatting, header footers, C#, VB.NET] keywords: [DocIO, headers, footers, textboxes, footer text, line dashing, text alignment] -->
```