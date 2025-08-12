```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_211.jpeg
document_name: DocIo
page_number: 211
page_id: DocIo#page_211
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:41:00Z
fidelity: lossless
--> 

## Overview
- Demonstrates how to set locale identifiers and format text with different fonts, font sizes, and styles.
- Provides example code for setting font attributes like bold, italic, underline, and strike-through.
- Includes instructions for adjusting font sizes for Asian characters.

## Content

### Setting Locale Identifiers
```csharp
// or
textRange.CharacterFormat.LocaleIdASCII = 1093;
// Sets the locale identifier (language) of the formatted Asian characters.
textRange.CharacterFormat.LocaleIdFarEast = 2052
```

### Formatting Text with Different Fonts and Font Sizes
```vb.net
' Write different font name / font size.
Dim fontNames As String() = New String() { "Times New Roman", "Verdana", "Symbol", }

Dim section As IWSection = doc.AddSection()
Dim paragraph As IParagraph
Dim textRange As ITextRange

Dim j As Integer = 0
len = fontNames.Length
Do While j < len
    paragraph = section.AddParagraph()
    Dim fontName As String = fontNames(j)

    For i As Integer = 9 To 39
        textRange = paragraph.AppendText(fontName & " " & i.ToString() & " ")
        textRange.CharacterFormat.FontSize = i
        textRange.CharacterFormat.FontName = fontName
        If i > 15 Then
            i += 5
        End If
    Next i
    Dim txtRange2 As ITextRange = paragraph.AppendText(fontName & "34,5 ")
    txtRange2.CharacterFormat.FontSize = CSng(34.5)
    txtRange2.CharacterFormat.FontName = fontName
    j += 1
Loop
```

### Formatting Text with Bold, Italic, Underline, and Strike-Through
```vb.net
' Write bold / italic / underline / strike text.
paragraph = section.AddParagraph()
textRange = paragraph.AppendText("Bold Text_Bold Text    ")
textRange.CharacterFormat.Bold = True
textRange = paragraph.AppendText("Italic Text_Italic Text    ")
textRange.CharacterFormat.Italic = True
textRange = paragraph.AppendText("Underline Text_Underline Text    ")
textRange.CharacterFormat.UnderlineStyle = UnderlineStyle.Dash
textRange = paragraph.AppendText("Strike Text_Strike Text    ")
```

### API Reference
- **Methods and Properties**
  - `CharacterFormat.LocaleIdASCII`: Sets the locale identifier for ASCII characters.
  - `CharacterFormat.LocaleIdFarEast`: Sets the locale identifier for Asian characters.
  - `CharacterFormat.FontSize`: Sets the font size for the text range.
  - `CharacterFormat.FontName`: Sets the font name for the text range.
  - `CharacterFormat.Bold`: Sets the bold attribute for the text range.
  - `CharacterFormat.Italic`: Sets the italic attribute for the text range.
  - `CharacterFormat.UnderlineStyle`: Sets the underline style for the text range.

### Code Examples
- The provided VB.NET code demonstrates how to set various font attributes and styles programmatically.
- Font sizes increment in steps and include a specific example for a size of `34.5`.

### Cross References
- Refer to the documentation for more comprehensive details on working with text formatting and locale settings in `DocIO`.

<!-- tags: [DocIo, text formatting, font attributes, locale identifiers] keywords: [WinForms, character format, font size, bold, italic, underline, strike-through, locale] -->
```