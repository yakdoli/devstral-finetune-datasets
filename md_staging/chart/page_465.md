```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_465.jpeg
document_name: chart
page_number: 465
page_id: chart#page_465
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:43:20Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Content

### Toolbar Items

| Command           | Class Name                     | Description                                                                 |
|-------------------|--------------------------------|-----------------------------------------------------------------------------|
| Save              | ChartToolbarSaveItem           | Using this command, user can save the chart to a specific location.       |
| Copy              | ChartToolbarCopyItem           | Clicking this toolbar command will copy the chart to the clipboard.        |
| Styles            | ChartToolbarStyleItem          | This opens a Chart Series Style dialog window, using which various properties and chart styles can be set. |
| Print             | ChartToolbarPrintItem          | This toolbar command is used to print the Chart.                          |
| Palette           | ChartToolbarPaletteItem        | Palette for the series can be chosen at run time using this command. All palette colors available in the designer will be available in this Palette option also. |
| Chart Types       | ChartToolbarTypeItem           | Any chart type can be set for the chart at run time using this command.   |
| Print Preview     | ChartToolbarPrintPreviewItem    | This toolbar command is used to see a print preview of the Chart.         |
| Toggling 3D       | ChartToolbarSeries3DItem       | This command is used to toggle the 3D mode of the chart.                  |
| Toggle Legend Appearance | ChartToolbarShowLegendItem | This command is used to toggle the legend appearance.                    |
| Splitter          | ChartToolbarSplitter           | This item provides a logical split between the collection of commands.   |

## Custom Toolbar Commands

You can also add custom toolbar items using the `ChartToolbarCommandItem` class. The `ChartCommands` enum lists the commands that can be added. The following table describes those commands.

## API Reference

### ChartToolbarCommandItem

- **Namespace**: Syncfusion.Windows.Forms.Chart
- **Class**: ChartToolbarCommandItem
- **Purpose**: Represents a custom command item for the chart toolbar.

### ChartCommands Enum

- **Namespace**: Syncfusion.Windows.Forms.Chart
- **Purpose**: Defines the commands that can be added to the chart toolbar.
- **Members**:
  - **Save**: Save the chart.
  - **Copy**: Copy the chart to the clipboard.
  - **Styles**: Change the chart styles.
  - **Print**: Print the chart.
  - **Palette**: Change the chart palette.
  - **ChartTypes**: Change the type of the chart.
  - **PrintPreview**: Show a print preview of the chart.
  - **Toggle3D**: Toggle the 3D mode of the chart.
  - **ToggleLegendAppearance**: Toggle the legend appearance.
  - **Splitter**: Add a logical split between commands.

## Code Examples

### Adding a Custom Toolbar Command

```csharp
using Syncfusion.Windows.Forms.Chart;

// Create a custom command item
ChartToolbarCommandItem customItem = new ChartToolbarCommandItem();
customItem.Text = "Custom Item";

// Add the custom item to the toolbar
Chart1.Toolbar.Add(customItem);
```

## Page-level Navigation/TOC

- [Save](#save)
- [Copy](#copy)
- [Styles](#styles)
- [Print](#print)
- [Palette](#palette)
- [Chart Types](#chart-types)
- [Print Preview](#print-preview)
- [Toggling 3D](#toggling-3d)
- [Toggle Legend Appearance](#toggle-legend-appearance)
- [Splitter](#splitter)

<!-- tags: [syncfusion sdk, windows forms, chart, toolbar, custom commands, print, save, copy, styles, palette, chart types, 3d, legend, designer, enum, api refence, code examples] keywords: [documentation, chart toolbar, visual studio, design time, runtime, controls, properties, methods, events, .NET] -->
```