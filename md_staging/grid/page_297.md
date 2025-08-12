```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_297.jpeg
document_name: grid
page_number: 297
page_id: grid#page_297
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:08:30Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

The following is the formula to calculate Growth for an array of cells in a column:

## Syntax

```plaintext
=GROWTH(known_y's, [known_x's], [new_x's],
```

- **Known_y's**: A set of y-values you already know in a relationship, where y = b*m^x.
- **Known_x's**: An optional set of x-values that you may already know in the relationship, where y = b*m^x.
- **New_x's**: New x-values for which you want GROWTH to return corresponding y-values.

## Code

```plaintext
=Growth(B2:B7,A2:A7,C6:C7)
```

## 4.1.4.6.6.104 HARMEAN

### Overview
This section describes the `HARMEAN` function, which returns the harmonic mean of a data set. The harmonic mean is the reciprocal of the arithmetic mean of reciprocals.

### Syntax

```plaintext
HARMEAN(number1, number2, ...), where:
```

- **number1, number2, ...**: are arguments for which you want to calculate the mean.

### Remarks
- The arguments must be either numbers or names, arrays, or references that contain numbers.
- All data values must be positive.
- The equation for the harmonic mean is,

<!-- tags: [essential-grid, windows-forms, growth-function, harmonic-mean, harmean] keywords: [growth formula, harmonic mean, essential grid, windows forms] -->
```