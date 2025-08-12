```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_133.jpeg
document_name: pdf
page_number: 133
page_id: pdf#page_133
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:32:20Z
fidelity: lossless
-->

# Essential PDF

## Overview
- Data to PdfLightTable can be set using specific events.
- Methods to set column and row counts dynamically.
- Dynamic data population using event handlers.

## Content

Data to PdfLightTable can also be set using the following three events:
- **QueryColumnCount** – Sets the number of columns.
- **QueryRowCount** – Sets the number of rows.
- **QueryNextRow** – Sets data to the PdfLightTable.

**Note:** These events will act only when the **DataSource** property is not set.

The following code snippet illustrates this:

```csharp
[C#]

public string[][] datastring = new string[2][];

// Giving it some column arrays
datastring[0] = new string[] { "111", "Maxim", "100" };
datastring[1] = new string[] { "222", "Calvin", "95" };

// Creating PdfLightTable
PdfLightTable pdfLightTable = new PdfLightTable();

pdfLightTable.QueryColumnCount += new
QueryColumnCountEventHandler(pdfLightTable_QueryColumnCount);
pdfLightTable.QueryNextRow += new
QueryNextRowEventHandler(pdfLightTable_QueryNextRow);
pdfLightTable.QueryRowCount += new
QueryRowCountEventHandler(pdfLightTable_QueryRowCount);

// Drawing the PdfLightTable
pdfLightTable.Draw(page, PointF.Empty);

// Getting the number of columns
void pdfLightTable_QueryColumnCount(object sender,
QueryColumnCountEventArgs args)
{
    args.ColumnCount = 3;
}

// Getting the number of rows
void pdfLightTable_QueryRowCount(object sender, QueryRowCountEventArgs args)
{
    args.RowCount = 2;
}

// Getting the row data
```

## Page-level Navigation/TOC (if applicable)
- The text provides a clear explanation of how to dynamically set data to a PdfLightTable using events.

## Code Examples (multi-language supported)
The example demonstrates the use of event handlers to populate a PdfLightTable dynamically without setting the DataSource property.

## Cross References
- Refer to documentation on PdfLightTable for more information on its methods and properties.

<!-- tags: [PdfLightTable, event handling, data population, WinForms, Syncfusion, 11.4.0.26] keywords: [PdfLightTable, QueryColumnCount, QueryRowCount, QueryNextRow, dynamic data population, WinForms, C#, event handlers] -->
```