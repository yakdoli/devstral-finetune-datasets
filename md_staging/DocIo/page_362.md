```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_362.jpeg
document_name: DocIo
page_number: 362
page_id: DocIo#page_362
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:51:11Z
fidelity: lossless
-->

## Code Examples

### Applying Character Formatting

```csharp
[C#]

// Create a new word document
WordDocument doc = new WordDocument();
IWSection section = doc.AddSection();
IWParagraph para = section.AddParagraph();

// Apply formatting
ITextRange range = para.AppendText("New Text");
range.CharacterFormat.FontName = "Arial";
range.CharacterFormat.FontSize = 14;

// Save the document
doc.Save("CharacterFormattingDocIO.doc", FormatType.Doc);
```

## API Reference

### Classes and Methods

- **WordDocument**: Represents a document object in the DocIO API.
- **IWSection**: Represents a section in the document.
- **IWParagraph**: Represents a paragraph in the document section.
- **ITextRange**: Represents a range of text in a paragraph.
- **CharacterFormat**: Represents the formatting for characters within a text range.
  - **FontName**: Gets or sets the font name.
  - **FontSize**: Gets or sets the font size.

## Cross References

See also:
- DocIO API Documentation
- Formatting Text in Documents

<!-- tags: [syncfusion, docio, winforms, character formatting, word document, text formatting] keywords: [docio, formatting, text, font, size, save document, csharp] -->
```