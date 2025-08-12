<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_567.jpeg
document_name: chart
page_number: 567
page_id: chart#page_567
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:48:32Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- This section explains the computation of the inverse of the cumulative distribution for the T-statistic using the `InverseTCumulativeDistribution` method in Syncfusion Windows Forms.
- Covers the parameters and return value of the method, along with examples in C# and VB.NET.

## Content

### 4.12.2.15 Inverse T Cumulative Distribution

This formula computes the inverse of the cumulative distribution for T-statistic.

#### Using the Formula

`InverseTCumulativeDistribution` is calculated using the `Statistics.UtilityFunctions` class. The following table describes this function's parameters and its values.

| Method Name                       | Parameters                                                                                       | Return Value                                                                              |
|-----------------------------------|--------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| `InverseTCumulativeDistribution`  | 1. `p`: the alpha value (probability).<br>2. `degreeOfFreedom`: an integer value that represents the degree of freedom.<br>3. `oneTail`: If true, one-tailed distribution is used; otherwise, two-tailed distribution is used. | A double that represents the Inverse of T cumulative distribution function probability. |

#### Example

Here is a code snippet that shows a sample usage.

**[C#]**

```csharp
using Syncfusion.Windows.Forms.Chart.Statistics;
double x = Statistics.UtilityFunctions.InverseTCumulativeDistribution(p, degreeOfFreedom, OneTail);
```

**[VB.NET]**

```vb
Imports Syncfusion.Windows.Forms.Chart.Statistics
Dim x As Double = Statistics.UtilityFunctions.InverseTCumulativeDistribution(p, degreeOfFreedom, OneTail)
```

### 4.12.2.16 TCumulative Distribution

## Page-level Navigation/TOC (if applicable)
- This subsection is dedicated to explaining the `TCumulative Distribution` method, which is likely to follow after the current content.

## Cross References
- See also: Related sections or API references for more details on cumulative distributions.

## RAG Annotations
<!-- tags: [windows forms, statistics, cumulative distribution, t-statistic, inverse function, chart] keywords: [inverse t cumulative distribution, alpha value, degree of freedom, one-tailed, two-tailed, tcumulative distribution, statistics.utilityfunctions, syncfusion] -->