```html
<!--  
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_122.jpeg
document_name: calculate
page_number: 122
page_id: calculate#page_122
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:06:27Z
fidelity: lossless
--> 

## Essential Calculate

### Content

#### Anything else
| Anything else | #N/A |
| --- | --- |

#### Example:
| FORMULA | RESULT |
| --- | --- |
| = ERROR.TYPE(#NULL!) | 1 |
| = ERROR.TYPE(even) | #NA |

### 4.5.6.7 SUBTOTAL

#### Overview
The SUBTOTAL function returns a subtotal in a list. Once the subtotal list is created, you can modify it by editing the SUBTOTAL function.

#### Syntax
The syntax of the SUBTOTAL function is
```
=SUBTOTAL(function_Number, ref1, (ref2),...)
```

#### Parameters
- **function_Number**: Required. Specifies which function to use in calculating subtotals within a list. Here is the list of functions supported by Syncfusion:

| FUNCTION NUMBER | FUNCTION NAME |
| --- | --- |
| 1 | AVERAGE |
| 2 | COUNT |
| 3 | COUNTA |
| 4 | MAX |
| 5 | MIN |
| 6 | PRODUCT |
| 7 | STDEV |
| 8 | STDEVP |
| 9 | SUM |
| 10 | VAR |

- **Ref1**: The first named range which is used for the subtotal. This value is required.
- **Ref2**: This value is optional.

---

<!-- tags: [product, module, control, api, version?] keywords: [calculate, subtotal, error.type, function_number, ref1, ref2, average, count, max, min, sum, subtotals] -->
```