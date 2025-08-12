```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_409.jpeg
document_name: chart
page_number: 409
page_id: chart#page_409
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:39:57Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview  
- Demonstrates creating a chart series and configuring axis labels and tooltips in a Windows Forms application.
- Detailed steps to add data points, set axis labels, and customize tooltips for a chart control.

## Content

### ChartSeries Configuration

```csharp
ChartSeries series = new ChartSeries("Series");
series.Points.Add(0, 120);
series.Points.Add(1, 220);
series.Points.Add(2, 150);
series.Points.Add(3, 240);

this.chartControl1.Series.Add(series);
```

### Setting Axis Labels

```csharp
// Set labeltext
arrLabel.Add("India");
arrLabel.Add("Pakistan");
arrLabel.Add("Srilanka");
arrLabel.Add("Japan");
```

### Configuring Tooltips

```csharp
// Set tooltip content
arrTooltip.Add("IND");
arrTooltip.Add("PAK");
arrTooltip.Add("SRL");
arrTooltip.Add("JPN");

this.chartControl1.ShowToolTips = true;
this.chartControl1.Series3D = true;
this.chartControl1.PrimaryYAxis.Title = "Product sold (Millions)";
this.chartControl1.PrimaryXAxis.Title = "Country";
this.chartControl1.Title.Text = "Product Sales";
```

### Axis Label Formatting Event

```csharp
void chartControl1_ChartFormatAxisLabel(object sender, ChartFormatAxisLabelEventArgs e)
{
    int index = (int)e.Value;
    if (e.AxisOrientation == ChartOrientation.Horizontal)
    {
        if (index >= 0 && index < arrLabel.Count)
        {
            e.Label = arrLabel[index].ToString();
            // Specify arrTooltip content as chartAxisLabel Tooltip
            e.ToolTip = arrTooltip[index].ToString();
        }
    }
}
```

## API Reference

### ChartControl Properties
- `ChartControl.Series`: Collection of ChartSeries elements.
- `ChartControl.PrimaryYAxis.Title`: Sets the title for the primary Y-axis.
- `ChartControl.PrimaryXAxis.Title`: Sets the title for the primary X-axis.
- `ChartControl.Title.Text`: Sets the title for the chart.

### ChartSeries Methods
- `ChartSeries.Points.Add(int, int)`: Adds data points to the chart.

### ChartSeries Properties
- `ChartSeries.Points`: Collection of data points for the series.

### Event Handling
- `ChartFormatAxisLabelEventArgs`: Event arguments for formatting axis labels.
- `ChartOrientation.Horizontal`: Indicates the orientation of the axis.

## Code Examples

### Complete Chart Control Configuration Example

```csharp
ChartSeries series = new ChartSeries("Series");
series.Points.Add(0, 120);
series.Points.Add(1, 220);
series.Points.Add(2, 150);
series.Points.Add(3, 240);

this.chartControl1.Series.Add(series);

// Arrays for labels and tooltips
List<string> arrLabel = new List<string>();
List<string> arrTooltip = new List<string>();

arrLabel.Add("India");
arrLabel.Add("Pakistan");
arrLabel.Add("Srilanka");
arrLabel.Add("Japan");

arrTooltip.Add("IND");
arrTooltip.Add("PAK");
arrTooltip.Add("SRL");
arrTooltip.Add("JPN");

// Enable tooltips and set 3D mode
this.chartControl1.ShowToolTips = true;
this.chartControl1.Series3D = true;

// Set axis titles
this.chartControl1.PrimaryYAxis.Title = "Product sold (Millions)";
this.chartControl1.PrimaryXAxis.Title = "Country";

// Set chart title
this.chartControl1.Title.Text = "Product Sales";

// Event for formatting axis labels
void chartControl1_ChartFormatAxisLabel(object sender, ChartFormatAxisLabelEventArgs e)
{
    int index = (int)e.Value;
    if (e.AxisOrientation == ChartOrientation.Horizontal)
    {
        if (index >= 0 && index < arrLabel.Count)
        {
            e.Label = arrLabel[index].ToString();
            e.ToolTip = arrTooltip[index].ToString();
        }
    }
}
```

## RAG Annotations
<!-- tags: [syncfusion, winforms, chartcontrol, chartseries, axislabels, tooltips, events] keywords: [chart series, data points, axis titles, tooltips, ChartOrientation, ChartFormatAxisLabel, ChartControl, ChartSeries] -->
```