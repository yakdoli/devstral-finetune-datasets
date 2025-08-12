```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_150.jpeg
document_name: calculate
page_number: 150
page_id: calculate#page_150
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:07:57Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Describes the syntax and usage of mathematical and statistical functions for rounding and calculating probabilities.
- Contains details on the `CEILING`, `Char`, and `CHIDIST` functions, including their parameters and remarks.

## CEILING Function

### Syntax

```markdown
CEILING(number, significance)
```

#### where:
- `number` is the value you want to round off.
- `significance` is the multiple to which you want to round.

### Remarks
- Both values must be numeric.
- Regardless of the sign of a number, a value is rounded up when adjusted away from zero. If the number is an exact multiple of significance, no rounding occurs.

## `4.7.16` Char Function

### Description
The `Char` function returns the character whose number code is defined in the parameter.

#### Syntax:
```markdown
Char(number)
```

#### where:
- `number` is the numeric value to retrieve the character.

## `4.7.17` CHIDIST Function

### Description
Returns the one-tailed probability of the chi-squared (χ²) distribution. The χ² distribution is associated with a χ² test.

#### Syntax:
```markdown
CHIDIST(x, degrees_freedom)
```

#### where:
- `x` is the value at which you want to evaluate the distribution.
- `degrees_freedom` is the number of degrees of freedom.
<!-- tags: [Syncfusion, Winforms, calculate, syntax, CEILING, Char, CHIDIST, chi-squared, probability, statistical functions, rounding, Excel functions] keywords: [CEILING, significance, Char, number code, CHIDIST, degrees of freedom, chi-squared distribution] -->
```