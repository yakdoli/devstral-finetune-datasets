```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_128.jpeg
document_name: calculate
page_number: 128
page_id: calculate#page_128
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:07:50Z
fidelity: lossless
-->

# Essential Calculate

If the value_error is an empty cell, then the function takes the error value as an empty string.

## 4.5.6.17 T

The T function tests whether the given value is text or not. If the given value is text, then it returns the given text. Otherwise, the function returns an empty text string.

### Syntax

The syntax of the T function is

```
=T( value )
```

- **value** – Required. This is a value to be checked.

If the value is not a number or logical value, then the function returns an empty string.

### Example

| FORMULA       | RESULT       |
|---------------|--------------|
| `=T("SYNCFUSION")` | SYNCFUSION |
| `=T(TRUE)`     |              |
| `=T(10)`       |              |

## 4.5.6.18 XOR

The XOR function returns the exclusive OR for the given arguments.

### Syntax

```
XOR (logical_value1, logical_value2, ...)
```

## Page-level Navigation/TOC (if applicable)

- **4.5.6.17 T**
- **4.5.6.18 XOR**

## Cross References

See also: [IFERROR] 

## RAG Annotations

<!-- tags: [Syncfusion, WinForms, Calculate, T function, XOR function, Error handling, Text validation, Logical operations] keywords: [IFERROR, T, XOR, error_value, logical_value, exclusive OR, text checking] -->
```