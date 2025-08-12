```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_012.jpeg
document_name: chart
page_number: 012
page_id: chart#page_012
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:16:13Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview

The Essential Chart for Windows Forms supports complete customization of the Chart control through Chart Wizard at design time and runtime. Key features include:

- Comprehensive customization options for the Chart control using Chart Wizard.
- Support for various data sources through the innovative Chart Data Model.
- Built-in support for date and time data types.
- Automatic interval calculation capabilities for any range of numbers or dates.

## Content

### Chart BackgroundImage Settings

The chart, titled "Chart BackgroundImage Settings," illustrates temperature ranges across different countries. The chart shows both highest and lowest temperatures for each country, with a legend indicating紫色 for the highest and green for the lowest values. The temperature is measured in degrees Celsius, and the chart background features a snowy landscape. Key data points are as follows:

- **China**: Highest = 42.6°C, Lowest = -27.4°C
- **Russia**: Highest = 36.7°C, Lowest = -42.2°C
- **Australia**: Highest = 42°C, Lowest = -10°C
- **Japan**: Highest = 25°C, Lowest = 16°C
- **India**: Highest = 47.2°C, Lowest = -5°C
- **Indonesia**: Highest = 37.8°C, Lowest = 17°C

### Key Features

Some of the key features of Essential Chart are listed below:

- **Customization Support**: The control provides complete support for customization of the Chart control through Chart Wizard at design time and also at run time. Chart Wizard comes with a new Office look and feel.
- **Chart Data Model**: An innovative data object model which makes it easy to populate the chart with any kind of data source.
- **Date Support**: Essential Chart features built-in support for dates. The data type of any series that is plotted on the chart can be set to DateTime.
- **Interval Calculation**: Offers automatic interval calculation capabilities for any range of numbers or dates. This calculation can be overridden by explicit allocation of ranges and intervals.

## API Reference

The Essential Chart for Windows Forms offers a comprehensive API for configuring and customizing the Chart control. Key elements include properties for setting data sources, series types, and styles, as well as methods for data binding and manipulation. The API also supports advanced features such as color customization, background image settings, and interactive chart elements.

## Code Examples

### Example: Creating a Basic Chart

```csharp
SfChart chart = new SfChart();
chart.PrimaryXAxis.Title = "Country";
chart.PrimaryYAxis.Title = "Temperature(°C)";

// Add data for highest temperatures
List<DataPoint> highestData = new List<DataPoint> 
{
    new DataPoint("China", 42.6),
    new DataPoint("Russia", 36.7),
    new DataPoint("Australia", 42),
    new DataPoint("Japan", 25),
    new DataPoint("India", 47.2),
    new DataPoint("Indonesia", 37.8)
};

chart.Series.Add(new ColumnSeries
{
    DataSource = highestData,
    XName = "Name",
    YName = "Value",
    Palette = ChartColorPalette.Blue
});

// Add data for lowest temperatures
List<DataPoint> lowestData = new List<DataPoint> 
{
    new DataPoint("China", -27.4),
    new DataPoint("Russia", -42.2),
    new DataPoint("Australia", -10),
    new DataPoint("Japan", 16),
    new DataPoint("India", -5),
    new DataPoint("Indonesia", 17)
};

chart.Series.Add(new ColumnSeries
{
    DataSource = lowestData,
    XName = "Name",
    YName = "Value",
    Palette = ChartColorPalette.Green
});

// Set background image
chart.ChartBevelEffectType = BevelEffectType.None;
chart.BackgroundImage = new System.Drawing.Image(location=".background.jpeg");
```

## Cross References

For more details on configuring data sources, refer to the section on "Chart Data Model."

### Figure: Chart BackgroundImage Settings
This figure illustrates the temperature ranges across different countries, highlighting the highest and lowest temperatures.

---

<!-- tags: [winforms, chart, backgroundimage,气温范围,数据模型,日期支持,区间计算,数据可视化] keywords: [chart wizard, data model, date support, interval calculation, temperature range, customizing chart, winforms, syncfusion] -->
```