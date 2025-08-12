```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_143.jpeg
document_name: chart
page_number: 143
page_id: chart#page_143
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:23:36Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- In Normal Mode, skewness of data is identified by the position of the median line within the box, where it should be equidistant from the hinges unless outliers are present. Whiskers indicate the minimum and maximum values or extend to 1.5 times the inter-quartile range if outliers exist.
- In Percentile Mode, the ends of the whiskers are determined by the Percentile property value, such as minimum being the 15th percentile and maximum the 85th percentile if Percentile = 0.15.
- Percentile values are bounded between 0.0 and 0.25, with the upper percentile calculated automatically.
- Outliers are present in Normal mode if whiskers extend 1.5 times the inter-quartile range, whereas in Percentile mode, they are calculated based on the Percentile value.
- The width of outliers can be adjusted via the `OutLierWidth` property, with zero signifying automatic calculation based on data points' range.

## Content

### Skewness Detection in Normal Mode
- If the median line within the box is not equidistant from the hinges, the data is considered skewed.
- Whiskers can extend to a maximum of 1.5 times the inter-quartile range if outliers are present.
- If there are no outliers (`Percentile` value is Zero), the whiskers extend to the minimum and maximum values.

### Percentile Mode Configuration
- When `Series1.ConfigItems.BoxAndWhiskerItem.PercentileMode` is set to `true`, the whiskers' ends are decided by the `Percentile` value.
- For a `Percentile` value of 0.15, the minimum value will be the 15th percentile, and the maximum will be the 85th percentile of the overall data set.

#### Note
1. The percentile value should be within the range of 0.0 to 0.25.
2. The upper Percentile value is automatically calculated based on the Percentile value. For example:
   - Percentile = 0.15
   - Upper Percentile = 1 - Percentile = 0.85

### Outlier Handling
- In Normal mode, outliers cause the whiskers to extend to a maximum of 1.5 times the inter-quartile range.
- In Percentile mode, outliers are calculated based on the Percentile value. For example:
   - Percentile = 0.15
   - Whiskers extend to the 15th and 85th percentiles.
- If the `Percentile` value is zero, there are no outliers in the chart.

### Outlier Width Adjustment
- The width of outliers can be adjusted using the `Series1.ConfigItems.BoxAndWhiskerItem.OutLierWidth` property.
- If `OutLierWidth` is zero, the outlier width is calculated based on the data points' range.

## Chart Details

| Details                      |                                                                                     |
|------------------------------|-------------------------------------------------------------------------------------|
| Number of Y values per point | 5 (minimum, lower quartile, median, upper quartile, maximum)                        |
| Number of Series              | One or more                                                                        |
| Cannot be Combined with       | Pie, Bar, Polar, Radar                                                             |

## API Reference (if applicable)
- `Series1.ConfigItems.BoxAndWhiskerItem.PercentileMode` (Boolean property)
- `Series1.ConfigItems.BoxAndWhiskerItem.Percentile` (Double property)
- `Series1.ConfigItems.BoxAndWhiskerItem.OutLierWidth` (Integer property)

## Code Examples (multi-language supported)
Code examples are not provided in the image. However, here is a sample structure:
```csharp
chart.Series.Add(new Series
{
    ConfigItems =
    {
        new BoxAndWhiskerItem
        {
            PercentileMode = true,
            Percentile = 0.15,
            OutLierWidth = 5
        }
    }
});
```

## Cross References
See also:
- [Box and Whisker Series](#box-and-whisker-series)
- [Percentile Mode Configuration](#percentile-mode-configuration)

<!-- tags: [syncfusion, winforms, boxandwhisker, chart, percentile, outlier, version:11.4.0.26] keywords: [normal mode, percentile mode, whiskers, median, quartile, outliers, data points, range, configuration] -->
```