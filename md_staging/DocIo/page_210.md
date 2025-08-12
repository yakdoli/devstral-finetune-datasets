<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_210.jpeg
document_name: DocIo
page_number: 210
page_id: DocIo#page_210
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:41:18Z
fidelity: lossless
-->

# Essential DocIO

```csharp
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

// Write bold / italic / underline / strike text.
paragraph = section.AddParagraph();
textRange = paragraph.AppendText("Bold Text_Bold Text    ");
textRange.CharacterFormat.Bold = true;
textRange = paragraph.AppendText("Italic Text_Italic Text    ");
textRange.CharacterFormat.Italic = true;
textRange = paragraph.AppendText("Underline Text_Underline Text    ");
textRange.CharacterFormat.UnderlineStyle = UnderlineStyle.Dash;
textRange = paragraph.AppendText("Strike Text_Strike Text    ");
textRange.CharacterFormat.Strikeout = true;

textRange = paragraph.AppendText("Shadow Text_Shadow Text    ");
textRange.CharacterFormat.Shadow = true;

paragraph = section.AddParagraph();
paragraph = section.AddParagraph();

textRange = paragraph.AppendText("Merged Font Style Text_Merged Font Style Text");
textRange.CharacterFormat.Bold = true;
textRange.CharacterFormat.Italic = true;
textRange.CharacterFormat.Strikeout = true;
textRange.CharacterFormat.UnderlineStyle = UnderlineStyle.Dash;

// Specify the locale so Microsoft Word recognizes.
// For the list of locale identifiers see
// http://www.microsoft.com/globaldev/reference/lcid-all.mspx.

// Sets the locale identifier (language) of the formatted characters.
textRange.CharacterFormat.LocaleIdASCII = (short)LocaleIDs.uk_UA;
```

## API Reference

### Properties
- `LocaleIdASCII`: Gets or sets the locale identifier (language) of the formatted characters.

### Methods
- `SetTextFont`: Sets the font and size for the text.

## Code Examples

The provided code examples demonstrate how to format text in a paragraph using various styles such as bold, italic, underline, and strikeout. It also illustrates how to specify the font size and font name for different text ranges. Additionally, the code shows how to apply shadow effects to text and how to set the locale identifier for formatted characters.

<!-- tags: [DocIO, text formatting, WinForms, rich text, document processing, version: 11.4.0.26] keywords: [bold, italic, underline, strikeout, font size, font name, shadow, locale identifier, text formatting, rich text, document processing] -->