```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_559.jpeg
document_name: chart
page_number: 559
page_id: chart#page_559
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:48:04Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

The Gamma function is calculated using the `Statistics.UtilityFunctions` class. The following table describes the parameters and the return value of the gamma function.

## Gamma Function Examples

### Key Values
\[
\begin{aligned}
\Gamma(-n) &= \infty \\
\Gamma(0) &= \infty \\
\Gamma\left(\frac{1}{2}\right) &= \sqrt{\pi} \\
\Gamma(1) &= 1 \\
\Gamma\left(\frac{3}{2}\right) &= \frac{\sqrt{\pi}}{2} \\
\Gamma(2) &= 1
\end{aligned}
\]

### Parameters and Return Values

| Method Name | Parameters | Return Value |
|-------------|------------|--------------|
| Gamma | p: a value for which the gamma value is required. | A double that represents the gamma function value. |

### Code Examples

#### C#

```csharp
using Syncfusion.Windows.Forms.Chart.Statistics;
double x = Statistics.UtilityFunctions.Gamma(p);
```

#### VB.NET

```vb
Imports Syncfusion.Windows.Forms.Chart.Statistics
double x = Statistics.UtilityFunctions.Gamma(p)
```

## API Reference

- **Namespace:** `Syncfusion.Windows.Forms.Chart`
- **Class:** `Statistics.UtilityFunctions`
- **Method:** `Gamma`
  - **Parameters:**
    - `p`: A value for which the gamma value is required.
  - **Return Value:** A `double` that represents the gamma function value.

### Notes

- The Gamma function method is used to calculate the gamma value for a given input `p`.
- Ensure to properly handle cases where the Gamma function diverges to infinity.

<!-- tags: [Syncfusion, Winforms, Chart, Gamma Function, API] keywords: [Gamma, StatisticsUtilityFunctions, Calculations, Charting, .NET] -->
```