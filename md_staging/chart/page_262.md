```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_262.jpeg
document_name: chart
page_number: 262
page_id: chart#page_262
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:31:12Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates unique pattern styles for each slice in a pie chart.
- Explains label placement options for data points in Pyramid and Funnel charts.

## Content

### Pie Chart with Unique Pattern Styles

![Figure 154: Unique PatternStyle for each Slice in Pie Chart](3454553)

Figure 154 shows a pie chart where each slice has a unique pattern style:
- **Server1**: Yellow with diagonal lines.
- **Server2**: Light blue with a grid pattern.
- **Server3**: Dark blue with a dot pattern.
- **Server4**: White with a crosshatch pattern.

**See Also**
- [Chart Types](Chart Types)

### 4.5.1.42 LabelPlacement

#### Overview
Gets or sets the Pyramid chart or Funnel chart data point label placement when `ChartAccumulationLabelStyle` is set as **Inside**.

#### Details

| Possible Values                                                                                               |
|--------------------------------------------------------------------------------------------------------------|
| - **Center** – DataPoint labels are aligned to the center of the Pyramid segment.                         |
| - **Top** - DataPoint labels are aligned to the top of the Pyramid segment.                               |

## API Reference (if applicable)
- Namespace: `Syncfusion.Windows.Forms.Chart`
- Class: `AccumulationSeries`
- Property: `LabelPlacement`

## Code Examples (multi-language supported)
- Example to set the `LabelPlacement` property:
  ```csharp
  chart.Series["Server"].AccumulationLabelPlacement = LabelPlacement.Center;
  ```

## Cross References
- See also: [Chart Types](Chart Types)

<!-- tags: [charts, windows forms, pie chart, pyramid chart, funnel chart, label placement, pattern styles] keywords: [DataPoint labels, ChartAccumulationLabelStyle, LabelPlacement, Pyramid segment, Funnel chart, pie chart styles] -->
```