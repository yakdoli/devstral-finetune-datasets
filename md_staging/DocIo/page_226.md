```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_226.jpeg
document_name: DocIo
page_number: 226
page_id: DocIo#page_226
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:42:31Z
fidelity: lossless
-->

# Essential DocIO

## Overview

- This page details the properties and methods of the `WListLevel` class within the Syncfusion Winforms SDK.
- The `WListLevel` class is used to represent and customize list level options in Word documents.

## Content

### WListLevel Class

The `WListLevel` class represents list level in the Word document. By using the `WListLevel` class, you can customize the list level options.

#### Public Constructor

| Name | Description |
| --- | --- |
| `WListLevel.WListLevel (ListStyle)` | Initializes new instance of `WListLevel` class. |

#### Public Methods

| Name | Description |
| --- | --- |
| `Clone` | Clones this instance. |
| `GetListLevelText` | Gets list symbol for specified item index. |

#### Public Properties

| Name | Description |
| --- | --- |
| `BulletCharacter` | Gets or sets bullet pattern. |
| `CharacterFormat` | Gets or sets character formats of list symbol. |
| `FollowCharacter` | Gets or sets the type of character following the number text for the paragraph. |
| `IsLegalStyleNumbering` | Gets or sets ArabicNumberFormat property ( true if the level turns all inherited numbers to arabic, false if it preserves their number format code ). |
| `NoRestartByHigher` | True if the level's number sequence is not restarted by higher (more significant) levels in the list. |
| `NumberAlignment` | Gets or sets alignment (left, right, or centered) of the paragraph number. |

## API Reference

### Namespace: Syncfusion.DocIO.DLS

#### Class: WListLevel

##### Methods
- `Clone()`: Clones this instance.
- `GetListLevelText(index)`: Gets list symbol for specified item index.

##### Properties
- `BulletCharacter`: Gets or sets bullet pattern.
- `CharacterFormat`: Gets or sets character formats of list symbol.
- `FollowCharacter`: Gets or sets the type of character following the number text for the paragraph.
- `IsLegalStyleNumbering`: Gets or sets ArabicNumberFormat property.
- `NoRestartByHigher`: Indicates if the level's number sequence is not restarted by higher (more significant) levels in the list.
- `NumberAlignment`: Gets or sets alignment of the paragraph number.

## Code Examples (C#)

```csharp
using Syncfusion.DocIO.DLS;

// Example: Creating a new WListLevel and setting properties
WListLevel newLevel = new WListLevel(new ListStyle());

// Set the bullet character
newLevel.BulletCharacter = "•";

// Set the alignment of the paragraph number
newLevel.NumberAlignment = HorizontalAlignment.Center;

// Customize the character format of the list symbol
newLevel.CharacterFormat.Bold = true;

// Additional customization as needed
```

## RAG Annotations

<!-- tags: [Syncfusion Winforms, DocIO, WListLevel, ListStyle, ListLevel, Word Document customization] keywords: [WListLevel, BulletCharacter, CharacterFormat, FollowCharacter, IsLegalStyleNumbering, NoRestartByHigher, NumberAlignment, Clone, GetListLevelText] -->
```