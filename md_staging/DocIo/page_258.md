```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_258.jpeg
document_name: DocIo
page_number: 258
page_id: DocIo#page_258
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:44:34Z
fidelity: lossless
-->

## Overview
- The document explains the variants of the `Replace` method for text substitution operations, including regular expressions, string replacements, and formatting options.
- Examples demonstrate how to use these `Replace` methods in C# code, with specific attention to case sensitivity, whole word options, and formatting preservation.

## Content

The following are the variants of the Replace method.

### Overview of the Replace Method Variants

- **Replace(Regex pattern, string replace):** Replaces all occurrences of a character pattern specified by a regular expression with the replace string.
- **Replace(string given, string replace, bool caseSensitive, bool wholeWord):** Replaces all entries of the given string with the replace string, considering the `caseSensitive` and `wholeWord` options.
- **Replace(Regex pattern, TextSelection textSelection):** Replaces all entries of the given regular expression with `TextSelection`.
- **Replace(string given, TextSelection textSelection, bool caseSensitive, bool wholeWord):** Replaces all entries of the given string with `TextSelection`, considering the `caseSensitive` and `wholeWord` options.
- **Replace(Regex pattern, TextBodyPart bodyPart):** Replaces all entries of the given regular expression with `TextBodyPart`.
- **Replace(string given, TextBodyPart bodyPart, bool caseSensitive, bool wholeWord):** Replaces all entries of the given string with `TextBodyPart`, considering the `caseSensitive` and `wholeWord` options.
- **Replace(string given, IWordDocument replaceDoc, bool caseSensitive, bool wholeWord, bool saveFormatting):** Replaces all entries of the given string with a new word document, considering the `caseSensitive`, `wholeWord`, and `saveFormatting` options.
- **Replace(string given, TextBodyPart bodyPart, bool caseSensitive, bool wholeWord, bool saveFormatting):** Replaces all entries of the given string with `TextBodyPart`, considering the `caseSensitive`, `wholeWord`, and `saveFormatting` options.
- **Replace(string given, TextSelection textSelection, bool caseSensitive, bool wholeWord, bool saveFormatting):** Replaces all entries of the given string with `TextSelection`, considering the `caseSensitive`, `wholeWord`, and `saveFormatting` options.

### Code Examples

#### Example 1

The following sample demonstrates how to replace a specified regular expression with a picture:

```csharp
[C#]

Example 1:

// This sample replaces the specified regular expression with an image.
TextBodyPart textBodyPart = new TextBodyPart(doc);
Image image = Image.FromFile(ImagesPath + "Image.gif");
WPicture pict = new WPicture(doc);
pict.LoadImage(image);

WParagraph para = new WParagraph(doc);
para.Items.Add(pict);
textBodyPart.BodyItems.Insert(0, para);
doc.Replace(new Regex("A"), textBodyPart);
```

#### Example 2

<!-- tags: [document, replace, regex, string, formatting, textSelection, textBodyPart, IWordDocument, syncfusion, winforms] keywords: [replace method, case sensitive, whole word, save formatting, regex pattern, text selection, text body part] -->
```html
<tool_call>
```