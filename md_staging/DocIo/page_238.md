```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_238.jpeg
document_name: DocIo
page_number: 238
page_id: DocIo#page_238
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:43:15Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- This page provides details about the properties and methods of the WTextBox class and its associated TextBoxFormat class, which are used for managing textboxes within documents.
- It includes explanations of various attributes such as line width, alignment, and formatting options for textboxes.

## Content

### Properties

| Property         | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| LineWidth        | Gets or sets the line width of textbox (in points).                       |
| NoLine           | Gets or sets value which defines if there is a line around textbox shape. |
| TextWrappingStyle| Gets or sets text Wrapping style.                                         |
| TextWrappingType | Gets or sets wrapping type for textbox.                                   |
| VerticalAlignment| Gets or sets vertical alignment of textbox.                               |
| VerticalOrigin   | Gets or sets vertical origin.                                             |
| VerticalPosition | Gets or sets the textbox vertical position (in points).                   |
| Width            | Gets or sets the textbox width (in points).                               |

### Public Methods

| Name   | Description                |
|--------|----------------------------|
| Clone  | Clones textbox format.    |

#### Example Usage

The following example illustrates how to use the WTextBox and TextBoxFormat classes.

```csharp
IWordDocument doc = new WordDocument();
IWSection section = doc.AddSection();
IParagraph paragraph = section.AddParagraph();
section.PageSetup.DifferentFirstPage = true;
section.PageSetup.DifferentOddAndEvenPages = true;

// Main doc textboxes
paragraph.AppendText("Testing textboxes");

// 1 textbox
IWTextBox mainTextbox = paragraph.AppendTextBox(150, 110);
mainTextbox.TextBoxBody.AddParagraph().AppendText("Textbox text 1");
mainTextbox.TextBoxFormat.FillColor = System.Drawing.Color.Blue;
mainTextbox.TextBoxFormat.LineDashing = LineDashing.LongDashDotDotGEL;
mainTextbox.TextBoxFormat.LineWidth = 4.0f;

// 2 textbox
IWTextBox mainTextbox1 = paragraph.AppendTextBox(150, 100);
```

## API Reference

### Namespace: Syncfusion.DocIO
- Properties and methods for managing textboxes in a document.

### Members

- **LineWidth**: Gets or sets the line width of textbox (in points).
- **NoLine**: Gets or sets value which defines if there is a line around textbox shape.
- **TextWrappingStyle**: Gets or sets text Wrapping style.
- **TextWrappingType**: Gets or sets wrapping type for textbox.
- **VerticalAlignment**: Gets or sets vertical alignment of textbox.
- **VerticalOrigin**: Gets or sets vertical origin.
- **VerticalPosition**: Gets or sets the textbox vertical position (in points).
- **Width**: Gets or sets the textbox width (in points).

#### Clone Method
- Clones textbox format.

## Code Examples

### Creating and Customizing a Textbox

```csharp
// Creating a textbox with custom formatting
IWTextBox mainTextbox = paragraph.AppendTextBox(150, 110);
mainTextbox.TextBoxBody.AddParagraph().AppendText("Textbox text 1");
mainTextbox.TextBoxFormat.FillColor = System.Drawing.Color.Blue;
mainTextbox.TextBoxFormat.LineDashing = LineDashing.LongDashDotDotGEL;
mainTextbox.TextBoxFormat.LineWidth = 4.0f;
```

### Multiple Textboxes

```csharp
// Adding another textbox
IWTextBox mainTextbox1 = paragraph.AppendTextBox(150, 100);
```

<!-- tags: [DocIO, WTextBox, TextBoxFormat, textboxes, document formatting, Syncfusion Winforms] keywords: [properties, methods, line width, text wrapping, vertical alignment, textbox management] -->
```