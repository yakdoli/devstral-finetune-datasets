```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_312.jpeg
document_name: grid
page_number: 312
page_id: grid#page_312
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:09:06Z
fidelity: lossless
-->

## 4.1.4.6.6.137 ISODD

### Overview
- The ISODD function checks if a given number is odd.
- Syntax: `=ISODD(value)`
- Numeric value rounding for non-integer inputs.
- Returns `TRUE` for odd numbers and `FALSE` for even numbers.

### Content

#### ISODD Function

The ISODD function returns `TRUE` if the given number is an odd number, and returns `FALSE` if the given number is even.

**Syntax:**

The syntax of the ISODD function is:

```
=ISODD(value)
```

**The given value must be a numeric value. If it is a non-integer value, the value is rounded down.**

**Remarks:**

If the given value is nonnumeric, the ISODD function returns the `#VALUE!` error value.

**Example:**

| FORMULA      | RESULT  |
|--------------|---------|
| =ISODD(-1)   | TRUE    |
| =ISODD(2.5)  | FALSE   |
| =ISODD(5)    | TRUE    |

### Keywords
- `ISEVEN`
- `ISODD`
- `numeric value`

---

## 4.1.4.6.6.138 Logest

### Overview
- Enables prediction of exponential growth using existing data.
- Returns an array of values for regression analysis.

### Content

#### Logest Function

This feature enables you to calculate predicted exponential growth using existing data. This calculates and returns an array of values used for the regression analysis. Logest calculates and returns an array of values that is used in regression analysis.

**Table 5: Method Table**

| Method       | Description                                   | Parameters                       | Type     | Return Type | Reference links |
|--------------|-----------------------------------------------|----------------------------------|----------|--------------|-----------------|
| Logest()     | Calculates Logest for an array of cells.     | known_y's,<br>known_x's,<br>const,<br>stats | Method   | String         | N/A            |

### Keywords
- `Logest`
- `exponential growth`
- `regression analysis`
- `array of values`

```