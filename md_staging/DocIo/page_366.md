```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_366.jpeg
document_name: DocIo
page_number: 366
page_id: DocIo#page_366
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:51:21Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- Demonstrates how to insert an empty table into a Word document.
- Utilizes the `ResetCells()` method to specify the number of rows and columns in the table.

## Content

### Using DocIO

The below code example shows how to insert an empty table to a Word document. The `ResetCells()` method is used to specify the number of rows and columns present in the table.

#### Code Example

```csharp
// Create a new word document
IWordDocument doc = new WordDocument();
IWSection section = doc.AddSection();

// Add a table to the document
IWTable table = section.AddTable();
table.ResetCells(3, 2);

// Save the document
doc.Save("TableDocIO.doc");
```

<!-- tags: [syncfusion, word document, table, resetcells, winforms, 11.4.0.26] keywords: [docio, word, document, table, rows, columns, resetcells, code example, csharp] -->
```