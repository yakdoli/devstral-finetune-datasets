```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_428.jpeg
document_name: chart
page_number: 428
page_id: chart#page_428
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:41:10Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Introduces the concept of chart breaks in Windows Forms.
- Explains how to enable breaks and specifies the different modes available for managing breaks.
- Outlines the manual and automatic methods for setting break ranges.
- Details the exclusions and limitations of the Auto mode.

## Content

### Chart Breaks
Breaks are very useful if you add points with too large a difference in values. To enable breaks, you need to set the `ChartAxis.MakeBreaks` property to `true` and set the break mode (`ChartAxis.BreakRanges.BreaksMode` property).

There are three possible modes. They are:

- **ChartBreaksMode.None** - If this value is set, breaks are not used.
- **ChartBreaksMode.Manual (default)** - If this value is set, you can manually set the breaks ranges. To do this, use the following methods:
  - `ChartAxis.BreakRanges.Union` - add a new break range.
  - `ChartAxis.BreakRanges.Exclude` - remove the break range.
  - `ChartAxis.BreakRanges.Clear` - remove all break ranges.
- **ChartBreaksMode.Auto** - If this mode is enabled, the chart will compute the breaks ranges automatically. You can use the `ChartAxis.BreakRanges.BreakAmount` to set the minimal relative difference between values (default value is `0.1`, value range is `0.1`). The ratio of empty space should be less than the property value to break the range.

This mode has several exclusions:
- Breaks are computed only for the actual y-axis of series.
- Breaks don't work with zooming.
- Breaks don't work with stacking.

All breaks work only with Cartesian axes.

## API Reference

### Properties
- `ChartAxis.MakeBreaks`: Boolean property to enable breaks.
- `ChartAxis.BreakRanges.BreaksMode`: Enum property to set the break mode.
- `ChartAxis.BreakRanges.BreakAmount`: Double property to set the minimal relative difference between values.

### Methods
- `ChartAxis.BreakRanges.Union`: Adds a new break range.
- `ChartAxis.BreakRanges.Exclude`: Removes a break range.
- `ChartAxis.BreakRanges.Clear`: Clears all break ranges.

## Code Examples

### Example: Manual Break Mode
```csharp
// Enable breaks and set the mode to Manual
chart1.PrimaryYAxis.MakeBreaks = true;
chart1.PrimaryYAxis.BreakRanges.BreaksMode = ChartBreaksMode.Manual;

// Add a new break range manually
chart1.PrimaryYAxis.BreakRanges.Union(new ChartRange { From = 50, To = 100 });
```

### Example: Auto Break Mode
```csharp
// Enable breaks and set the mode to Auto
chart1.PrimaryYAxis.MakeBreaks = true;
chart1.PrimaryYAxis.BreakRanges.BreaksMode = ChartBreaksMode.Auto;

// Set the minimal relative difference between values
chart1.PrimaryYAxis.BreakRanges.BreakAmount = 0.2;
```

## See also
- [Syncfusion Chart Documentation](https://help.syncfusion.com/windowsforms/chart/overview)
- [Windows Forms Controls](https://help.syncfusion.com/windowsforms/controls/overview)

<!-- tags: [syncfusion, windowsforms, chart, breaks, manual, automatic] keywords: [breaks, makebreaks, breakranges, breaksmode, chartaxis, y-axis, zooming, stacking, cartesian axes] -->
```