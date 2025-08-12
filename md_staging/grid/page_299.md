```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_299.jpeg
document_name: grid
page_number: 299
page_id: grid#page_299
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:08:28Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Overview
- **serial_number**: The `serial_number` variable contains the hour you want to find, which can be entered in text strings, decimal numbers, or as results of other formulas or functions.
- **Examples**: Time entries include text strings like `"6:00 PM"`, decimal numbers such as `0.75` (representing 6:00 PM), or functions like `TIMEVALUE("6:00 PM")`.

### 4.1.4.6.6.107 HYPGEOMDIST

#### HYPGEOMDIST Function
- **Purpose**: Returns the hypergeometric distribution, calculating the probability of a given number of sample successes.
- **Parameters**:
  - `sample_s`: Number of successes in the sample.
  - `number_sample`: Size of the sample.
  - `population_s`: Number of successes in the population.
  - `number_population`: Size of the population.
- **Equation**: The hypergeometric distribution equation is:
  \[
  P(X = x) = h(x; n, M, N) = \frac{\binom{M}{x} \binom{N - M}{n - x}}{\binom{N}{n}}
  \]
  where:
  - \( x = \text{sample_s} \)
  - \( n = \text{number_sample} \)

#### Remarks
- All arguments are truncated to integers.
- `sample_s` must be >= 0 and less than both `number_sample` and `population_s`.
- `number_sample` must be >= 0 and < `number_population`.
- `population_s` must be >= 0 and < `number_population`.
- `number_population` must be >= 0.
<!-- tags: [Essential Grid, Windows Forms, HYPGEOMDIST, Hypergeometric Distribution, Probability, Sample, Population] keywords: [serial_number, sample_s, number_sample, population_s, number_population, hypergeometric distribution, probability calculation, formula, truncate, integer, arguments, equation, HYPGEOMDIST function, parameters] -->
```