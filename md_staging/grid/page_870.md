```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_870.jpeg
document_name: grid
page_number: 870
page_id: grid#page_870
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:48:59Z
fidelity: lossless
-->

## QueryCellStyleInfo Event in Syncfusion Grid

### Overview
- The `QueryCellStyleInfo` event is triggered whenever a request is made to access style information for a cell.
- It allows customization of cell styles using a `GridTableCellStyleInfoEventArgs` parameter, which can be used to apply specific styling based on the `CellType` property.
- The `TableCellIdentity.TableCellType` property helps determine the type of cell being styled.

### Content

The `QueryCellStyleInfo` event is raised every time a request is made to access the style information for a cell. You can do any type of formatting cells with this event. It accepts `GridTableCellStyleInfoEventArgs` as one of its parameters, which can be used to customize the cells of the grouping grid control. For instance, you can apply style settings for a given `CellType` by using the `TableCellIdentity.TableCellType` property on the instances of `GridTableCellStyleInfoEventArgs` to set the style for a given cell.

Here is an example code that applies different styles to different cells in the grouping grid.

```csharp
[C#]

// Hook up the event.
this.gridGroupingControl1.QueryCellStyleInfo += new GridTableCellStyleInfoEventHandler(gridGroupingControl1_QueryCellStyleInfo);

// QueryCellStyleInfo event : To Format Cell by Cell Basis on demand.
private void gridGroupingControl1_QueryCellStyleInfo(object sender, GridTableCellStyleInfoEventArgs e)
{
    if (e.TableCellIdentity.TableCellType == GridTableCellType.RecordFieldCell)
    {
        if (e.TableCellIdentity.ColIndex % 2 == 0)
        {
            e.Style.BackColor = Color.FromArgb(255, 187, 111);
            e.Style.Font.FontStyle = FontStyle.Bold;
        }
        else
        {
            e.Style.TextColor = Color.White;
            e.Style.BackColor = Color.FromArgb(55, 91, 114);
        }
    }
    else if (e.TableCellIdentity.TableCellType == GridTableCellType.AlternateRecordFieldCell)
    {
        if (e.TableCellIdentity.ColIndex % 2 == 0)
        {
            e.Style.Font.FontStyle = FontStyle.Underline;
            e.Style.BackColor = Color.FromArgb(0, 21, 84);
            e.Style.TextColor = Color.White;
        }
        else
        {
            e.Style.BackColor = Color.FromArgb(255, 188, 112);
        }
    }
}
```

## RAG Annotations
<!-- tags: [grid, groupgrid, customization, cellstyle, event] keywords: [QueryCellStyleInfo, GridTableCellStyleInfoEventArgs, TableCellIdentity, RecordFieldCell, AlternateRecordFieldCell, CellType, style settings] -->
```