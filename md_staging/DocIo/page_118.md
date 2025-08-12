```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_118.jpeg
document_name: DocIo
page_number: 118
page_id: DocIo#page_118
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:35:01Z
fidelity: lossless
-->

# Essential DocIO

## Table Properties - Cell Format Options

### Overview
- The *Cell Format Options* dialog box allows users to customize cell properties in a table.
- This includes settings for cell margins, text wrapping, and alignment options.
- The public properties listed detail how these settings can be programmatically accessed and modified.

## Content

### Visual Representation of Cell Format Options

![Figure 39: Cell Format Options in Table Properties Dialog Box](image.png)

#### Description

The image depicts the *Cell Format Options* dialog box within the *Table Properties* interface. This dialog allows the user to:
- Adjust cell margins individually or keep them consistent.
- Enable text wrapping with the *Wrap text* option.
- Choose between different alignment settings for vertical alignment (Top, Center, Bottom).

### WinForms-specific Cell Format Properties

#### Cell Format Public Properties

| **Name**          | **Description**                                                                 |
|-------------------|---------------------------------------------------------------------------------|
| **BackColor**     | Gets or sets background color.                                                 |
| **Borders**       | Gets borders.                                                                 |
| **FitText**       | Gets or sets fit text option.                                                  |
| **HorizontalMerge** | Gets or sets the way of horizontal merging of the cell.                        |
| **Paddings**      | Gets paddings.                                                                |
| **TextDirection** | Gets or sets cell text direction.                                              |
| **TextWrap**      | Gets or sets a value indicating whether text wrap is enabled.                  |

## API Reference

### Public Properties

The following table summarizes the public properties related to cell formatting in Syncfusion Winforms:

#### Description

The properties listed below are available for adjusting various aspects of a cell in a table. They can be accessed or modified programmatically as needed.

| **Name**           | **Description**                                                                 |
|--------------------|---------------------------------------------------------------------------------|
| **BackColor**      | Gets or sets the background color of the cell.                                 |
| **Borders**        | Retrieves the cell borders.                                                   |
| **FitText**        | Gets or sets whether the text is resized to fit within the cell dimensions.    |
| **HorizontalMerge** | Controls how the cells are horizontally merged.                               |
| **Paddings**       | Gets or sets the padding values for the cell.                                 |
| **TextDirection**  | Gets or sets the direction in which the text is displayed within the cell.     |
| **TextWrap**       | Indicates whether text wrapping is enabled for the cell.                      |

### Usage Example

Here’s a sample code snippet demonstrating how to modify some of these properties programmatically:

```csharp
// Example: Changing background color and enabling text wrap
cell.BackColor = System.Drawing.Color.LightGray;
cell.TextWrap = true;
cell.Paddings = new System.Drawing.Padding(5);
```

## Page-level Navigation/TOC
- This is the main content block for the document section titled "Cell Format Options."
- The section includes explanations and a reference to public properties available for cell formatting in Syncfusion Winforms.

## Cross References
- Refer to the *Table Properties* section for more information on overall table formatting.
- For additional formatting options, consult the documentation on *Row* and *Column* properties.

### RAG Annotations
<!-- tags: table-properties, cell-formatting, text-wrapping, vertical-alignment, public-properties, syncfusion-winforms keywords: essential docio, cell format, table properties dialog box, public properties, syncfusion, winforms -->

```