```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_224.jpeg
document_name: calculate
page_number: 224
page_id: calculate#page_224
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:13:13Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Describes how to calculate standard deviation based on the entire population using the STDEVP function.
- Explains the syntax and formula for the STDEVP function.
- Provides remarks on when to use the STDEVP function versus the STDEV function.

## Content

### 4.7.154 STDEVP

**Calculates standard deviation based on the entire population given as arguments.**

#### Syntax
STDEVP(number1, number2, ...)

**where:**
- `number1, number2, ...` are 1 to 30 number arguments corresponding to a population. You can also use a single array or a reference to an array instead of arguments separated by commas.

#### Remarks
- STDEVP assumes that its arguments are the entire population. If your data represents a sample of the population, then compute the standard deviation using STDEV.
- STDEVP uses the following formula:

  \[
  \sqrt{\frac{\sum(x - \bar{x})^2}{n}}
  \]

  **where:**
  - \(x\) is the sample mean AVERAGE(number1, number2, ...).
  - \(n\) is the sample size.

### 4.7.155 STDEVPA

#### Overview
Describes how to calculate standard deviation based on the entire population, including logical values and text representations of numbers.

#### Syntax
STDEVPA(number1, number2, ...)

#### Remarks
STDEVPA assumes that its arguments represent the entire population, similar to STDEVP. It includes logical values and text representations of numbers in the calculation.

## API Reference
- **Namespace:** Syncfusion.Windows.Forms
- **Class:** Essentials.Calculate
- **Method:** STDEVP
  - **Parameters:**
    - `number1`: Number or reference to a number.
    - `number2`: Number or reference to a number.
    - `...`: Up to 30 numbers or references to numbers.
  - **Returns:** The standard deviation of the population.
  - **Exceptions:** None.

## Code Examples
### Example: Using STDEVP
```csharp
double[] population = {10, 20, 30, 40, 50};
double standardDeviation = STDEVP(population);
```

### Example: Using STDEVPA with Logical Values and Text
```csharp
object[] mixedValues = {10, "20", true, false, 30};
double standardDeviation = STDEVPA(mixedValues);
```

## Cross References
- Refer to section 4.7.153 for details on the STDEV function.
- Refer to section 4.7.156 for further calculations involving standard deviation.

<!-- tags: [Syncfusion, WinForms, standard deviation, STDEVP, STDEVPA, population, sample, formula] keywords: [STDEVP, STDEVPA, population arguments, standard deviation, sample size, sample mean, logical values, text representations] -->
```