```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_117.jpeg
document_name: DocIo
page_number: 117
page_id: DocIo#page_117
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:35:45Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- Describes the properties and methods of a table row in the Word document.
- Highlights the Table Cell class functionality in a Word document.
- Explains how to format table cells using the CellFormat property.

## Content

### Properties of a Table Row

The following table lists the properties of a table row in a Word document.

| Name         | Description                                                                 |
|--------------|-----------------------------------------------------------------------------|
| Cells        | Gets or sets cell collection.                                              |
| ChildEntities| Gets the child entities.                                                   |
| EntityType   | Gets the type of the entity.                                               |
| Height       | Gets or sets the height of the row (in points).                            |
| HeightType   | Get or set table row height type.                                          |
| IsHeader     | Gets or sets whether the row is a table header.                            |
| RowFormat   | Gets table format.                                                         |

---

### Public Methods of a Table Row

The following table lists the public methods of a table row in a Word document.

| Name        | Description                                                                |
|-------------|-----------------------------------------------------------------------------|
| AddCell     | Adds a cell.                                                               |
| Clone       | Clones this instance.                                                      |
| GetRowIndex | Returns index of the row in owner table.                                   |
| WTableRow   | Initializes a new instance of the WTableRow class.                         |

---

### 4.3.3.2 Table Cell

#### Overview

The WTableCell class represents a table cell in the Word document. WTextBody is the base class of WTableCell, which means that a WTableCell object can hold paragraphs. You can format the table cell by using the CellFormat property. This property returns the value of the CellFormat type.

#### Example

The following screenshot illustrates how to set the Cell Format in MS Word.

```html
<!-- tags: DocIO, TableRow, TableCell, CellFormat, WTextBody, WTableCell keywords: TableRow properties, TableHeader, TableCell formatting, CellFormat, WTextBody base class -->
```
```