```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_327.jpeg
document_name: DocIo
page_number: 327
page_id: DocIo#page_327
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:49:09Z
fidelity: lossless
-->

# Essential DocIO

## Overview

- Demonstrates how to set OpenType features using code snippets in C# and VB.NET.
- Focuses on customizing styles such as contextual alternates, ligatures, number formatting, and stylized sets.

## Content

### Setting OpenType Features in C#

This section showcases how to apply various OpenType features using C#.

```csharp
// Sets the contextual alternates.
text = paragraph.AppendText("Text to check contextual alternates.");
text.CharacterFormat.FontName = "Segoe Script";
text.CharacterFormat.UseContextualAlternates = true;

// Sets the historical discretionary ligatures.
text = paragraph.AppendText("Check your fast facts on Fiji Islands");
text.CharacterFormat.FontName = "Calibri";
text.CharacterFormat.Ligatures = LigatureType.HistoricalDiscretional;

// Sets the old style number format.
text = paragraph.AppendText("3457645");
text.CharacterFormat.FontName = "Calibri";
text.CharacterFormat.NumberForm = NumberFormType.OldStyle;

// Sets the tabular type number spacing.
text = paragraph.AppendText("53127");
text.CharacterFormat.FontName = "Calibri";
text.CharacterFormat.NumberSpacing = NumberSpacingType.Tabular;

// Sets the stylistic set option.
text = paragraph.AppendText("The quick red fox.");
text.CharacterFormat.FontName = "Gabriola";
text.CharacterFormat.StylisticSet = StylisticSetType.StylisticSet06;
```

### Setting OpenType Features in VB.NET

This section demonstrates how to apply the same OpenType features using VB.NET.

```vbnet
' Sets the contextual alternates.
text = paragraph.AppendText("Text to check contextual alternates.")
text.CharacterFormat.FontName = "Segoe Script"
text.CharacterFormat.UseContextualAlternates = True

' Sets the historical discretionary ligatures.
text = paragraph.AppendText("Check your fast facts on Fiji Islands")
text.CharacterFormat.FontName = "Calibri"
text.CharacterFormat.Ligatures = LigatureType.HistoricalDiscretional

' Sets the old style number format.
text = paragraph.AppendText("3457645")
text.CharacterFormat.FontName = "Calibri"
```

## Page-level Navigation/TOC (if applicable)

- Sets OpenType Features in C#
- Sets OpenType Features in VB.NET

## Cross References

See also: OpenType feature documentation for detailed information on the properties and methods used.

<!-- tags: [Syncfusion Winforms, OpenType features, C#, VB.NET] keywords: [OpenType, contextual alternates, ligatures, number formatting, stylized sets, C#, VB.NET] -->
```