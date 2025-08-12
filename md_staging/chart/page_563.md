```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_563.jpeg
document_name: chart
page_number: 563
page_id: chart#page_563
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:48:17Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Describes the Inverse Normal Distribution function inSyncfusion.Windows.Forms.Chart.Statistics.
- Highlights the minimax approximation behavior and relative error constraints of the algorithm.
- Provides examples of usage in both C# and VB.NET.
- Explains the concept and mathematical formula for the Normal Distribution and its properties.

## Content

### Inverse Normal Distribution Method

| Method Name           | Parameters                     | Example                                                                 |
|-----------------------|--------------------------------|-------------------------------------------------------------------------|
| InverseNormalDistribution | p: the probability at which the function value is evaluated. p must be in (0,1) range. | A double that represents the inverse of the normal distribution function. |

The algorithm uses a minimax approximation by rational functions and the result has a relative error whose absolute value is less than 1.15e-9.

#### Example

Here is a code snippet that shows a sample usage.

**[C#]**

```csharp
using Syncfusion.Windows.Forms.Chart.Statistics;
double x = Statistics.UtilityFunctions.InverseNormalDistribution(p);
```

**[VB.NET]**

```vb
Imports Syncfusion.Windows.Forms.Chart.Statistics
double x = Statistics.UtilityFunctions.InverseNormalDistribution(p)
```

### 4.12.2.13 Normal Distribution

This formula yields the value of the standard normal cumulative distribution. Normal distributions are symmetric and have bell-shaped density curves with a single peak. Two factors, the mean (µ) and the standard deviation (σ), come into place when we speak of normal distribution. The mean indicates the peak of the density curve and the standard deviation indicates the spread of the bell curve.

The normal density function is given by,

\[
\frac{1}{\sqrt{2\pi}\sigma}e^{-\frac{(x-\mu)^{2}}{\sigma^{2}}}
\]

## API Reference (if applicable)
- **Method: InverseNormalDistribution**
  - **Parameters:**
    - p: double (the probability at which the function value is evaluated, in the range (0,1))
  - **Returns:**
    - double: The inverse of the normal distribution function value at the given probability.
  - **Exceptions:**
    - ArgumentNullException: If p is null.
    - ArgumentOutOfRangeException: If p is not in the range (0,1).

## Code Examples (multi-language supported)
- The examples provided demonstrate how to use the `InverseNormalDistribution` method in both C# and VB.NET.

<!-- tags: [chart, winforms, normal distribution, inverse normal distribution, statistics] keywords: [inverse normal distribution, normal density function, minimax approximation, Syncfusion.Windows.Forms.Chart.Statistics, C#, VB.NET] -->
```