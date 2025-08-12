```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_159.jpeg
document_name: grid
page_number: 159
page_id: grid#page_159
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:59:03Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates the use of formula cells in the Essential Grid for Windows Forms.
- Explains the GridListControl cell type, which allows for drop-down lists with multiple columns.
- Highlights properties like `DataSource`, `DisplayMember`, and `ValueMember` used for controlling grid cell behavior.

## Content

### Formula Cells
#### Figure 81: Formula Cells shown as Text Boxes
![](images/Figure_081.png)

#### Figure 82: Same Cells shown as Formula Cells
![](images/Figure_082.png)

### Grid List Control
#### Section: 4.1.4.1.7 Grid List Control

The GridListControl cell type allows you to display a drop-down list that can contain multiple columns as an image. It uses `DataSource`, `DisplayMember`, and `ValueMember` properties to control what is shown in the multiple columns. The `DataSource` member is generally stored in a parent style, and this member is then shared among grid cells which might use `DisplayMember` and `ValueMember` properties to customize their look if needed.

#### GridStyleInfo Property Details
| GridStyleInfo Property | Description |
|------------------------|-------------|
| DisplayMember          | Any object that implements either `IList` or `IListSource`. These include `DataTable`, `DataView`, or `ArrayList` objects. |
| ValueMember            | Indicates the column from the data source that is to be used for the value of the cell. |
| ExclusiveChoiceList    | Determines whether the user is required to select an item in the drop-down list. |
| MultiColumn            | Determines whether all the columns in the data source are displayed or if the single `DisplayMember` column is displayed. |

## Page-level Navigation/TOC
- Figure 81: Formula Cells shown as Text Boxes
- Figure 82: Same Cells shown as Formula Cells
- Section: 4.1.4.1.7 Grid List Control
- GridStyleInfo Property Details

## RAG Annotations
<!-- tags: [syncfusion, winforms, grid, formula-cells, gridlistcontrol, displaymember, valuemember, multicoloumn] keywords: [grid, windows forms, formula, drop-down list, multicoloumn support, displaymember, valueMember] -->
```