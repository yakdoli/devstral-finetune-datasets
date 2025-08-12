```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_233.jpeg
document_name: DocIo
page_number: 233
page_id: DocIo#page_233
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:43:30Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- Demonstrates how to manage list formatting and numbering styles in documents using both C# and VB.NET code examples.

## Content

### Code Examples for Managing List Formatting

#### C#

```csharp
paragraph = section.AddParagraph();
paragraph.AppendText( "First numbered" );
paragraph.ListFormat.ApplyStyle( "UserStyle" );

paragraph = section.AddParagraph();
ListStyle bulletStyle = doc.AddListStyle( ListType.Bulleted, "UserStyle1" );
WListLevel level = bulletStyle.Levels[ 0 ];
level.NumberPosition = 30f;
level.TabSpaceAfter = 15f;
level.FollowCharacter = FollowCharacterType.Tab;

paragraph.AppendText( "First bullet" );
paragraph.ListFormat.ApplyStyle( "UserStyle1" );

paragraph = section.AddParagraph();
paragraph.AppendText( "Bulleted level 1" );
paragraph.ListFormat.ContinueListNumbering();

paragraph = section.AddParagraph();
paragraph.AppendText( "Numbered level 0 again" );
paragraph.ListFormat.ApplyStyle( "UserStyle" );
section.AddParagraph();
section.AddParagraph();
```

#### VB.NET

```vb
'Write default numbered list
Dim paragraph As IWParagraph = section.AddParagraph()
paragraph.AppendText("First Numbered ( level 0 )")
paragraph.ListFormat.ApplyDefNumberedStyle()

paragraph = section.AddParagraph()
paragraph.AppendText("Level 1")
paragraph.ListFormat.ContinueListNumbering()
paragraph.ListFormat.IncreaseIndentLevel()

paragraph = section.AddParagraph()
paragraph.AppendText("Level 0")
paragraph.ListFormat.ContinueListNumbering()
paragraph.ListFormat.DecreaseIndentLevel()

section.AddParagraph()
section.AddParagraph()

'Write default bulleted list
```

### Explanation

The provided code examples illustrate how to configure and adjust list formatting and numbering styles in a document. 

- **C# Example:**
  - Adds paragraphs with different list styles and numbering options.
  - Specifies the numbering position, tab spacing, and follow character for a bulleted style.
  - Continues the list numbering and applies styles to the paragraphs.

- **VB.NET Example:**
  - Demonstrates the use of default numbered and bulleted lists.
  - Adjusts indentation levels to maintain hierarchical structure in the document.
  - Includes methods to continue numbering and indentation for structured lists.

## API Reference

#### Methods Used
- `AddParagraph()`: Creates a new paragraph in the document.
- `AppendText(String)`: Adds text to the paragraph.
- `ListFormat.ApplyStyle(String)`: Applies a predefined list style to the paragraph.
- `ListFormat.ContinueListNumbering()`: Continues the numbering sequence from the previous paragraph.
- `ListFormat.IncreaseIndentLevel()`: Increases the indentation level of the list item.
- `ListFormat.DecreaseIndentLevel()`: Decreases the indentation level of the list item.

#### Classes Used
- `ListStyle`: Represents a list style for numbered and bulleted lists.
- `WListLevel`: Represents a level in a list style.
- `FollowCharacterType`: Enum for specifying what character should follow a list item.

## Code Examples (multi-language supported)

### C# Example

The provided C# code example shows how to:
1. Create a numbered paragraph with a custom style.
2. Define a bulleted list style with specific formatting.
3. Continue numbering and indentation for structured lists.

### VB.NET Example

The VB.NET code example demonstrates:
1. Writing default numbered and bulleted lists.
2. Adjusting indentation levels and continuing list numbering to maintain document structure.

<!-- tags: [syncfusion-sdk, DocIO, list formatting, numbered lists, bulleted lists, style application, version: 11.4.0.26] keywords: [paragraph, numbering, indentation, bulleted style, list format, document styling, DocIO] -->
```