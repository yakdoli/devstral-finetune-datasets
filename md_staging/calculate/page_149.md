```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_149.jpeg
document_name: calculate
page_number: 149
page_id: calculate#page_149
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:08:09Z
fidelity: lossless
-->

## Essential Calculate

### BINOMDIST(number_s, trials, probability_s, cumulative)

Where:
- **number_s**: is the number of successes in trials.
- **trials**: is the number of independent trials.
- **probability_s**: is the probability of success on each trial.
- **Cumulative**: a logical value that determines the form of the function. If cumulative is `True`, then BINOMDIST returns the cumulative distribution, which is the probability that there are at most `number_s` successes; if `False`, it returns the probability that there are exactly `number_s` successes.

### Remarks

- Number_s and trials are truncated to integers.
- Number_s should be `>= 0` and `<=` trials.
- Probability_s should be `>= 0` and `<= 1`.
- The binomial probability mass function is:
  \[
  b(x,n,p) = \binom{n}{x} p^n (1-p)^{n-x}
  \]
  where:
  \[
  \binom{n}{x}
  \]
  is COMBIN(n,x).
  
- The cumulative binomial distribution is:
  \[
  B(x,n,p) = \sum_{y=0}^{x} b(y,n,p)
  \]

### 4.7.15 CEILING

Returns number rounded up, away from zero, to the nearest multiple of significance. For example, if you want to avoid using pennies in your prices and your product is priced at $4.82, use the formula =CEILING(4.82,0.05) to round prices up to the nearest nickel.
```