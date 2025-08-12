```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_554.jpeg
document_name: chart
page_number: 554
page_id: chart#page_554
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:51:16Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Implements a method for the `Binomial` distribution in VB.NET.
- Detailed explanation of the `InverseBetaCumulativeDistribution` formula and its usage.
- Comprehensive explanation of parameters and return values for the `InverseBetaCumulativeDistribution` method.
- Example code snippets in both C# and VB.NET for using the `InverseBetaCumulativeDistribution` method.

## Content

### 4.12.2.4 Inverse Beta Cumulative Distribution

This formula returns the inverse of Beta Cumulative Distribution.

#### Using the formula

The `InverseBetaCumulativeDistribution` method of the `UtilityFunctions` class returns the inverse of beta cumulative distribution (for \(1 \geq p \geq 0\), \(a > 0\), \(b > 0\)).

| **Method Name**                       | **Parameters**                                                                 | **Return Value**                                                |
|----------------------------------------|--------------------------------------------------------------------------------|----------------------------------------------------------------|
| `InverseBetaCumulativeDistribution`   | 1. \(a\): First Parameter of Beta function. <br> 2. \(b\): Second Parameter of Beta function. <br> 3. \(p\): The probability. | A double that inverts the beta cumulative distribution value. |

#### Example

Here is a code snippet that shows a sample usage.

#### C# Example

```csharp
using Syncfusion.Windows.Forms.Chart.Statistics;

double result = UtilityFunctions.InverseBetaCumulativeDistribution(a, b, p);
```

#### VB.NET Example

```vb
Imports Syncfusion.Windows.Forms.Chart.Statistics
Dim double as result = UtilityFunctions.InverseBetaCumulativeDistribution(a, b, p)
```

## API Reference (if applicable)

### `InverseBetaCumulativeDistribution` Method

- **Namespace**: `Syncfusion.Windows.Forms.Chart.Statistics`
- **Class**: `UtilityFunctions`
- **Parameters**:
  - `a`: First Parameter of Beta function (`double`).
  - `b`: Second Parameter of Beta function (`double`).
  - `p`: The probability (`double`).
- **Return Type**: `double`
- **Return Description**: A double that inverts the beta cumulative distribution value.

## Code Examples (multi-language supported)

### C# Example

```csharp
using Syncfusion.Windows.Forms.Chart.Statistics;

double result = UtilityFunctions.InverseBetaCumulativeDistribution(a, b, p);
```

### VB.NET Example

```vb
Imports Syncfusion.Windows.Forms.Chart.Statistics
Dim double as result = UtilityFunctions.InverseBetaCumulativeDistribution(a, b, p)
```

## Page-level Navigation/TOC (if applicable)

- 4.12.2.4 Inverse Beta Cumulative Distribution
  - Using the formula
  - Example

<!-- tags: [inversebeta, beta cumulative distribution, utilityfunctions, chart, statistics] keywords: [inversebeta, beta cumulative distribution, utilityfunctions, chart, statistics, c#, vb.net, parameters, return value] -->
```