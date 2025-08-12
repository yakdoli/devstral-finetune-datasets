```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_302.jpeg
document_name: grid
page_number: 302
page_id: grid#page_302
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:07:50Z
fidelity: lossless
-->

<a name="top"></a>
## Overview
- Describes the use of `range`, `row`, and `col` to specify specific ranges, rows, and columns.
- Explains the `Indirect` function that returns a reference as a string.
- Details the `INT` function for rounding down to the nearest integer.
- Provides information on the `INTRATE` function for calculating the interest rate for a fully invested security.

### WinForms-specific conventions
- Emphasizes the importance of specifying range, row, and column indices for precise grid operations.
- Highlights the use of `Indirect`, `INT`, and `INTRATE` functions in context of grid operations.

## Function Reference

### `Indirect`

#### Description
The `Indirect` function returns the reference as a string instead of providing the content or range within the cell.

#### Syntax
```plaintext
Indirect(content)
```

#### Parameters
- **content**: The string that provides the textual representation of the cell reference.

---

### `INT`

#### Description
The `INT` function rounds a number down to the nearest integer.

#### Syntax
```plaintext
INT(number)
```

#### Parameters
- **number**: The real number that you want to round down to an integer.

---

### `INTRATE`

#### Description
The `INTRATE` function returns the interest rate for a fully invested security.

#### Syntax
```plaintext
INTRATE(settlement, maturity, investment, redemption, basis)
```

#### Parameters
- **settlement**: The security's settlement date.
- **maturity**: The security's maturity date.
- **investment**: The amount invested in the security.
- **redemption**: The amount to be received at maturity.
- **basis**: The kind of day count basis to use.

#### Remarks
- Additional remarks can be included based on specific use cases or conditions.

---

## Code Examples

The following code examples demonstrate how to use the `Indirect`, `INT`, and `INTRATE` functions:

### Using `Indirect`
```csharp
// Example usage of Indirect
string reference = "A1";
string result = Indirect(reference);
```

### Using `INT`
```csharp
// Example usage of INT
double number = 3.7;
int roundedDown = INT(number);
```

### Using `INTRATE`
```csharp
// Example usage of INTRATE
DateTime settlement = new DateTime(2025, 1, 1);
DateTime maturity = new DateTime(2030, 1, 1);
double investment = 1000.0;
double redemption = 1200.0;
int basis = 0;

double interestRate = INTRATE(settlement, maturity, investment, redemption, basis);
```

---

## Cross References
- See also: Documentation on grid operations, date handling, and financial functions in the Syncfusion Winforms library.

<!-- tags: [syncfusion, winforms, grid, functions, interest rate, int, indirect] keywords: [range, row, col, settlement, maturity, investment, redemption, basis, text representation, nearest integer, fully invested security] -->
```