```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_210.jpeg
document_name: calculate
page_number: 210
page_id: calculate#page_210
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:11:32Z
fidelity: lossless
-->

## Essential Calculate

### Consistency in Units

- **Guideline**: Make sure that you are consistent about the units you use for specifying rate and nper. If you make monthly payments on a four-year loan at 12 percent annual interest, use 12%/12 for rate and 4*12 for nper. If you make annual payments on the same loan, use 12% for rate and 4 for nper.

## 4.7.129 PROB

### Functionality

Returns the probability whose values are in a range that is between two limits. If upper_limit is not supplied, returns the probability that values in x_range are equal to lower_limit.

### Syntax

**PROB(x_range, prob_range, lower_limit, upper_limit)**

#### Parameters:

- **x_range**: The range of numeric values of x with which there are associated probabilities.
- **prob_range**: A set of probabilities associated with values in x_range.
- **lower_limit**: The lower bound on the value for which you want a probability.
- **upper_limit**: The optional upper bound on the value for which you want a probability.

### Remarks

- Any value in prob_range must be \( > 0 \) and \( < 1 \).
- If upper_limit is omitted, PROB returns the probability of being equal to lower_limit.

## 4.7.130 PRODUCT

### Functionality

Multiplies all the numbers given as arguments and returns the product.

### Syntax

**PRODUCT(number1, number2, ...)**

#### Parameters:

- **number1, number2, ...**: Numbers that you want to multiply.

<!-- tags: [product, module, control, api, version?] keywords: [PROB, PRODUCT, function, probability, multiplication, calculate, parameters, range, limits, upper_limit, lower_limit, probabilities] -->
```