```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_346.jpeg
document_name: chart
page_number: 346
page_id: chart#page_346
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:37:32Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Explains how to set text color for specific data points in a chart series.
- Demonstrates the use of `Series.Styles[0].TextColor` property to customize text colors.
- Provides examples in both C# and VB.NET for setting text colors.
- Describes the `TextFormat` property for setting text display formats.

## Content

### Specific Data Point Setting

We can set `TextColor` for specific data points in a series by using `Series.Styles[0].TextColor` property as follows.

#### Code Examples

- **C#**
  ```csharp
  // Set the text color for the three data points in the Series
  this.chartControl1.Series[0].Styles[0].TextColor = Color.Blue;
  this.chartControl1.Series[0].Styles[1].TextColor = Color.SteelBlue;
  this.chartControl1.Series[0].Styles[2].TextColor = Color.LightBlue;
  ```

- **VB.NET**
  ```vb
  ' Set the text color for the three data points in the Series
  Private Me.chartControl1.Series(0).Styles(0).TextColor = Color.Blue
  Private Me.chartControl1.Series(0).Styles(1).TextColor = Color.SteelBlue
  Private Me.chartControl1.Series(0).Styles(2).TextColor = Color.LightBlue
  ```

### See Also
- [Chart Types](Chart Types)

### 4.5.1.84 TextFormat

**Sets the format that is to be applied to values that are displayed as text**

#### Details

| **Possible Values**      | Any string value with '{0}' as place holder for the Y value.  |
|--------------------------|---------------------------------------------------------------|
| **Default Value**        | Nil                                                         |
| **2D / 3D Limitations** | No                                                          |
| **Applies to Chart Element** | Any Series and Points                                       |
| **Applies to Chart Types**   | All Chart Types                                            |

## Page-level Navigation/TOC (if applicable)
- Specific Data Point Setting
- C# Example
- VB.NET Example
- TextFormat Property

<!-- tags: [chart, windows forms, data point, text color, text format, Syncfusion Winforms] keywords: [series, styles, text color, text format, chart control, data points, chart types, series element, default value, chart formatting] -->
```