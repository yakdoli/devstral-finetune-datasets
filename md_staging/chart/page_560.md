```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_560.jpeg
document_name: chart
page_number: 560
page_id: chart#page_560
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:49:40Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Gamma Cumulative Distribution

The formula for the cumulative distribution function for the gamma distribution is,

\[
F(x)=\frac{\Gamma_{x}(\gamma)}{\Gamma(\gamma)} \quad x \geq 0 ; \gamma > 0
\]

where $\Gamma_x(\gamma)$ is the gamma function defined above and $\Gamma_x(\gamma)$ is the incomplete gamma function. The incomplete gamma function has the formula.

\[
\Gamma_{x}(a)=\int_{0}^{x} t^{a-1} e^{-t} d t
\]

### Example

Here is a code snippet that shows a sample usage.

#### Code Example: C#

```csharp
ChartSeries series = this.ChartControl1.Model.NewSeries("a=2");
for (double i = 0; i <= 20; i += 2)
{
    // Calculate Gamma Cumulative function for a points and plot the points
    // in chart control.
    series.Points.Add(i, Syncfusion.Windows.Forms.Chart.Statistics.UtilityFunctions.GammaCumulativeDistribution(2.0, i));
}
series.Type = ChartSeriesType.Spline;
series.Text = series.Name;
this.ChartControl1.Series.Add(series);
```

#### Code Example: VB.NET

```vb
Dim series As ChartSeries = Me.ChartControl1.Model.NewSeries("a=2")
For i As Double = 0 To 20 Step 2

    ' Calculate Gamma Cumulative function for a points and plot the points
    ' in chart control.
    series.Points.Add(i, Syncfusion.Windows.Forms.Chart.Statistics.UtilityFunctions.GammaCumulativeDistribution(2.0, i))
Next i
```

## Cross References

See also: [unclear] - Further references to related topics may be present in other sections of the document.
<!-- tags: [chart, windows forms, gamma distribution, cumulative distribution, C#, VB.NET, code examples] keywords: [gamma distribution, cumulative distribution function, gamma function, incomplete gamma function, Syncfusion, Windows Forms, C#, VB.NET, code examples] -->
```