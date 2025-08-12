```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_606.jpeg
document_name: chart
page_number: 606
page_id: chart#page_606
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:55:39Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Chart Region Events

### Overview
- The Chart handles specific mouse-related events when the user interacts with its various regions, such as Axis Labels, Chart Points, or custom regions.
- Events include ChartRegionClick, ChartRegionMouseEnter, ChartRegionMouseHover, ChartRegionMouseMove, ChartRegionMouseLeave, ChartRegionMouseUp, ChartRegionMouseDown, and ChartRegionDoubleClick.
- These events are raised with a `ChartRegionMouseEventArgs` that captures essential properties like the event point, region information, and mouse button details.

### Content

#### Chart Region Events
The Chart handles the following mouse-related events when the user interacts with the Chart using mouse, on certain specific regions in the Chart - Axis Labels, Chart Points or a custom region.

- **ChartRegionClick Event**
- **ChartRegionMouseEnter Event**
- **ChartRegionMouseHover Event**
- **ChartRegionMouseMove Event**
- **ChartRegionMouseLeave Event**
- **ChartRegionMouseUp Event**
- **ChartRegionMouseDown Event**
- **ChartRegionDoubleClick Event**

The above events are raised with a **ChartRegionMouseEventArgs** that contain the following properties.

| ChartRegionMouseEventArgs Property | Description |
|------------------------------------|-------------|
| Point                               | Represents the client point where the event occurred. |
| Region (Expanded below)             | Returns the region associated with this event. |
| Button                              | Returns the right mouse button actions. |

#### Region Property Details
The **Region** property above includes several useful information about the kind of region the user is currently interacting with:

| ChartRegion Property | Description |
|-----------------------|-------------|
| Description           | A text description of this region. |
| Type                  | Specifies the type of region. Possible values:<br>• **SeriesPoint** - interacted on a data point.<br>• **HorAxisLabel** - interacted on a horizontal axis<br>• **VerAxisLabel** - interacted on a vertical axis<br>• **ChartCustom** - interacted with a region that is none of the above. |
| IsChartPoint          | Indicates whether the region is a Chart Point in the ChartSeries. This simply checks if the above mentioned Type is SeriesPoint. |

## API Reference

### Events

#### ChartRegionMouseEventArgs
- **Point**: Represents the client point where the event occurred.
- **Region**: Returns the region associated with this event.
- **Button**: Returns the right mouse button actions.

### Region Property

- **Description**: A text description of the region.
- **Type**: Specifies the type of region. Possible values:
  - **SeriesPoint**: interacted on a data point.
  - **HorAxisLabel**: interacted on a horizontal axis.
  - **VerAxisLabel**: interacted on a vertical axis.
  - **ChartCustom**: interacted with a region that is none of the above.
- **IsChartPoint**: Indicates whether the region is a Chart Point in the ChartSeries.

## Code Examples

```csharp
// Example of handling ChartRegionClick event
chart.ChartRegionClick += (sender, args) =>
{
    System.Diagnostics.Debug.WriteLine($"Clicked on {args.Region.Description} at point {args.Point}");
};
```

<!-- tags: [chart, syncfusion, windows forms, mouse events, custom regions, axis labels, chart points] keywords: [chartregionclick, chartregionmouseeventargs, mouse interactions, region handling, point interactions, custom regions, axis labels] -->
```