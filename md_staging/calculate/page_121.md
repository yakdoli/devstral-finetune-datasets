```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_121.jpeg
document_name: calculate
page_number: 121
page_id: calculate#page_121
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:06:16Z
fidelity: lossless
-->

## Essential Calculate

### NA Function

#### Syntax:

The syntax of the NA function is:

```plaintext
=NA()
```

The NA function syntax has no arguments.

**Note:** The function doesn't have any arguments.

#### Example:

| FORMULA   | RESULT |
|-----------|--------|
| =NA()     | #NA    |

### 4.5.6.6 ERROR.TYPE

The Error.Type function returns an integer for the given error value that denotes the type of the given error.

#### Syntax:

The syntax of the ERROR.TYPE function is:

```plaintext
= ERROR.TYPE(value)
```

The given value is required.

#### Return Value of Function:

Here is the return value of the function:

| Given Value         | Return value of function |
|---------------------|--------------------------|
| #NULL!             | 1                        |
| #DIV/0!            | 2                        |
| #VALUE!            | 3                        |
| #REF!              | 4                        |
| #NAME?             | 5                        |
| #NUM!              | 6                        |
| #N/A               | 7                        |
| #GETTING_DATA      | 8                        |

<!-- tags: [syncfusion, error handling, na function, error.type function, winforms, calculate function, version: 11.4.0.26] keywords: [na, error types, error handling, winforms, essential calculate, function syntax, return values, div/0, value, ref, name, num, n/a, getting_data] -->
```