```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_250.jpeg
document_name: DocIo
page_number: 250
page_id: DocIo#page_250
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:44:02Z
fidelity: lossless
-->

## Overview
- Describes methods and properties related to `TextSelection`.
- Explains how to use the `TextSelection` class to find and manipulate text ranges.
- Discusses the `TextBodyPart` class for handling body items such as paragraphs, tables, and sections.

## Content

### TextSelection Class

The following table lists the methods and properties of the `TextSelection` class:

| Name           | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| GetAsOneRange  | Gets as one range.                                                          |
| GetEnumerator  | Returns an enumerator that iterates through a collection.                  |
| GetRanges       | Gets the ranges.                                                            |
| this\[int]      | Gets the `System.String` at the specified index.                          |

**Note:** `TextSelection` and `GetAsOneRange` should not be used for text replacement.

The following example illustrates how to use the `TextSelection` class.

#### Example: Using the TextSelection Class

**C#**
```csharp
docTemplate.Open( FINDTEMPLATE );
TextSelection rangesHolder1 = docSource1.Find( "The PlaceHolder1", false, false );
```

**VB.NET**
```vbnet
docTemplate.Open(FINDTEMPLATE)
Dim rangesHolder1 As TextSelection = docSource1.Find("The PlaceHolder1", False, False)
```

### 4.5.2 TextBodyPart

**TextBodyPart** class contains the collection of body items (it means that `TextBodyPart` can contain paragraphs, tables, and even sections). `TextBodyPart` is usually used with the Bookmark Navigator.

**Note:** `TextBodyPart` contains the copy of objects from the documents (paragraph(s), table(s), section(s), etc). So if you modify the content of the `TextBodyPart`, it does not affect the objects inside the document.

#### Public Constructors

| Name                        | Description                                     |
|-----------------------------|-------------------------------------------------|
| `TextBodyPart.TextBodyPart()` | Initializes a new instance of the `TextBodyPart` class. |

## API Reference

### Constructors
- `TextBodyPart.TextBodyPart()`  
  Initializes a new instance of the `TextBodyPart` class.

## Code Examples

### C#
```csharp
docTemplate.Open( FINDTEMPLATE );
TextSelection rangesHolder1 = docSource1.Find( "The PlaceHolder1", false, false );
```

### VB.NET
```vbnet
docTemplate.Open(FINDTEMPLATE)
Dim rangesHolder1 As TextSelection = docSource1.Find("The PlaceHolder1", False, False)
```

## Page-level Navigation/TOC (if applicable)

- TextSelection Class
  - Methods and Properties
    - GetAsOneRange
    - GetEnumerator
    - GetRanges
    - this\[int]
  - Example Usage
- 4.5.2 TextBodyPart
  - Description
  - Public Constructors
  - Code Examples

## Cross References

- See also: `TextSelection`, `BookmarkNavigator`, `Find`, `Paragraph`, `Table`, `Section`

<!-- tags: [DocIo, TextSelection, TextBodyPart, WinForms, Syncfusion] keywords: [TextSelection, GetAsOneRange, GetEnumerator, GetRanges, TextBodyPart, Bookmark Navigator, Paragraph, Table, Section] -->
```