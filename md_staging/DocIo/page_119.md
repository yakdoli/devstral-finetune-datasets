```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_119.jpeg
document_name: DocIo
page_number: 119
page_id: DocIo#page_119
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:35:21Z
fidelity: lossless
-->

## Summary of Table Cell Properties and Methods in DocIO

The page provides an overview of the `WTableCell` class in the `DocIO` library, detailing its constructors, properties, and methods for managing table cells in word documents. It emphasizes non-default formatting options and includes code examples for customization.

### Table Properties and Methods

#### Overview
- **VerticalAlignment**: Gets or sets the vertical alignment of the cell content.
- **VerticalMerge**: Gets or sets the way of vertical merging of the cell.
- The `WTableCell` class allows for comprehensive control over cell formatting and layout.

#### Public Constructor
| Name                                   | Description                                    |
|----------------------------------------|------------------------------------------------|
| WTableCell.WTableCell(IWordDocument)  | Initializes a new instance of the `WTableCell` class. |

#### Public Properties
| Name         | Description                                               |
|--------------|-----------------------------------------------------------|
| CellFormat   | Gets cell format.                                        |
| EntityType   | Gets the type of the entity.                             |
| OwnerRow     | Gets owner row of the cell.                             |
| Width        | Gets or sets the cell width (in points).                |

#### Public Methods
| Name       | Description                         |
|------------|-------------------------------------|
| Clone      | Clones this instance.              |
| GetCellIndex | Get cell index in the table row. |

### Example: Creating a Table with Non-Default Formatting

The following example demonstrates how to create a table with custom formatting in a Word document using C#.

```csharp
// C#

paragraph = section.AddParagraph();
paragraph.AppendText("Table with different formatting");
paragraph = section.AddParagraph();

// Add a table
table = section.AddTable();

// Set number of rows and columns
table.ResetCells(3, 3);
table.TableFormat.Borders.LineWidth = 2f;
```

### How the Example Works
- The code snippet initializes a table by adding a paragraph describing the table's purpose.
- It creates a table with 3 rows and 3 columns, setting the border width to 2 points for non-default formatting.

### Key Features
- **Custom Formatting**: Allows modification of cell dimensions and styles.
- **Fluent Interface**: Enables method chaining for concise and readable code.
- **Flexibility**: Supports dynamic table creation and customization.

### See Also
- DocIO documentation for comprehensive table formatting options.
- `IWordDocument` interface for additional document manipulation features.

<!-- tags: DocIO, WTableCell, Table Formatting, DocIO Table Properties, Syncfusion Winforms, Version: 11.4.0.26 -->
```