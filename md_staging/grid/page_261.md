```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_261.jpeg
document_name: grid
page_number: 261
page_id: grid#page_261
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:06:09Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Content

### 4.1.4.6.6.26 Binom.Inv

The `Binom.Inv` function returns the smallest value for which the cumulative binomial distribution is greater than or equal to a criterion value.

#### Syntax

```plaintext
BINOM.INV(trials, probability_s, alpha)
```

Where:
- `trials` is the number of Bernoulli trials.
- `probability_s` is the probability of a success on each trial.
- `alpha` is the criterion value.

#### Remarks

- `#NUM!` - occurs if `trials` is less than zero.
- `#VALUE!` - occurs if `trials` is non-numeric.
- `#NUM!` - occurs if `probability_s` is less than zero.
- `#NUM!` - occurs if `probability_s` is greater than one.
- `#VALUE!` - occurs if `probability_s` is non-numeric.
- `#NUM!` - occurs if `alpha` is less than zero.
- `#NUM!` - occurs if `alpha` is greater than one.
- `#VALUE!` - occurs if `alpha` is non-numeric.

### 4.1.4.6.6.27 CEILING

Returns a number rounded up, away from zero, to the nearest multiple of significance. For example, if you want to avoid using pennies in your prices and your product is priced at $4.82, use the formula `=CEILING(4.82,0.05)` to round prices up to the nearest nickel.

#### Syntax

```plaintext
CEILING(number, significance)
```

Where:
- `number` is the value you want to round off.
- `significance` is the multiple to which you want to round.

## Page-level Navigation/TOC

- 4.1.4.6.6.26 `Binom.Inv`
- 4.1.4.6.6.27 `CEILING`

<!-- tags: [Syncfusion, Winforms, Essential Grid, Binom.Inv, CEILING, cumulative binomial distribution, probability, rounding, Bernoulli trials] keywords: [Binom.Inv, CEILING, cumulative, binomial, distribution, probability, rounding, trials, significance] -->
```