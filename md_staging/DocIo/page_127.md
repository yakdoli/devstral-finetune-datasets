```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_127.jpeg
document_name: DocIo
page_number: 127
page_id: DocIo#page_127
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:35:54Z
fidelity: lossless
-->

## Overview
- Describes properties and methods related to paragraph breaks and formatting.
- Explains how to format break symbols and create lists in documents.
- Details about adding paragraph items and class hierarchy for text body items.

## Content

### IsEndOfSection
- Defines whether the current paragraph is the last paragraph in the section.

### IsEndOfDocument
- Defines whether the current paragraph is the last paragraph in the document.

### Formatting Break Symbol
#### BreakCharacterFormat
The BreakCharacterFormat property is used to set the character formatting for the break symbol.

![](Figure 42: Formatted Break Symbol)

#### DocIO List
DocIO paragraphs can also be displayed as a list by using the ListFormat property. This property returns the object of the WListFormat type. The WListFormat class defines the formatting for the list (applied list style, list level number, and so on). For more details on the WListFormat class, see [WListFormat](#WListFormat).

#### Adding Paragraph Items
DocIO paragraph enables the addition of paragraph items to the end of the current paragraph by using the Append function. For example, methods such as AppendText, AppendBreak, and others are used for this purpose.

### Class Hierarchy

```
TextBodyItem
    |
    WPparagraph
```

### Public Constructor

| Name | Description |
| --- | --- |
| WParagraph.WParagraph (IWordDocument) | Initializes a new instance of the WParagraph class. |

## API Reference

### Methods
- ListFormat: Returns the object of the WListFormat type.
- AppendText: Adds text to the end of the current paragraph.
- AppendBreak: Adds a break to the end of the current paragraph.

## Code Examples

```csharp
// Example of using the AppendText method
public void AddParagraphItems()
{
    // Create a new paragraph
    WParagraph paragraph = new WParagraph(IWordDocument);

    // Append text to the paragraph
    paragraph.AppendText("This is the first line.");

    // Append a break to the paragraph
    paragraph.AppendBreak();
    paragraph.AppendText("This is the second line.");
}
```

## Cross References

- See also: [WListFormat](#WListFormat) for detailed information about list formatting in DocIO.

<!-- tags: syncfusion, winforms,/docio,paragraphs, formatting,freaks,symbools,lists, methods,classes, version 11.4.0.26 -->
```