```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_183.jpeg
document_name: calculate
page_number: 183
page_id: calculate#page_183
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:09:52Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Functions to check for specific types of values such as errors, logical values, and missing values.
- Returns `TRUE` or `FALSE` based on the evaluation of the input value against specific conditions.

## Content

### 4.7.77 ISERROR

Returns `True` if the value is a string that starts with a `#`.

#### Syntax
```plaintext
ISERROR(value)
```
where:
- `value` is the value that is to be tested.

---

### 4.7.78 IsLogical

The `IsLogical` function checks whether a value is a logical value and returns a `TRUE` or `FALSE`.

#### Syntax:
```plaintext
IsLogical( value )
```
where,
- This value is the value that you want to test. If the value is a `TRUE` or `FALSE` value, this function will return `TRUE`. Otherwise, it will return `FALSE`.

---

### 4.7.79 IsNA

The `IsNA` function returns a boolean value after determining that the provided value is a `#NA` error value.

#### Syntax:
```plaintext
IsNA(value)
```
where,
- `value` the function will test.

## Page-level Navigation/TOC (if applicable)
- None in this section

## Cross References
- See also: `ISERROR`, `IsLogical`, `IsNA`

## RAG Annotations
<!-- tags: [product, module, control, api, version?] keywords: [ISERROR, IsLogical, IsNA, boolean, logical values, error values, missing values, Syncfusion Winforms] -->
```