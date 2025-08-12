<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_134.jpeg
document_name: DocIo
page_number: 134
page_id: DocIo#page_134
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:36:05Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- Demonstrates how to apply various text effects and font styles in Word documents.
- Includes formatting options such as bold, italic, underline, strikethrough, shadow, and merged styles.
- Also shows how to iterate through font names and font sizes to apply them programmatically.

## Content

### Applying Various Text Effects and Font Styles

Here is an example in C# to apply different text effects and font styles:

```csharp
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
```

### Iterating Through Font Names and Font Sizes

Below is an example in VB.NET to iterate through font names and font sizes:

```vb.net
Dim doc As IWordDocument = New WordDocument()

' Write different font name/font size.
Dim fontNames As String() = New String() { "Times New Roman", "Verdana", "Symbol", }

Dim section As IWSecton = doc.AddSection()
Dim paragraph As IParagraph
Dim textRange As ITextRange

Dim j As Integer = 0
len = fontNames.Length

Do While j < len
    paragraph = section.AddParagraph()
    Dim fontName As String = fontNames(j)
    
    For i As Integer = 9 To 39
        textRange = paragraph.AppendText(fontName & "   " & i.ToString() & "    ")
        textRange.CharacterFormat.FontSize = i
        textRange.CharacterFormat.FontName = fontName
        If i > 15 Then
            ' Additional formatting logic can be added here.
        End If
    Next
    j += 1
Loop
```

## Code Examples

### C#

```csharp
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
```

### VB.NET

```vb.net
Dim doc As IWordDocument = New WordDocument()

' Write different font name/font size.
Dim fontNames As String() = New String() { "Times New Roman", "Verdana", "Symbol", }

Dim section As IWSecton = doc.AddSection()
Dim paragraph As IParagraph
Dim textRange As ITextRange

Dim j As Integer = 0
len = fontNames.Length

Do While j < len
    paragraph = section.AddParagraph()
    Dim fontName As String = fontNames(j)
    
    For i As Integer = 9 To 39
        textRange = paragraph.AppendText(fontName & "   " & i.ToString() & "    ")
        textRange.CharacterFormat.FontSize = i
        textRange.CharacterFormat.FontName = fontName
        If i > 15 Then
            ' Additional formatting logic can be added here.
        End If
    Next
    j += 1
Loop
```

## Tags and Keywords

<!-- tags: [Syncfusion Winforms, DocIO, Word documents, text effects, font styles, document formatting, iterating fonts, font sizes, bold, italic, underline, strikethrough, shadow, merged styles] keywords: [font name, font size, bold, italic, underline, strikethrough, shadow, merged, font styles, text formatting, Syncfusion, DocIO, Word documents] -->