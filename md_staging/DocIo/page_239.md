```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_239.jpeg
document_name: DocIo
page_number: 239
page_id: DocIo#page_239
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:43:02Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- Demonstrates setting up textboxes with various styling options.
- Examples include header, footer, and inline textboxes with formatting attributes like fill color, line style, and alignment.
- Shows how to add text, set line properties, and adjust textbox positions within a document.

## Content

### Code Examples

```csharp
mainTextbox1.TextBoxFormat.VerticalPosition = 500;
mainTextbox1.TextBoxBody.AddParagraph().AppendText("Another textbox");
mainTextbox1.TextBoxFormat.FillColor = System.Drawing.Color.Yellow;
mainTextbox1.TextBoxFormat.LineDashing = LineDashing.DashGEL;
mainTextbox1.TextBoxFormat.LineWidth = 3.75f;
mainTextbox1.TextBoxFormat.TextWrappingStyle = TextWrappingStyle.Through;
mainTextbox1.TextBoxFormat.TextWrappingType = TextWrappingType.Both;
mainTextbox1.TextBoxFormat.HorizontalAlignment = ShapeHorizontalAlignment.Center;
mainTextbox1.TextBoxFormat.VerticalAlignment = ShapeVerticalAlignment.Bottom;

//Header/footer textboxes
paragraph = new WParagraph(doc);
paragraph.AppendText("Hello textboxes");
IWTextBox textbox = paragraph.AppendTextBox(20, 50);
textbox.TextBoxBody.AddParagraph().AppendText("Header textbox");
textbox.TextBoxFormat.FillColor = System.Drawing.Color.Blue;
textbox.TextBoxFormat.LineDashing = LineDashing.LongDashDotDotGEL;
textbox.TextBoxFormat.LineWidth = 4.0f;

IWTextBox textbox1 = paragraph.AppendTextBox(250, 50);
textbox1.TextBoxBody.AddParagraph().AppendText("Header textbox 2");
textbox1.TextBoxFormat.FillColor = System.Drawing.Color.Tomato;
textbox1.TextBoxFormat.VerticalPosition = 250;
textbox1.TextBoxFormat.LineStyle = TextBoxLineStyle.Triple;
textbox1.TextBoxFormat.LineDashing = LineDashing.LongDashGEL;
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

## API Reference

### Namespaces and Classes
- `System.Drawing`
- `Syncfusion.DocIO.WrittenDocument`

### Properties and Methods
- `TextBoxFormat.VerticalPosition`
- `TextBoxBody.AddParagraph()`
- `TextBoxFormat.FillColor`
- `TextBoxFormat.LineDashing`
- `TextBoxFormat.LineWidth`
- `TextBoxFormat.TextWrappingStyle`
- `TextBoxFormat.TextWrappingType`
- `TextBoxFormat.HorizontalAlignment`
- `TextBoxFormat.VerticalAlignment`
- `IWSegment.AppendTextBox()`
- `Document.Save(string fileName)`

## Code Examples (Multi-Language)

### C#
The given code snippet shows how to configure textboxes in a document using C#.

### Explanation
- The code demonstrates adding custom textboxes with specific styling attributes such as fill color, line dashing, line width, and text alignment.
- Examples include adding textboxes for headers and footers with unique properties like positioning and line styles.

## Page-level Navigation/TOC

### Local Table of Contents
- Introduction to Textboxes in DocIO
- Customizing Textbox Styles and Properties
- Header and Footer Textbox Setup
- Saving Documents with Configured Textboxes

## Cross References

- Related pages in the user guide:
  - "Working with Headers and Footers"
  - "Formatting Text in Documents"

<!-- tags: [syncfusion, winforms, docio, textboxes, document formatting, header, footer] keywords: [DocIO, textboxes, fill color, line dashing, text alignment, header, footer, document styling] -->
```