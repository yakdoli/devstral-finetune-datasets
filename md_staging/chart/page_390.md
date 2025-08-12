```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_390.jpeg
document_name: chart
page_number: 390
page_id: chart#page_390
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:40:15Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

- double
- datetime
- logarithmic

If you set the `ValueType` to `Logarithmic`, then you need to specify the log base for the axis using `Axes.LogBase` property. The default value of `LogBase` is 10.

```csharp
this.chartControl1.PrimaryXAxis.ValueType = ChartValueType.Logarithmic;
this.chartControl1.PrimaryXAxis.LogBase = 3;
```

## See Also

- [Axis Range and Intervals](Axis Range and Intervals)

### 4.6.6 Axis Range and Intervals

#### Automatic Range Calculation

The range and intervals for an axis are automatically calculated by the built-in "nice range calculation engine", by default. This engine takes a raw data series and comes up with a nice human readable range of numbers in which to represent them. For example, if the data series contains points in the range 1.2 - 3.7, the engine would come up with a scale of 0 - 5 for the axis with 10 intervals of 0.5 each.

This default behavior is controlled by the `ChartAxis.RangeType` property which is set to `Auto` by default.

#### Specifying Custom Ranges

Sometimes the automatic range generation might not be good enough for you, in which case you can specify a custom range on the axis. You should start by setting the `ChartAxis.RangeType` property to `Set`. Then use one of the following properties to specify a custom range.

| ChartAxis Property | Applies to RangeType | Applies to ValueType | Description |
|--------------------|-----------------------|-----------------------|-------------|
| Range             | Set                   | Double                | Specifies the minimum, maximum and interval for the axis. Use this if the data points are of double type. |

## Page-level Navigation/TOC (if applicable)
- If the body contains a local Table of Contents for this page, keep it as a bullet/numbered list with links/text as shown. Do not create links that don’t exist.
- Ignore global site TOC or breadcrumbs unless the page explicitly describes them.

## Cross References
- Add See also: bullet list of explicit links/texts present on the page. Do not fabricate.

<!-- tags: [chart, axis, range, interval, axis range calculation, log base, chart control, windows forms] keywords: [ChartAxis, RangeType, LogBase, ChartValueType, automatically calculated, custom range, double, datetime, logarithmic] -->
```