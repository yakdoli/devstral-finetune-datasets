```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_224.jpeg
document_name: DocIo
page_number: 224
page_id: DocIo#page_224
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:42:29Z
fidelity: lossless
-->

## Customizing Numbered Lists in DocIO

### Overview

- This section demonstrates how to customize numbered lists in DocIO, allowing users to define number styles, positions, and text formatting for lists in documents.

### Content

#### Customized Numbered List Style

The following dialog box is used to configure the appearance of numbered lists in your documents. It provides options to customize various aspects of the list, including number formatting, position, and text alignment.

#### Dialog Box Description

**Figure 75: Numbered List Style**

- **Number format**: The format of the list item numbers (e.g., "1.", "a.", etc.).
- **Number style**: The style of the numbers in the list, such as numerical (1, 2, 3...) or alphabetical (a, b, c...).
- **Start at**: The starting number for the list.
- **Number position**: Alignment options for the list numbers, such as left, right, or center.
- **Text position**: Defines the tab spacing and indenting for the text following the list numbers.
- **Tab space after**: The distance after the numbers where the text will begin.
- **Indent at**: The indentation level for the text in the list.

In the **Preview** section, the anticipated appearance of the customized numbered list is displayed, showing the alignment and spacing applied.

#### Example

The dialog box in the figure illustrates creating a numbered list with the following customizations:
- Number format: "1."
- Number style: "1, 2, 3..."
- Start at: 1
- Number position: Left
- Tab space after: 0.25"
- Indent at: 0.25"

The **Preview** section shows the expected output of the list, with each item numbered consecutively, followed by a 0.25-inch tab space and indented 0.25 inches.

#### Usage

To apply these customizations:
1. Open the **Customize Numbered List** dialog box.
2. Configure the settings as per the requirements.
3. Click **OK** to apply the changes.

## API Reference

### Methods and Properties

You can programmatically customize numbered lists using the following APIs:

- `NumberFormat` property: Sets the number format of the list.
- `NumberStyle` property: Defines the style of the numbers (numerical, alphabetical, etc.).
- `StartPosition` property: Sets the starting number for the list.
- `NumberPosition` property: Manages the alignment of the numbers in the list.
- `TabSpaceAfter` property: Configures the tab spacing after the numbers.
- `IndentDistance` property: Manages the indenting for the text following the numbers.

```csharp
// Example usage in code
NumberedList.numberFormat = "1.";
NumberedList.numberStyle = ListNumberStyle.Numerical;
NumberedList.startPosition = 1;
NumberedList.numberPosition = HorizontalAlignment.Left;
NumberedList.tabSpaceAfter = 0.25;
NumberedList.indentDistance = 0.25;
```

## Code Examples

Here is a sample C# code snippet demonstrating how to programmatically customize a numbered list:

```csharp
using Syncfusion.DocIO;
using Syncfusion.DocIO.DWord;

// Create a new document
WordDocument document = new WordDocument();

// Add a numbered list
NumberedList numberedList = document.AddNumberedList();
numberedList.NumberFormat = "1.";
numberedList.NumberStyle = ListNumberStyle.Numerical;
numberedList.StartPosition = 1;
numberedList.NumberPosition = HorizontalAlignment.Left;
numberedList.TabSpaceAfter = 0.25F;
numberedList.IndentDistance = 0.25F;

// Add list items
numberedList.AddListItem("First item");
numberedList.AddListItem("Second item");
numberedList.AddListItem("Third item");

// Save the document
document.Save("CustomNumberedList.docx", vsSaveFormat.Docx);
```

## RAG Annotations

<!-- tags: [syncfusion, winforms, numbered lists, customization, DocIO, version:11.4.0.26] keywords: [customization, numbered lists, number format, number style, position, DocIO, Syncfusion] -->
```