```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_117.jpeg
document_name: chart
page_number: 117
page_id: chart#page_117
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:22:49Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates the use of a 3D Funnel Chart with a Gap ratio of 0.1.
- Explains the key features and details of the Funnel Chart including the numerical values and series configuration.
- Provides a C# code snippet for creating a Funnel Chart.

## Content

### Figure: World Crop Statistics
The image shows a 3D Funnel Chart illustrating crop statistics for different types of crops. The chart is labeled "World Crop Statistics" and displays the following data:

- **Wheat**: 37.5%
- **Rice**: 23.75%
- **Maize**: 21.62%
- **Barley**: 12.89%
- **Oats**: 4.15%

#### Details
The chart is structured as follows:

- **Number of Y values per point**: 1
- **Number of Series**: One.
- **Cannot be Combined with**: Any other chart types.

#### Chart Parameters
- **Gap Ratio**: 0.1

### Code Implementation
Below is the C# code snippet for creating the Funnel Chart:

```csharp
[C#]

ChartSeries series1 = this.chartControl1.Model.NewSeries("Funnel chart", ChartSeriesType.Funnel);
series1.Points.Add(0, 25.3);
series1.Points.Add(1, 45.7);
series1.Points.Add(2, 97.3);
series1.Points.Add(3, 20.6);
series1.Points.Add(4, 125.8);
```

## API Reference
- **Class**: `ChartSeries`
- **Method**: `NewSeries`
- **Parameters**:
  - Name: string - The name of the series.
  - Type: ChartSeriesType - Specifies the type of the series.
- **Method**: `Points.Add`
- **Parameters**:
  - X: decimal - The X-coordinate value.
  - Y: decimal - The Y-coordinate value.

## Code Examples
The provided C# code snippet demonstrates how to create a Funnel Chart series and add points to it.

## RAG Annotations
<!-- tags: [chart, funnel chart, winforms, syncfusion, gap ratio] keywords: [3d funnel chart, world crop statistics, chart series, points add, csharp, chartcontrol] -->
```