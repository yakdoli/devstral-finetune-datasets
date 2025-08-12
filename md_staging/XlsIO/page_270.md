```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_270.jpeg
document_name: XlsIO
page_number: 270
page_id: XlsIO#page_270
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:05:26Z
fidelity: lossless
-->

# Essential XlsIO

## Overview

- Calculated fields in PivotTables perform calculations using formulas that reference other fields in the pivot table.
- Formulas can include operators, expressions, constants, and data from PivotTables.
- XlsIO supports reading and creating calculated fields in existing pivot tables.
- MS Excel restriction: Avoid cell references, defined names, and array functions in formulas.

## Content

### Calculated Fields in PivotTables

Calculated fields are a special type of database field that perform calculations by using the contents of other fields in the pivot table with the given formula. The formula can contain operators and expressions as in other worksheet formulas. You can use constants and refer to data from the PivotTable. XlsIO supports reading and creating the Calculated Fields in the existing pivot table. The following are MS Excel restriction when using the formula:

- **Formula cannot contain cell references or defined names.**
- **Formula cannot contain Worksheet functions that require cell references.**
- **Formula cannot use array functions.**

In MS Excel, the Calculated Field can be added using the calculation option from the Option tab. In XlsIO, the same can be achieved with the following code sample.

#### Code Example in C#

```csharp
[CS#]

IPivotTable pivotTable = sheet.PivotTables[0];
IPivotField field = pivotTable.CalculatedFields.Add("Percent", "Sales/Total*100");
```

The formula can be fetched from the formula property of the IPivotField.

#### Retrieving the Formula

```csharp
[CS#]

field.Formula = "Sales/Total*100";
```

### Layouting the Pivot Table as MS Excel 2007

We have provided support for drawing a pivot table similar to the MS Excel layout using Essential XlsIO. Previously, we let MS Excel lay out the pivot table for XlsIO. By using a layout method, we draw the pivot table layout using XlsIO. Now we can get any values of the pivot table using XlsIO dynamically, apply a filter to the pivot table, and can get the filtered values of the pivot table dynamically.

#### Methods

| Method Name | Description |
|-------------|-------------|
| Layout      | Method to lay out the pivot table using XlsIO like the MS Excel pivot table layout. |

#### Code Example

The following code example illustrates how to enable Essential XlsIO to lay out the pivot table like MS Excel.

## Footer
© 2013 Syncfusion. All rights reserved. 270 | Page
``` 

<!-- tags: [xlsio, pivot tables, calculated fields, formula restrictions, ms excel layout, layout method, winforms, c#] keywords: [calculated fields, pivot tables, formula restrictions, ms excel, layout method, essential xlsio, dynamic access, filtered pivot table values, ms excel layout] -->
