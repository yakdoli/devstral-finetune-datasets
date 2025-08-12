<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_736.jpeg
document_name: grid
page_number: 736
page_id: grid#page_736
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:37:11Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```vb
ElseIf e.PropertyName = "Appearance" Then
    ' Base class will end edit mode, which is not necessary.
    Return
End If

MyBase.Engine_PropertyChanging(sender, e)
End Sub
```

## 4.3.4.3.2 Sorting

Grid Grouping control allows you to sort the table data against one or more columns. The number of columns by which the data can be sorted is unlimited. When sorting is applied, the grid will rearrange the data to match with the current sort criteria.

### SortedColumns Collection

The **SortedColumns** collection defines the sort order for records within groups. Multiple entries can be added with the first entry having the highest precedence when sorting records. The properties and methods in this collection lets you manage the elements in the collection. The collection can be viewed as a set of **SortColumnDescriptors** one for every column against which the data is sorted. The **SortColumnDescriptor** of a field contains the details like the name of a field, sort direction, and optionally a custom comparer and categorization object. The custom comparer and categorizer will allow you to customize the sorting.

### Sorting Methods

There are multiple ways through which you can apply sorting on table data. A simple one is just clicking the desired column headers by which the grouping grid needs to be sorted. Once the sorting is applied, the grid will display a sort icon in the respective column headers showing the sort direction. The sorting can also be done against multiple columns by holding the Ctrl key and doing a click on the desired column headers.

### Through Designer

<!-- tags: [Syncfusion, WindowsForms, Grid, Sorting, SortedColumns, SortColumnDescriptor, CustomComparer, Categorization] keywords: [Grid Grouping, Sort Methods, Designer, Sort Columns, Sort Direction, Custom Sort] -->