```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_137.jpeg
document_name: calculate
page_number: 137
page_id: calculate#page_137
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:07:09Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Provides essential calculation functions for various statistical and mathematical operations.
- Includes functions such as Fisher transformation, gamma distribution, geometric mean, and more.
- Supports both direct calculations and inverse functions for specific distributions.

## Content

### Functions List

| Function Name   | Description                                                                                                                                                   |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Fisher          | Returns the Fisher transformation.                                                                                                                           |
| Fisherinv       | Returns the inverse of Fisher.                                                                                                                               |
| Forecast        | Returns the value forecasted by the linear trend.                                                                                                           |
| Gammadist       | Returns the gamma distribution.                                                                                                                              |
| Gammainv        | Returns the inverse of Gammdist.                                                                                                                            |
| Gammaln         | Returns the natural logarithm of gamma function.                                                                                                           |
| Geomean         | Returns the geometric mean.                                                                                                                                  |
| Harmean         | Returns the harmonic mean.                                                                                                                                   |
| Hypgeomdist     | Returns the hypergeometric distribution.                                                                                                                   |
| Intercept       | Returns the Y intercept of the least squares fit line.                                                                                                     |
| Kurt            | Returns the kurtosis of the set of arguments.                                                                                                               |
| Large           | Returns the kth largest value.                                                                                                                               |
| Loginv          | Returns the inverse of the Lognormdist.                                                                                                                    |
| Lognormdist     | Returns the cumulative lognormal distribution function.                                                                                                    |
| Max             | Returns the largest value among the arguments.                                                                                                              |
| Maxa           | Returns the largest value among the arguments.                                                                                                              |
| Median          | Returns the median value among the arguments.                                                                                                               |
| Min             | Returns the smallest value among the arguments.                                                                                                             |
| Mina           | Returns the smallest value among the arguments.                                                                                                              |
| Mode            | Returns the most frequently occurring value.                                                                                                                |
| Negbinomdist    | Returns the negative binomial distribution.                                                                                                                 |
| Normdist        | Returns the normal cumulative distribution.                                                                                                                 |
| Norminv         | Returns the inverse of Normdist.                                                                                                                            |
| Pearson         | Returns the Pearson product.                                                                                                                                  |

### Function Groups
- Statistical Functions: Fisher, Fisherinv, Forecast, Gammadist, Gammainv, Gammaln, Geomean, Harmean, Hypgeomdist, Large, Loginv, Lognormdist, Median, Mode, Negbinomdist, Normdist, Norminv, Pearsons.
- Distribution Functions: Gammadist, Gammainv, Loginv, Lognormdist, Normdist, Norminv.
- Central Tendency: Geomean, Harmean, Median, Mode, Max, Maxa, Min, Mina.

## API Reference

### Statistical Functions
- **Fisher**:  
  **Returns**: Fisher transformation result.  
  **Description**: Transforms a correlation coefficient into a normalized variable.

- **Fisherinv**:  
  **Returns**: Inverse of Fisher transformation.  
  **Description**: Transforms a normalized variable back to a correlation coefficient.

- **Forecast**:  
  **Returns**: Forecasted value based on a linear trend.  
  **Description**: Calculates the future value using existing values.

- **Gammadist**:  
  **Returns**: Gamma distribution value.  
  **Description**: Computes the probability density or cumulative distribution for a gamma variable.

### Distribution Functions
- **Gammainv**:  
  **Returns**: Inverse of Gammdist.  
  **Description**: Computes the value for which the cumulative gamma distribution is a specified probability.

### Summary Functions
- **Geomean**:  
  **Returns**: Geometric mean of a dataset.  
  **Description**: Calculates the nth root of the product of the values in the dataset.

- **Harmean**:  
  **Returns**: Harmonic mean of a dataset.  
  **Description**: Calculates the reciprocal of the arithmetic mean of the reciprocals of the values.

## Code Examples

### Example: Using the Fisher Transformation
```csharp
double correlation = 0.8;
double fisherTransform = Math.Tanh(correlation);
//鱼曼变换前的值
```

### Example: Forecasting Using Linear Trend
```csharp
double[] xValues = { 1, 2, 3, 4, 5 };
double[] yValues = { 2, 4, 6, 8, 10 };
double forecastValue = Forecast(xValues, yValues, 6);
```

## Cross References
- **Related Functions**: Mean, Standard Deviation, Variance.
- **Documentation**: Refer to the complete statistical functions section for more detailed information.

<!-- tags: [calculate, statistical functions, syncfusion winforms, distribution functions, harmonic mean, geometric mean, median, mode] keywords: [fisher transformation, gamma distribution, hypergeometric distribution, linear trend, forecast, kurtosis, harmonic mean, geometric mean, maximum, minimum] -->
```