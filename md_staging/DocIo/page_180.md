```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_180.jpeg
document_name: DocIo
page_number: 180
page_id: DocIo#page_180
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:39:18Z
fidelity: lossless
-->

## Overview

- This page demonstrates how to create and customize textboxes in a Word document using the Syncfusion DocIO library.
- The code examples illustrate adding textboxes with various formatting options such as fill colors, line styles, and text wrapping.

## Content

The following C# code snippet demonstrates the creation of different textboxes with various styles and configurations in a Word document using Syncfusion DocIO.

### Adding Textboxes to a Word Document

```csharp
[C#]

IWordDocument doc = new WordDocument();
ISection section = doc.AddSection();
IParagraph paragraph = section.AddParagraph();
section.PageSetup.DifferentFirstPage = true;
section.PageSetup.DifferentOddAndEvenPages = true;

// Main doc text boxes
paragraph.AppendText("Testing textboxes");

// 1st text box
ItextBox mainTextbox = paragraph.AppendTextBox(150, 110);
mainTextbox.TextBoxBody.AddParagraph().AppendText("Textbox text 1");
mainTextbox.TextBoxFormat.FillColor = System.Drawing.Color.Blue;
mainTextbox.TextBoxFormat.LineDashing = LineDashing.LongDashDotDotGEL;
mainTextbox.TextBoxFormat.LineWidth = 4.0f;

// 2nd text box
ItextBox mainTextbox1 = paragraph.AppendTextBox(150, 100);
mainTextbox1.TextBoxFormat.VerticalPosition = 500;
mainTextbox1.TextBoxBody.AddParagraph().AppendText("Another textbox");
mainTextbox1.TextBoxFormat.FillColor = System.Drawing.Color.Yellow;
mainTextbox1.TextBoxFormat.LineDashing = LineDashing.DashGEL;
mainTextbox1.TextBoxFormat.LineWidth = 3.75f;
mainTextbox1.TextBoxFormat.TextWrappingStyle = TextWrappingStyle.Through;
mainTextbox1.TextBoxFormat.TextWrappingType = TextWrappingType.Both;
mainTextbox1.TextBoxFormat.HorizontalAlignment = ShapeHorizontalAlignment.Center;
mainTextbox1.TextBoxFormat.VerticalAlignment = ShapeVerticalAlignment.Bottom;

// Header/footer text boxes
paragraph = new WParagraph(doc);
paragraph.AppendText("Hello textboxes");
ItextBox textbox = paragraph.AppendTextBox(20, 50);
textbox.TextBoxBody.AddParagraph().AppendText("Header textbox");
textbox.TextBoxFormat.FillColor = System.Drawing.Color.Blue;
textbox.TextBoxFormat.LineDashing = LineDashing.LongDashDotDotGEL;
textbox.TextBoxFormat.LineWidth = 4.0f;

ItextBox textbox1 = paragraph.AppendTextBox(250, 50);
textbox1.TextBoxBody.AddParagraph().AppendText("Header textbox 2");
textbox1.TextBoxFormat.FillColor = System.Drawing.Color.Tomato;
textbox1.TextBoxFormat.VerticalPosition = 250;
textbox1.TextBoxFormat.LineStyle = TextBoxLineStyle.Triple;
textbox1.TextBoxFormat.LineDashing = LineDashing.LongDashGEL;
```

## API Reference

### Classes and Methods

- **`IWordDocument`**: Represents a Word document.
- **`ISection`**: Represents a section in a Word document.
- **`IParagraph`**: Represents a paragraph in a Word document.
- **`ItextBox`**: Represents a textbox in a Word document.
- **`TextBoxFormat`**: Provides properties for customizing the appearance of a textbox.

### Properties and Methods

- **`PageSetup.DifferentFirstPage`**: Sets whether the first page has a different page setup.
- **`PageSetup.DifferentOddAndEvenPages`**: Sets whether odd and even pages have different page setups.
- **`AppendText`**: Appends text to a paragraph.
- **`AppendTextBox`**: Adds a textbox to a paragraph.
- **`TextBoxFormat.FillColor`**: Sets the fill color of the textbox.
- **`TextBoxFormat.LineDashing`**: Sets the line dashing pattern of the textbox.
- **`TextBoxFormat.LineWidth`**: Sets the line width of the textbox.
- **`TextBoxFormat.TextWrappingStyle`**: Sets the text wrapping style of the textbox.
- **`TextBoxFormat.TextWrappingType`**: Sets the text wrapping type of the textbox.
- **`TextBoxFormat.HorizontalAlignment`**: Sets the horizontal alignment of the textbox.
- **`TextBoxFormat.VerticalAlignment`**: Sets the vertical alignment of the textbox.
- **`TextBoxFormat.LineStyle`**: Sets the line style of the textbox.

## Code Examples

The provided code examples showcase how to:

1. Create a new Word document.
2. Add sections and paragraphs to the document.
3. Configure page setup settings.
4. Create textboxes with custom fill colors, line styles, and text wrapping.
5. Position textboxes with specific vertical and horizontal alignments.

## Cross References

- For more information on advanced Word document formatting, refer to the Syncfusion DocIO documentation.
- Related topics include page setup, text formatting, and advanced textbox customization.

<!-- tags: [Syncfusion, Winforms, DocIO, WordDocument, Textbox, TextBoxFormat] keywords: [Syncfusion, Winforms, DocIO, Word, Document, Textbox, Formatting, Customization, Line Styles, Fill Colors, Text Wrapping] -->
```