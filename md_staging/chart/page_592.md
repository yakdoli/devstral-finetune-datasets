```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_592.jpeg
document_name: chart
page_number: 592
page_id: chart#page_592
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:51:49Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Chart Positioning and Appearance

### Positioning Options

| Option   | Description                                                                 |
|----------|-------------------------------------------------------------------------------|
| Top      | Above the chart; default setting.                                          |
| Left     | Left of the chart.                                                         |
| Right    | Left of the chart.                                                         |
| Bottom   | Left of the chart.                                                         |
| Floating | Will not be docked to any specific location. Can be docked manually by dragging the title panel. |

### Background Brush Customization

#### Back Interior
Specifies background brush of the control.

#### Area Back Interior
Specifies background brush of Chart Area of the control.

#### Chart Back Interior
Specifies background brush of ChartInterior.

### Palette Management

#### Palette
The Palette that is to be used to provide default colors for the chart series and other chart elements. The `Allow Gradient Palette` property is used to enable or disable the gradient values of the palettes.

### Legend Configuration

#### ShowLegend
Specifies if the legend is to be displayed or not.

#### Legend Position
Configuration information of the Legend object.

| ChartLegend.Position Property | Description                                      |
|-------------------------------|---------------------------------------------------|
| Top                          | Positions the legend panel to the Top of Chart.  |
| Left                         | Positions the legend panel to the Left of Chart. |

## API Reference

### ChartLegend.Position Property
- **Description**: Specifies the position of the legend panel relative to the chart.
- **Values**:
  - `Top`: Positions the legend panel at the top of the chart.
  - `Left`: Positions the legend panel to the left of the chart.

## Code Examples

```csharp
// Example: Setting the legend position to Top
chart.Legend.Position = ChartLegendPosition.Top;

// Example: Setting the legend position to Left
chart.Legend.Position = ChartLegendPosition.Left;
```

## Page-level Navigation/TOC (if applicable)
- Chart Positioning and Appearance
  - Positioning Options
  - Background Brush Customization
  - Palette Management
  - Legend Configuration

## Cross References
- See also:
  - Chart Styles and Appearance
  - Chart Series Customization
  - Legend Object Configuration

<!-- tags: [chart, positioning, appearance, legend, palette, winforms] keywords: [chartposition, legendposition, backgroundbrush, gradientpalette, stylecustomization, legendobject] -->
```