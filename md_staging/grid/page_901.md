```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_901.jpeg
document_name: grid
page_number: 901
page_id: grid#page_901
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:47:27Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates the creation and customization of stacked headers in a Grid control.
- Explains the use of multi-row records in a Table using `ColumnSets`.
- Provides programming steps for spanning records across multiple rows.

## Content

### Creating Stacked Headers

```vb
Dim shd As GridStackedHeaderDescriptor = New GridStackedHeaderDescriptor("header1", "StackedHeader1")
shd.VisibleColumns.Add(New GridStackedHeaderVisibleColumnDescriptor("CustomerName"))
shd.VisibleColumns.Add(New GridStackedHeaderVisibleColumnDescriptor("CompanyName"))
Dim shrd As GridStackedHeaderRowDescriptor = New GridStackedHeaderRowDescriptor("Row1", New GridStackedHeaderDescriptor() { shd })
Me.gridGroupingControl1.TableDescriptor.StackedHeaderRows.Add(shrd)

' Customize the Appearance.
Me.gridGroupingControl1.Appearance.StackedHeaderCell.BackColor = Color.Teal
```

**Note**: For more details, refer the following browser sample:

```
<Install Location>\Syncfusion\EssentialStudio\<Version Number>\Windows\Grid.Grouping.Windows\Samples\2.0\Grouping Grid Layout\Stacked Multi Headers Demo
```

### 4.3.4.6.2 Multi Row Record

Grid Grouping control offers built-in support for MultiRowRecords. This feature allows the records to span across multiple rows and columns. It is achieved through the property `TableDescriptor.ColumnSets`. It allows you to modify the default alignment of the visible columns.

#### The ColumnSets Collection

**ColumnSets** acts as a superset of `TableDescriptor.Columns` collection. Once the ColumnSets are defined, the grouping grid will then loop through the collection and organize the data display accordingly. Each ColumnSet is defined by a `GridColumnSetDescriptor`. ColumnSets are managed by `GridColumnSetDescriptorCollection` that is returned by the `TableDescriptor.ColumnSets` property.

#### Programmatically

Follow the steps below to span the records across multiple rows.

## API Reference (if applicable)
- Namespace: [Grid API]
- Members: Properties: `StackedHeaderRows`, `Appearance.StackedHeaderCell.BackColor`, `TableDescriptor.ColumnSets`
- Methods: `Add`, `Rows.Add`

## Code Examples (multi-language supported)
- **C# Example**: Similar functionality can be achieved in C# using the Syncfusion grid control.

```csharp
GridStackedHeaderDescriptor shd = new GridStackedHeaderDescriptor("header1", "StackedHeader1");
shd.VisibleColumns.Add(new GridStackedHeaderVisibleColumnDescriptor("CustomerName"));
shd.VisibleColumns.Add(new GridStackedHeaderVisibleColumnDescriptor("CompanyName"));
GridStackedHeaderRowDescriptor shrd = new GridStackedHeaderRowDescriptor("Row1", new GridStackedHeaderDescriptor[] { shd });
gridGroupingControl1.TableDescriptor.StackedHeaderRows.Add(shrd);

gridGroupingControl1.Appearance.StackedHeaderCell.BackColor = Color.Teal;
```

## Page-level Navigation/TOC (if applicable)
- **Creating Stacked Headers**
- **Multi Row Record**
  - The ColumnSets Collection
  - Programmatically

# RAG Annotations

<!-- tags: [syncfusion-sdk, grid, stacked headers, multi-row records] keywords: [GridStackedHeaderDescriptor, GridStackedHeaderVisibleColumnDescriptor, GridStackedHeaderRowDescriptor, TableDescriptor, ColumnSets, Stacked Header, Multi Row Record, grid groupRow] -->
```