```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_448.jpeg
document_name: chart
page_number: 448
page_id: chart#page_448
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:42:28Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Describes the methods and properties of the ChartLegend in Windows Forms.
- Highlights customization options for legend items.
- Explains how to dynamically filter and manipulate legend items during runtime.

## Content

### ChartLegend Methods

| Event Name         | Description                                                                 | EventArgs                                                                 | Default | Required |
|--------------------|-----------------------------------------------------------------------------|--------------------------------------------------------------------------|---------|----------|
| DrawItemText       | Used to customize the rendering of the legend item text.                  | object sender, ChartLegendDrawItemTextEventArgs e                       | NA      | NA       |
| FilterItems        | Used to dynamically provide a list of legend items during runtime.        | object sender, ChartLegendFilterItemsEventArgs e                         | NA      | NA       |

### ChartLegend Method

| ChartLegend Method | Description                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| GetItemBy          | Gets the legend item at the specified coordinates.                         |

You can also reference specific legend items and apply settings on them individually:

### LegendItem Properties

| LegendItem Property | Description                                                                                   |
|--------------------|-----------------------------------------------------------------------------------------------|
| BorderColor        | Specifies the color of the border around the legend shape.                                    |
| Font               | Specifies the font for the text in this legend item.                                          |
| Spacing            | Specifies the space between this item and its adjacent items. Default is 20.                  |
| Text               | Specifies the text of the legend item. By default this will reflect the corresponding series name. |
| TextColor          | Specifies the text color for this item.                                                      |
| IconAlignment      | Specifies how the icon should be aligned within the item rectangle.                        |
| TextAlignment      | Specifies how the text should be aligned within the item rectangle.                        |
| VisibleCheckBox    | If this property is set to `true`, a checkbox will be shown beside the legend item through which the user can show/hide the corresponding series in the chart. |
| ShowShadow         | Will render a shadow around the item image and text using the ItemsShadowColor.             |
| ShadowOffset       | Specifies the breadth of the shadow.                                                         |

## API Reference

### ChartLegend Properties

- **BorderColor** (Color): Specifies the color of the border around the legend shape.
- **Font** (Font): Specifies the font for the text in the legend item.
- **Spacing** (int): Specifies the space between legend items. Default is 20.
- **Text** (string): Specifies the text of the legend item.
- **TextColor** (Color): Specifies the text color for the legend item.
- **IconAlignment** (Alignment): Specifies how the icon should be aligned within the item rectangle.
- **TextAlignment** (Alignment): Specifies how the text should be aligned within the item rectangle.
- **VisibleCheckBox** (bool): If set to `true`, shows a checkbox for hiding/showing the corresponding series.
- **ShowShadow** (bool): Renders a shadow around the item image and text.
- **ShadowOffset** (int): Specifies the breadth of the shadow.

## Code Examples

### Customizing Legend Items
```csharp
private void chart1_CustomizeLegend(object sender, CustomizeLegendEventArgs e)
{
    foreach (var item in e.Legend.BorderItems)
    {
        item.BorderColor = Color.Blue;
        item.Font = new Font("Arial", 10, FontStyle.Bold);
        item.TextColor = Color.Red;
    }
}
```

## Cross References
- Refer to the section on "Customizing Chart Appearance" for more details on styling charts.

<!-- tags: [Syncfusion Winforms, ChartLegend, LegendItem, Customization, Windows Forms, Chart, Design-Time, Run-Time] keywords: [legend, chart, legend item, customization, Windows Forms, DrawItemText, FilterItems, GetItemBy, BorderColor, Font, Spacing, Text, TextColor, IconAlignment, TextAlignment, VisibleCheckBox, ShowShadow, ShadowOffset] -->
```