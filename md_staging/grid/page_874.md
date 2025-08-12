```markdown
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_874.jpeg
document_name: grid
page_number: 874
page_id: grid#page_874
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:49:15Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- BaseStyles play a significant role within Essential Grid, enabling property definition and reuse.
- They allow users to apply predefined properties to grid cells, ensuring consistency and ease of maintenance.
- Users can define, store, and manage custom BaseStyles, enhancing flexibility and control over grid appearance.

## Content

### Understanding BaseStyles in Essential Grid

BaseStyles serve a crucial role within Essential Grid. You can define a BaseStyle named `Header1` as having specific properties and apply these properties to any cell by assigning `Header1` to the cell. This feature is particularly useful because if you later want to change what `Header1` means (for example, altering its `BackColor` property from white to red), you can make the change in one place by modifying the `Header1` BaseStyle without needing to update every cell assigned to this BaseStyle.

### Storage and Predefined BaseStyles

BaseStyles are stored in the `GridGroupingControl.TableModel.BaseStylesMap` class. In addition to the standardstyle, other BaseStyles commonly used by all Essential Grids include `Row Header`, `Header`, and `Column Header`. Users can define and apply their own BaseStyles as well.

### Creating and Applying BaseStyles

Users can add base styles to the engine and inherit style settings through the `GridStyleInfo.BaseStyle` property. You can create any number of style templates using BaseStyles.

#### Applying BaseStyles

1. **Adding Style Templates at Design Time**:  
   To add style templates at design time, you need to access the `BaseStyles` property in the property editor. This will open the `GridTableStyle Collection Editor`, which lists the `StyleInfo` properties that can be associated with a grid cell. Here is an example of a property editor showing the creation of two style templates named `BaseStyle1` and `BaseStyle2`.

### Example of BaseStyle Creation

This step outlines the process of creating and accessing BaseStyles within the Grid control, facilitating efficient design-time customization.

## Code Examples

To implement BaseStyles, you can use the following example to create and apply a style template:

```csharp
// Accessing BaseStyles property
GridGroupingControl.MyGrid.TableModel.BaseStyles.Add("BaseStyle1");

// Applying BaseStyle to a grid cell
GridStyleInfo styleInfo = new GridStyleInfo();
styleInfo.BaseStyle = "BaseStyle1";

// Assigning the styleInfo to a cell
MyGrid.Table[0, 0].StyleInfo = styleInfo;
```

## Page-level Navigation/TOC
- **Introduction to BaseStyles**
- **Storage and Standard BaseStyles**
- **Creating and Applying Custom BaseStyles**
- **Design-Time Template Addition**

## Cross References
- See also: [Grid Grouping Control Documentation](#grid-grouping-control)
- For more details on `GridStyleInfo`, refer to the [GridStyleInfo Class Reference](#gridstyleinfo-class-reference)

<!-- tags: [essential-grid, windows-forms, basestyles, grid-style-info, gridgroupingcontrol] keywords: [basestyle, gridcell, styletemplate, propertyeditor, design-time, tablemodel, header, rowheader, columnheader] -->
```