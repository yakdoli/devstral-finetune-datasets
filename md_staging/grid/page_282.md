```markdown
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_282.jpeg
document_name: grid
page_number: 282
page_id: grid#page_282
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:06:19Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Description of functions: DOLLARDE, DOLLARFR, and DSTDEV.
- Overview of converting dollar prices between fractions and decimals, and estimating standard deviation based on samples.

## Content

### 4.1.4.6.6.73 DollarDe
A dollar price expressed as a fraction will be converted into a dollar price expressed as a decimal number.

**Syntax:**
DOLLARDE(object arg1, object arg2) where:
- **Arg1** is a number expressed as a fraction.
- **Arg2** is an integer to use in the denominator of the fraction.

**Remarks:**
- **#NUM!** - Occurs if the fraction is less than 0.
- **#DIV/0!** - Occurs if the fraction is equal to 0.

### 4.1.4.6.6.74 DollarFr
A dollar price expressed as a decimal number will be converted into a dollar price expressed as a fraction.

**Syntax:**
DOLLARFR (object arg1, object arg2) where:
- **arg1** is a decimal number.
- **arg2** is an integer to use in the denominator of a fraction.

**Remarks:**
- **#NUM!** - Occurs if the fraction is less than 0.
- **#DIV/0!** - Occurs if the fraction is 0.

### 4.1.4.6.6.75 DSTDEV
The DSTDEV function estimates the standard deviation of a population based on a sample by using the numbers in a column of a list or database that matches the conditions that have been specified.

**Syntax:**
DSTDEV(database, field, criteria) where:
- **database** is the range of cells that makes up the list or database.
- **field** indicates which column is used in the function.
- **criteria** is the range of cells that contains the conditions that you specify.

## API Reference (if applicable)
- **Namespace:** Excel-like functions related to financial and statistical analysis.
- **Class:** Not applicable in this context as these are Excel-like functions.
- **Members:**
  - **DOLLARDE(object arg1, object arg2)**
    - Parameters:
      - `arg1`: A number expressed as a fraction.
      - `arg2`: An integer used in the denominator of the fraction.
  - **DOLLARFR(object arg1, object arg2)**
    - Parameters:
      - `arg1`: A decimal number.
      - `arg2`: An integer used in the denominator of a fraction.
  - **DSTDEV(database, field, criteria)**
    - Parameters:
      - `database`: The range of cells making up the list or database.
      - `field`: Indicates which column is used in the function.
      - `criteria`: The range of cells that contains the conditions to specify.

## Code Examples (if applicable)
Not directly applicable, as these functions can be directly used in Excel-like installations.

<!-- tags: [DollarDe, DollarFr, DSTDEV, dollar-price, standard-deviation, fraction-to-decimal, decimal-to-fraction, population-estimation] keywords: [DOLLARDE, DOLLARFR, DSTDEV, dollar fraction, decimal, standard deviation, function usage, conditions] -->
```