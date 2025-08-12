```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_228.jpeg
document_name: DocIo
page_number: 228
page_id: DocIo#page_228
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:42:50Z
fidelity: lossless
-->

# Essential DocIO

```csharp
paragraph.AppendText("Level 1");
paragraph.ListFormat.ContinueListNumbering();
paragraph.ListFormat.IncreaseIndentLevel();

paragraph = section.AddParagraph();
paragraph.AppendText("Level 0");
paragraph.ListFormat.ContinueListNumbering();
paragraph.ListFormat.DecreaseIndentLevel();

// User numbered list style
ListStyle newStyle = doc.AddListStyle(ListType.Numbered, "NewStyle");
WListLevel listLevelNew = newStyle.Levels[0];
listLevelNew.FollowCharacter = FollowCharacterType.Tab;
listLevelNew.TextPosition = 80f;
listLevelNew.NumberAlignment = ListNumberAlignment.Right;
listLevelNew.TabSpaceAfter = 40f;
listLevelNew.StartAt = 2;
listLevelNew.NumberPrefix = ">>";
listLevelNew.NumberSuffix = "<<";
listLevelNew.CharacterFormat.FontSize = 15;
listLevelNew.CharacterFormat.TextColor = Color.Blue;

WListLevel listLevelNew1 = newStyle.Levels[1];
listLevelNew1.IsLegalStyleNumbering = true;

WListLevel listLevelNew2 = newStyle.Levels[2];
listLevelNew1.NoRestartByHigher = true;

paragraph = section.AddParagraph();
paragraph.AppendText("First Numbered ( level 0 )");
paragraph.ListFormat.ApplyStyle("NewStyle");

paragraph = section.AddParagraph();
paragraph.AppendText("Level 1");
paragraph.ListFormat.ContinueListNumbering();
paragraph.ListFormat.IncreaseIndentLevel();

paragraph = section.AddParagraph();
paragraph.AppendText("Level 0");
paragraph.ListFormat.ContinueListNumbering();
paragraph.ListFormat.ListLevelNumber = 0;
```

### VB.NET
```vbnet
[VB.NET]
```

## Page-level Navigation/TOC (if applicable)

<!-- tags: [DocIO, list formatting, numbered lists, indentation, custom styles, MS Word integration, code examples] keywords: [paragrah, listFormat, indentation, numbered lists, custom list styles, color formatting, font size, WordML, MS Word] -->
```