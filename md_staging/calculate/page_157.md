```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_157.jpeg
document_name: calculate
page_number: 157
page_id: calculate#page_157
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:08:31Z
fidelity: lossless
-->

# Essential Calculate

Counts the number of items in a list that contains numbers.

## Syntax

```plaintext
COUNT(value1, value2,...)
```

where:

`value1, value2, ...` are arguments that can contain or refer to a variety of different types of data, but only numbers are counted.

## Remarks

- Arguments that are numbers, dates or text representations of numbers are counted; arguments that are error values or text that cannot be translated into numbers are ignored.
- If an argument is an array or reference, only numbers in that array or reference are counted. Empty cells, logical values, text or error values in the array or reference are ignored.

### 4.7.29 COUNTA

Counts the number of cells that are not empty.

## Syntax

```plaintext
COUNTA(value1, value2,...)
```

where:

`value1, value2, ...` are arguments representing the values you want to count. In this case, a value is any type of information, excluding empty cells.

### 4.7.30 COUNTBLANK

Counts empty cells in a specified range of cells.

## Syntax

<!-- tags: [essential calculate, count, counta, countblank, arguments, array, reference, empty cells, data types, numbers, text, error values, logical values, count function] keywords: [count, counta, countblank, numbers, data types, text, error values, logical values, empty cells, array, reference, arguments] -->
```