```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_260.jpeg
document_name: grid
page_number: 260
page_id: grid#page_260
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:06:08Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Content
- Math.BigMul(x, y); where:
  - x is the first number to multiply
  - y is the second number to multiply

#### 4.1.4.6.6.25 BINOMDIST

**Returns the individual term binomial distribution probability.**

##### Syntax

**BINOMDIST(number_s, trials, probability_s, cumulative)**, where:

- **number_s** is the number of successes in trials.
- **trials** is the number of independent trials.
- **probability_s** is the probability of success on each trial.
- **Cumulative** is a logical value that determines the form of the function. If cumulative is True, then BINOMDIST returns the cumulative distribution, which is the probability that there are at most number_s successes; if False, it returns the probability that there are exactly number_s successes.

##### Remarks

- Number_s and trials are truncated to integers.
- Number_s should be >= 0 and <= trials.
- Probability_s should be >= 0 and <= 1.
- The binomial probability mass function is,

  \[
  b(x, n, p) = \binom{n}{x} p^n (1-p)^{n-x}
  \]

  where:

  \[
  \binom{n}{x}
  \]

  is COMBIN(n, x).
- The cumulative binomial distribution is,

## API Reference (if applicable)
- None explicitly defined in the current scope.

## Code Examples (if applicable)
- None provided in the current scope.

## Page-level Navigation/TOC (if applicable)
- None explicitly defined in the current scope.

## Cross References
- None explicitly defined in the current scope.

## RAG Annotations
<!-- tags: [binomial distribution, math, bigmul, windows forms] keywords: [binomdist, number of successes, trials, probability, cumulative, binomial probability mass function, binomial probability distribution, probability mass function, cumulative distribution function] -->
```