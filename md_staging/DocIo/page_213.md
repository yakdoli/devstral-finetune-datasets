```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_213.jpeg
document_name: DocIo
page_number: 213
page_id: DocIo#page_213
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:42:04Z
fidelity: lossless
 -->

## Overview

- WParagraphStyle class has three properties.
  - Defines formatting for the paragraph to which the style is applied.
  - Defines base paragraph style.
  - Returns type of style (StyleType.ParagraphStyle).

## Content

### Paragraph Styles

WParagraphStyle class has three properties:

- **ParagraphFormat**: defines formatting for the paragraph to which the style is applied to.
- **BaseStyle**: defines base paragraph style.
- **StyleType**: returns type of style (StyleType.ParagraphStyle).

You can add your own paragraph styles to the document. Collection of DocIO paragraph styles is accessible through `WordDocument.Styles` property. You can apply one of the built-in Word paragraph styles by using the `WParagraph.ApplyStyle` method.

Also, you can use the `ApplyBaseStyle` method to apply the base style for the current paragraph style.

### Class Hierarchy

Note: Figure 71: Paragraph Styles is a screenshot demonstrating the use of paragraph styles in a document editor interface.

## API Reference

### WParagraphStyle Class

#### Properties

- **ParagraphFormat**: Defines formatting for the paragraph to which the style is applied.
- **BaseStyle**: Defines the base paragraph style.
- **StyleType**: Returns the type of style (StyleType.ParagraphStyle).

### Methods

- **ApplyStyle**: Applies one of the built-in Word paragraph styles to the current paragraph.
- **ApplyBaseStyle**: Applies the base style for the current paragraph style.

## Code Examples

### Applying a Paragraph Style

```csharp
// Example of applying a paragraph style
WParagraph paragraph = new WParagraph("Sample paragraph text");
OWrdDocument wordDocument = new OWrdDocument();
wordDocument.Add(paragraph);

// Access paragraph styles
WPStyle style = wordDocument.Styles.Add("NewStyle", StyleType.ParagraphStyle);
style.ParagraphFormat.Font.Name = "Arial";
style.ParagraphFormat.Font.Size = 12;
style.ParagraphFormat.Alignment = Syncfusion.DocIO.Export.ParaAlignment.Left;

// Apply the style to the paragraph
paragraph.ApplyStyle(style);
```

### Retrieving and Using Base Styles

```csharp
// Example of retrieving and using base styles
WParagraph paragraph = new WParagraph("Base style paragraph text");
OWrdDocument wordDocument = new OWrdDocument();
wordDocument.Add(paragraph);

// Use the base style
paragraph.ApplyBaseStyle(wordDocument.Styles["Normal"]);
```

## Page-level Navigation/TOC

- **Paragraph Styles** (Section)
  - WParagraphStyle Class Overview
  - Properties and Methods

## Cross References

See also:
- **OWrdDocument Class**: For document-level operations and style management.
- **WPStyle Class**: For creating and managing paragraph styles.

## RAG Annotations

<!-- tags: [elp.io, WParagraphStyle, paragraph styles, WordDocument, ApplyStyle, ApplyBaseStyle] keywords: [style formatting, base paragraph style, paragraph type, paragraph alignment, font settings] -->
```