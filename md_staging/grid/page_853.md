```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_853.jpeg
document_name: grid
page_number: 853
page_id: grid#page_853
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:44:03Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

| SummaryFillRowCell                        | Style information for any fill cell in a summary row.        |
|-------------------------------------------|-------------------------------------------------------------|
| SummaryRowHeaderCell                      | Style information for any header cell in a summary row.      |
| SummaryTitleCell                          | Style information for any title cell in a summary row.       |
| TopLeftHeaderCell                         | Style information for any top left header cell.              |

### 4.3.4.5.1.1 Styles At Table Level

This section demonstrates how to provide different appearances to the tables at different levels. Properties set through `grid.TableDescriptor.Appearance` property will be applied to the top level table (parent). To control the appearance of individual child tables, you need to first get the `TableDescriptor` of the desired Child Table. You can then use `ChildTableDescriptor.Appearance` property to provide the appearances to the respective child table.

#### Example

This implementation applies unique styles to the tables at different levels (Parent and Child). The grouping grid is bound to an hierarchical dataset with two tables. Below is the code to customize the appearance of these tables.

1. Set styles to the Parent Table.

```csharp
[C#]

// Column Header Cell styles.
this.gridGroupingControl.Appearance.ColumnHeaderCell.CellTipText = "ColumnHeader";
this.gridGroupingControl.Appearance.ColumnHeaderCell.Interior = new BrushInfo(GradientStyle.Vertical, Color.FromArgb(214, 220, 232), Color.FromArgb(106, 111, 151));
this.gridGroupingControl.Appearance.ColumnHeaderCell.TextColor = System.Drawing.Color.White;

// Record Field Cell style.
this.gridGroupingControl.Appearance.RecordFieldCell.Interior = new BrushInfo(Color.Lavender);
```
```


<!-- tags: [Essential Grid, Windows Forms, Table Style, Hierarchical Dataset] keywords: [TableDescriptor, Appearance, Styles, Parent Table, Child Table, Column Header Cell, Record Field Cell, C#, Customization, Subsection] -->
```