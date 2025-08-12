```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_924.jpeg
document_name: grid
page_number: 924
page_id: grid#page_924
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:49:51Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Content

### Row and Column Selection with Respect to the Current Cell

| Row and Column | Selects the row and the column with respect to the current cell. |
| --- | --- |
| Default | Enables ListBoxSelection mode by default. |
| None | Disable the cell selection. |

### Implementation

Follow the steps below to create a sample that shows the above selections.

1. Create a grid grouping control and bind it to any data table. This example uses the grouping grid that has been bound to the Statistics Table from Northwind.MDB.

2. Setup the designer to add options for different selection types. Add six radio buttons to the form to enable the selection options **Cell Only**, **Row Only**, **Column Only**, **Row and Column**, **Default**, and **None**.

3. Set the required flags with respect to the current cell.

#### Code Example: Setting Up Flags

**[C#]**

```csharp
this.gridGroupingControl1.TableModel.Options.RefreshCurrentCellBehavior = GridRefreshCurrentCellBehavior.RefreshCell;
this.gridGroupingControl1.TableModel.Options.ShowCurrentCellBorderBehavior = GridShowCurrentCellBorder.GrayWhenLostFocus;
```

**[VB.NET]**

```vb
Me.gridGroupingControl1.TableModel.Options.RefreshCurrentCellBehavior = GridRefreshCurrentCellBehavior.RefreshCell
Me.gridGroupingControl1.TableModel.Options.ShowCurrentCellBorderBehavior = GridShowCurrentCellBorder.GrayWhenLostFocus
```

4. Handle `PrepareViewStyleInfo` event to focus the current selection according to the chosen selection type. It also includes the code to highlight the current selection. This works for **CellOnly**, **RowOnly**, **ColumnOnly**, and **Row and Column** types.

#### Code Example: Handling Selection Highlighting

**[C#]**

```csharp
this.gridGroupingControl1.TableControl.PrepareViewStyleInfo += new GridPrepareViewStyleInfoEventHandler(TableControl_PrepareViewStyleInfo);

void TableControl_PrepareViewStyleInfo(object sender, 
```

---

© 2013 Syncfusion. All rights reserved. 924 | Page
```