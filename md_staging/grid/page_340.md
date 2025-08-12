```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_340.jpeg
document_name: grid
page_number: 340
page_id: grid#page_340
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:11:05Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Overview
- Describes parameters used in financial calculations within the Essential Grid for Windows Forms.
- Explains the significance of pmt, fv, and type in annuity and loan formulas.

### Content

#### Parameters Explained
- **pmt**: The payment made for each period and remains constant over the life of the annuity.
  - Includes principal and interest but excludes other fees or taxes.
  - Example: Monthly payments on a $10,000, four-year car loan at 12 percent are $263.33.
  - Enter $-263.33 if pmt is used in the formula.
  - If omitted, the fv argument must be included.

- **fv**: The future value or cash balance desired after the last payment.
  - If omitted, assumed to be 0 (e.g., future value of a loan).
  - Example: Saving $50,000 over 18 years for a special project.
  - Helps in determining monthly savings with a guessed interest rate.
  - If omitted, the pmt argument must be included.

- **type**: Indicates when payments are due, with values 0 or 1.
  - 0: Payments are due at the end of the period.
  - 1: Payments are due at the beginning of the period.

#### Remarks
- **Consistency**: Ensure consistency in units for rate and nper.
  - For monthly payments on a four-year loan at 12% annual interest:
    - Use `12%/12` for rate and `4*12` for nper.
  - For annual payments, use `12%` for rate and `4` for nper.
- **Cash Representation**: In annuity functions:
  - Outflow (e.g., deposit to savings) represented by a negative number.
  - Inflow (e.g., dividend check) represented by a positive number.
- **Rate Calculations**:
  - If rate is not 0:
    \[
    pv*(1 + rate)^{nper} + pmt(1 + rate*type) * \left( \frac{(1 + rate)^{nper} - 1}{rate} \right) + fv = 0
    \]
  - If rate is 0:
    \[
    (pmt * nper) + pv + fv = 0
    \]

#### QUARTILE Function
- **Purpose**: Returns the quartile of a data set.
- **Syntax**: `QUARTILE(array, quart)`
  - `array`: Array or cell range of numeric values for which the quartile value is required.
  - `quart`: Indicates which quartile value to return.

---

## API Reference

### Methods
- **QUARTILE**
  - **Parameters**:
    - `array`: The array or cell range of numeric values.
    - `quart`: Specifies which quartile value to return.
  - **Returns**: The quartile value based on the input array and quartile specified.

---

## Code Examples

```csharp
// Example to calculate the quartile of a data set
double[] data = { 10, 20, 30, 40, 50 };
int quartile = 1; // Calculate the first quartile
double result = QUARTILE(data, quartile);
// result will be the first quartile of the data set.
```

---

<!-- tags: [winforms, essential grid, financial calculations, quartile, pmt, fv, type] keywords: [annuity, loan, future value, cash balance, payments, quartile, quartile calculation, financial parameters] -->
```