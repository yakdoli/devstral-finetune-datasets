```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_613.jpeg
document_name: chart
page_number: 613
page_id: chart#page_613
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:53:10Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

### 4.19.8 ChartLegendFilterItems Event

This event is discussed in detail in this topic: **Chart Legend**.

### 4.19.9 PreChartAreaPaint Event

The PreChartAreaPaint event is raised before the chart area is painted.

```csharp
[C#]

this.chartControl1.PreChartAreaPaint += new
System.Windows.Forms.PaintEventHandler(this.chartControl1_PreChartAreaPaint);

private void chartControl1_PreChartAreaPaint(object sender,
PaintEventArgs e)
{
    this.chartControl1.BackColor = Color.Yellow;
}
```

### 4.20 Localization

Localization allows a chart to display data according to the language and culture specific to a particular country or region.

#### Overview
- Localization is now supported in Essential Chart.
- Built-in resource files for specific languages can be easily added.
- Context menu items, exception messages, and some toolbar items can be localized.

#### Use Case Scenario
This enables you to localize any part of the chart that has static strings in it.

#### Properties

| Property    | Description | Type       | Data Type | Reference links | Dependencies |
|-------------|-------------|------------|-----------|-----------------|--------------|
|             |             |             |           |                 |              |
|             |             |             |           |                 |              |

## API Reference (if applicable)
The details of the API, including methods, properties, and events related to chart localization, can be found in the documentation for the specific `Localize` class or within the `Localization` section of the chart control's API reference.

## Code Examples (multi-language supported)
Example showcasing the localization feature for a chart:

```csharp
[C#]

// Set the culture for the chart
this.chartControl1.Chart.Culture = new CultureInfo("fr-FR");

// Example of using a localized property
this.chartControl1.Chart.PaletteName = "EnumPalette.StandardColorPalette.French";
```

## Cross References
- See also: **Chart Legend**, **PreChartAreaPaint Event**, **Localization API Reference**

<!-- tags: [Syncfusion, Winforms, Chart, Localization, PreChartAreaPaint] keywords: [chart, localization, PreChartAreaPaint, C#, culture, resource files, static strings, French, API, Chart Legend] -->
```