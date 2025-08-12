```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_067.jpeg
document_name: edit
page_number: 067
page_id: edit#page_067
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:57:44Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

A sample which demonstrates Content Dividers is available in the following sample installation path.

```
..\My Documents\Syncfusion\EssentialStudio\Version
Number\Windows\Edit.Windows\Samples\2.0\Text Formatting\ContentDividersDemo
```

## 4.4.4 Underlines, Wavelines and StrikeThrough

Underlines and Wavelines are mainly used to highlight certain sections of text, possibly to notify the user about errors or important sections of the document. Edit Control allows you to underline any desired text in its contents. The underlines can be of different styles, colors, and weights, with each of them being used to convey a different meaning. Edit Control supports underlines of the following styles: Solid, Dot, Dash, Wave and DashDot styles. You can also specify the weight of the underlines to be Single or Double.

Before the underlining can be applied to the selected text, a custom underlining format has to be defined. The `RegisterUnderlineFormat` method of `ISnippetFormat` registers the custom underline format to be used while underlining a region. You can create a custom underlining format, as shown in the code below.

### C#

```csharp
// Registers the custom underline format.
ISnippetFormat format = editControl1.RegisterUnderlineFormat(SelectedColor, SelectedStyle, SelectedWeight);
```

### VB.NET

```vb.net
' Registers the custom underline format.
Dim format As ISnippetFormat =
editControl1.RegisterUnderlineFormat(SelectedColor, SelectedStyle, SelectedWeight)
```

The `SelectedColor` value can be set to any desired color. The `SelectedStyle` value is specified by using the `UnderlineStyle` enumerator. The `SelectedWeight` value is specified by using the `UnderlineWeight` enumerator.

| Edit Control Underline Enumerator | Description                              |
|------------------------------------|------------------------------------------|
| UnderlineStyle                    | UnderlineStyle.Solid(default),           |

<!-- tags: [Windows Forms, Underlines, Wavelines, StrikeThrough, Edit Control, UnderlineStyle, UnderlineWeight, ISnippetFormat, Syncfusion Winforms, 11.4.0.26] keywords: [underlines, wavelines, strikeThrough, style, weight, color, text formatting, custom underline, Syncfusion, Windows Forms] -->
```