```html
<!--  
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_178.jpeg
document_name: calculate
page_number: 178
page_id: calculate#page_178
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:09:43Z
fidelity: lossless
-->

# Essential Calculate

## Content

### 4.7.67 HYPGEOMDIST

**Returns the hypergeometric distribution.** HYPGEOMDIST returns the probability of a given number of sample successes, given the sample size, population successes and population size.

#### Syntax

HYPGEOMDIST(sample_s, number_sample, population_s, number_population)

where:
- **sample_s** is the number of successes in the sample.
- **number_sample** is the size of the sample.
- **population_s** is the number of successes in the population.
- **number_population** is the population size.

#### Remarks

- All arguments are truncated to integers.
- sample_s must be >= 0 and less than both number_sample and population_s.
- number_sample must be >= 0 and < number_population.
- population_s must be >= 0 and < number_population.
- number_population must be >= 0.
- The equation for the hypergeometric distribution is:

\[
P(X=x) = h(x; n, M, N) = \frac{\binom{M}{x}\binom{N-M}{n-x}}{\binom{N}{n}}
\]

where:
- x = sample_s
- n = number_sample
- M = population_s
- N = number_population

## API Reference

### Parameters

| Name           | Type          | Description                                                                 |
|----------------|---------------|-----------------------------------------------------------------------------|
| sample_s       | integer       | The number of successes in the sample.                                         |
| number_sample  | integer       | The size of the sample.                                                     |
| population_s   | integer       | The number of successes in the population.                                    |
| number_population | integer | The size of the population.                                                   |

### Returns

The probability of exactly sample_s successes in a sample of size number_sample.

### Exceptions

- If any of the arguments are non-integer or do not meet the criteria specified in the Remarks section, an error may occur.

## Code Examples

### Example in C#

```csharp
double probability = HYPGEOMDIST(2, 5, 10, 20);
Console.WriteLine($"Probability: {probability}");
```

## See also

- Probability distributions
- Hypergeometric distribution formula
- Statistical functions in WinForms

<!-- tags: [winforms, statistical functions, hypergeometric distribution, syncfusion windows forms, 11.4.0.26] keywords: [HYPGEOMDIST, hypergeometric, probability, sample, population, successes] -->
```