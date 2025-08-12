```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_196.jpeg
document_name: calculate
page_number: 196
page_id: calculate#page_196
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:11:27Z
fidelity: lossless
-->

# Essential Calculate

**values** is an array or a reference to cells that contain numbers. These numbers represent a series of payments (negative values) and income (positive values) occurring at regular periods. Values must contain at least one positive value and one negative value to calculate the modified internal rate of return.

**finance_rate** is the interest rate you pay on the money used in the cash flows.

**reinvest_rate** is the interest rate you receive on the cash flows as you reinvest them.

## Remarks

- MIRR uses the order of values to interpret the order of cash flows. Be sure to enter your payment and income values in the sequence you want and with the correct signs (positive values for cash received, negative values for cash paid).
- If \( n \) is the number of cash flows in values, \( \text{frate} \) is the finance_rate, and \( \text{rrate} \) is the reinvest_rate, then the formula for MIRR is:

\[
\left( \frac{-NPV(\text{rrate}, \text{values[positive]}) \cdot (1+\text{rrate})^n}{NPV(\text{frate}, \text{values[negative]}) \cdot (1+\text{frate})} \right)^{\frac{1}{n-1}} - 1
\]

## 4.7.104 MOD

Returns the remainder after the number is divided by a divisor. The result has the same sign as the divisor.

### Syntax

MOD(number, divisor)

**where:**

- number is the number for which, you want to find the remainder.
- divisor is the value by which, you want to divide the number.

## Remarks

- The MOD function can be expressed in terms of the INT function:

\[
\text{MOD}(n, d) = n - d \cdot \text{INT}(n/d)
\]

<!-- tags: [MIRR, MOD, finance_rate, reinvest_rate, cash_flows, integers, divisors, interest_rates, number_manipulation, calculate, essential_calculate] keywords: [MIRR calculation, MOD function, negative_values, positive_values, reinvest_rate, finance_rate, remainder, number, divisor, INT function, cashflows, array, reference_cells] -->
```