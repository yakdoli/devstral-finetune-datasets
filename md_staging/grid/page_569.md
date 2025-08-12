```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_569.jpeg
document_name: grid
page_number: 569
page_id: grid#page_569
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:24:37Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Introduction

### Note

The `IBindingList` interface provides the features required to support both complex and simple scenarios when binding to a data source.

### Sort Method

The `Sort` method relies on the data source for the grid. By default, sorting is done based on the value members present in the data source and not based on the display member. We can implement the `Sort By DisplayMember` feature in Grid Data Bound Grid. The code for foreign key column can be added to the `View` of the data table so that the sort behavior can be redirected to use the foreign key column linked to the combo box column, when the user sorts the combo box column.

## Example

The following code example implements a solution for sorting a column by its display member instead of its value member. Here the foreign key column is added to the `View` of the data to redirect the sort behavior to use the foreign key column.

To accomplish this, two handlers—the `CellClick` event and the `QueryCellInfo` event have been used. In the `CellClick` event, the display member is set to the existing mapping name in the `sortName` (which will be the value member) so that the sorting is done by display member.

### Code Example

```csharp
string sortName = column.MappingName;

if (column.MappingName == "SupplierID")
    sortName = "CompanyName";
else if (column.MappingName == "CategoryID")
    sortName = "CategoryName";
```

```vbnet
Dim sortName As String = column.MappingName

If column.MappingName = "SupplierID" Then
    sortName = "CompanyName"
ElseIf column.MappingName = "CategoryID" Then
    sortName = "CategoryName"
End If
```

### DataView Creation

A `DataView` is created by using the `List` property under the `CurrencyManager` class.

```csharp
CurrencyManager cm = BindingContext[grid.DataSource, grid.DataMember]
    as CurrencyManager;
```

## Page Footer

© 2013 Syncfusion. All rights reserved.
``` 

<!-- tags: [Syncfusion Winforms, Grid, IbindingList, Sort Method, DataView] keywords: [IBindingList, Sort, DisplayMember, Foreign Key Column, DataView, Grid Data Bound Grid, CellClick, QueryCellInfo, CurrencyManager] -->
```