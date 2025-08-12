<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_317.jpeg
document_name: grid
page_number: 317
page_id: grid#page_317
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:09:37Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Remarks

- You can specify arguments that are numbers, empty cells, logical values or text representations of numbers. Arguments that are error values cause errors. If the calculation does not include text or logical values, use the MAX worksheet function instead.
- If an argument is an array or reference, only values in that array or reference are used. Empty cells and text values in the array or reference are ignored.
- Arguments that contain True evaluate as 1; arguments that contain text or False evaluate as 0 (zero).
- If the arguments contain no values, MAXA returns 0 (zero).

### 4.1.4.6.6.146 MDETERM

The MDETERM function retrieves the matrix determinant of an array.

#### Syntax:

**MDETERM(array)** where:
- array is a numeric array with an equal number of rows and columns.

#### Remarks:

- #VALUE! - occurs if any cell in the array is empty or has text in it.
- #VALUE! - occurs if the array does not have an equal number of rows and columns.

### 4.1.4.6.6.147 MEDIAN

Returns the median of the given numbers. The median is the number in the middle of a set of numbers; that is, half the numbers have values that are greater than the median and half have values that are less.

#### Syntax

**MEDIAN(number1, number2, ...),** where:

- **number1, number2, ...** are numbers for which you want the median.

#### Remarks

- If there is an even number of numbers in the set, then MEDIAN calculates the average of the two numbers in the middle.

<!-- tags: [grid, windows forms, function, syntax, remarks] keywords: [MDETERM, MEDIAN, matrix determinant, median, arguments, array, logical values, text representations, error values, even number, average] -->