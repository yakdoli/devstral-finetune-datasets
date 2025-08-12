```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_913.jpeg
document_name: grid
page_number: 913
page_id: grid#page_913
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:48:13Z
fidelity: lossless
-->


# Essential Grid for Windows Forms

## Selections

### Overview
- Explains the two types of selection architectures in a Grid Grouping control: Record-Based Selection and Model-Based Selection.
- Describes the functionality and limitations of each selection method.
- Guides on how to enable and configure these selection modes.

### Content

#### 4.3.4.7 Selections

There are two types of selection architectures in a Grid Grouping control. One is designed specifically for the Grid Grouping control referred to as **Record-Based Selection**, and the other is inherited from **GridControlBase** named as **Model-Based Selection**.

If you use the Record-Based selection functionality, then whole records are selected, and these selections function properly with nested tables, sorting, and so on. If you choose to use the inherited selection capability, you will be able to select cell ranges, but the selections will have no knowledge of nested tables, grouping, or sorts and thus is limited in a Grid Grouping control.

To use the Grid Grouping control record selections, you must set **AllowSelections** to **None** and then set **ListBoxSelectionMode** to something other than **None**. To use the inherited selection capability, set **AllowSelections** to something other than **None**.

In this section, you will learn about the following topics.

#### 4.3.4.7.1 Model Based Selection

**Model Based Selection** is cell-based, allowing you to do a selection across the cell which is not possible with record-based selection. This derives from the GridControlBase and hence will not be aware of the grouping elements like nested tables, groups, and so on.

A model-based selection can be set by initializing the **AllowSelection** property to a value other than **None**. The possible values for this type of selection are defined by the enum **GridSelectionFlags**. By setting the various flags in **AllowSelection**, you can control the selection behavior of the grouping grids.

##### Selection Flags

| Flag Name | Description |
|-----------|-------------|
| AlphaBlend | Uses alpha blending to highlight selected cells. |
| Cell | Individual cells can be selected. |

## Page-level Navigation/TOC (if applicable)
- This section covers an explanation of the two selection architectures and provides guidance on enabling and configuring these modes.

### Cross References
- See also: Grid Grouping, GridControlBase, Record-Based Selection, Model-Based Selection, GridSelectionFlags.

### RAG Annotations
<!-- tags: [grid, selection, gridgrouping, model-based-selection, record-based-selection, gridcontrolbase, selection-flags] keywords: [selection architectures, nested tables, sorting, inherited selection, record selection, cell selection, allowselection, gridselectionflags] -->
```