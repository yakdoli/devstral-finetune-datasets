```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_289.jpeg
document_name: chart
page_number: 289
page_id: chart#page_289
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:33:02Z
fidelity: lossless
-->

## Chart Elements and Color Customization

### Overview
- This section details the customization of chart elements using `PriceDownColor` and `PriceUpColor` properties, focusing on Point and Figure Chart styles.
- Demonstrates how to apply specific color properties to chart elements in a Point and Figure Chart using both C# and VB.NET code snippets.

### Content

#### Chart Element Details

| Details                               |                                    |
|---------------------------------------|------------------------------------|
| **Possible Values**                   | Any valid color                   |
| **Default Value**                     | Color.Red                         |
| **2D / 3D Limitations**              | No                                 |
| **Applies to Chart Element**          | Any series                         |
| **Applies to Chart Types**            | Kagi Chart, Point and Figure Chart, Renko Chart, Three Line Break Chart |

#### Using `PriceDownColor` and `PriceUpColor` in Point and Figure Chart

Here is a code snippet using `PriceDownColor` in a Point and Figure Chart.

##### C#
```csharp
series7.PriceDownColor = Color.Magenta;
series7.PriceUpColor = Color.Orange;
```

##### VB.NET
```vb
series7.PriceDownColor = Color.Magenta
series7.PriceUpColor = Color.Orange
```

### API Reference

#### Properties
- **PriceDownColor**
  - *Type:* System.Drawing.Color
  - *Description:* Specifies the color used for price decline in charts.
  - *Default Value:* Color.Red
- **PriceUpColor**
  - *Type:* System.Drawing.Color
  - *Description:* Specifies the color used for price increase in charts.
  - *Default Value:* (Not specified but typically a contrasting color to `PriceDownColor`)

### Code Examples

The provided examples demonstrate how to set distinct colors for price decline and price increase in a Point and Figure Chart using C# and VB.NET. This customization can enhance the visual differentiation between different data trends in the chart.

### Related Topics
- Customizing chart elements in Syncfusion WinForms.
- Using color properties in various chart types.
- Point and Figure Chart customization examples.

<!-- tags: [Syncfusion, WinForms, Point and Figure Chart, PriceDownColor, PriceUpColor, Chart Elements, API, version 11.4.0.26] keywords: [chart customization, chart elements, price down color, price up color, point and figure chart, syncfusion chart controls, c#, vb.net, code examples] -->
``` 
