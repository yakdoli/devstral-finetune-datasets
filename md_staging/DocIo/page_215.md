```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_215.jpeg
document_name: DocIo
page_number: 215
page_id: DocIo#page_215
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:41:22Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- Demonstrates how to create and apply paragraph styles in a Word document using Syncfusion's DocIO library.

## Content

This example shows how to define and apply different paragraph styles to a Word document. It includes styles such as bold, italic, and underlined text with various font and size settings.

### C# Code Example

```csharp
style.CharacterFormat.Italic = true;
style.CharacterFormat.FontName = "Verdana";
style.CharacterFormat.FontSize = 20;

style = (IWParagraphStyle)doc.AddParagraphStyle("UserStyle_Heading3");
style.CharacterFormat.Bold = true;
style.CharacterFormat.FontName = "Times New Roman";
style.CharacterFormat.FontSize = 20;
style.CharacterFormat.UnderlineStyle = UnderlineStyle.Single;

IWSection section = doc.AddSection();

for (int i = 0; i < doc.Styles.Count; i++)
{
    style = (IWParagraphStyle)doc.Styles[i];
    IWParagraph paragraph = section.AddParagraph();
    paragraph.ApplyStyle(style.Name);
    paragraph.AppendText("[ Style Applied ]: ");
    paragraph.AppendText(style.Name);
}
section.AddParagraph();
doc.Save("UserStyle.doc");
```

### VB.NET Code Example

```vb
Dim doc As IWordDocument = New WordDocument()

Dim style As IWParagraphStyle = CType(doc.AddParagraphStyle("Normal"), IWParagraphStyle)
Dim style = CType(doc.AddParagraphStyle("UserStyle_Heading1"), IWParagraphStyle)
style.CharacterFormat.Bold = True
style.CharacterFormat.FontName = "Verdana"
style.CharacterFormat.FontSize = 25

style = CType(doc.AddParagraphStyle("UserStyle_Heading2"), IWParagraphStyle)
style.CharacterFormat.Italic = True
style.CharacterFormat.FontName = "Verdana"
style.CharacterFormat.FontSize = 20

style = CType(doc.AddParagraphStyle("UserStyle_Heading3"), IWParagraphStyle)
style.CharacterFormat.Bold = True
style.CharacterFormat.FontName = "Times New Roman"
style.CharacterFormat.FontSize = 20
style.CharacterFormat.UnderlineStyle = UnderlineStyle.Single
```

## API Reference

### Methods Used
- `AddParagraphStyle`: Adds a new paragraph style.
- `ApplyStyle`: Applies a specific style to a paragraph.
- `AppendText`: Appends text to a paragraph.
- `Save`: Saves the document to a specified file path.

### Classes Used
- `IWParagraphStyle`: Represents a paragraph style in the Word document.
- `IWordDocument`: Represents the Word document in which styles are applied.

## Code Examples (Summary)

The code examples demonstrate how to:
1. Create custom paragraph styles with formatting attributes such as font, size, bold, italic, and underline.
2. Apply these styles to paragraphs within a Word document section.
3. Save the document with the applied styles.

## Cross References

- [See also: DocIO Documentation](https://help.syncfusion.com/windowsforms/docio/essentials)
- [See also: Style Management in DocIO](https://help.syncfusion.com/windowsforms/docio/style-management)

<!-- tags: [DocIO, Paragraph Styles, Syncfusion API, C#, VB.NET, Word Document, Style Management] keywords: [paragraph styles, custom styles, bold, italic, underline, font, size, apply style, save document] -->
```