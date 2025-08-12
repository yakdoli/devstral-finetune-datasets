```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_388.jpeg
document_name: grid
page_number: 388
page_id: grid#page_388
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:14:07Z
fidelity: lossless
-->

### Essential Grid for Windows Forms

The basic types that can be passed into the datasouce parameter include IListSource, Array and IList. This includes things like a DataTable and DataView, since a DataTable implements IListSource and a DataView implements IList.

#### Note

When you use the GridControl.PopulateValues method, the data values are copied from your data source and placed into the Essential Grid object. Thus, this is an entirely different concept than binding a grid to a data source. In such cases, the data is not moved into the grid object, but instead is provided on demand from the data source to the grid. So, the grid never stores any values in a databound grid. When you use the PopulateValues method, the data is actually copied from the data source and is placed in the grid's internal storage.

#### Example in C#

```csharp
this.gridControl1.BeginUpdate();
this.gridControl1.RowCount = this.numArrayRows;
this.gridControl1.ColCount = this.numArrayCols;

// Call PopulateValues Method to move values from a given data source (this.initArray) into the Grid Range specified.
this.gridControl1.Model.PopulateValues(GridRangeInfo.Cells(1, 1, this.numArrayRows, this.numArrayCols), this.intArray);
this.gridControl1.EndUpdate();
this.gridControl1.Refresh();
```

#### Example in VB.NET

```vb
Me.gridControl1.BeginUpdate()
Me.gridControl1.RowCount = Me.numArrayRows
Me.gridControl1.ColCount = Me.numArrayCols

' Call PopulateValues Method to move values from a given data source (this.initArray) into the Grid Range specified.
Me.gridControl1.Model.PopulateValues(GridRangeInfo.Cells(1, 1, Me.numArrayRows, Me.numArrayCols), Me.intArray)
Me.gridControl1.EndUpdate()
Me.gridControl1.Refresh()
```

To see a program sample that uses these techniques to populate a grid, look at the Grid Population Demo sample that ships with the product. It allows you to time the different population methods including the using of a grid virtually. For small grids, the three techniques are comparable. But, as you increase the grid size, the virtual grid timing values remain the same, whereas the other two methods vary depending upon the number of data points. In general, the population of a grid by using the indexer technique is about a factor of ten slower than using the PopulateValues method. And, depending upon the size of the grid, the virtual technique can be thousands of times quicker than the other techniques.

<!-- tags: [grid, populatevalues, bindto, virtualgrid, datatablesource, dataview, gridpopulation, essentialgrid, windowsforms] keywords: [gridcontrol, gridrangeinfo, populatevalues, virtualgrid, datasouce, ilistsource, array, ilist, datatablesource, dataview, gridpopulationdemo, indexer] -->
```