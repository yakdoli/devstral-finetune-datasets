```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_323.jpeg
document_name: grid
page_number: 323
page_id: grid#page_323
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:10:12Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

| Formula            | Result |
|-------------------|--------|
| `=MROUND(10,2.6)` | 8      |
| `=MROUND(-10,-2.6)` | -8     |
| `=MROUND(10,-2)` | #NUM!  |

### 4.1.4.6.6.159 Multinomial

The MULTINOMIAL function returns the ratio of the factorial of a sum of values to the product of factorials.

### Syntax

The syntax of the MULTINOMIAL function is

```markdown
=MULTINOMIAL(number1, (number2), ...)
```

### Remarks:

- `#NUM!` - Occurs if any of the supplied arguments are less than 0.
- `#VALUE!` - Occurs if any of the supplied arguments are non-numeric.

### Example:

| Formula          | Result |
|------------------|--------|
| `=MULTINOMIAL(2, 3, 4)` | 1260 |

### 4.1.4.6.6.160 MUNIT

The MUNIT function retrieves the unit matrix for the particular dimension that has been specified.

#### Syntax:
MUNIT(dimension) where:

- Dimension is an integer specifying the dimension of the unit matrix that you want to return.

#### Remarks:

- `#VALUE!` - occurs if the dimension is a value that is equal to or smaller than zero.
```