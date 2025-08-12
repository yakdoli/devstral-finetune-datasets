```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_199.jpeg
document_name: chart
page_number: 199
page_id: chart#page_199
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:27:01Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

| Applies to Chart Element | All series and points |
| --- | --- |
| Applies to Chart Types | Area Chart, Bar Chart, Bubble Chart, Column Chart, Stacking Column Chart, Stacking Column100 Chart, Line Chart, Spline Chart, Rotated Spline chart, Stepline Chart, Candle Chart, Kagi Chart, Point and Figure Chart, Renko Chart, Threeline Break Charts, Gantt Chart, Histogram chart, Tornado Chart, Combination Chart, Box and Whisker Chart, Pie Chart, Polar And Radar Chart, Step Area Chart |

Here is some sample code.

## Series Wide Setting

```csharp
// To display shadow for specific data points use Styles[]
series1.Styles[0].DisplayShadow = true;
```

```vbnet
' To display shadow for specific data points use Styles[]
series1.Styles(0).DisplayShadow = True
```

## API Reference (if applicable)
None provided in the current page.

## Code Examples (multi-language supported)

```csharp
this.chartControl1.Series[0].Style.DisplayShadow = true;
```

```vbnet
Me.chartControl1.Series(0).Style.DisplayShadow = True
```

## Cross References
See also: [Other relevant sections or pages in the user guide related to chart styles and customization.]
```