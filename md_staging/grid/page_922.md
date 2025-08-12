```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_922.jpeg
document_name: grid
page_number: 922
page_id: grid#page_922
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:52:16Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

Figure 339: Cell Appearance customized by handling TableControlPrepareViewStyleInfo and TableControlCellDrawn Events  
![Figure 339](https://i.imgur.com/2E6TT6.jpg)

## ListBoxSelection CurrentCellOptions

When ListBoxSelection mode was set, you will be able to control the appearance and behavior of the CurrentCell by setting ListBoxSelectionCurrentCellOptions property to a desired value. Possible values are defined by the GridListBoxSelectionCurrentCellOptions enumeration which are described below.

- **HideCurrentCell**  
  Don't select a current cell in the current row.  
  ![Figure 340: ListBoxSelectionCurrentCellOptions.HideCurrentCell Enabled](https://i.imgur.com/2E5EE.jpg)

- **WhiteCurrentCell**  
  When a current cell is in the current row, it is drawn with the original cell background color.  
  ![Figure 341: ListBoxSelectionCurrentCellOptions.WhiteCurrentCell Enabled](https://i.imgur.com/2E6TT7.jpg)

- **None**  
  When a current cell is in the current row, it is drawn with the same color used for highlighting the whole record.  
  ![Figure](https://i.imgur.com/2E6TT9.jpg)

## API Reference

### Enumerations

- **GridListBoxSelectionCurrentCellOptions**  
  - **HideCurrentCell**: Don't select a current cell in the current row.  
  - **WhiteCurrentCell**: Draw the current cell with the original cell background color.  
  - **None**: Draw the current cell with the same color used for highlighting the whole record.

## Code Examples

Example demonstrating the usage of ListBoxSelectionCurrentCellOptions:

```csharp
// Setting ListBoxSelectionCurrentCellOptions to HideCurrentCell
grid.ListBoxSelectionCurrentCellOptions = GridListBoxSelectionCurrentCellOptions.HideCurrentCell;

// Setting ListBoxSelectionCurrentCellOptions to WhiteCurrentCell
grid.ListBoxSelectionCurrentCellOptions = GridListBoxSelectionCurrentCellOptions.WhiteCurrentCell;

// Setting ListBoxSelectionCurrentCellOptions to None
grid.ListBoxSelectionCurrentCellOptions = GridListBoxSelectionCurrentCellOptions.None;
```

## Cross References

See also:
- TableControlPrepareViewStyleInfo
- TableControlCellDrawn

<!-- tags: [product, module, control, api, version] keywords: [ListBoxSelection, CurrentCellOptions, GridListBoxSelectionCurrentCellOptions, HideCurrentCell, WhiteCurrentCell, None, TableControlPrepareViewStyleInfo, TableControlCellDrawn] -->
```