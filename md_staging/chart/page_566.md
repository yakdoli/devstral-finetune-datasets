```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_566.jpeg
document_name: chart
page_number: 566
page_id: chart#page_566
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:52:01Z
fidelity: lossless
-->

### Overview

- The page describes the *Normal Distribution Density* and its implementation in Syncfusion Winforms.
- It includes a formula for evaluating the Normal Distribution Density and an example code snippet demonstrating its usage.
- The `NormalDistributionDensity` method is detailed, showing parameters such as `x`, `m`, and `sigma`, along with the expected return value.

### Content

#### Figure 349: Normal Distribution Density

![](https://i.imgur.com/mRvOJfj.png)

The figure illustrates the *Probability density function* for various values of sigma (`σ`), centered around `μ=0`. It shows the shape of the normal distribution for different standard deviations (`σ=10, 3/2, 1, 1/2, 1/4, 1/8`).

#### Using the formula

##### Parameters

The *NormalDistribution Density* function is detailed in the table below:

| Method Name             | Parameters                                                                 | Return Value                                                |
|-------------------------|---------------------------------------------------------------------------|-------------------------------------------------------------|
| NormalDistributionDensity | 1. **x**: the value at which the distribution density is evaluated.<br>2. **m**: the expected value of distribution.<br>3. **sigma**: the variance of distribution. | A double that represents the Normal Distribution Density function value. |

#### Example

Here is a code snippet that shows a sample usage.

##### [C#]

```csharp
using Syncfusion.Windows.Forms.Chart.Statistics;
double result = UtilityFunctions.NormalDistributionDensity(x, m, sigma);
```

##### [VB.NET]

```vb
Imports Syncfusion.Windows.Forms.Chart.Statistics
Dim double as result = UtilityFunctions.NormalDistributionDensity(x, m, sigma)
```

--- 

### API Reference

#### Namespace: Syncfusion.Windows.Forms.Chart.Statistics

##### Method: `NormalDistributionDensity`

- **Parameters**:
  - `x`: double - The value at which the distribution density is evaluated.
  - `m`: double - The expected value of distribution.
  - `sigma`: double - The variance of distribution.

- **Return Value**: double - Represents the Normal Distribution Density function value.

#### Code Examples

##### C#

```csharp
using Syncfusion.Windows.Forms.Chart.Statistics;

// Example usage
double x = 1.0;
double m = 0.0;
double sigma = 1.0;
double density = UtilityFunctions.NormalDistributionDensity(x, m, sigma);
```

##### VB.NET

```vb
Imports Syncfusion.Windows.Forms.Chart.Statistics

' Example usage
Dim x As Double = 1.0
Dim m As Double = 0.0
Dim sigma As Double = 1.0
Dim density As Double = UtilityFunctions.NormalDistributionDensity(x, m, sigma)
```

--- 

<!-- tags: [chart, normaldistribution, probabilitydensityfunction, normaldistributiondensity, syncfusionwinforms, winforms, statistics, utilityfunctions] keywords: [normal distribution, probability density function, expected value, variance, standard deviation, density function, Syncfusion Winforms, utility functions, API reference] -->
```