```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_164.jpeg
document_name: calculate
page_number: 164
page_id: calculate#page_164
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:09:45Z
fidelity: lossless
-->

### depreciation/calculation

- The double-declining balance method computes the depreciation at an accelerated rate. Depreciation is highest in the first period and decreases in successive periods. DDB uses the following formula to calculate depreciation for a period:
  
  \[
  (\text{cost-salvage}) - \text{total depreciation from prior periods} * (\text{factor/life})
  \]

### 4.7.40 Degrees

**Converts radians into degrees.**

#### Syntax

```text
DEGREES(angle)
```

**where:**

- angle is the angle in radians that you want to convert.

### 4.7.41 DEVSQ

**Returns the sum of squares of deviations of data points from their sample mean.**

#### Syntax

```text
DEVSQ(number1, number2,...)
```

**where:**

- number1, number2, ... are arguments for which you want to calculate the sum of squared deviations. You can also use a single array or a reference to an array instead of arguments separated by commas.

#### Remarks

- The arguments must be numbers or names, arrays or references that contain numbers.
- The equation for the sum of squared deviations is:

  \[
  \text{DEVSQ} = \sum (x - \bar{x})^2
  \]
```