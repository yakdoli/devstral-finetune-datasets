```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_179.jpeg
document_name: calculate
page_number: 179
page_id: calculate#page_179
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:09:42Z
fidelity: lossless
-->

## Essential Calculate

### 4.7.68 IF

Returns one value if a condition you specify evaluates to True and another value if it evaluates to False.

Use IF to conduct conditional tests on values and formulas.

#### Syntax

```markdown
IF(logical_test, value_if_true, value_if_false)
```

#### where:

- `logical_test` is any value or expression that can be evaluated to True or False.
- `value_if_true` is the value that is returned if a logical_test is True.
- `value_if_false` is the value that is returned if a logical_test is False.

#### Remarks

- Countif and Sumif are additional methods that provide conditional calculations.

### 4.7.69 Index

The Index function returns the exact value from the provided row index and column index from a specific range.

#### Syntax:

```markdown
Index(range,row,col)
```

#### where,

- `range` is a string to mention the specific range.
- `row` is the integer that indicates the specific row index.
- `col` is the integer that indicates the specific column index.

### 4.7.70 Indirect

The Indirect function returns the reference as a string instead of providing the content or range within it.

<!-- tags: [IF, Index, Indirect, conditional calculations] keywords: [logical_test, value_if_true, value_if_false, Countif, Sumif, row index, column index, reference] -->
```