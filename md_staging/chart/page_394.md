```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_394.jpeg
document_name: chart
page_number: 394
page_id: chart#page_394
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:40:30Z
fidelity: lossless
--> 

# Essential Chart for Windows Forms

| et |   |   | you want to specify the OffsetType (see below). |
| --- | --- | --- | --- |
| DateTimeInterval.OffsetType | Set | DateTime | Specifies the type of offset specified above. Could be Auto, Years, Months, Weeks, Days, Hours, Minutes, Seconds or Milliseconds. |
| RangePaddingType | Auto | Double and DateTime | Specifies if there should be any padding applied between the points and the axes, before and after the datapoints. |

## Overview

- Specifies various axis offset settings for DateTime values.
- Configures padding between axis labels and data points.
- Includes detailed information on setting axis dimensions.

## Content

### 4.6.7 Axis Dimensions

The axis' starting point, length, and the whole rectangle (comprising the axis and its labels) can be customized using the following properties.

#### ChartAxis Property Description

| ChartAxis Property | Description |
| --- | --- |
| Location | Specifies the starting location of the axis. **LocationType** property should be equal to **Set** to set the Location property. |
| LocationType | <ul><li>**Set** - To be able to use the above Location property.</li><li>**Auto** - Axis position will be automatically calculated to prevent overlap with the labels. (Default value)</li><li>**AntiLabelCut** - Axis thickness is calculated and the corresponding axis will be placed automatically, to prevent cutting of the labels by the sides of the control. Doing this preserves one co-ordinate of the axis location (X coordinate for horizontal axis and y coordinate for vertical axis).</li></ul> |
| AutoSize | Specifies whether the length of an axis is calculated automatically or specified via the Size property. |
| Size | Lets you specify the length of the axis. Uses the x value for x-axis and y-value for y-axis. Increasing or decreasing the default length will cause the intervals to expand or shrink correspondingly. The **AutoSize** should be set to **false** for this property to be used. |

## API Reference

### Properties

- DateTimeInterval.OffsetType: Specifies the type of offset for DateTime values.
- RangePaddingType: Specifies padding between points and axes.
- Location: Specifies the starting location of the axis.
- LocationType: Controls how the axis position is calculated.
- AutoSize: Controls whether axis length is automatically calculated.
- Size: Allows specifying the length of the axis.

## Code Examples (multi-language supported)

### C#

```csharp
using Syncfusion.Windows.Forms.Chart;

// Example of setting DateTimeInterval.OffsetType
ChartAxis axis = chartControl1.PrimaryXAxis;
axis.DateTimeInterval.OffsetType = DateTimeIntervalOffsetType.Days;

// Example of setting RangePaddingType
axis.RangePaddingType = AxisPaddingType.Auto;

// Example of setting LocationType to Autos
axis.LocationType = ChartAxisLocationType.Auto;

// Example of setting Size
axis.AutoSize = false;
axis.Size = new System.Drawing.SizeF(500, 100);
```

## Cross References

See also:

- [DateTimeInterval.OffsetType Enum](#datetimeinterval-offsettype-enum)
- [RangePaddingType Enum](#rangepaddingtype-enum)
- [LocationType Enum](#locationtype-enum)
- [AutoSize Property](#autosize-property)
- [Size Property](#size-property)

### Anchor for Section
<!-- anchor: chart#page_394#axis-dimensions -->

## RAG Annotations

<!-- tags: [essential chart, windows forms, axis dimensions, DateTimeInterval.OffsetType, RangePaddingType, LocationType] keywords: [axis starting point, length, rectangle, control, customize, DateTime, padding, co-ordinate, AutoSize, Size] -->
```