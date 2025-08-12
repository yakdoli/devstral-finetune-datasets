```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_108.jpeg
document_name: grid
page_number: 108
page_id: grid#page_108
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:28:20Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

While working on your Virtual Grid, you will see that the changes do not stay around after you leave the current cell, i.e., if you overtype a cell entry, when you move off the cell, the old value is restored. The reason is that currently, there is no way for the changed value to be moved back to the external data source. So, as you move off the cell, when the grid redraws the old cell, it will query the external data source (through GridQueryCellInfo), get the original value and display it. The value which you have typed will be lost.

In order to edit and save values in the Virtual Grid, you must be able to get the changed value back to the external data source. This is accomplished through the **GridControl.SaveCellInfo** event. You must add a handler for this event and in this handler, you must save the changed value back to the external data source.

## Code Example

```csharp
[C#]

private void Form1_Load(object sender, System.EventArgs e)
{
    // Create a new external data source with 100 rows and 20 columns.
    this._extData = new ExternalData(100, 20);

    // Hook up the events needed for the virtual grid.
    gridControl1.ResetVolatileData();
    gridControl1.QueryCellInfo += new GridQueryCellInfoEventHandler(GridQueryCellInfo);
    gridControl1.QueryRowCount += new GridRowColCountEventHandler(GridQueryRowCount);
    gridControl1.QueryColCount += new GridRowColCountEventHandler(GridQueryColCount);

    // Handle saving data back to the data source.
    gridControl1.SaveCellInfo += new GridSaveCellInfoEventHandler(GridSaveCellInfo);
}

void GridSaveCellInfo(object sender, GridSaveCellInfoEventArgs e)
{
    try
    {
        // Move the changes back to the external data object.
        if (e.ColIndex > 0 && e.RowIndex > 0)
        {
            this._extData[e.RowIndex - 1, e.ColIndex - 1] = int.Parse(e.Style.CellValue.ToString());
        }
    }
    catch {}
    e.Handled = true;
}
```

## Summary

- The Virtual Grid's changed values are restored to their original state when the cell is exited.
- To persist these changes, handle the **GridControl.SaveCellInfo** event.
- In the handler, save the changes back to the external data source.
- Hook up necessary events for the virtual grid to function correctly.

```html
<!-- tags: [gridcontrol, virtualgrid, datasource, eventhandling] keywords: [savecellinfo, gridquerycellinfo, gridqueryrowcount, gridquerycolcount, cellvalue, externaldata] -->
```