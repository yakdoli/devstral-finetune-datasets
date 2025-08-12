```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_289.jpeg
document_name: DocIo
page_number: 289
page_id: DocIo#page_289
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:47:23Z
fidelity: lossless
-->

## Content

### Table Features

The table below outlines the various features and their supported functionality within the `DocIo` component for `Syncfusion Winforms`.

#### Table Features Summary

| Feature            | Aspect              | Supported | Notes                                     |
|--------------------|---------------------|-----------|-------------------------------------------|
| **Table**          | Cell margins        | Yes       | -                                         |
|                    | Column widths       | Yes       | -                                         |
|                    | Indent from left    | Yes       | -                                         |
|                    | Preferred width     | Yes       | -                                         |
|                    | Spacing between cells | Yes       | -                                         |
| **Table Cell**     | Borders             | Partial    | See Borders, for more details.          |
|                    | Cell margins        | Partial    | Only default table cell margins left and right are supported. |
|                    | Horizontal merge    | Yes       | -                                         |
|                    | Shading             | Partial    | See Shading, for more details.          |
|                    | Text direction      | Yes       | -                                         |
|                    | Vertical alignment  | Yes       | -                                         |
|                    | Vertical merge      | Yes       | -                                         |
| **Table Row**      | Height              | Yes       | -                                         |
|                    | Padding             | Yes       | -                                         |

#### Text Features Summary

| Feature            | Aspect              | Supported | Notes                                     |
|--------------------|---------------------|-----------|-------------------------------------------|
| **Text**          | All caps            | Yes       | -                                         |
|                    | Bold                | Yes       | -                                         |
|                    | Character spacing   | Yes       | -                                         |
|                    | Color               | Yes       | -                                         |
|                    | Emboss              | Partial    | Rendered as bold.                        |
|                    | Engrave             | Partial    | Rendered as bold.                        |
|                    | Font                | Yes       | -                                         |
|                    | Hidden              | Yes       | -                                         |
|                    | Highlighting        | Yes       | -                                         |

---

## API Reference

This section provides a reference to the relevant types and functionalities related to the features listed above. For detailed information on the specific namespaces, classes, and properties, refer to the Syncfusion Winforms API documentation.

### Namespaces and Classes

- **Syncfusion.DocIO**
  - Provides classes and methods for handling various features of the `DocIo` component.

### Members

#### Properties
- **CellMargins**: Gets or sets the margins around the cell content.
- **ColumnWidths**: Gets or sets the individual column widths in the table.
- **IndentFromLeft**: Gets or sets the indentation from the left margin.
- **PreferredWidth**: Gets or sets the preferred width of the table.
- **SpacingBetweenCells**: Gets or sets the spacing between cells.
- **Borders**: Gets or sets the border styles for table cells.
- **TextDirection**: Gets or sets the text direction (e.g., left-to-right, right-to-left).
- **VerticalAlignment**: Gets or sets the vertical alignment of text within a cell.
- **Height**: Gets or sets the height of a table row.
- **Padding**: Gets or sets the padding within a table row.
- **AllCaps**: Gets or sets whether the text is in all capital letters.
- **Bold**: Gets or sets whether the text is bold.
- **CharacterSpacing**: Gets or sets the spacing between characters.
- **Color**: Gets or sets the color of the text.
- **Hidden**: Gets or sets whether the text is hidden.
- **Highlighting**: Gets or sets the highlighting color for the text.

---

## Code Examples

### Example: Creating a Table

```csharp
using Syncfusion.DocIO;
using Syncfusion.DocIO.DLS;

// Create a new document.
WordDocument doc = new WordDocument();

// Add a new section to the document.
IWSection sec = doc.AddSection();

// Add a table to the section.
IWTable table = sec.AddTable();

// Set the table borders.
table.Borders.Width = 0.75f;
table.Borders.Color = Syncfusion.DocIO.DLS.Color.FromHtml("#000000");

// Set the table cell margins.
table.CellFormat.Margin.Left = 10;
table.CellFormat.Margin.Right = 10;

// Add rows and set content.
IWTableRow row = table.Rows[0];
row.Cells[0].AddParagraph("Row 1, Cell 1");
row.Cells[1].AddParagraph("Row 1, Cell 2");

// Add another row and set content.
row = table.Rows.Add();
row.Cells[0].AddParagraph("Row 2, Cell 1");
row.Cells[1].AddParagraph("Row 2, Cell 2");

// Save the document.
doc.Save("SampleTable.docx", SaveFormat.Docx);
```

---

### Example: Formatting Text

```csharp
using Syncfusion.DocIO;
using Syncfusion.DocIO.DLS;

// Create a new document.
WordDocument doc = new WordDocument();

// Add a new section to the document.
IWSection sec = doc.AddSection();

// Add a paragraph with formatted text.
IWParagraph para = sec.AddParagraph();
(para.AppendText("Bold Text")).Font.Bold = true;
(para.AppendText(" and Highlighted Text")).CharacterFormat.HighlightColor = Syncfusion.DocIO.DLS.Color.Blue;

// Add another paragraph with different formatting.
para = sec.AddParagraph();
(para.AppendText("Hidden Text")).Font.Hidden = true;

// Save the document.
doc.Save("FormattedText.docx", SaveFormat.Docx);
```

---

<!-- tags: [DocIo, table, cell, margins, column, width, alignment, text, formatting, bold, hidden, highlighting, syncfusion, winforms, version 11.4.0.26] keywords: [cell margins, column widths, text direction, vertical alignment, table height, text color, bold formatting, text hiding, text highlighting] -->
```