```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_123.jpeg
document_name: DocIo
page_number: 123
page_id: DocIo#page_123
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:35:38Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- Focuses on Table Properties in Document Formats.
- Describes row formatting options within the Table Properties dialog box.
- Lists public properties related to table formatting and layout.

## Content

### Table Properties

This section showcases the row format options available within the Table Properties dialog box, as illustrated in the figure below.

#### Figure 40: Row Format Options in Table Properties Dialog Box

The dialog box allows users to specify various row properties, including size, options, and more. Key features are:

- **Size**
  - **Row 83:**
    - Specify Height: Enabled with a value of `0.28"` set.
    - Row Height is: Set to "At least."

- **Options**
  - Allow row to break across pages:Checked.
  - Repeat as header row at the top of each page: Unchecked.

Navigation buttons for "Previous Row" and "Next Row" are available for sequential adjustment.

### Public Properties

This section defines the public properties available for table formatting and alignment.

| Name                 | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| Bidi                 | Gets or sets whether the table is right-to-left.                         |
| Borders              | Gets borders.                                                             |
| CellSpacing          | Gets or sets spacing between cells (in points).                         |
| HorizontalAlignment  | Gets or sets horizontal alignment for the paragraph.                   |
| IsAutoResized        | Gets or sets the boolean value indicating if the table is auto resized. |
| IsBreakAcrossPages   | Gets or sets the boolean value indicating if there is a break across pages. |

## Code Examples

The table properties and public methods can be utilized in various programming contexts using the Syncfusion Winforms SDK. Below is an example demonstrating how these properties can be accessed programmatically.

```csharp
// Accessing and setting table properties using public methods
Table currentTable = document.LastSection.Tables[0];
currentTable.Bidi = true;
currentTable.CellSpacing = 5;
currentTable.IsAutoResized = false;
currentTable.IsBreakAcrossPages = true;
```

## Page-level Navigation/TOC (if applicable)
- [overview of Table Properties]
- [detailed explanation of row format options]
- [list of public properties for table formatting]

## Cross References
- See also: [Table Operations in Document Formatting], [Advanced Table Properties in Essential DocIO]

## RAG Annotations
<!-- tags: Document Formatting, Tables, Row Properties, Public Properties keywords: Table Properties, Row Format Options, Bidi, CellSpacing, HorizontalAlignment, IsAutoResized, IsBreakAcrossPages -->
```