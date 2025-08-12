```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_392.jpeg
document_name: chart
page_number: 392
page_id: chart#page_392
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:39:02Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

You can however tweak the ranges and intervals that get generated through these properties.

## Changing Intervals

Use these properties to customize the intervals that get generated:

| ChartAxis Property       | Applies to RangeType | Applies to ValueType | Description                                                        |
| ------------------------- | -------------------- | -------------------- | ------------------------------------------------------------------ |
| DesiredIntervals         | Auto                 | Double, DateTime     | A request for the nice-range calculation engine to come up with a nice range with so many intervals. The engine will only use this setting as a guidance. Default value is 6. |
| IntervalType             | Auto                 | DateTime             | Specifies whether the interval that gets calculated should be in Years, Months, Weeks, Days, Hours, Minutes, Seconds or Milliseconds. This setting is used only if the ValueType of the axis is set to DateTime. Default value is Auto. |

## Changing Origin

Use these properties to customize the origin of the axes:

| ChartAxis Property | Applies to RangeType | Applies to ValueType | Description |
| ------------------- | -------------------- | -------------------- | ----------- |
| PreferZero          | Auto                 | Double               | Indicates whether one boundary of the calculated range should be tweaked to zero. Such tweaking will happen only if zero is within a reasonable distance from the calculated boundary. To ensure that one boundary is always zero, use the |

```html
<!-- tags: [product, module, control, api, version?] keywords: [k1, k2, ...] -->
```