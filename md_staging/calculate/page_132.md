```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_132.jpeg
document_name: calculate
page_number: 132
page_id: calculate#page_132
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:08:01Z
fidelity: lossless
-->

# Essential Calculate

## Input Table

|     | A       | B     | C       |
|-----|---------|-------|---------|
| 1   | Earning | Tax   | other   |
| 2   | 100000  | 3000  | 100     |
| 3   | 200000  | 6000  | 200     |
| 4   | 300000  | 7500  | 300     |
| 5   | 400000  | 9000  | 500     |

### Formula Result

| FORMULA                                                                | RESULT |
|------------------------------------------------------------------------|--------|
| `AVERAGEIFS(C2:C5, B2:B5, ">7000", B2:B5, "<10000")`                | 400    |

## NETWORKDAYS

### Overview
- **Networkdays Function**: Calculates the number of whole work days between two given dates.
- **Key Features**:
  - Includes all weekdays from Monday to Friday.
  - Excludes a supplied list of holidays.

### Syntax

```plaintext
= NETWORKDAYS(start_date, end_date, [holidays])
```

#### Parameters
- **start_date**: The start of the period to find the working days.
- **end_date**: The end of the period to find the working days.
- **[holidays]**: An optional argument, specifying an array of dates that are not to be counted as working days.

### Notes
- If any argument is not a valid date, `NETWORKDAYS` returns the `#VALUE!` error value.

### Example

| FORMULA                                                  | RESULT |
|----------------------------------------------------------|--------|
| `=NETWORKDAYS(DATE(2012,10,1), DATE(2013,3,1))`       | 110    |
```