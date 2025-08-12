```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_387.jpeg
document_name: grid
page_number: 387
page_id: grid#page_387
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:13:59Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Content
```csharp
this.gridControl.RowCount = this.numArrayRows;
this.gridControl.ColCount = this.numArrayCols;

for (int i = 0; i < this.numArrayRows; ++i)
{
    for (int j = 0; j < this.numArrayCols; ++j)
        this.gridControl[i + 1, j + 1].CellValue = this.intArray[i, j];
}
this.gridControl.EndUpdate();
this.gridControl.Refresh();
```
```vb
' Turn off undo.
Me.gridControl.CommandStack.Enabled = False

' Prevent the grid from redrawing for each change.
Me.gridControl.BeginUpdate()

Me.gridControl.RowCount = Me.numArrayRows
Me.gridControl.ColCount = Me.numArrayCols

Dim i As Integer
Dim j As Integer
For i = 1 To Me.numArrayRows
    For j = 1 To Me.numArrayCols
        Me.gridControl(i + 1, j + 1).CellValue = Me.intArray(i, j)
    Next j
Next i

Me.gridControl.EndUpdate()
Me.gridControl.Refresh()
```

### 4.1.4.7.2 The GridControl.PopulateValues Method

To overcome the cell-by-cell event overhead intrinsic, Grid control has a **PopulateValues** method. This method is a member of the **GridControl** class which is in the indexer population technique and which was discussed in the Grid Control Indexer Technique section. This method will allow you to pass in a range of cells and a data source of the type object. With this information, the method will then use techniques that will bypass the event overhead to retrieve data from the **datasource** object in a manner that depends upon the object type and will move it into the range.
```