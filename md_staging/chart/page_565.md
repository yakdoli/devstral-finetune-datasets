<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_565.jpeg
document_name: chart
page_number: 565
page_id: chart#page_565
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:50:20Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates the usage of statistical functions in Syncfusion.Windows.Forms.Chart.Statistics.
- Provides code examples for generating a random number using the normal distribution.

## Content

### Normal Distribution Density

#### WinForms-specific Code Examples

##### C#

```csharp
using Syncfusion.Windows.Forms.Chart.Statistics;
double x = Statistics.UtilityFunctions.NormalDistribution(p);
```

##### VB.NET

```vb
Imports Syncfusion.Windows.Forms.Chart.Statistics
double x = Statistics.UtilityFunctions.NormalDistribution(p)
```

#### Explanation of Normal Distribution Density

4.12.2.14 Normal Distribution Density

In probability and statistics, the log-normal distribution is the probability of distribution of any random variable whose logarithm is normally distributed (the base of the logarithmic function is immaterial in that loga x is normally distributed if and only if logb X is normally distributed). If x is a random variable with a normal distribution, then exp(X) will have a log-normal distribution.

"Log-normal" can also be written as "log normal", "lognormal" or "logistic normal".

A variable might be modeled as log-normal if it can be thought of as the multiplicative product of many small independent factors. A typical example of this is the long-term return rate on a stock investment: it can be considered as the product of the daily return rates.

The log-normal distribution has a probability density function (pdf),

\[
f(x; \mu, \sigma) = \frac{1}{x \sigma \sqrt{2 \pi}} e^{-\frac{(\ln x - \mu)^2}{2 \sigma^2}}
\]

for \( x > 0 \), where \(\mu\) and \(\sigma\) are the median and standard deviation of the variable's logarithm. The expected value is,

\[
\mathbb{E}(X) = e^{\mu + \sigma^2/2}
\]

and the variance is,

\[
\text{var}(X) = (e^{\sigma^2} - 1)e^{2\mu + \sigma^2}
\]

### Notes
- The log-normal distribution is often used to model data that is skewed to the right.
- The \( \mu \) parameter is the median, and \( \sigma \) is the standard deviation of the logarithmic scale.

## API Reference

### Utility Functions for Normal Distribution
- `NormalDistribution(p)`  
  This method generates a random number from the normal distribution.

### Parameters
- \( p \): A probability value, typically between 0 and 1, used to determine the quantile.

### Returns
- A double representing a random number from the normal distribution.

## Code Examples

#### Usage of NormalDistribution Method

##### C#

```csharp
using Syncfusion.Windows.Forms.Chart.Statistics;

// Example usage
double probability = 0.5;
double randomNumber = Statistics.UtilityFunctions.NormalDistribution(probability);
Console.WriteLine("Generated random number: " + randomNumber);
```

##### VB.NET

```vb
Imports Syncfusion.Windows.Forms.Chart.Statistics

' Example usage
Dim probability As Double = 0.5
Dim randomNumber As Double = Statistics.UtilityFunctions.NormalDistribution(probability)
Console.WriteLine("Generated random number: " + randomNumber)
```

### Notes on Usage
- The `NormalDistribution` method is useful in simulations and statistical analysis where random numbers from a normal distribution are required.

<!-- tags: [Syncfusion, Chart, Statistical Functions, Normal Distribution, Log-Normal Distribution] keywords: [normal distribution, log-normal distribution, random number generation, probability density function, WinForms, Syncfusion, charting, statistics] -->