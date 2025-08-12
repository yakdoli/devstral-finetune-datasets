```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_338.jpeg
document_name: chart
page_number: 338
page_id: chart#page_338
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:35:35Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Content

### Symbol Border Properties

```csharp
Private Me.chartControl1.Series(0).Style.Symbol.Border.Color = Color.Blue
' Used to set the Width of the Symbol border.
Private Me.chartControl1.Series(0).Style.Symbol.Border.Width = 1
' Used to set the Alignment of the Symbol border.
Private Me.chartControl1.Series(0).Style.Symbol.Border.Alignment = PenAlignment.Outset
' Used to set the Dash style of the Symbol Border.
Private Me.chartControl1.Series(0).Style.Symbol.Border.DashStyle = DashStyle.Solid
```

**Figure 214: Blue Color Diamond symbol in a Column Chart with vertical offset of 20**

![](attachment:Illustrates_Symbol.png)

#### Specific Data Point Setting

To specify customized symbols for individual data points, use the `Series.Series[i].Symbol` property, where `i` ranges from 0 to `n` representing the data points.

### C#

```csharp
this.chartControl1.Series[0].Styles[0].Symbol.Shape = ChartSymbolShape.Diamond;
this.chartControl1.Series[0].Styles[0].Symbol.Color = Color.Green;
this.chartControl1.Series[0].Styles[0].Symbol.Size = new Size(10, 10);
this.chartControl1.Series[0].Styles[0].Symbol.Offset = new Size(1, 20);

this.chartControl1.Series[0].Styles[1].Symbol.Shape = ChartSymbolShape.Hexagon;
this.chartControl1.Series[0].Styles[1].Symbol.Color = Color.Yellow;
```

## API Reference

The `Series.Series[i].Symbol` property is used to specify the appearance of individual data points in a chart. This property supports various properties to customize the shape, color, size, and offset of the data point symbols.

### Parameters

- **Shape**: Defines the geometric shape of the symbol.
- **Color**: Sets the fill color of the symbol.
- **Size**: Specifies the dimensions of the symbol.
- **Offset**: Defines the position offset of the symbol relative to the data point.

## Code Examples

The following examples demonstrate how to set different properties of the `Symbol` for individual data points in a chart.

### Example 1: Setting the Symbol Shape and Color

```csharp
this.chartControl1.Series[0].Styles[0].Symbol.Shape = ChartSymbolShape.Diamond;
this.chartControl1.Series[0].Styles[0].Symbol.Color = Color.Green;
```

### Example 2: Setting the Symbol Size and Offset

```csharp
this.chartControl1.Series[0].Styles[0].Symbol.Size = new Size(10, 10);
this.chartControl1.Series[0].Styles[0].Symbol.Offset = new Size(1, 20);
```

### Example 3: Using Different Shapes for Each Data Point

```csharp
this.chartControl1.Series[0].Styles[0].Symbol.Shape = ChartSymbolShape.Diamond;
this.chartControl1.Series[0].Styles[0].Symbol.Color = Color.Green;

this.chartControl1.Series[0].Styles[1].Symbol.Shape = ChartSymbolShape.Hexagon;
this.chartControl1.Series[0].Styles[1].Symbol.Color = Color.Yellow;
```

## Page-Level Navigation/TOC

- Symbol Border Properties
- Specific Data Point Setting
- API Reference
- Code Examples

### Summary

This page demonstrates how to customize the appearance of individual data points in a chart using the `Series.Series[i].Symbol` property in Syncfusion WinForms. It includes setting properties such as shape, color, size, and offset, and provides code examples to illustrate these customizations.

<!-- tags: [Syncfusion WinForms, Chart, Symbol, Data Points, Customization] keywords: [ChartSymbolShape, Color, Size, Offset, Series, Styles] -->
```