```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_741.jpeg
document_name: grid
page_number: 741
page_id: grid#page_741
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:36:33Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates configuring dropdown display for foreign key columns using the `RelationDescriptor` and `TableDescriptor`.
- Details how to add foreign key relationships and set up column visibility and sorting.
- Example in both C# and VB.NET, including steps to replace main table columns with foreign table columns.

## Content

### Configuring Dropdown Display for Foreign Key Columns

1. **Display and Sort Columns**:
   ```csharp
   rd.ChildTableDescriptor.SortedColumns.Add("CustomerName");
   ```

   ```vb.net
   ' Display column.
   rd.ChildTableDescriptor.VisibleColumns.Add("CustomerName")

   ' Sort it for dropdown display.
   rd.ChildTableDescriptor.SortedColumns.Add("CustomerName")
   ```

2. **Add Relation Descriptor to MainTableDescriptor**:
   ```csharp
   td.Relations.Add(rd);
   ```

   ```vb.net
   td.Relations.Add(rd)
   ```

3. **Replace mainTable.Customer with foreignTable.CustomerName**:
   ```csharp
   string foreignCustomerColInMainTable = rd.Name + "_" + "CustomerName";
   td.VisibleColumns.Insert(CustomerColIndex,
   foreignCustomerColInMainTable);
   ```

   ```vb.net
   Dim foreignCustomerColInMainTable As String = rd.Name & "_" & "CustomerName"
   td.VisibleColumns.Insert(CustomerColIndex,
   foreignCustomerColInMainTable)
   ```

### Running the Application

**Result**: The following output is generated.

## API Reference

### Methods and Properties
- `TableDescriptor.SortedColumns.Add(columnName)` 
- `TableDescriptor.VisibleColumns.Add(columnName)`
- `TableDescriptor.VisibleColumns.Insert(index, columnName)`
- `RelationDescriptor`

## Code Examples

### Example: Setting Up Dropdown Display
```csharp
// Setting up foreign key relationship and dropdown display
RelationDescriptor rd = new RelationDescriptor();
rd.Nested = true;
rd.ChildTableDescriptor.SortedColumns.Add("CustomerName");
rd.ChildTableDescriptor.VisibleColumns.Add("CustomerName");
rd.ChildTableDescriptor.SortedColumns.Add("CustomerName");

td.Relations.Add(rd);

string foreignCustomerColInMainTable = rd.Name + "_" + "CustomerName";
td.VisibleColumns.Insert(CustomerColIndex,
foreignCustomerColInMainTable);
```

---

```vb.net
'Relation descriptor setup in VB.NET
Dim rd As New RelationDescriptor()
rd.Nested = True
rd.ChildTableDescriptor.VisibleColumns.Add("CustomerName")
rd.ChildTableDescriptor.SortedColumns.Add("CustomerName")

td.Relations.Add(rd)

Dim foreignCustomerColInMainTable As String = rd.Name & "_" & "CustomerName"
td.VisibleColumns.Insert(CustomerColIndex,
foreignCustomerColInMainTable)
```

## Page-level Navigation/TOC (if applicable)
- Setting up and displaying dropdown for foreign key columns
- Adding relation descriptor
- Replacing main table columns with foreign table columns

## Cross References
See also:
- [Getting Started with Essential Grid for Windows Forms](#)
- [TableDescriptor and RelationDescriptor Documentation](#)

<!-- tags: [Essential Grid, Windows Forms, RelationDescriptor, TableDescriptor, dropdown display, foreign key] keywords: [syncfusion, grid, dropdown, relation, table, foreign key, configuration, vb.net, csharp] -->
```