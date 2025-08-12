<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_972.jpeg
document_name: grid
page_number: 972
page_id: grid#page_972
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:53:15Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Visual representation of Grid Grouping control.
- Property grid displaying related properties.
- Integrated help feature showing descriptions for selected properties.
- Immediate preview of changes made using the designer.

## Content

![Figure 363: Preview and Edit Support](#)

**Figure 363: Preview and Edit Support**

### Grid Designer Functionality

Grid Designer presents a populated Grid Grouping control along with a property grid listing out the related properties. It also includes an integrated help feature to display a brief description on the property selected. You will be able to set any kind of properties using the designer so that you could see the results immediately. Here is a brief discussion on how to work with grid elements through the designer.

The Grid Grouping control shows a structured view of sports statistics, grouped by sport and school. Properties like `ID`, `losses`, `School`, and `ties` are displayed, with sorting options and grouping functionalities readily available. The property grid on the right permits customization of appearance and behavior, such as `GridVisualStyles`, `TableOptions`, and `Look and Feel` settings.

## API Reference

### Namespace: Syncfusion.Windows.Forms

#### Class: GridVisualStyles

- **GridVisualStyles**  
  Specifies the skin for the Grid.  
  - **Default ColumnWidth**: 60
  - **Visual Style**: Office2007Blue

### Properties

- **GridLineBorder**: Solid; 208, 215, 229; This
- **CaptionRowHeight**: 23
- **ColumnsMaxWidth**: 100
- **AllowSortColumns**: True
- **AllowSelection**: None
- **GroupFooterSectionHeight**: 10
- **IndentWidth**: 19
- **ListboxSelectionColor**: ApplySelectionColor

## Code Examples

```csharp
// Example of setting GridVisualStyles
Grid grid = new Grid();
grid.GridVisualStyles = GridVisualStyles.Office2007Blue;
grid.TableOptions.AllowSortColumns = true;
grid.TableOptions.GridLineBorder = "Solid; 208, 215, 229; This";
```

## Cross References

- Refer to the documentation on Grid Designer features and property customization for more details.

<!-- tags: [Essential Grid, Windows Forms, Grid Grouping, Designer, Syncfusion, Winforms, GridVisualStyles, TableOptions] keywords: [grid grouping, designer, property grid, visual styles, appearance settings, look and feel, sports statistics, column sorting, customization, Windows Forms] -->