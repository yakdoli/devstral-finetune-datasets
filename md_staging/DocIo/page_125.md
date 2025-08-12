```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_125.jpeg
document_name: DocIo
page_number: 125
page_id: DocIo#page_125
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:36:12Z
fidelity: lossless
-->

# Essential DocIO

## Overview

- This page discusses the application of built-in table styles in Microsoft Word using the API provided by Syncfusion. It explains how to apply predefined table styles to enhance the visual presentation of tables in a document.

## Content

### Table Styles

The screenshot below shows the assortment of built-in table styles available in Word. These styles offer a variety of designs to choose from, enhancing the visual appeal and organization of tables within a document.

#### Figure 41: Table Styles

The figure includes a grid of table styles categorized under "Plain Tables" and "Built-In". Each cell within the grid represents a different table style, allowing users to easily apply a desired visual theme to their tables. Additional features like "Modify Table Style...", "Clear", and "New Table Style..." are available for customizing the styles further.

#### Applying Built-In Table Styles

You can apply the Word built-in table styles by using the `WTable.ApplyStyle` method with the `BuiltInTableStyle` enumeration parameter. This parameter specifies the built-in table style to be applied.

## API Reference

### Methods

- **`WTable.ApplyStyle(BuiltInTableStyle style)`**
  - **Description**: Applies one of the built-in table styles to the current table.
  - **Parameters**:
    - `style`: Specifies the type of built-in table style to apply. It is an enumeration value from the `BuiltInTableStyle` class.
  - **Returns**: `void`
  - **Example**:
    ```csharp
    // Apply the first built-in table style to a table
    WTable table = document.InsertTable(new[] { "Column 1", "Column 2" }, new[] { "Row 1", "Row 2" });
    table.ApplyStyle(BuiltInTableStyle.TableGrid);
    ```

## Code Examples

### Example: Applying a Built-In Table Style

```csharp
using Syncfusion.DocIO;
using Syncfusion.DocIO.DLS;

// Create a new Word document
WDocument document = new WDocument();

// Insert a table
WTable table = document.InsertTable(new[] { "Header 1", "Header 2" }, new[] { "Row 1", "Row 2" });

// Apply a built-in table style (e.g., TableGrid)
table.ApplyStyle(BuiltInTableStyle.TableGrid);

// Save the document
document.Save("output.docx");
```

## RAG Annotations

<!-- tags: [Syncfusion, Winforms, Word, DocIO, table styles, built-in styles, WTable, BuiltInTableStyle] keywords: [TableGrid, ApplyStyle, built-in styles, styles, table formatting, visual enhancement, table design] -->
```