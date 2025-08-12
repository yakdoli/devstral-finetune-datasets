```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_133.jpeg
document_name: DocIo
page_number: 133
page_id: DocIo#page_133
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:36:43Z
fidelity: lossless
-->

# Essential DocIO

| **CharacterFormat** | Gets character format( font properties ). |
|----------------------|---------------------------------------------|
| **EntityType**      | Gets the type of the entity.               |
| **Text**            | Gets or sets text.                        |

## Overview
- Illustrates the use of the WTextRange class through a C# code example.

### Example Usage of WTextRange Class

```csharp
[C#]

IWordDocument doc = new WordDocument();

// Write different font name/font size.
string[] fontNames = new string[] { "Times New Roman", "Verdana", "Symbol", };

IWSection section = doc.AddSection();
IWParagraph paragraph;
IWTextRange textRange;

for (int j = 0, len = fontNames.Length; j < len; j++)
{
    paragraph = section.AddParagraph();
    string fontName = fontNames[j];

    for (int i = 9; i < 40; i++)
    {
        textRange = paragraph.AppendText(fontName + " " + i.ToString() + " ");
        textRange.CharacterFormat.FontSize = i;
        textRange.CharacterFormat.FontName = fontName;
        if (i > 15)
        {
            i += 5;
        }
    }
    IWTextRange txtRange2 = paragraph.AppendText(fontName + "34,5 ");
    txtRange2.CharacterFormat.FontSize = (float)34.5;
    txtRange2.CharacterFormat.FontName = fontName;
}
// Write bold/italic/underline/strike text.
paragraph = section.AddParagraph();
textRange = paragraph.AppendText("Bold Text_Bold Text ");
```

## Code Examples (multi-language supported)
- Sample C# code demonstrating the usage of WTextRange to modify font properties and format text.
```csharp
// Sample code for modifying font properties using WTextRange
// Demonstrates appending text with different font names, sizes, and styles.

// Note: The code snippet provided shows how to manipulate text ranges to apply various font formats and sizes.
```

## RAG Annotations
<!-- tags: [DocIO, WTextRange, font formatting, text manipulation, C# example, WordDocument, ISection, IParagraph, ITextRange] keywords: [DocIO, WTextRange, font size, font name, bold, italic, underline, strike, WordDocument, ISection, IParagraph, ITextRange, C#] -->
```