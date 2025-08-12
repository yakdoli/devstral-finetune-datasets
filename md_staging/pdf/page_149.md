```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_149.jpeg
document_name: pdf
page_number: 149
page_id: pdf#page_149
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:33:13Z
fidelity: lossless
-->

# AllowRowBreakAcrossPages

This property allows changing the row split behavior across pages. By default, this Boolean property is set to True, which allows splitting the row across pages when the row cannot accommodate within the bounds of the page. If set to false, the entire row will be shifted to the next page.

**Note:** If the row height is greater than the page height, the row will be split or cut based on the True and False value of this property.

## 4.1.2.3.2.2.1 Data

### External Data Source

You can bind data to a PdfGrid by associating it with an external data source. You can set the external data source by using the DataSource property. The following code example illustrates this.

#### C#

```csharp
DataTable dt = new DataTable();
dt.Columns.Add("ID");
dt.Columns.Add("Name");

dt.Rows.Add(new object[] { "E01", "Clay" });
dt.Rows.Add(new object[] { "E02", "Thomas" });

// Create a PdfGrid.
PdfGrid pdfGrid = new PdfGrid();

// dt is an object that can be an array (two-dimensional, one-
// dimensional or nested), a DataTable, DataColumn, DataView or DataSet.
pdfGrid.DataSource = dt;
```

#### VB.NET

```vb
Dim dt As DataTable = New DataTable()
dt.Columns.Add("ID")
dt.Columns.Add("Name")

dt.Rows.Add(New Object() { "E01", "Clay" })
dt.Rows.Add(New Object() { "E02", "Thomas" })

' Create a PdfGrid.
```

## API Reference

### Methods
- `Rows.Add()`: Adds rows to the data table.
- `Columns.Add()`: Adds columns to the data table.

## Code Examples

### C#

```csharp
DataTable dt = new DataTable();
dt.Columns.Add("ID");
dt.Columns.Add("Name");

dt.Rows.Add(new object[] { "E01", "Clay" });
dt.Rows.Add(new object[] { "E02", "Thomas" });

PdfGrid pdfGrid = new PdfGrid();
pdfGrid.DataSource = dt;
```

### VB.NET

```vb
Dim dt As DataTable = New DataTable()
dt.Columns.Add("ID")
dt.Columns.Add("Name")

dt.Rows.Add(New Object() { "E01", "Clay" })
dt.Rows.Add(New Object() { "E02", "Thomas" })

Dim pdfGrid As PdfGrid = New PdfGrid()
pdfGrid.DataSource = dt
```

## Cross References

- Refer to the PdfGrid documentation for more details on data binding and properties.
- See also: External Data Source, PdfGrid Methods, and DataSourceProperty.

<!-- tags: [syncfusion, winforms, grid, data binding, properties, pdfgrid, external data source] keywords: [AllowRowBreakAcrossPages,DataTable,PdfGrid, DataSource, Rows, Columns, data binding, methods, properties] -->
```