```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_232.jpeg
document_name: DocIo
page_number: 232
page_id: DocIo#page_232
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:43:06Z
fidelity: lossless
-->

# Essential DocIO

```csharp
IWParagraph paragraph = section.AddParagraph();
paragraph.AppendText("First Numbered (level 0)");
paragraph.ListFormat.ApplyDefNumberedStyle();

paragraph = section.AddParagraph();
paragraph.AppendText("Level 1");
paragraph.ListFormat.ContinueListNumbering();
paragraph.ListFormat.IncreaseIndentLevel();

paragraph = section.AddParagraph();
paragraph.AppendText("Level 0");
paragraph.ListFormat.ContinueListNumbering();
paragraph.ListFormat.DecreaseIndentLevel();

section.AddParagraph();
section.AddParagraph();

// Write default bulleted list
paragraph = section.AddParagraph();
paragraph.AppendText("First bulleted (level 0)");
paragraph.ListFormat.ApplyDefBulletStyle();

paragraph = section.AddParagraph();
paragraph.AppendText("Level 1");
paragraph.ListFormat.ContinueListNumbering();
paragraph.ListFormat.IncreaseIndentLevel();

paragraph = section.AddParagraph();
paragraph.AppendText("Level 0");
paragraph.ListFormat.ContinueListNumbering();
paragraph.ListFormat.DecreaseIndentLevel();

section.AddParagraph();
section.AddParagraph();

// Write mixed bulleted and numbered list
ListStyle myStyle = doc.AddListStyle(ListType.Numbered, "UserStyle");
WListLevel listLevel1 = myStyle.Levels[0];
listLevel1.FollowCharacter = FollowCharacterType.Tab;
listLevel1.TextPosition = 80f;
listLevel1.NumberAlignment = ListNumberAlignment.Right;
listLevel1.TabSpaceAfter = 40f;
listLevel1.StartAt = 3;
listLevel1.NumberPrefix = "((";
listLevel1.NumberSufix = "))";
```

## API Reference

### Methods
- `ApplyDefNumberedStyle()`: Applies the default numbered list style to the current paragraph.
- `ApplyDefBulletStyle()`: Applies the default bulleted list style to the current paragraph.
- `ContinueListNumbering()`: Continues the numbering of the list from the previous paragraph.
- `IncreaseIndentLevel()`: Increases the indentation level of the list.
- `DecreaseIndentLevel()`: Decreases the indentation level of the list.

## Code Examples

### Creating Numbered Lists

```csharp
// Example of creating a numbered list
IWParagraph paragraph = section.AddParagraph();
paragraph.AppendText("First Numbered (level 0)");
paragraph.ListFormat.ApplyDefNumberedStyle();

paragraph = section.AddParagraph();
paragraph.AppendText("Level 1");
paragraph.ListFormat.ContinueListNumbering();
paragraph.ListFormat.IncreaseIndentLevel();
```

### Creating Bulleted Lists

```csharp
// Example of creating a bulleted list
IWParagraph paragraph = section.AddParagraph();
paragraph.AppendText("First bulleted (level 0)");
paragraph.ListFormat.ApplyDefBulletStyle();

paragraph = section.AddParagraph();
paragraph.AppendText("Level 1");
paragraph.ListFormat.ContinueListNumbering();
paragraph.ListFormat.IncreaseIndentLevel();
```

### Creating Mixed Lists

```csharp
// Example of creating a mixed numbered and bulleted list
ListStyle myStyle = doc.AddListStyle(ListType.Numbered, "UserStyle");
WListLevel listLevel1 = myStyle.Levels[0];
listLevel1.FollowCharacter = FollowCharacterType.Tab;
listLevel1.TextPosition = 80f;
listLevel1.NumberAlignment = ListNumberAlignment.Right;
listLevel1.TabSpaceAfter = 40f;
listLevel1.StartAt = 3;
listLevel1.NumberPrefix = "((";
listLevel1.NumberSufix = "))";
```

## RAG Annotations

<!-- tags: [DocIO, list styles, numbered lists, bulleted lists, mixed lists, indentation, Syncfusion, Winforms, version 11.4.0.26] keywords: [numbered, bulleted, mixed lists, indentation, list styles, syncfusion, winforms] -->
```