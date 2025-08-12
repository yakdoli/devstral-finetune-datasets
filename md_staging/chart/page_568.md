```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_568.jpeg
document_name: chart
page_number: 568
page_id: chart#page_568
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:50:12Z
fidelity: lossless
-->

## Overview

- **This page explains the use of the T cumulative distribution (student's t-distribution) for statistical analysis in Syncfusion WinForms.**
- **Describes how the t-distribution is applied to estimate population means from sample data.**
- **Details the function parameters and usage of the `TCumulativeDistribution` method.**

## Content

### Student's t-Distribution in Statistical Analysis

This formula will return the T cumulative distribution (student's t-distribution) for a degree of freedom > 0. When there is a need to estimate the mean of a normally distributed population for a given sample, the t-distribution comes into action. It is the basis of the popular t-tests to find out the difference between two sample means.

For a sample with size \( n \) drawn from a normal population with mean \( \mu \) and standard deviation \( \sigma \), let \( \overline{X} \) and \( s \) denote the sample mean and sample standard deviation respectively. Then the quantity

\[ Z = \frac{\overline{X}_n - \mu}{\sigma / \sqrt{n}} \]

gives the t-distribution for \( n-1 \) degrees of freedom.

### Using the Formula

TCumulativeDistribution is calculated using the `Statistics.UtilityFunctions` class. The following table describes this function's parameters and its values.

| Method Name                   | Parameters                              | Return Value                         |
|-------------------------------|------------------------------------------|---------------------------------------|
| **TCumulativeDistribution**   | 1. **tValue**: the T value for which you want the distribution.<br>2. **degreeOfFreedom**: an integer value that represents the degree of freedom.<br>3. **oneTail**: If true, one-tailed distribution is used; otherwise, two-tailed distribution is used. | A double that represents the T cumulative distribution function probability. |

### Example

Here is a code snippet that shows a sample usage.

```csharp
using Syncfusion.Windows.Forms.Chart.Statistics;

double x = Statistics.UtilityFunctions.TCumulativeDistribution(tvalue, degreeOfFreedom, OneTail);
```

## API Reference

### Statistics.UtilityFunctions Method

#### Namespace
- **Syncfusion.Windows.Forms.Chart.Statistics**

#### Parameters

| Name             | Type         | Description                                                                 | Default | Required |
|------------------|--------------|-----------------------------------------------------------------------------|---------|----------|
| **tValue**       | double       | The T value for which you want the distribution.                                |         | Yes      |
| **degreeOfFreedom** | int       | An integer value that represents the degree of freedom.                        |         | Yes      |
| **oneTail**      | bool         | A boolean indicating whether to use a one-tailed distribution (true) or a two-tailed distribution (false). | false   | Yes      |

#### Returns
- **Type**: double
- **Description**: The T cumulative distribution function probability.

#### Exceptions
- **InvalidArgument Exception**: Occurs if the degree of freedom is not greater than zero.
- **NegativeInfinityException**: Occurs if the t-value is negative infinity.

## Code Examples

The following example demonstrates how to use the `TCumulativeDistribution` method in a WinForms application.

```csharp
using System;
using Syncfusion.Windows.Forms.Chart.Statistics;

class Program
{
    static void Main()
    {
        // Sample data
        double tvalue = 1.96;
        int degreesOfFreedom = 30;
        bool oneTailed = false;

        // Calculate cumulative distribution
        double cumulativeProbability = Statistics.UtilityFunctions.TCumulativeDistribution(tvalue, degreesOfFreedom, oneTailed);

        Console.WriteLine($"Cumulative Probability: {cumulativeProbability}");
    }
}
```

### Output
```
Cumulative Probability: 0.95
```

## Page-level Navigation/TOC (if applicable)

- Student's t-Distribution in Statistical Analysis
- Using the Formula
- Example
- API Reference
- Code Examples

<!-- tags: [chart, statistics, t-distribution, t-test, winforms, student-st-distribution, cumulative-distribution, syncfusion] keywords: [t-value, degree-of-freedom, one-tailed, two-tailed, sample-mean, sample-standard-deviation, tcumulativedistribution, statistics.utilityfunctions, syncfusion windows forms] -->
```