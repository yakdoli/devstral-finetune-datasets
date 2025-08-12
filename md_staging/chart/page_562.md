```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_562.jpeg
document_name: chart
page_number: 562
page_id: chart#page_562
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:51:46Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Explanation of `InverseFCumulativeDistribution` method and its parameters.
- Example usage of the method in both C# and VB.NET.
- Brief overview of the `Inverse Normal Distribution` formula.

## Content

### InverseFCumulativeDistribution Method

`InverseFCumulativeDistribution` is calculated using the `Statistics.UtilityFunctions` class. The following table describes its parameters and return values.

| Method Name                | Parameters                                                                                                           | Return Value                                                                                                                                              |
|---------------------------|----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| **InverseFCumulativeDistribution** | 1. **fValue**: The F value for which you need the distribution.<br>2. **firstDegreeOfFreedom**: an integer value that represents the first degree of freedom.<br>3. **secondDegreeOfFreedom**: an integer value that represents the second degree of freedom. | A double that represents the inverse F cumulative distribution.                                                                                                   |

#### Example

Here is a code snippet that shows a sample usage.

```csharp
using Syncfusion.Windows.Forms.Chart.Statistics;

double x = Statistics.UtilityFunctions.InverseFCumulativeDistribution(fvalue, firstdegreeOfFreedom, secondDegreeOfFreedom);
```

```vb
Imports Syncfusion.Windows.Forms.Chart.Statistics

double x = Statistics.UtilityFunctions.InverseFCumulativeDistribution(fvalue, firstdegreeOfFreedom, secondDegreeOfFreedom)
```

### 4.12.2.12 Inverse Normal Distribution

This formula returns an approximation of the inverse of the standard normal cumulative distribution. That is, for a given P, it returns an approximation to the x satisfying \( P = \operatorname{Pr}(z \text{ is smaller than } x) \) where \( z \) is a random variable from the standard normal distribution.

#### Using the Formula

`InverseNormalDistribution` is calculated using the `Statistics.UtilityFunctions` class. The following table describes its parameters and its values.

## API Reference (if applicable)
- Not explicitly detailed in the current content.

## Code Examples (multi-language supported)
- Provided in both C# and VB.NET for `InverseFCumulativeDistribution`.

## Cross References
- Refer to the `Statistics.UtilityFunctions` class for more details.
- Related topics could include other statistical functions and distributions.

## RAG Annotations
<!-- tags: [product, module, control, api, version?] keywords: [InverseFCumulativeDistribution, Statistics.UtilityFunctions, Inverse Normal Distribution, fValue, firstDegreeOfFreedom, secondDegreeOfFreedom, P, pr(z is smaller than x)] -->
```