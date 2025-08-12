```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_195.jpeg
document_name: calculate
page_number: 195
page_id: calculate#page_195
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:10:31Z
fidelity: lossless
-->

# Essential Calculate

## Overview

This page provides information on calculating values using specific functions, including finding the smallest value among a list of arguments, extracting minutes from a time value, and calculating the modified internal rate of return for cash flows.

## Content

### Finding the Smallest Value

Where:

- `value1, value2, ...` are values for which you want to find the smallest value.

#### Remarks
- **Arguments that contain True evaluate as 1; arguments that contain text or False evaluate as 0 (zero).**

### 4.7.102 MINUTE

Returns the minutes of a time value. The minute is given as an integer, ranging from 0 to 59.

#### Syntax
```markdown
MINUTE(serial_number)
```

Where:

- `serial_number` is the time that contains the minute you want to find. Times may be entered as text strings within quotation marks (for example, "6:00 PM"), as decimal numbers (for example, 0.75, which represents 6:00 PM), or as results of other formulas or functions (for example, `TIMEVALUE("6:00 PM")).`

#### Remarks
- Time values are a portion of a date value and are represented by a decimal number (for example, 12:00 PM is represented as 0.5).

### 4.7.103 MIRR

Returns the modified internal rate of return for a series of periodic cash flows.

#### Syntax
```markdown
MIRR(values, finance_rate, reinvest_rate)
```

Where:
- `values`: The series of cash flows.
- `finance_rate`: The interest rate you pay on the money borrowed.
- `reinvest_rate`: The interest rate you receive on the cash flows as you reinvest them.

---

## RAG Annotations
 <!-- tags: [Syncfusion Winforms, Calculate, MINUTE, MIRR, essential, function, parameters, cash flow] keywords: [calculate, MINUTE, MIRR, smallest value, time, decimal, rate of return] -->
```