```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_131.jpeg
document_name: pdf
page_number: 131
page_id: pdf#page_131
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:32:35Z
fidelity: lossless
-->

# Essential PDF

## Content
### 4.1.2.3.1.2.1.2 Table Direct

You can directly add rows and columns to PdfLightTable. To achieve this, set `DataSourceType` property to `PdfLightTableDataSourceType.TableDirect`. The following code example illustrates this:

```csharp
[C#]

PdfLightTable pdfLightTable = new PdfLightTable();

// Setting the DataSourceType as Direct
pdfLightTable.DataSourceType = PdfLightTableDataSourceType.TableDirect;

// Creating Columns
pdfLightTable.Columns.Add(new PdfColumn("Roll Number"));
pdfLightTable.Columns.Add(new PdfColumn("Name"));
pdfLightTable.Columns.Add(new PdfColumn("Class"));

// Adding Rows
pdfLightTable.Rows.Add(new object[] { "111", "Maxim", "III" });

// Drawing the PdfLightTable
pdfLightTable.Draw(page, PointF.Empty);
```

```vb
[VB.NET]

Dim pdfLightTable As PdfLightTable = New PdfLightTable()

' Setting the DataSourceType as Direct
pdfLightTable.DataSourceType = PdfLightTableDataSourceType.TableDirect

' Creating Columns
pdfLightTable.Columns.Add(New PdfColumn("Roll Number"))
pdfLightTable.Columns.Add(New PdfColumn("Name"))
pdfLightTable.Columns.Add(New PdfColumn("Class"))

' Adding Rows
pdfLightTable.Rows.Add(New Object() { "111", "Maxim", "III" })
```

## API Reference

### WinForms-specific conventions
- **Namespace**: The code examples use `PdfLightTable` and `PdfLightTableDataSourceType`.
- **Properties/Methods**:
  - `DataSourceType`: Set to `PdfLightTableDataSourceType.TableDirect` to use table direct data.
  - `Columns.Add(PdfColumn)`: Adds a new column to the table.
  - `Rows.Add(object[])`: Adds a new row with data.
  - `Draw(PdfPage, PointF)`: Draws the table on the specified PDF page.

## Cross References

See also:
- Documentation on `PdfLightTable` and data manipulation.
- Examples of using `PdfLightTable` for creating tables in PDF documents.

<!-- tags: [Syncfusion, WinForms, PdfLightTable, dataSource, TableDirect, .NET, version 11.4.0.26] keywords: [PdfLightTable, TableDirect, DataSourceType, C#, VB.NET, PDF, Table, Rows, Columns, Data manipulation, Syncfusion WinForms] -->
```