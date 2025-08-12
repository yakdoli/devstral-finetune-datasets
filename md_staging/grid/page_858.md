```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_858.jpeg
document_name: grid
page_number: 858
page_id: grid#page_858
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:48:10Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Customized appearance of groups at different levels in a grid.
- How to achieve Column-Based formatting for unique grid column appearances.
- Use of GridColumnDescriptor.Appearance property for column styling.

## Content

### Customized Appearance of Groups at Different Levels

#### Figure 331: Customized Appearance of Groups at Different Levels
![](https://example.com/image.png)

**Note:** For more details, refer to the following browser sample:

`<Install Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Grouping.Windows\Samples\2.0\Appearance\Group Style Demo`

#### ColumnStyles

##### 4.3.4.5.1.3 ColumnStyles

Grid Grouping control allows you to do **Column-Based formatting**. With this feature, you can provide an unique appearance to different grid columns. Grid columns can be customized by setting the **GridColumnDescriptor.Appearance** property.

ColumnFormatting can be done at design time. Once the data source is set, select **TableDescriptor.Columns** property in the property window of the grid grouping control. This will open the **GridColumnDescriptor** collection editor that is populated with the columns in the datasource. You can modify the appearance of the desired column by setting the **Appearance** property of that column in this editor. The following picture shows this process.

## API Reference

### Properties
- **GridColumnDescriptor.Appearance**: Facilitates the customization of the appearance of specific grid columns.

### Methods
- None specific to this section.

### Events
- None specific to this section.

## Code Examples

### Example of Column-Based Formatting in C#
```csharp
// Example usage of GridColumnDescriptor.Appearance
grid.GridColumnDescriptor["CategoryName"].Appearance.TextColor = Color.Blue;
grid.GridColumnDescriptor["CategoryID"].Appearance.BackColor = Color.LightYellow;
```

## Cross References
- Refer to Figure 331 in the user guide for a visual example of group styles in action.
- Documentation on designing custom grid column styles.
- Details on setting appearance properties dynamically or at design time.

<!-- tags: grid, column-styling, appearance, group-style, column-based-formatting, Syncfusion-Winforms, version-11.4.0.26 keywords: grid, grouping, appearance customization, column styles -->
```