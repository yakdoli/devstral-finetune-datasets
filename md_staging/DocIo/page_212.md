```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_212.jpeg
document_name: DocIo
page_number: 212
page_id: DocIo#page_212
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:41:40Z
fidelity: lossless
-->

# Essential DocIO

```csharp
textRange.CharacterFormat.Strikeout = True

textRange = paragraph.AppendText("Shadow Text_Shadow Text    ")
textRange.CharacterFormat.Shadow = True

paragraph = section.AddParagraph()
paragraph = section.AddParagraph()

textRange = paragraph.AppendText("Merged Font Style Text_Merged Font Style Text")
textRange.CharacterFormat.Bold = True
textRange.CharacterFormat.Italic = True
textRange.CharacterFormat.Strikeout = True
textRange.CharacterFormat.UnderlineStyle = UnderlineStyle.Dash

' Specify the locale so Microsoft Word recognizes.
' For the list of locale identifiers, see
http://www.microsoft.com/globaldev/reference/lcid-all.mspx.

' Sets the locale identifier (language) of the formatted characters.
textRange.CharacterFormat.LocaleIdASCII = CType(LocaleIDs.uk_UA, Short)

' or
textRange.CharacterFormat.LocaleIdASCII = 1093

' Sets the locale identifier (language) of the formatted Asian characters.
textRange.CharacterFormat.LocaleIdFarEast = 2052
```

## 4.4.2.3 Paragraph Styles

The `WParagraphStyle` class represents paragraph style in the Word document. Paragraph style is a pattern of paragraph formatting. You can also apply custom paragraph styles in MS Word.

## API Reference

### Namespace: Syncfusion.DocIO.DWF

#### Class: WParagraphStyle
- Represents paragraph style in a Word document.

#### Properties
- **Bold**: Setting this to `true` makes the text bold.
- **Italic**: Setting this to `true` makes the text italic.
- **Strikeout**: Setting this to `true` adds a strikeout through the text.
- **UnderlineStyle**: Defines the underline style applied to the text.
- **LocaleIdASCII**: Specifies the locale (language) identifier for ASCII characters.
- **LocaleIdFarEast**: Specifies the locale (language) identifier for Far East characters.

#### Methods
- None specific to `WParagraphStyle` are listed here.

## Code Examples

### Example: Applying Paragraph Styles

```csharp
// Create a new Word document.
WordDocument document = new WordDocument();

// Add a new section to the document.
IWSection section = document.AddSection();

// Add a new paragraph to the section.
IWParagraph paragraph = section.AddParagraph();

// Get the text range of the paragraph.
ICharacterFormat characterFormat = paragraph.CharacterFormat;

// Set various formatting properties.
characterFormat.Bold = true;
characterFormat.Italic = true;
characterFormat.Strikeout = true;
characterFormat.UnderlineStyle = UnderlineStyle.Dash;

// Add text with the specified style.
paragraph.AppendText("This text demonstrates various formatting options.").CharacterFormat = characterFormat;

// Save the document.
document.Save("StyledParagraph.docx", Response, ContentDisposition.Attachment);
```

## Related Topics

For more information on working with styles in Word documents, refer to the [Syncfusion DocIO Documentation](https://help.syncfusion.com/xamarin-docio/working-with-styles).

<!-- tags: Syncfusion Winforms, DocIO, Word processing, Paragraph Styles, WParagraphStyle, CharacterFormat, Bold, Italic, Strikeout, UnderlineStyle, LocaleIdASCII, LocaleIdFarEast, custom formatting, document manipulation keywords: paragraph styles, formatting, DocIO, WParagraphStyle, text styling -->
```