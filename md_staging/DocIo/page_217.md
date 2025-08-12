```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_217.jpeg
document_name: DocIo
page_number: 217
page_id: DocIo#page_217
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:42:20Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- This page demonstrates the advanced formatting options available in the Format menu, specifically focusing on paragraph formatting.
- Detailed steps to access and configure paragraph settings using the Paragraph Dialog Box are provided.

## Content

### Paragraph Option in Format Menu
The paragraph option in the Format menu allows users to access comprehensive configuration settings for text formatting. The Format menu includes various tools for text manipulation:
- Paragraph...
- Bullets and Numbering...
- Borders and Shading...
- Columns...
- Background
- Styles and Formatting...
- Object...

**Figure 72: Paragraph Option in Format Menu**

### Paragraph Dialog Box
The Paragraph Dialog Box provides options for controlling Indents and Spacing, Line and Page Breaks, and Asian Typography. Here is a detailed breakdown of the configuration options available in the Indents and Spacing tab:

#### General Settings
- **Alignment**: 
  - Left (selected)
  - Right-to-left
- **Outline level**: Body text
- **Direction**: Left-to-right

#### Indentation
- **Before text**: 0 inch
- **After text**: 0 inch
- **Special**: "none"
- **By**: Custom spacing adjustable
- **Automatically adjust right indent when document grid is defined**: checked

#### Spacing
- **Before**: 0 pt
- **After**: 0 pt
- **Line spacing**: Single
- **At**: Custom spacing adjustable
- **Don't add space between paragraphs of the same style**: not checked
- **Snap to grid when document grid is defined**: checked

**Figure 73: Paragraph Dialog Box**

## API Reference
This section references the API used for programmatically configuring paragraph properties in DocIO:
- **Namespace**: Syncfusion.DocIO
- **Class**: PDFFormat
- **Method**: ApplyParagraphFormatting()

## Code Examples
Below is an example demonstrating how to apply paragraph formatting in C# using Syncfusion.DocIO.

```csharp
// Example code snippet
Document document = new Document();
Paragraph paragraph = document.LastSection.AddParagraph();
paragraph.Format.Alignment = Syncfusion.DocIO.FormatAlignment.Left;
paragraph.Format.OutlineLevel = 0;
paragraph.Format.BeforeParagraphSpace = 0;
paragraph.Format.AfterParagraphSpace = 0;
document.Save("FormattedDocument.docx");
```

## Page-level Navigation/TOC
- Paragraph Option in Format Menu
- Paragraph Dialog Box
- API Reference
- Code Examples

## Cross References
- See also: Other formatting options in the Format menu, such as Bullets and Numbering, Borders and Shading, and Styles and Formatting.

<!-- tags: [syncfusion-sdk, DocIo, paragraph formatting, winforms, version 11.4.0.26] keywords: [format menu, paragraph dialog box, paragraph settings, outline level, indentation, spacing, api reference, code example] -->
```