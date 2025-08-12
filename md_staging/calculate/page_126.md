```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_126.jpeg
document_name: calculate
page_number: 126
page_id: calculate#page_126
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:06:38Z
fidelity: lossless
-->

## Essential Calculate

### Overview
- Required numerical input for calculations.
- Handles rounding of non-integer values and error handling for invalid inputs.

### GCD Calculation

#### Number1 – Required
- If any value is not an integer, it will be rounded down.
- Errors:
  - **#NUM!** - If the number is less than zero (0).
  - **#VALUE!** - Occurs if any of the given arguments are non-numeric.

#### Example:
| FORMULA         | RESULT    |
|------------------|-----------|
| = GCD(5,3,2)    | 1         |
| = GCD(-2)       | #NUM!     |

### 4.5.6.14 LCM

#### Overview
- The LCM function returns the least common multiple of two or more given values. The values must be numeric.

#### Syntax
- The syntax of the LCM function is:
  ```
  = LCM(number1, number2, ...)
  ```
- **number1** – Required.
  - If any value is not an integer, it will be rounded down.

#### Errors:
- **#NUM!** - If the number is less than zero (0).
- **#VALUE!** - Occurs if any of the given arguments are non-numeric.

#### Example:
| FORMULA         | RESULT    |
|------------------|-----------|
| = LCM(5,2)      | 10        |
| = LCM(-2)       | #NUM!     |

### 4.5.6.15 ROMAN

## API Reference (if applicable)
- Describes members and methods related to the calculation functions.

## Code Examples
- Provides examples of how to use the LCM and GCD functions in your code.

## Cross References
- Refer to related functions and documentation for more information.

<!-- tags: [syncfusion-sdk, winforms, calculation, gcd, lcm, roman, api, l11.4.0.26] keywords: [calculate, gcd, lcm, roman, numeric, rounding, errors, least common multiple] -->
```