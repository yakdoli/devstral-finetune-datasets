```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_322.jpeg
document_name: grid
page_number: 322
page_id: grid#page_322
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:08:56Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Functions to extract the month from a serial number and round numbers to the nearest multiple.
- Explanation of serial numbers for dates and their usage in calculations.

## Content

### 4.1.4.6.6.157 MONTH

#### Functionality
Returns the month of a date represented by a serial number. The month is given as an integer, ranging from 1 (January) to 12 (December).

#### Syntax
MONTH(serial_number), where:

- `serial_number` is the date of the month you are trying to find. Dates should be entered by using the DATE function or as results of other formulas or functions. For example, use `DATE(2002,11,12)` for the 12th day of Nov, 2002.

#### Remarks
- Dates are stored as sequential serial numbers so that they can be used in calculations. By default, January 1, 1900 is serial number 1 and January 1, 2008 is serial number 39448 because it is 39,448 days after January 1, 1900.

### 4.1.4.6.6.158 MROUND

#### Functionality
The MROUND function rounds a given number up or down to the nearest multiple of a given number.

#### Syntax
The syntax of the MROUND function is:
```
= MROUND(number, multiple)
```
- **Number** – The value to be rounded. This value is required.
- **Multiple** – This value is required.

#### Remarks:
- The number must be is greater than or equal to half the value of multiple.
- **\#NUM!** – Occurs if the number and multiple have different signs.
- **\#VALUE!** – Occurs if any of the given arguments are non-numeric.

#### Example:
| **FORMULA** | **RESULT** |
|-------------|------------|

## API Reference (if applicable)

- Namespace: `Essential.Grid`
- Class: `Winforms`
- Members:
  - `MONTH(serial_number)`
    - **Returns**: Integer (1-12)
    - **Parameters**:
      - `serial_number`: Date serial number (required)
  - `MROUND(number, multiple)`
    - **Returns**: Rounded number
    - **Parameters**:
      - `number`: Value to be rounded (required)
      - `multiple`: Multiple to round to (required)

### Code Examples (multi-language supported)

```csharp
// Example of using MONTH function
int serialNumber = 37867; // Example serial number
int month = MONTH(serialNumber);

// Example of using MROUND function
double number = 123.45;
double multiple = 10;
double roundedNumber = MROUND(number, multiple);
```

## RAG Annotations
- HTML comment with tags and keywords derived from the visible content:
<!-- tags: [syncfusion, winforms, grid, month, mround, date serial number, rounding, api] keywords: [month, multiple, serial_number, date_function, formula, result, grid, functionality, syntax, remarks, types] -->

<!-- anchor: grid#page_322#overview -->

<!-- anchor: grid#page_322#content -->

<!-- anchor: grid#page_322#syntax -->

<!-- anchor: grid#page_322#api-reference -->

<!-- anchor: grid#page_322#code-examples -->

<!-- anchor: grid#page_322#tags-and-keywords -->
```