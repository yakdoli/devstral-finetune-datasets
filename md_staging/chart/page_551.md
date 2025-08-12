```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_551.jpeg
document_name: chart
page_number: 551
page_id: chart#page_551
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:47:36Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

There are two widely used utility functions, the Gamma and Beta functions, which are used in statistics to calculate distribution values. These functions always return a double value and use two double values for input. The beta function was studied by Euler and Legendre and was named by Jacques Binet. In mathematics, the beta function (occasionally written as Beta function) which, is also called the Euler integral of the first kind, is a special function defined by:

\[
B(x, y) = \frac{\Gamma(x) \Gamma(y)}{\Gamma(x + y)}
\]

where \(\Gamma(x)\) is the gamma function.

## Using the Formula

### The Beta method of the UtilityFunctions class calculates the beta function for given two values.

| Method Name | Parameters                     | Return Value                                      |
|-------------|---------------------------------|---------------------------------------------------|
| Beta        | 1. a: The first value.         | A double that represents the beta function value. |
|             | 2. b: The second value.        |                                                   |

### Example

Here is a code snippet that shows a sample usage.

```csharp
using Syncfusion.Windows.Forms.Chart.Statistics;
double result = UtilityFunctions.Beta(a, b);
```

```vb.net
Imports Syncfusion.Windows.Forms.Chart.Statistics
Dim double as result = UtilityFunctions.Beta(a, b);
```

## 4.12.2.2 Beta Cumulative Distribution

The Beta Distribution can be defined as a family of probability distributions differing in the values of \( \alpha \) and \( \beta \). The Cumulative distribution function is given below.

---
```