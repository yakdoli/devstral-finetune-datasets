```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_200.jpeg
document_name: edit
page_number: 200
page_id: edit#page_200
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:05:30Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- Discusses parsing modes for text editing in Windows Forms.
- Highlights options for balancing performance and accuracy in syntax highlighting and other text features.
- Provides code examples for setting parsing modes in C# and VB.NET.

## Content

### Parsing Modes

When ParsingMode is set to **FullParsing**, the text in the Edit Control is parsed completely and accurately, applying features like syntax highlighting, outlining, bracket highlighting, indentation guidelines, etc. **FullParsing** is time-consuming and may freeze the Edit Control until parsing is complete. It is ideal for small files only.

When ParsingMode is set to **PartialParsingNoFallback**, text parsing is done on a need basis, i.e., only displayed regions are parsed. This mode is not always accurate, potentially causing incorrect application of features like syntax highlighting, outlining, and bracket highlighting. It is the fastest ParsingMode and should be used for large file handling.

When ParsingMode is set to **PartialParsingWithFallback**, text parsing is also done on a need basis. However, if the text gets incorrectly parsed, the incorrectly parsed text is treated as regular "Text" format. Features like syntax highlighting, outlining, Bracket highlighting, and indentation guidelines are applied as per Text format specifications.

#### Code Examples

- **[C#]**

```csharp
// ParsingMode is set to FullParsing.
this.editControl1.ParsingMode =
Syncfusion.Windows.Forms.Edit.Enums.TextParsingMode.FullParsing;
```

- **[VB.NET]**

```vb
' ParsingMode is set to FullParsing.
Me.editControl1.ParsingMode =
Syncfusion.Windows.Forms.Edit.Enums.TextParsingMode.FullParsing
```

### Clearing/Flushing Saved Changes

- **MarkChangedLines**: When used in the Edit control, changed lines are denoted by a yellow color indicator, and saved lines are indicated by a green color indicator.
- **FlushChanges()**: Calling this method removes changes made in the editor after the last save, while preserving the saved lines.

<!-- tags: [edit, parsing, windows-forms, syntax-highlighting, text-editing, partial-parsing, full-parsing, flushchanges, markchangedlines] keywords: [Syncfusion Windows Forms, FullParsing, PartialParsingNoFallback, PartialParsingWithFallback, MarkChangedLines, FlushChanges] -->
```