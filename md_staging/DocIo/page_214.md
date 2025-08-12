```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_214.jpeg
document_name: DocIo
page_number: 214
page_id: DocIo#page_214
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:41:33Z
fidelity: lossless
-->

# Essential DocIO

## Style

### Public Constructor 

| Name                                | Description                                                                      |
|-------------------------------------|----------------------------------------------------------------------------------|
| WParagraphStyle.WParagraphStyle <br/> (IWordDocument)       | Initializes a new instance of the WParagraphStyle class. |

### Public Properties 

| Name         | Description                                  |
|--------------|----------------------------------------------|
| BaseStyle    | Gets a base style of paragraph.             |
| ParagraphFormat | Gets formatting of paragraph.          |
| StyleType    | Gets the type of the style.                |

### Public Methods 

| Name              | Description                     |
|-------------------|---------------------------------|
| ApplyBaseStyle    | Applies base style for current style. |
| Clone             | Clones itself.                |

## Overview

- 1. Introduces the WParagraphStyle class for managing paragraph styles.
- 2. Explains the constructor and properties for working with paragraph styles.
- 3. Demonstrates creating user-defined paragraph styles using DocIO.

## Content

### Step-by-Step Guide to Creating User-Defined Paragraph Styles

The following example illustrates how to create user-defined paragraph styles by using DocIO.

#### Code Example

```csharp
// Create a new WordDocument
IWordDocument doc = new WordDocument();

// Add a new paragraph style named "Normal"
IParagraphStyle style = (IParagraphStyle)doc.AddParagraphStyle("Normal");

// Add a new paragraph style named "UserStyle_Heading1"
style = (IParagraphStyle)doc.AddParagraphStyle("UserStyle_Heading1");
style.CharacterFormat.Bold = true;
style.CharacterFormat.FontName = "Verdana";
style.CharacterFormat.FontSize = 25;

// Add another new paragraph style named "UserStyle_Heading2"
style = (IParagraphStyle)doc.AddParagraphStyle("UserStyle_Heading2");
```

## API Reference

### Class: WParagraphStyle

#### Constructors

##### WParagraphStyle.WParagraphStyle (IWordDocument)
- **Description**: Initializes a new instance of the WParagraphStyle class.

#### Properties

##### BaseStyle
- **Type**: WParagraphStyle
- **Description**: Gets a base style of paragraph.

##### ParagraphFormat
- **Type**: ParagraphFormat
- **Description**: Gets formatting of paragraph.

##### StyleType
- **Type**: StyleType
- **Description**: Gets the type of the style.

#### Methods

##### ApplyBaseStyle
- **Description**: Applies base style for current style.

##### Clone
- **Description**: Clones itself.

## Code Examples

### C#

```csharp
IWordDocument doc = new WordDocument();
IParagraphStyle style = (IParagraphStyle)doc.AddParagraphStyle("Normal");

style = (IParagraphStyle)doc.AddParagraphStyle("UserStyle_Heading1");
style.CharacterFormat.Bold = true;
style.CharacterFormat.FontName = "Verdana";
style.CharacterFormat.FontSize = 25;

style = (IParagraphStyle)doc.AddParagraphStyle("UserStyle_Heading2");
```

## Cross References

See also:
- [DocIO API Documentation](#)
- [Working with Styles in DocIO](#)

<!-- tags: [syncfusion, winforms, wparagraphstyle, docio, styles, paragraph styles] keywords: [paragraph, formatting, styletype, applybasestyle, clone, bold, fontname, fontsize] -->
```