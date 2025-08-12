```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_252.jpeg
document_name: grid
page_number: 252
page_id: grid#page_252
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:05:41Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Remarks

- **#VALUE!** - occurs if the number is a non-numeric value.
- The returned angle is given in radians in the range of 0 (zero) to pi.

### 4.1.4.6.6.6 ACOTH

#### Description:
The ACOTH function retrieves the inverse hyperbolic cotangent of a value.

#### Syntax:
ACOTH(number) where:
- **number** is the cotangent of the angle you need.

#### Remarks:
- **#NUM!** - occurs if number is less than one.
- **#VALUE!** - occurs if the absolute value of number is less than one.

#### Mathematical Equation:
\[ \text{coth}(N) = \frac{1}{2} \ln\left(\frac{N+1}{N-1}\right) \]

### 4.1.4.6.6.7 AcscH

#### Description:
The AcscH function computes the inverse hyperbolic cosecant of its argument.

#### Syntax:
\[ x = \text{acsch}(y) \] where:
- **x** is a complex or real array
- **y** is a complex or real array

### 4.1.4.6.6.8 ADDRESS

#### Description:
The ADDRESS function returns the address of a cell in a worksheet given specified row and column numbers.

#### Syntax:
ADDRESS(row_num, column_num, [abs_num], [a1], [sheet_text])

- **row_num**: A numeric value that specifies the row number.
- **column_num**: A numeric value that specifies the column number.
- **abs_num**: Optional. A numeric value that specifies the type of reference to return.
- **A1**: A logical value that specifies the A1 or R1C1 reference style.

<!-- tags: [Windows Forms, ACOTH, AcscH, ADDRESS, Essential Grid, Hyperbolic Functions, Mathematical Functions, Cell Address, Row Column Numbers] -->
```