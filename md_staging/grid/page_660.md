```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_660.jpeg
document_name: grid
page_number: 660
page_id: grid#page_660
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:31:53Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Content

### Handling QueryCellStyleInfo

The `QueryCellStyleInfo` event is used to enable the coloring of cells in the grid. The background colors of the cells in the records depend on the values in column "1". This dependency is specified using the `Referred Fields` property. To enhance user-friendliness, a `CheckBox` control can be used to enable or disable this coloring. The event should be hooked when the `CheckBox` is checked; otherwise, it should be unhooked.

```csharp
[C#]

Color[] colors = new Color[] { Color.FromArgb(0x85, 0xbf, 0x75),
                              Color.FromArgb(0xb4, 0xe7, 0xf2),
                              Color.FromArgb(0xff, 0xbf, 0x34),
                              Color.FromArgb(0x82, 0x2e, 0x1b),
                              Color.FromArgb(0x3a, 0x86, 0x7e) };

void gridGroupingControl1_QueryCellStyleInfo(object sender,
                                           GridTableCellStyleInfoEventArgs e)
{
    GridTableCellStyleInfo style = (GridTableCellStyleInfo)e.Style;
    if (e.TableCellIdentity.TableCellType == GridTableCellStyleType.RecordFieldCell
        || e.TableCellIdentity.TableCellType == GridTableCellStyleType.AlternateRecordFieldCell)
    {
        if (e.TableCellIdentity.Column.FieldDescriptor.FieldPropertyType == typeof(string))
        {
            return;
        }
        // Get the value from column 1 and color all cells in record based on this value.
        Record r = e.Style.TableCellIdentity.DisplayElement.GetRecord();
        object value = r.GetValue("1");
        int v = Convert.ToInt32(value) % colors.Length;
        e.Style.BackColor = colors[v];
    }
}

// CheckBox event to enable or disable cell coloring.
private void checkBoxColor_CheckedChanged(object sender, System.EventArgs e)
{
    if (this.checkBoxColor.Checked)
    {
        // Callback for dynamically coloring cells.
        gridGroupingControl1.QueryCellStyleInfo += new GridTableCellStyleInfoEventHandler(gridGroupingControl1_QueryCellStyleInfo);
    }
    else
    {
        gridGroupingControl1.QueryCellStyleInfo -= new GridTableCellStyleInfoEventHandler(gridGroupingControl1_QueryCellStyleInfo);
    }
}
```

## Code Examples

The example above demonstrates how to dynamically color cells in a grid based on the value in column "1". It also shows how a `CheckBox` can be used to enable or disable this functionality. The `QueryCellStyleInfo` event is hooked or unhooked based on the checked state of the `CheckBox`.

## RAG Annotations

<!-- tags: [syncfusion, grid, windows forms, querycellstyleinfo, checkbox] -->
<!-- keywords: [cell coloring, referenced fields, gridtablecellstyleinfo, enable, disable, querycellstyleinfo event, checked state, dynamic coloring] -->
```