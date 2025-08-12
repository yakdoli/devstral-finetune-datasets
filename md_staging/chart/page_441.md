```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_441.jpeg
document_name: chart
page_number: 441
page_id: chart#page_441
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:42:05Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

[C#]

```csharp
// Associate legend1 with series1
series[0].LegendName = "legend1";
// Associate legend2 with series2
series[1].LegendName = "legend2";
```

[VB.NET]

```vb
' Associate legend1 with series1
series[0].LegendName = "legend1"
' Associate legend2 with series2
series[1].LegendName = "legend2"
```

## Legend Look and Feel

Here are some common properties you could use to customize the overall legend appearance:

| ChartLegend Property     | Description                                                                                                                                                                                   |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BackColor                | Gets / sets the background color of the legend. The default value is Transparent.                                                                                                              |
| VisibleCheckBox          | If set to `true`, a checkbox will be displayed beside each legend item. And if this checkbox is unchecked the corresponding series will disappear from the chart plot. Default is `false`. |
| Border                   | Gets / sets the border style of the legend. **ShowBorder** should be `true`.                                                                                                                   |
| ShowBorder               | Specifies whether a border should be drawn. By default it is set to `false`.                                                                                                                   |
| Font                     | Specifies the font that is to be used for the text rendered in the legend items. The default font style is Verdana, 8, Regular.                                                                 |
| BackInterior             | Sets the interior appearance for the legend. This overrides the BackColor property.                                                                                                             |
| BackgroundImage          | Sets the background image for the legend. This setting overrides the BackInterior property settings.                                                                                           |
| BackgroundImageLayout    | Sets the layout for the background image.                                                                                                                                                      |

<!-- tags: [Windows Forms, Chart, Legend, customization, properties, appearance] keywords: [Syncfusion, legend style, legend background, checkbox visibility, border style, font, image background] -->
```