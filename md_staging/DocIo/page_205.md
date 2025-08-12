```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_205.jpeg
document_name: DocIo
page_number: 205
page_id: DocIo#page_205
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:41:34Z
fidelity: lossless
-->

# Essential DocIO

## Overview

- The collection of DocIO character and paragraph styles is accessible through the `WordDocument.Styles` property.
- The collection of list styles is accessible through the `WordDocument.ListStyles` property.
- The `DocIO Style` class serves as a base class for `CharacterStyle` and `WParagraphStyle`, with `Style` being an abstract class.
- The `CharacterFormat` property of the `Style` class defines character formatting.
- The `Name` property specifies the style name, and the `BaseStyle` property defines the base style.
- Users can apply built-in Word styles using the `WParagraph.ApplyStyle` method.
- Built-in styles are accessible through the `BuiltinStyle` enumeration.

## Content

### Public Properties

| Name          | Description                         |
|---------------|-------------------------------------|
| CharacterFormat | Gets the character format.          |
| Name           | Gets or sets style name.            |
| StyleType      | Gets the type of the style.         |

### Public Methods

| Name           | Description                   |
|----------------|-------------------------------|
| ApplyBaseStyle | Apply base style for current style. |
| Clone          | Clones itself.                |

### 4.4.2.1 Accessing Styles

You can access the collection of styles defined in the document by using the `Styles` property. This collection holds both built-in and user-defined styles in a document. A particular style can be obtained by its name or index.

The following example illustrates how to access the collection of styles defined in the document.

## Code Examples

### Example: Accessing and Applying Styles

```csharp
// Assuming you have a WordDocument object named `document`
var styles = document.Styles;

// Access a specific style by name
var specificStyle = styles["Heading1"];

// Apply the style to a paragraph
var paragraph = document.LastSection.AddParagraph();
paragraph.ApplyStyle(specificStyle);
```

<!-- tags: [Syncfusion Winforms, DocIO, Styles] keywords: [DocIO, styles, WordDocument, accessor, ApplyStyle, CharacterFormat, BaseStyle, BuiltinStyle, WParagraphStyle] -->
```