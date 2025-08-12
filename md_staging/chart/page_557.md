```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_557.jpeg
document_name: chart
page_number: 557
page_id: chart#page_557
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:49:51Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Code Examples

```csharp
using Syncfusion.Windows.Forms.Chart.Statistics;
int result = UtilityFunctions.Factorial(int n);
```

```vb
Imports Syncfusion.Windows.Forms.Chart.Statistics
Dim int as result = UtilityFunctions.Factorial(int n)
```

## Content

### 4.12.2.7 F Cumulative Distribution

This formula returns cumulative F Distribution, which can be defined as the ratio of two chi-square distributions. The formula can be expressed as given below.

\[
\frac{U_1/d_1}{U_2/d_2}
\]

where,

- **U1** is the first chi-square distribution with \(d1\) degrees of freedom.
- **U2** is the second chi-square distribution with \(d2\) degrees of freedom.

#### Using the Formula

FCumulativeDistribution is calculated using the `Statistics.UtilityFunctions` class. The following table describes the F Cumulative distribution method.

| Method Name           | Parameters                                           | Return Value                          |
|-----------------------|------------------------------------------------------|----------------------------------------|
| **FCumulativeDistribution** | 1. **fValue**: The F value for which you want the distribution. <br> 2. **firstDegreeOfFreedom**: an integer value that represents the first degree of freedom. <br> 3. **secondDegreeOfFreedom**: an integer value that represents the second degree of freedom. | A double that represents the T cumulative distribution. |

#### Example

## API Reference

- **Namespace**: Syncfusion.Windows.Forms.Chart.Statistics
- **Class**: UtilityFunctions
- **Method**: `FCumulativeDistribution(double fValue, int firstDegreeOfFreedom, int secondDegreeOfFreedom)`
  - **Parameters**:
    - `fValue`: The F value for which you want the distribution.
    - `firstDegreeOfFreedom`: An integer value representing the first degree of freedom.
    - `secondDegreeOfFreedom`: An integer value representing the second degree of freedom.
  - **Return Value**: A double that represents the T cumulative distribution.

## Code Examples

```csharp
double result = UtilityFunctions.FCumulativeDistribution(3.5, 10, 20);
```

```vb
Dim result As Double = UtilityFunctions.FCumulativeDistribution(3.5, 10, 20)
```

## Conclusion

This section details the use of the `FCumulativeDistribution` method from the `Syncfusion.Windows.Forms.Chart.Statistics` namespace to calculate the cumulative distribution for an F value given the degrees of freedom. The example demonstrates how to use this method in both C# and VB.NET.

<!-- tags: [product, module, control, api, version?] keywords: [essential chart, windows forms, f cumulative distribution, chi-square, degrees of freedom, statistics, utility functions, fcumulativedistribution method] -->
```