```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_555.jpeg
document_name: chart
page_number: 555
page_id: chart#page_555
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:47:48Z
fidelity: lossless
-->

## 4.12.2.5 Error Function

### Overview
- The Error function, denoted as `Erf(x)`, is explained in detail.
- It provides the probability that a measurement, under the influence of accidental errors, has a distance less than `x` from the average value at the center.
- The formula and its relation to the Gauss curve are documented.
- An example code snippet using the `Erf` method is provided.

### Content

#### 4.12.2.5 Error Function

The Error function, denoted as `Erf(x)`, gives the probability that a measurement under the influence of accidental errors has a distance less than `x` from the average value at the center. It is the integral of the Gauss curve, that is usually normalized to one with a factor of \(2/\sqrt{\pi}\). It is otherwise called as integrated Gauss function or Gauss Error function.

\[
\text{erf}(x) = \frac{2}{\sqrt{\pi}} \int_{0}^{x} e^{-t^{2}} \, dt.
\]

**Here is the plot of error function.**

![](https://via.placeholder.com/300x200?text=Figure+347%3A+Error+Function)
*Figure 347: Error Function*

#### Using the formula

The `Erf` method of the `UtilityFunctions` class returns the integral of the Gauss curve for `x > 0`.

| Method Name | Parameters                         | Return Value                     |
|-------------|------------------------------------|----------------------------------|
| Erf         | `x`: must be greater than zero.   | A double that represents the Gauss integral. |

#### Example

Here is a code snippet that shows a sample usage.

```csharp
using Syncfusion.Windows.Forms.Chart.Statistics;
```

## API Reference

### Method: Erf

#### Parameters

- **`x`**: A double that must be greater than zero.

#### Return Value

- **Type**: `double`
- **Description**: Represents the Gauss integral.

## Code Examples

The example demonstrates how to use the `Erf` method in a C# application.

```csharp
using Syncfusion.Windows.Forms.Chart.Statistics;
```

### Callouts
- The `Erf` method is part of the `UtilityFunctions` class and is used for computing the integral of the Gauss curve for positive values of `x`.

## Page-level Navigation/TOC
- **4.12.2.5 Error Function**
  - Overview
  - Content
    - Using the formula
    - Example
  - API Reference
  - Code Examples

## Cross References
- See also: Related sections or features within the same document.

<!-- tags: [windowsforms, errorfunction, erfmethod, utilityfunctions] keywords: [error, function, gauss, integral, erf, utilityfunctions, csharp, sample, code] -->
```