```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_125.jpeg
document_name: calculate
page_number: 125
page_id: calculate#page_125
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:06:27Z
fidelity: lossless
-->

# Essential Calculate

## Remarks

- **#VALUE!** - Occurs if any of the given arguments are non-numeric.

## Example

| **FORMULA**       | **RESULT** |
|-------------------|------------|
| = QUOTIENT (10,3) | 3          |
| = QUOTIENT (-20,6)| -3         |

---

## 4.5.6.12 FACTDOUBLE

### Overview
The FACTDOUBLE function returns the double factorial of a given value. The given value must be an integer value.

### Syntax
The syntax of the FACTDOUBLE function is:
```
= FACTDOUBLE (number).
```
- **number** – Required.

### Errors
- **#NUM!** - If the number is less than zero (0).
- **#VALUE!** - Occurs if any of the given arguments are non-numeric.

### Example

| **FORMULA**        | **RESULT** |
|--------------------|------------|
| = FACTDOUBLE (6)   | 48         |
| = FACTDOUBLE (-2)  | #NUM!      |

---

## 4.5.6.13 GCD

### Overview
The GCD function returns the greatest common divisor of two or more given values. The values must be a numeric value.

### Syntax
The syntax of the GCD function is:
```
= GCD (number1, number2, ...)
```

## Cross References
- **Product:** Syncfusion Winforms
- **Version:** 11.4.0.26

<!-- tags: [syncfusion-sdk, winforms, essential-calculate, factdouble, gcd, version] keywords: [syncfusion, winforms, calculate, factdouble, gcd, numeric values, errors, arguments, integer, greatest common divisor, user guide] -->
```