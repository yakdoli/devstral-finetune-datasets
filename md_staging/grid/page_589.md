```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_589.jpeg
document_name: grid
page_number: 589
page_id: grid#page_589
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:25:50Z
fidelity: lossless
--> 

## Windows Forms Grid Properties and Events

### Properties

| Property Name           | Source                         | Description                                                                 |
|-------------------------|--------------------------------|-----------------------------------------------------------------------------|
| RowHeadersVisible       | Properties.RowHeaders         | Gets or sets a value indicating whether the column that contains row headers is displayed. |
| RowHeadersWidth         | Model.ColWidths[0]            | Gets or sets the width of the column.                                       |
| VerticalScrollingOffset | VScrollIncrement              | Gets the number of pixels by which the control is scrolled vertically.       |
| IsCurrentCellInEditMode | CurrentCell.IsEditing         | Gets a value indicating whether the currently active cell is being edited.   |
| RightToLeft             | RightToLeft                    | Gets or sets a value indicating whether control's elements are aligned to support locales using right-to-left fonts. |

### Equivalent Events Available

| .Net Grid                | Essential Grid                | Description                                                                 |
|--------------------------|-------------------------------|-----------------------------------------------------------------------------|
| BackgroundColorChanged   | BackColorChanged              | Occurs when the value of the System.Windows.Forms.Control.BackColor property changes. |
| CellMouseEnter           | CellMouseHoverEnter           | Occurs when the mouse pointer hovers over a cell.                                 |
| CellMouseLeave           | CellMouseHoverLeave           | Occurs when the mouse pointer leaves a cell.                                    |
| CellPainting             | CellDrawn                    | Occurs when a cell needs to be drawn.                                          |
| ColumnWidthChanged       | Model.ColWidthsChanged       | Occurs when column width changes.                                              |
| DataSourceChanged        | Binder.DataSourceChanged     | Occurs when the DataSource property is changed.                                    |

```