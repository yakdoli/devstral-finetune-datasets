```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_260.jpeg
document_name: DocIo
page_number: 260
page_id: DocIo#page_260
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:45:05Z
fidelity: lossless
-->

# Essential DocIO

```vb
' Finds and returns entry of specified regular expression along with formatting
Dim rangesHolder1 As TextSelection = docSource1.Find("The Placeholder1 was replaced by this sample Text.", False, False)

' Create new TextSelection object, with text and its formatting specified by character range. In the current sample, the character range is a paragraph's range of symbols from 1 to 4 positions.
Dim rangesHolder2 As TextSelection = New TextSelection(docSource2.LastParagraph, 1, 4)

docTemplate.Replace(New Regex("Placeholder1"), rangesHolder1)
docTemplate.Replace(New Regex("Placeholder2"), rangesHolder2)
```

If you want to replace the first occurrence of a particular text alone, which appears more than once, set `doc.ReplaceFirst` property to `True`.

### C#

```csharp
doc.ReplaceFirst = true;
```

### VB.NET

```vb
doc.ReplaceFirst = true;
```

## Replace with SingleLine Mode

It is also possible to replace the string with .NET Regex `SingleLine` mode by using the `ReplaceSingleLine` method of DocIO. This enables the user to find the specified text of regular expression including the newline or carriage return, and replaces it with the given text.

The following table lists the overloads of this method.

| Name                            | Description                                             |
|---------------------------------|---------------------------------------------------------|
| ReplaceSingleLine(Regex, TextBodyPart) | Replaces the pattern with specified replacement in single-line mode. |
| ReplaceSingleLine(Regex, TextSelection) | Replaces the given pattern with replacement in single-line mode.     |

## API Reference

### Methods

- **ReplaceSingleLine(Regex, TextBodyPart)**  
  Replaces the pattern with specified replacement in single-line mode.

- **ReplaceSingleLine(Regex, TextSelection)**  
  Replaces the given pattern with replacement in single-line mode.
```