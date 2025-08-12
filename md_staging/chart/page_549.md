```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_549.jpeg
document_name: chart
page_number: 549
page_id: chart#page_549
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:49:14Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates the use of statistical formulas in Windows Forms applications.
- Provides examples in both C# and VB.NET for implementing these formulas.
- Highlights utility functions available for statistical analysis.

## Content

### Sample Code Usage

Here is a code snippet that shows a sample usage.

```csharp
[C#]

ZTestResult ztr = BasicStatisticalFormulas.ZTest(
    Convert.ToDouble(TextBox6.Text.ToString()),
    sqrtVarianceOfFirstSeries * sqrtVarianceOfFirstSeries,
    sqrtVarianceOfSecondSeries * sqrtVarianceOfSecondSeries,
    0.05,
    series1,
    series2
);
```

```vbnet
[VB.NET]

Dim ztr As ZTestResult =
    BasicStatisticalFormulas.ZTest( _
        Convert.ToDouble(TextBox6.Text.ToString()), _
        sqrtVarianceOfFirstSeries * sqrtVarianceOfFirstSeries, _
        sqrtVarianceOfSecondSeries * sqrtVarianceOfSecondSeries, _
        0.05, _
        series1, _
        series2 _
    )
```

**Note:** For programming example, refer to the following Sample:

```
[Installed drive]:\Documents and Settings\[User name]\My Documents\Syncfusion\EssentialStudio\[Installed version]\Windows\Chart.Windows\Samples\2.0\Statistical Analysis\Chart Statistical Formulas
```

### 4.12.2 Utility Functions

Listed below are some common statistical formulas that are implemented in the `Utilities` type.

| Statistical Formulas                  | Description                                                                 |
|----------------------------------------|-----------------------------------------------------------------------------|
| **Beta Function**                     | The BetaFunction method returns the beta function for a given value.      |
| **Beta Cumulative Distribution**      | The Beta Cumulative Distribution method returns the Beta cumulative distribution for a given value. |
| **Inverse Beta Cumulative Distribution** | The Inverse Beta Cumulative Distribution method returns the Inverse Beta cumulative distribution for a given value. |

## API Reference

<!-- tags: [windows-forms, statistical-analysis, utilities, z-test, beta-function, cumulative-distribution] keywords: [chart, statistical formulas, utilities, z-test, beta function, beta cumulative distribution, inverse beta cumulative distribution] -->
```