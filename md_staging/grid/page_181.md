```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_181.jpeg
document_name: grid
page_number: 181
page_id: grid#page_181
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:00:56Z
fidelity: lossless
-->

## Overview
- The page discusses the use of `BaseStyles` in the Grid control for customizing cell appearance.
- It explains that `BaseStyles` are similar to styles in word processing software, providing reusable style definitions.
- It covers applying, altering, and integrating `BaseStyles` into the Grid control's precedence hierarchy.

## Content

### 4.1.4.2.2 BaseStyles

The Grid control supports another parent-type style, **BaseStyles**, which is used to customize a cell's appearance. BaseStyles are **GridStyleInfo** objects that can be associated with an arbitrary collection of cells. In a Word Processing software, there is the common task of defining a particular style (such as a style named **Header1** representing a bold, 20-point Helvetica font), and then using it repeatedly in your document whenever you need a 'Header1' type. BaseStyles play the same role within Grid control.

You can define a BaseStyle named **Header1** as having certain properties, and then you can place these properties onto any cell just by applying this BaseStyle Header1 to the cell. More importantly, if you want to change **Header1** (for example, changing its **BackColor** property from white to red), you can make the change one time by just changing the **Header1** BaseStyle, and not having to reassign every other cell assigned to this BaseStyle.

Since BaseStyles are considered as parent styles, where do they fit within the precedence hierarchy that we have discussed above? BaseStyles are applied between the table style and the standard style. Thus, they are the 'weakest' style other than the fully populated standard style. BaseStyles are stored in the **GridControl.BaseStylesMap** class. In addition to the standard style, other BaseStyles used by all Essential Grids include **Row Header**, **Header**, and **Column Header**. You can define and apply your own BaseStyles as well.

### Figure 99: Text and Cell Value

![Figure 99: Text and Cell Value](https://example.com/figure99)

The figure showcases various styles and validations applied to cells within the Grid control.

## API Reference (if applicable)

**Namespace:** Syncfusion.Windows.Forms.Grid

- **Class:** GridControl
  - **Property:** BaseStylesMap
    - **Description:** Stores and manages BaseStyles within the Grid control.
- **Member:** GridStyleInfo
  - **Description:** Represents an individual style rule that can be applied to cells.

### Code Examples

#### Applying a BaseStyle to a Cell

```csharp
// Define a BaseStyle
GridStyleInfo headerStyle = new GridStyleInfo();
headerStyle.Font.Bold = true;
headerStyle.Font.Size = 18;
headerStyle.BackColor = Color.Red;

// Add the BaseStyle to the BaseStylesMap
GridControl.BaseStylesMap.Add("Header1", headerStyle);

// Apply the BaseStyle to a cell
gridControl[0, 0].StyleInfo = gridControl.BaseStylesMap["Header1"];
```

## Cross References

- See also:
  - [Essential Grid for Windows Forms](#)
  - [Number Formats](#number-formats)
  - [Validation](#validation)
  - [GridControl](#gridcontrol)

<!-- tags: [Syncfusion, Winforms, GridControl, BaseStyles, GridStyleInfo, standardstyle, tablestyle] keywords: [custom cell appearance, reusable styles, BaseStyles, GridStyleInfo, precedence hierarchy, BaseStylesMap,Header1] -->
```