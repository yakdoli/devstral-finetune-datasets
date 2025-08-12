```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_151.jpeg
document_name: grid
page_number: 151
page_id: grid#page_151
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:58:22Z
fidelity: lossless
--> 

## Overview

- Describes the use of color edit cells with dropdown color palettes.
- Explains the functionality and properties of combo box cells in grid controls.
- Details how to populate drop-down lists using GridStyleInfo properties.

## Content

### Color Edit Cells

#### Description
Color edit cells allow users to select colors from a dropdown list, similar to the one displayed in the figure. The cell's content is visually represented by the chosen color, and the user can toggle the editor between palette, web, and system colors.

#### Figure: Color Edit Cells

The figure shows a grid with color edit cells. The colors like "Aqua" and "Plum" are visibly displayed in the cells with dropdown editors ready to adjust the selection.

---

### 4.1.4.1.3 Combo Box

#### Description
When a combo box is added to a grid cell, it enables the user to choose from a drop-down list of predefined options. The behavior and content of the combo box can be controlled using various GridStyleInfo properties.

#### Populating the Drop-Down List
You can populate the drop-down list in several ways by setting the appropriate GridStyleInfo properties, such as `ChoiceList`, `ExclusiveChoiceList`, and `DataSource`.

#### Restricting and Auto-Completion
Other properties limit the choices to those listed in the drop-down and support auto-completion of possible matches as the user types new items.

#### GridStyleInfo Properties Table

| GridStyleInfo Property | Description |
|-------------------------|-------------|
| `CellType`             | Set to "combo box" for a combo box control. |
| `ChoiceList`           | StringCollection holding the strings for the drop down. |
| `ExclusiveChoiceList`  | True if you want to list the items in the drop-down, false otherwise. |
| `DataSource`           | This property lets you populate the drop-down list from by using an object that implements IListSource or IList. Examples include DataTable, DataSet, DataView, and ArrayList. |
| `DisplayMember`        | String that names the public property from the data source which determines how each item is displayed. |

---

## API Reference

### Properties

| Property               | Type                                   | Description                                                     |
|-------------------------|----------------------------------------|-----------------------------------------------------------------|
| `CellType`             | string                                | Type of grid cell. Set to "combo box" for a combo box control. |
| `ChoiceList`           | StringCollection                      | Collection of strings displayed in the drop-down list.         |
| `ExclusiveChoiceList`  | bool                                  | Determines if only listed items can be selected.                |
| `DataSource`           | Object implementing IListSource or IList | Populate the drop-down list from a data source like DataSet.   |
| `DisplayMember`        | string                                | Name of the property that determines item display.              |

---

## Code Examples

### Example of Configuring a Combo Box Cell

```csharp
// Example: Creating a combo box cell in a grid.
using Syncfusion.Grids;

GridStyleInfo myStyle = new GridStyleInfo();
myStyle.CellType = "combo box";
myStyle.ChoiceList = new StringCollection();
myStyle.ChoiceList.Add("Option 1");
myStyle.ChoiceList.Add("Option 2");
myStyle.ChoiceList.Add("Option 3");

gridModel[0, 0].Style = myStyle; // Apply the style to a specific cell.
```

---

## References

- [Combo Box Cells Documentation](#)
- [GridStyleInfo Reference](#)
- [Data Binding with DataSource](#)

---

<!-- tags: [combo box, GridStyleInfo, ColorEditCells, drop-down lists, WinForms, grid control, Syncfusion Winforms] keywords: [color edit, drop-down palette, cell editor, auto completion, CHOICELIST, DATASOURCE, DISPLAYMEMBER] -->
``` 
