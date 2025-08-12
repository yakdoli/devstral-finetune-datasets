```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_148.jpeg
document_name: grid
page_number: 148
page_id: grid#page_148
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:57:36Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

| Feature            | Description                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| Header            | Displays cells as grid header cells with static text.                     |
| Masked Edit       | Uses a mask to control values entered into the cell.                        |
| Month Calendar    | Displays a DateTime value and allows editing of it.                        |
| Numeric Up Down   | Displays numeric text that can be edited or modified with spinner buttons. |
| Progress Bar      | Displays a ProgressBar control in a cell.                                  |
| Push Button       | Displays a button in the cell that the user can click.                     |
| Rich Text         | Displays rich text in the cell and allows editing while in a drop down.    |
| Slider            | Displays a slider control in a cell.                                       |
| Static            | Displays text in the cell that cannot be edited.                           |
| Text Box          | Displays text in the cell that can be edited.                              |

## Check Box

### Overview
- The Check Box cell type displays a check box in a grid cell.
- The check box has three states: Checked, Unchecked, and Indeterminate.
- You can decide whether the check box should behave as a two-state check box or a three-state check box.

### Functionality Control
The following `GridStyleInfo` properties can be used to control the functioning of the check box.

| GridStyleInfo Property | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| CellType               | Set to "check box" for a check box control.                                 |
| CheckBoxOptions        | Defines the display value of True, False, or indeterminate (i.e., the value returned by the GridStyleInfo.Text property). |

## Page-level Navigation/TOC (if applicable)
<!-- tags: [grid, check box, cell properties, winforms] keywords: [checkbox, states, grid, GridStyleInfo, cell types] -->
```