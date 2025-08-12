```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_291.jpeg
document_name: chart
page_number: 291
page_id: chart#page_291
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:32:01Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates how to use `PriceUpColor` in a Kagi Chart.
- Highlights chart customization features applicable to specific chart types.

## Content

### Chart Customization Details

Here is a table summarizing the applicability of the chart customization feature:

| 2D / 3D Limitations | Applies to Chart Element | Applies to Chart Types |
|----------------------|---------------------------|-------------------------|
| No                   | Any series               | Kagi Chart, PointandFigure Chart, Renko Chart, Three Line Break Chart |

### Sample Code Snippet

#### C#

```csharp
series.PriceUpColor = Color.Red;
series.PriceDownColor = Color.Green;
```

#### VB.NET

```vb
series.PriceUpColor = Color.Red
series.PriceDownColor = Color.Green
```

### Illustration

The following chart shows an example where `PriceUpColor` is set to "Red":

- **Figure 179: PriceUpColor = "Red"**

![Illustrates PriceUpColor](https://example.com/PriceUpColor.png)

This figure demonstrates the use of `PriceUpColor` in a Kagi Chart to visually distinguish periods of rising or falling prices.

## API Reference

### Properties
- **PriceUpColor**: Sets the color for periods when the price is rising.
- **PriceDownColor**: Sets the color for periods when the price is falling.

### Examples

#### C#

```csharp
series.PriceUpColor = Color.Red;
series.PriceDownColor = Color.Green;
```

#### VB.NET

```vb
series.PriceUpColor = Color.Red
series.PriceDownColor = Color.Green
```

### See also
- Kagi Chart
- PointandFigure Chart
- Renko Chart
- Three Line Break Chart

## Page-level Navigation/TOC
- [Overview]
- [Content]
  - Chart Customization Details
  - Sample Code Snippet
  - Illustration
- [API Reference]
  - Properties
  - Examples
- [See also]

<!-- tags: [chart, Windows Forms, Kagi Chart, PriceUpColor, customizations, Syncfusion] keywords: [essential chart, kagi chart, price color customization, priceupcolor, pricedowncolor] -->
```