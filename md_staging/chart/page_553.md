```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_553.jpeg
document_name: chart
page_number: 553
page_id: chart#page_553
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:49:28Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

```csharp
series.Points.Add(i, Syncfusion.Windows.Forms.Chart.Statistics.UtilityFunctions.BetaCumulativeDistribution(0.5, 0.5, i));
Next i
series.Type = ChartSeriesType.Spline
series.Text = series.Name
Me.ChartControl1.Series.Add(series)
```

## 4.12.2.3 Binomial Coefficient

### Overview
- Explores the utility of Binomial Coefficient in statistical calculations.
- Describes formula and implementation of Binomial Coefficient.
- Highlights the use of `UtilityFunctions.Binomial` method.

## Content

### Binomial Coefficient
**Binomial Coefficient** is an utility function used in statistical calculations. This function is used to determine the possible number of combinations of 'k' items that can be selected from a set of 'n' items. The binomial coefficient formula can be explicitly stated as given below.

\[
\binom{n}{k} = \frac{n!}{k!(n-k)!} \quad \text{if } n \geq k \geq 0
\]

where \( n! \) denotes the factorial of \( n \).

**Alternative Names/Notations**:
- The binomial coefficient is also known as the choose function.
- It is often read as "n choose k".
- Alternative notations include \( \text{C}(n, k) \), nCk (C for combination).
- These numbers are called binomial coefficients because they are coefficients in the binomial theorem.

### Using the formula

#### Method Details
The Binomial method of the `UtilityFunctions` class returns the binomial coefficient for given \( n \) and \( k \) values.

| **Method Name** | **Parameters** | **Return Value** |
|------------------|----------------|------------------|
| Binomial         | 1. The \( n \) value.<br>2. The \( k \) value. | An integer that represents the binomial coefficient value. |

### Example

#### Code Snippet
Here is a code snippet that shows a sample usage:

```csharp
using Syncfusion.Windows.Forms.Chart.Statistics;
int result = UtilityFunctions.Binomial(n, k);
```

## API Reference

### Method: Binomial
#### Namespace: Syncfusion.Windows.Forms.Chart.Statistics.UtilityFunctions
- **Parameters**:
  - \( n \): The \( n \) value (integer).
  - \( k \): The \( k \) value (integer).
- **Returns**: An integer representing the binomial coefficient value.
- **Usage**: Computes the number of combinations of \( k \) items from a set of \( n \) items.

## Code Examples
The provided example demonstrates how to use the `UtilityFunctions.Binomial` method to calculate binomial coefficients.

```csharp
using Syncfusion.Windows.Forms.Chart.Statistics;

// Example usage
int n = 5; // Total number of items
int k = 2; // Number of items to choose
int result = UtilityFunctions.Binomial(n, k);
// result will hold the binomial coefficient value
```

### References
- Refer to the Syncfusion WinForms Chart documentation for further details on statistical functions and their usage.

### Notes:
- Ensure that the values for \( n \) and \( k \) are non-negative integers where \( n \geq k \).
- The factorial calculations may lead to large numbers; use appropriate data types or methods to handle potential overflow.

## RAG Annotations
<!-- tags: [syncfusion, winforms, chart, binomial coefficient, statistical calculations] keywords: [binomial, combinations, n choose k, factorial, binomial theorem, utility functions, binomial method] -->
```