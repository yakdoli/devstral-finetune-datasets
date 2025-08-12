```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_219.jpeg
document_name: DocIo
page_number: 219
page_id: DocIo#page_219
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:41:40Z
fidelity: lossless
-->

# Overview

- This page provides a detailed description of various properties and attributes of a paragraph in the context of document formatting.
- Properties such as `Keep`, `KeepFollow`, `FirstLineIndent`, and `HorizontalAlignment` are explained with their functionalities.
- Programming examples in C# are included to demonstrate how to set the `OutlineLevel` property for a paragraph.

## Content

### Paragraph Properties

The following table describes the different properties that can be applied to a paragraph in document formatting:

| **Property**         | **Description**                                                                 |
|----------------------|---------------------------------------------------------------------------------|
| Keep                 | True if all lines in the paragraph are to remain on the same page.            |
| KeepFollow          | True if the paragraph is to remain on the same page as the paragraph that follows it. |
| FirstLineIndent     | Gets or sets first paragraph line indent (in points).                          |
| HorizontalAlignment | Gets or sets horizontal alignment for the paragraph.                           |
| Keep                 | True if all lines in the paragraph are to remain on the same page.            |
| KeepFollow          | True if the paragraph is to remain on the same page as the paragraph that follows it. |
| LeftIndent           | Gets or sets the value that represents the left indent for paragraph (in points) |
| LineSpacing         | Gets or sets the line spacing property of the paragraph (in points) that specifies the space between two paragraphs. |
| LineSpacingRule     | Gets or sets the line spacing rule property of the paragraph.                 |
| PageBreakAfter      | True if a page break is forced after the paragraph.                           |
| PageBreakBefore     | True if a page break is forced before the paragraph.                          |
| RightIndent         | Gets or sets the right indent for paragraph (in points).                      |
| MirrorIndents       | Gets or sets a value indicating whether the indentation type is mirror indents (Microsoft Word 2007 and 2010 specific property) |

### Code Examples

#### Setting the OutlineLevel Property

Here is an example of how to set the `OutlineLevel` property for a paragraph using C#:

```csharp
para.ParagraphFormat.OutlineLevel = OutlineLevel.Level8;
```

## Notes

- The properties listed are essential for managing the layout and formatting of text within paragraphs.
- The `OutlineLevel` property example demonstrates how to programmatically control the indentation and formatting of paragraphs in documents.

### Reference

- All rights reserved by Syncfusion in 2013.
- This documentation is part of the Syncfusion Winforms documentation for version 11.4.0.26.

<!-- tags: [syncfusion, winforms, document formatting, paragraph properties, c#, outline level] keywords: [keep, keepfollow, firstlineindent, horizontalalignment, leftindent, linespacing, linespacingrule, pagebreakafter, pagebreakbefore, rightindent, mirrorindents] -->
```