```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_227.jpeg
document_name: DocIo
page_number: 227
page_id: DocIo#page_227
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:42:12Z
fidelity: lossless
-->

# Essential DocIO

## Overview

This page focuses on the customization of list styles in a document using the Syncfusion Winforms SDK. By defining various properties such as bullet positions, numbering suffixes, paragraph formats, and alignment, users can create personalized list styles.

## Content

### List Style Properties

The following table outlines the keys for defining different aspects of list styles:

| Property         | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| NumberPosition   | Gets or sets the number/bullet position for the current list level (in points). |
| NumberPrefix     | Gets or sets prefix pattern for numbered level.                              |
| NumberSuffix     | Gets or sets suffix pattern for numbered level.                              |
| ParagraphFormat  | Gets or sets paragraph format of list level.                                 |
| PatternType      | Gets or sets list numbering type.                                           |
| StartAt          | Gets or sets start at value.                                                |
| TabSpaceAfter    | Gets or sets spacing after list level's number or bullet (tab position if follow character is tab). |
| TextPosition     | Gets or sets the left list level indent (in points).                        |
| UsePrevLevelPattern | When true, number generated will include previous levels (used for legal numbering). |

#### Example of Creating User-Defined List Styles

The following example shows how to create a user-defined bullet list style and apply it to a paragraph:

```csharp
// User bullet list style
ListStyle bulStyle = doc.AddListStyle(ListType.Bulleted, "BulletStyle");
WListLevel bulLevel1 = bulStyle.Levels[0];
bulLevel1.FollowCharacter = FollowCharacterType.Space;
bulLevel1.TextPosition = 40f;
bulLevel1.NumberAlignment = ListNumberAlignment.Right;

WListLevel bulLevel2 = bulStyle.Levels[1];
bulLevel2.FollowCharacter = FollowCharacterType.Space;
bulLevel2.TextPosition = 60f;
bulLevel2.NumberAlignment = ListNumberAlignment.Right;
bulLevel2.TabSpaceAfter = 40f;

paragraph = section.AddParagraph();
paragraph.AppendText("First bulleted ( level 0 )");
paragraph.ListFormat.ApplyStyle("BulletStyle");

paragraph = section.AddParagraph();
```

### Application of the Created List Style

Once the list style is defined, it can be applied to specific paragraphs to achieve the desired formatting. This provides precise control over the appearance of lists in the document.

<!-- tags: [syncfusion, winforms, liststyle, documentFormatting, bullet, numbering] keywords: [liststyle, document formatting, bullet, numbering, listposition, textposition] -->
```