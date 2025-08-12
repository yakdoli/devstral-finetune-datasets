```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_198.jpeg
document_name: DocIo
page_number: 198
page_id: DocIo#page_198
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:40:25Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- Note: DocIO can't create Outline levels. However, enabling UseOutlineLevels property allows TOC creation from existing outline levels.
- Public methods for managing TOC styles.
- Code example demonstrating custom TOC insertion using custom styles.

## Content

### Note: DocIO and Outline Levels
DocIO cannot create Outline levels, but enabling the UseOutlineLevels property allows TOC creation from existing outline levels. Figure 69 shows the outline levels configuration in a paragraph settings window.

![Figure 69: Outline Levels](https://i.imgur.com/9X9X9X9.jpg)

### Public Methods
The following table lists the public methods for managing TOC styles:

| Name                | Description                                          |
|---------------------|------------------------------------------------------|
| GetTOCLevelStyleName | Gets the style name for TOC level.                  |
| SetTOCLevelStyle    | Sets the style for TOC level.                        |

### Code Example: Inserting TOC Based on Custom Styles
The following C# code demonstrates how to insert a TOC based on custom styles:

```csharp
WordDocument doc = new WordDocument();
doc.EnsureMinimal();

WParagraph para = doc.LastParagraph;
TableOfContent toc = para.AppendTOC(1, 1);

toc.UseHeadingStyles = false;

// Set the TOC level style based on which the TOC should be created.
toc.SetTOCLevelStyle(1, "MyStyle1");
```

## API Reference

### Methods
- **GetTOCLevelStyleName**
  - **Description:** Gets the style name for TOC level.
- **SetTOCLevelStyle**
  - **Description:** Sets the style for TOC level.

## Code Examples

### C#
The provided code example illustrates how to insert a TOC using custom styles in a Word document. This example demonstrates the use of the `SetTOCLevelStyle` method to specify a custom style for the TOC.

```csharp
// Create a new Word document and ensure minimal formatting.
WordDocument doc = new WordDocument();
doc.EnsureMinimal();

// Get the last paragraph in the document.
WParagraph para = doc.LastParagraph;

// Append a Table of Contents (TOC) with specific parameters.
TableOfContent toc = para.AppendTOC(1, 1);

// Disable heading styles for the TOC.
toc.UseHeadingStyles = false;

// Set the TOC level style using the custom style "MyStyle1".
toc.SetTOCLevelStyle(1, "MyStyle1");
```

## RAG Annotations
<!-- tags: DocIO, TOC, Outline Levels, Table of Contents, Custom Styles, Public Methods keywords: DocIO, TOC, UseOutlineLevels, TOC Styles, Custom TOC, Public Methods, GetTOCLevelStyleName, SetTOCLevelStyle -->
```