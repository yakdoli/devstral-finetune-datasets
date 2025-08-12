```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_213.jpeg
document_name: calculate
page_number: 213
page_id: calculate#page_213
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:11:38Z
fidelity: lossless
-->

# Essential Calculate

### RADIANS(angle)

where:
- `angle` is an angle in degrees that you want to convert.

### 4.7.134 RAND

Returns an evenly distributed random number greater than or equal to 0 and less than 1.

#### Syntax
```plaintext
RAND( )
```

### 4.7.135 RANK

Returns the rank of a number in a list of numbers. The rank of a number is its size relative to other values in a list. (If you were to sort the list, the rank of the number would be its position.)

#### Syntax
```plaintext
RANK(number, ref, order)
```

#### Parameters
- `number` is the number whose rank you want to find.
- `ref` is an array of or a reference to a list of numbers.
- `order` is a number specifying how to rank numbers.
  - If the order is 0 (zero) or omitted, the number is ranked as if `ref` were a list sorted in descending order.
  - If the order is any nonzero value, the number is ranked as if `ref` were a list sorted in ascending order.

#### Remark
- `RANK` gives duplicate numbers of the same rank. However, the presence of duplicate numbers will affect the ranks of subsequent numbers.
```