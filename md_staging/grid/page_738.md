```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_738.jpeg
document_name: grid
page_number: 738
page_id: grid#page_738
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:39:26Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates how to achieve Multicolumn Sorting using the `SortedColumns` property.
- Provides examples in both C# and VB.NET for specifying the sort direction.
- Highlights the display of sort icons and index numbers in column headers for clarification.

## Content

### Multicolumn Sorting

```csharp
this.gridGroupingControl1.TableDescriptor.SortedColumns.Add("ProductName");
```

```vb.net
Me.gridGroupingControl1.TableDescriptor.SortedColumns.Add("ProductName")
```

Multicolumn Sorting can be achieved by adding the field names into the `SortedColumns` property and optionally specifying the sort direction. The following code example sorts the data by the `ProductName` and `UnitPrice` in ascending Order and by the column `Quantity` in descending Order.

```csharp
this.gridGroupingControl1.TableDescriptor.SortedColumns.Add("ProductName", ListSortDirection.Ascending);
this.gridGroupingControl1.TableDescriptor.SortedColumns.Add("QuantityPerUnit", ListSortDirection.Descending);
this.gridGroupingControl1.TableDescriptor.SortedColumns.Add("UnitPrice", ListSortDirection.Ascending);
```

```vb.net
Me.gridGroupingControl1.TableDescriptor.SortedColumns.Add("ProductName", ListSortDirection.Ascending)
Me.gridGroupingControl1.TableDescriptor.SortedColumns.Add("QuantityPerUnit", ListSortDirection.Descending)
Me.gridGroupingControl1.TableDescriptor.SortedColumns.Add("UnitPrice", ListSortDirection.Ascending)
```

#### Sample Output

Here is a sample output. To indicate the sort direction, a sort icon will be displayed in the column headers. When multicolumn sorting is applied, an index number will be displayed in the column headers along with the sort icon that facilitates the sort order. In the below example, the order of the sorting would be `ProductName(0)`, `Quantity(1)` and then `UnitPrice(2)`.

## Code Examples

### C#

```csharp
this.gridGroupingControl1.TableDescriptor.SortedColumns.Add("ProductName", ListSortDirection.Ascending);
this.gridGroupingControl1.TableDescriptor.SortedColumns.Add("QuantityPerUnit", ListSortDirection.Descending);
this.gridGroupingControl1.TableDescriptor.SortedColumns.Add("UnitPrice", ListSortDirection.Ascending);
```

### VB.NET

```vb.net
Me.gridGroupingControl1.TableDescriptor.SortedColumns.Add("ProductName", ListSortDirection.Ascending)
Me.gridGroupingControl1.TableDescriptor.SortedColumns.Add("QuantityPerUnit", ListSortDirection.Descending)
Me.gridGroupingControl1.TableDescriptor.SortedColumns.Add("UnitPrice", ListSortDirection.Ascending)
```

### Explanation

- **`SortedColumns.Add`**: Adds the column name along with the sort direction to the sorted columns list.
- **`ListSortDirection.Ascending`/`Descending`**: Specifies the direction of sorting for each column.

### Display

- **Sort Icons**: Icons (such as arrows) indicate ascending or descending sort direction.
- **Index Numbers**: Numbers (e.g., 0, 1, 2) in headers clarify the priority of sorting.

<!-- tags: [grid, multicolumn sorting, sort direction, column headers, Syncfusion, Windows Forms] keywords: [gridgroupingcontrol, sortedcolumns, listsortdirection, sort icons, index numbers, multicoloumn sorting, asc, desc] -->
```