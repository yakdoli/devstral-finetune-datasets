```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_135.jpeg
document_name: DocIo
page_number: 135
page_id: DocIo#page_135
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:36:25Z
fidelity: lossless
-->

## Essential DocIO

```csharp
i += 5
End If
Next i
Dim txtRange2 As IWTextRange = paragraph.AppendText(fontName & "34,5 ")
txtRange2.CharacterFormat.FontSize = CSng(34.5)
txtRange2.CharacterFormat.FontName = fontName
j += 1
Loop

// Write bold/italic/underline/strike text.
paragraph = section.AddParagraph()
textRange = paragraph.AppendText("Bold Text_Bold Text    ")
textRange.CharacterFormat.Bold = True
textRange = paragraph.AppendText("Italic Text_Italic Text    ")
textRange.CharacterFormat.Italic = True
textRange = paragraph.AppendText("Underline Text_Underline Text    ")
textRange.CharacterFormat.UnderlineStyle = UnderlineStyle.Dash
textRange = paragraph.AppendText("Strike Text_Strike Text    ")
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
```

### 4.4.1.2 Fields

Fields are special elements of the Word document. To insert a field, open the Insert menu and click Field option in Microsoft Word.

## API Reference (if applicable)
None provided in the current content.

## Code Examples (multi-language supported)
- The code examples provided above demonstrate how to apply various text formats, such as bold, italic, underline, strikeout, and shadow, to text in a Word document using Synfusion DocIO.

## Page-level Navigation/TOC (if applicable)
None provided in the current content.

## Cross References
None provided in the current content.

<!-- tags: [DocIO, text formatting, Microsoft Word, fields, Syncfusion Winforms, 11.4.0.26] keywords: [bold, italic, underline, strikeout, shadow, textRange, paragraph, fontname, fontsize, document elements, field insertion, text styles] -->
```