```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_209.jpeg
document_name: DocIo
page_number: 209
page_id: DocIo#page_209
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:41:48Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- Describes properties of the WCharacterFormat class that can be used to format individual characters in a document.
- Includes common formatting options for right-to-left text, line breaks, outlines, shadow, small caps, strikeouts, sub/superscripts, text background and foreground colors, underline styles, and locale identifiers for ASCII and FarEast characters.

## Content

### WCharacterFormat Properties

This section lists the properties of the WCharacterFormat class and their functionalities:

| Property           | Description                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| ItalicBidi        | Gets or sets italic property for right-to-left text.                        |
| LineBreak         | Gets or sets line break after.                                              |
| OutLine           | Gets or sets outline character property.                                    |
| Position          | Gets or sets text vertical position.                                        |
| Shadow            | Gets or sets shadow property of text.                                       |
| SmallCaps         | Gets or sets SmallCaps property of text.                                    |
| Strikeout         | Gets or sets strikeout style.                                               |
| SubSuperScript    | Gets or sets subscript / superscript mode.                                  |
| TextBackgroundColor | Gets or sets text background color.                                        |
| TextColor         | Gets or sets text color.                                                   |
| UnderLineStyle    | Gets or sets underline style.                                               |
| LocaleIdASCII     | Gets or sets the locale identifier (language) of the formatted characters.   |
| LocaleIdFarEast   | Gets or sets the locale identifier (language) of the formatted Asian characters. |

### Example

The following example illustrates how to use the WCharacterFormat class.

```csharp
[C#]

// Write different font name / font size
string[] fontNames = new string[] { "Times New Roman", "Verdana", "Symbol", };

IWSection section = doc.AddSection();
IWPagraph paragraph;
IWTextrange textRange;

for (int j = 0, len = fontNames.Length; j < len; j++)
{
    paragraph = section.AddParagraph();
    string fontName = fontNames[j];
}
```

## Code Examples (multi-language supported)
- The example above demonstrates how to use the WCharacterFormat class to apply different font names and sizes to individual characters in a document.
- The code snippet provided is written in C# and utilizes the Syncfusion.DocIO library for formatting character properties.

## RAG Annotations
<!-- tags: [DocIO, WCharacterFormat, Syncfusion.Winforms, CharacterFormatting] keywords: [WCharacterFormat, ItalicBidi, LineBreak, OutLine, Position, Shadow, SmallCaps, Strikeout, SubSuperScript, TextBackgroundColor, TextColor, UnderLineStyle, LocaleIdASCII, LocaleIdFarEast, CharacterFormatting, DocIO, Winforms, Syncfusion] -->
```