```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_181.jpeg
document_name: chart
page_number: 181
page_id: chart#page_181
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:26:49Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Customizing Column Chart Appearance

### Setting Shadow Offset

You can apply a shadow effect to a series by setting the shadow offset. This is done using the `ShadowOffset` property, which specifies the shadow's offset from the series.

```csharp
series.Style.ShadowOffset = new Size(3, 3)
```

### Border Lined Column Chart

The following figure illustrates a border-lined column chart where specific data points have been customized with borders.

![Border Lined Column Chart](image.png)
**Figure 97: Border Lined Column Chart**

### Applying Border to Specific Data Points

To customize the appearance of specific data points by adding borders, you can use the `Border` property of the `Series` object's `Styles` collection. Here's how you can apply borders to specific points in a series:

#### C#
```csharp
// Sets border for the 1st point in 1st series
series1.Styles[0].Border.Width = 3;
series1.Styles[0].Border.Color = Color.White;

// Sets border for the 3rd point in 2nd series
series2.Styles[2].Border.Width = 3;
series2.Styles[2].Border.Color = Color.White;
```

#### VB.NET
```vb.net
' Sets border for the 1st point in 1st series
series1.Styles(0).Border.Width = 3
series1.Styles(0).Border.Color = Color.White
```

## API Reference

### Series Style Properties
- **ShadowOffset**: Specifies the shadow offset of the series.
- **Border.Width**: Sets the thickness of the border around a data point.
- **Border.Color**: Sets the color of the border around a data point.

## Code Examples

### C# Example
The following C# code demonstrates how to apply a white border to specific data points in a series.

```csharp
// Example: Applying white borders to specific data points
series1.Styles[0].Border.Width = 3;
series1.Styles[0].Border.Color = Color.White;

series2.Styles[2].Border.Width = 3;
series2.Styles[2].Border.Color = Color.White;
```

### VB.NET Example
The following VB.NET code demonstrates how to apply a white border to the first data point in a series.

```vb.net
' Example: Applying white border to the first data point
series1.Styles(0).Border.Width = 3
series1.Styles(0).Border.Color = Color.White
```

<!-- tags: windows forms, chart, column chart, border, shadow offset, series style, custom data point, vb.net, csharp, winforms, syncfusion winforms, chart control keywords: chart, column, border, shadow, data point, customization, styles, series style -->
```