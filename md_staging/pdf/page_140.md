```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_140.jpeg
document_name: pdf
page_number: 140
page_id: pdf#page_140
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:32:16Z
fidelity: lossless
-->

# Essential PDF

The values of existing rows, entered with `DataSourceType` as `PdfLightTableDataSourceType.TableDirect`, can be edited using the `Values` property. The following is the code:

## Content

### Setting Values for Existing Rows

#### C#

```csharp
pdfLightTable.Rows[1].Values = new string[] { "333", "John", "234" };
```

#### VB.NET

```vb
pdfLightTable.Rows(1).Values = New String() { "333", "John", "234" }
```

### Setting Minimum Height for Rows

The minimum height of a row in `PdfLightTable` can be set using `BeginRowLayout` and `EndRowLayout` events.

### Column Settings

#### Column Properties

| Name        | Description                                   | Data Type       |
|-------------|-----------------------------------------------|-----------------|
| ColumnName  | Gets or sets the column name                  | String          |
| StringFormat | Gets or sets the string format for the column | PdfStringFormat |
| Width       | Gets or sets the width of the column          | float           |

#### ColumnName

**ColumnName**

By default, `PdfLightTable` displays the column text as the `DataSource` column name. You can change the column text using the `ColumnName` property. The following code snippet illustrates this:

#### C#

```csharp
// Specifying Column name
pdfLightTable.Columns[2].ColumnName = "Student Name";
```

#### VB.NET
```vb
' Specifying Column name
pdfLightTable.Columns(2).ColumnName = "Student Name"
```

## Page-level Navigation/TOC (if applicable)
- [ ] Table of Contents for the page (if any)

## Cross References
- Refer to related sections or pages for more details on properties and methods.

<!-- tags: [Essential PDF, pdfLightTable, PdfLightTableDataSourceType, column settings, data editing, minimum row height] keywords: [pdfLightTable, column, string format, width, columnName, property, method, data editing, row layout, mininum height] -->
```