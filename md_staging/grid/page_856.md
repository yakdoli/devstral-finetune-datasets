```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_856.jpeg
document_name: grid
page_number: 856
page_id: grid#page_856
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:45:02Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates the customization of table appearances at different levels.
- Explains how to apply different styles to various group elements in a grid.

## Content

### WinForms-specific conventions

#### Customized Appearance of Tables at Different Levels

**Figure 330: Customized Appearance of Tables at Different Levels**

![Figure 330](https://example.com/figure330)

- The figure illustrates a grid with grouped data, showing tables at different levels with customized appearances.
- The `Customers` group is expanded to display detailed information about orders for each customer.

**Note:** For more details, refer to the following browser sample:

**Path:**  
`<Install Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Grouping.Windows\Samples\2.0\Appearance\Table Style Demo`

#### Styles at Group Level

**4.3.4.5.1.2 Styles At Group Level**

This section allows you to customize the appearances of different group elements. You can provide unique appearances to every element of a group, such as GroupCaptionCell, Group Header / Footer Cells, by setting the following properties under the Appearance section:

- GroupCaptionCell
- GroupCaptionPlusMinusCell
- GroupHeaderSectionCell
- GroupIndentCell
- GroupFooterSectionCell
- GroupPreviewCell

**Example**

Below is the code to apply different styles to various group members.

```csharp
this.gridGroupingControl1.Appearance.AnyGroupCell.Interior = new
```

## Page-level Navigation/TOC (if applicable)
- The page provides instructions on customizing table appearances and applying styles at group levels.

## Cross References
- Refer to the browser sample located at the provided path for additional details.

## RAG Annotations
<!-- tags: [product, module] keywords: [grid, customization, table, group styles, appearance] -->
```