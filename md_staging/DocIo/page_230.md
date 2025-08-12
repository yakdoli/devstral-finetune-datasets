```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_230.jpeg
document_name: DocIo
page_number: 230
page_id: DocIo#page_230
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:42:48Z
fidelity: lossless
-->

# Essential DocIO

```csharp
listLevelNew1.NoRestartByHigher = True;

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

### 4.4.2.5.1 List Format

The `WListFormat` class defines the formatting for DocIO list paragraphs. The type of the list is specified by using the `ListType` property of `WListFormat`. The `ListLevelNumber` property defines the level number for the list paragraph. The `CurrentListStyle` property defines the list style applied for the current list paragraph. The `CurrentListLevel` property returns the object of the `WListLevel` type, which defines the formatting for the list level (paragraph). For example, it defines values such as the starting point for numbered lists, list symbols, alignment of list text, and so forth.

- To apply default bullet or numbered style to the paragraph, use `ApplyDefBulletStyle` or `ApplyDefNumberedStyle` function.
- To apply custom style, use `ApplyStyle` function.
- Use `ContinueListNumbering` function to continue previous list numbering.
- Use `IncreaseIndentLevel` or `DecreaseIndentLevel` to increase or decrease indent for the level.
- To remove list from the paragraph, use `RemoveList` function.

#### Class Hierarchy

```plaintext
FormatBase
└── WListFormat
```

#### Public Constructor

| Name          | Description |
|---------------|-------------|
| (Constructor) |             |

---

<!-- tags: [DocIO, WinForms, ListFormat, WListFormat, list types, indent levels, numbered lists, bullet lists] keywords: [DocIO, list formatting, levels, numbering, indents, styles] -->
```