```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_391.jpeg
document_name: chart
page_number: 391
page_id: chart#page_391
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:37:35Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates how to specify the start and end dates and interval time for the axis when working with datetime type data points.
- Provides sample code in both C# and VB.NET for customizing axis ranges.

## Content

### DateTimeRange Property

| Property        | Range Type | Value Type | Description                                                                 |
|-----------------|------------|------------|---------------------------------------------------------------------------|
| **DateTimeRange** | **Set**    | **DateTime** | Specifies the start and end dates and interval time for the axis. Use this if the data points are of datetime type. |

Here is some sample code that shows how this is done.

### C# Code Examples

```csharp
// Customize the X axis range and interval which has points of type DateTime
this.chartControl1.PrimaryXAxis.RangeType = ChartAxisRangeType.Set;
this.chartControl1.PrimaryXAxis.ValueType = ChartValueType.DateTime;
this.chartControl1.PrimaryXAxis.DateTimeRange = new ChartDateTimeRange(baseDate.AddMonths(-1), baseDate.AddMonths(6), 1, ChartDateTimeIntervalType.Months);

// Customize the Y axis range and interval which has points of type double
this.chartControl1.PrimaryYAxis.RangeType = ChartAxisRangeType.Set;
this.chartControl1.PrimaryYAxis.Range = new MinMaxInfo(1, 20, 2);

// Customize the Y axis range and interval which has points of type double
this.chartControl1.PrimaryXAxis.RangeType = ChartAxisRangeType.Set;
this.chartControl1.PrimaryXAxis.Range = new MinMaxInfo(0, 6, 1);
```

### VB.NET Code Examples

```vb
' Customize the X axis range and interval which has points of type DateTime
Me.chartControl1.PrimaryXAxis.RangeType = ChartAxisRangeType.Set
Me.chartControl1.PrimaryXAxis.ValueType = ChartValueType.DateTime
Me.chartControl1.PrimaryXAxis.DateTimeRange = New ChartDateTimeRange(baseDate.AddMonths(-1), baseDate.AddMonths(6), 1, ChartDateTimeIntervalType.Months)

' Customize the Y axis range and interval which has points of type double
Me.chartControl1.PrimaryYAxis.RangeType = ChartAxisRangeType.Set
Me.chartControl1.PrimaryYAxis.Range = New MinMaxInfo(1, 20, 2)

' Customize the x axis range and interval which has points of type double
Me.chartControl1.PrimaryXAxis.RangeType = ChartAxisRangeType.Set
```

## API Reference

### DateTimeRange Property
- **Namespace**: Syncfusion.Windows.Forms.Chart
- **Class**: ChartAxis
- **Property**: DateTimeRange
- **Type**: ChartDateTimeRange
- **Description**: Specifies the start and end dates and interval time for the axis. Use this if the data points are of datetime type.

### ChartDateTimeRange Structure
- **Constructors**:
  - `ChartDateTimeRange(DateTime start, DateTime end, int interval, ChartDateTimeIntervalType type)`

### ChartDateTimeIntervalType Enum
- **Members**:
  - `Months`
  - `Years`
  - `Days`
  - `Hours`
  - `Minutes`
  - `Seconds`

### ChartAxisRangeType Enum
- **Members**:
  - `Set`
  - `Auto`

### MinMaxInfo Structure
- **Constructors**:
  - `MinMaxInfo(double minimum, double maximum, double interval)`

## Code Examples (Multi-Language)

### C# Example

```csharp
// Example for setting DateTimeRange
chartControl1.PrimaryXAxis.DateTimeRange = new ChartDateTimeRange(
    startDate: new DateTime(2023, 1, 1),
    endDate: new DateTime(2023, 12, 31),
    interval: 1,
    intervalType: ChartDateTimeIntervalType.Months
);

// Example for setting range on numeric axis
chartControl1.PrimaryYAxis.Range = new MinMaxInfo(
    minimum: 0,
    maximum: 100,
    interval: 10
);
```

### VB.NET Example

```vb
' Example for setting DateTimeRange
chartControl1.PrimaryXAxis.DateTimeRange = New ChartDateTimeRange(
    startDate:=New DateTime(2023, 1, 1),
    endDate:=New DateTime(2023, 12, 31),
    interval:=1,
    intervalType:=ChartDateTimeIntervalType.Months
)

' Example for setting range on numeric axis
chartControl1.PrimaryYAxis.Range = New MinMaxInfo(
    minimum:=0,
    maximum:=100,
    interval:=10
)
```

<!-- tags: data visualization, axis customization, datetime ranges, Syncfusion Windows Forms Chart, C# examples, VB.NET examples, ChartDateTimeRange, MinMaxInfo, ChartAxisRangeType, ChartDateTimeIntervalType keywords: date time range, axis range, axis interval, numeric axis, datetime axis, data points, C#, VB.NET, Syncfusion WinForms -->
```