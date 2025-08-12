```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_558.jpeg
document_name: chart
page_number: 558
page_id: chart#page_558
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:51:33Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

Here is a code snippet that shows a sample usage.

### Code Snippets

#### C#

```csharp
using Syncfusion.Windows.Forms.Chart.Statistics;
double x = Statistics.UtilityFunctions.FCumulativeDistribution(fvalue, firstdegreeOfFreedom, secondDegreeOfFreedom);
```

#### VB.NET

```vb
Imports Syncfusion.Windows.Forms.Chart.Statistics
Dim x As Double = Statistics.UtilityFunctions.FCumulativeDistribution(fvalue, firstdegreeOf Freedom, secondDegreeOfFreedom)
```

### Overview
- Demonstrates the usage of the `FCumulativeDistribution` method for statistical calculations.

### Content

#### 4.12.2.8 Gamma Function

The Gamma Function is an attempt to generalize the factorial function to real and complex numbers. It is related to the factorial function by the relationship:

\[
\Gamma(n) = (n-1)!
\]

##### The Gamma Function

For a complex number \( x \) with a positive real part, the function can be given by:

\[
\Gamma(x) = \int_0^\infty t^{x-1} e^{-t} \, dt, \quad x > 0
\]

##### Special Values of gamma function

### API Reference

#### Namespace: Syncfusion.Windows.Forms.Chart.Statistics

##### UtilityFunctions

- **Methods:**
  - `FCumulativeDistribution(fvalue, firstdegreeOfFreedom, secondDegreeOfFreedom): double`

--- 

### Code Examples

#### C#

```csharp
using Syncfusion.Windows.Forms.Chart.Statistics;
double x = Statistics.UtilityFunctions.FCumulativeDistribution(fvalue, firstdegreeOfFreedom, secondDegreeOfFreedom);
```

#### VB.NET

```vb
Imports Syncfusion.Windows.Forms.Chart.Statistics
Dim x As Double = Statistics.UtilityFunctions.FCumulativeDistribution(fvalue, firstdegreeOf Freedom, secondDegreeOfFreedom)
```

### RAG Annotations
<!-- tags: [syncfusion, windowsforms, gamma function, statistical methods, f cumulative distribution] keywords: [chart, statistics, utility functions, gamma function, factorial, complex numbers] -->
```