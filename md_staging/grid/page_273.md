```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_273.jpeg
document_name: grid
page_number: 273
page_id: grid#page_273
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:06:49Z
fidelity: lossless
-->

## Overview

- Describes functions related to trigonometric calculations (`CSC`, `CSCH`) and financial calculations (`DURATION`).
- Lists requirements and syntax for these functions.
- Explains remarks and error cases for the functions.

## Content

### 4.1.4.6.6.51 CSC

#### Overview
- The `CSC` function returns the cosecant of an angle specified in radians.

#### Syntax
- `CSC(number)` where:
  - `number` – the angle in radians for which you want the cosecant.

#### Remarks
- `#NUM!` – occurs if the number is outside of its constraints.
- `#VALUE!` – occurs if the number is a non-numeric value.

### 4.1.4.6.6.52 CSCH

#### Overview
- The `CSCH` function returns the hyperbolic cosecant of an angle specified in radians.

#### Syntax
- `CSCH(number)` where:
  - `number` – the angle in radians for which you want the cosecant.

#### Remarks
- `#NUM!` – occurs if the number is outside of its constraints.
- `#VALUE!` – occurs if the number is a non-numeric value.

### 4.1.4.6.6.53 CUMIPMT

#### Overview
- Returns the Macaulay duration for an assumed par value of \$100. Duration is defined as the weighted average of the present value of the cash flows and is used as a measure of a bond price's response to changes in yield.

#### Syntax
- `DURATION(settlement, maturity, coupon, yld, frequency, basis)` where:
  - `Settlement` – security's settlement date.
  - `Maturity` – security's maturity date.
  - `Coupon` – annual coupon rate.
  - `Yld` – security's annual yield.
  - `Frequency` – number of coupon payments per year.

## RAG Annotations

<!-- tags: [Syncfusion Winforms, CSC, CSCH, DURATION, financial functions, trigonometric functions, version 11.4.0.26] keywords: [trigonometry, cosecant, hyperbolic cosecant, Macaulay duration, yield, settlement, maturity, coupon rate] -->
```