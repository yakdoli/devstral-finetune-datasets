```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_001.jpeg
document_name: chart
page_number: 001
page_id: chart#page_001
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:15:21Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview

- Introduction to Syncfusion’s Essential Chart for Windows Forms.
- discuss the charting capabilities for Windows Forms applications.
- highlight the features and benefits of using this tool in development.

## Content

### Introduction

Welcome to the documentation for *Essential Chart for Windows Forms*. This guide provides detailed information on how to effectively utilize the charting controls in your Windows Forms applications.

### Features and Benefits

#### 1. Comprehensive Charting Tools
Essential Chart offers a wide range of chart types suitable for various data visualization needs:
- Line, Bar, Column, Pie, Doughnut
- Polar, Radar, and more

#### 2. Customization Options
Users can customize every aspect of their charts, including:
- Themes and styles
- Axes and labels
- Data points and trends
- Annotations and legends

#### 3. Integration and Performance
Seamlessly integrates with .NET applications, providing:
- High-performance rendering and responsiveness
- Support for real-time data updates
- Extensibility through APIs and events

## API Reference

### Chart Control

#### Namespace
- `Syncfusion.Windows.Forms.Chart`

#### Methods and Properties
- **AddSeries()**: Adds a new series to the chart.
- **Render()**: Renders the chart with updated data.
- **Clear()**: Clears all data and series from the chart.

#### Events
- **OnSeriesAdded**: Triggered when a new series is added.
- **OnRender**: Triggered during chart rendering.

## Code Examples

### Creating a Basic Bar Chart

```csharp
using Syncfusion.Windows.Forms.Chart;
using System.Drawing;

// Initialize chart object
BarChart char = new BarChart();

// Add series data
char.AddSeries(new Series() {
    Name = "Sales Data",
    ItemsSource = new[] { 100, 200, 300, 400, 500 },
    Color = Color.Blue
});

// Render chart in a Windows Forms application
Form form = new Form();
form.Controls.Add(char);
form.Show();
```

### Using Themes

```csharp
char.Theme = new Syncfusion.Windows.Forms.Chart.ChartTheme("Material");
```

## RAG Annotations

<!-- tags: [product, windows forms, chart, essential studio, data visualization, api, version] keywords: [syncfusion, windows forms, chart, essential chart, data, visualization, controls, api, charting, documentation, features] -->
```