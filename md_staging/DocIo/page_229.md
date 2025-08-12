```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_229.jpeg
document_name: DocIo
page_number: 229
page_id: DocIo#page_229
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:43:09Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- This page explains how to create and customize bullet and numbered list styles using the `DocIO` library in Syncfusion Winforms.
- Demonstrates setting up `WListLevel` for different levels within a list style.
- Includes examples for both bullet and numbered list formatting, complete with indentation, alignment, and appearance customization.

## Content

### Example: User Bullet List Style
This section demonstrates how to create a custom bullet list style and apply it to paragraphs.

```csharp
' User bullet list style
Dim bulStyle As ListStyle = doc.AddListStyle(ListType.Bulleted, "BulletStyle")
Dim bulLevel1 As WListLevel = bulStyle.Levels(0)
bulLevel1.FollowCharacter = FollowCharacterType.Space
bulLevel1.TextPosition = 40f
bulLevel1.NumberAlignment = ListNumberAlignment.Right

Dim bulLevel2 As WListLevel = bulStyle.Levels(1)
bulLevel2.FollowCharacter = FollowCharacterType.Space
bulLevel2.TextPosition = 60f
bulLevel2.NumberAlignment = ListNumberAlignment.Right
bulLevel2.TabSpaceAfter = 40f

paragraph = section.AddParagraph()
paragraph.AppendText("First bulleted ( level 0 )")
paragraph.ListFormat.ApplyStyle("BulletStyle")

paragraph = section.AddParagraph()
paragraph.AppendText("Level 1")
paragraph.ListFormat.ContinueListNumbering()
paragraph.ListFormat.IncreaseIndentLevel()

paragraph = section.AddParagraph()
paragraph.AppendText("Level 0")
paragraph.ListFormat.ContinueListNumbering()
paragraph.ListFormat.DecreaseIndentLevel()
```

### Example: User Numbered List Style
This section showcases the creation of a custom numbered list style with detailed formatting options.

```csharp
' User numbered list style
Dim newStyle As ListStyle = doc.AddListStyle(ListType.Numbered, "NewStyle")
Dim listLevelNew As WListLevel = newStyle.Levels(0)
listLevelNew.FollowCharacter = FollowCharacterType.Tab
listLevelNew.TextPosition = 80f
listLevelNew.NumberAlignment = ListNumberAlignment.Right
listLevelNew.TabSpaceAfter = 40f
listLevelNew.StartAt = 2
listLevelNew.NumberPrefix = ">>"
listLevelNew.NumberSufix = "<<"
listLevelNew.CharacterFormat.FontSize = 15
listLevelNew.CharacterFormat.TextColor = Color.Blue

listLevelNew1 As WListLevel = newStyle.Levels(1)
listLevelNew1.IsLegalStyleNumbering = True

listLevelNew2 As WListLevel = newStyle.Levels(2)
```

## Code Examples

The provided examples illustrate the creation and application of both bullet and numbered list styles. The code demonstrates how to customize list levels with specific indentation, alignment, and formatting properties to achieve the desired layout in documents.

## API Reference

### Methods
- `AddListStyle`: Adds a new list style to the document.
- `Levels`: Retrieves the levels defined for a specific list style.
- `FollowCharacter`: Sets the character that follows the list number or bullet.
- `TextPosition`: Specifies the horizontal position of the list number or bullet.
- `NumberAlignment`: Determines the horizontal alignment of the list number or bullet.
- `IncreaseIndentLevel`: Increase the indent level of the list for the current paragraph.
- `DecreaseIndentLevel`: Decrease the indent level of the list for the current paragraph.

### Properties
- `ListType`: Specifies the type of list (Bulleted or Numbered).
- `FollowCharacterType`: Defines the type of follow character (Space or Tab).
- `ListNumberAlignment`: Determines the alignment of list numbers.
- `CharacterFormat`: Controls the font, size, and color of the list numbers or bullets.

<!-- tags: [docio, list styles, numbered lists, bullet lists, winforms, syncfusion] keywords: [AddListStyle, Levels, FollowCharacter, TextPosition, NumberAlignment, IncreaseIndentLevel, DecreaseIndentLevel, ListType, CharacterFormat] -->
```