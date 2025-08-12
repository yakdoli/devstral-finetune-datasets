```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_341.jpeg
document_name: grid
page_number: 341
page_id: grid#page_341
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:10:58Z
fidelity: lossless
-->

### Winforms Grid for Windows Forms

#### Overview
- Explains the QUOTIENT function and its behavior in WinForms applications.
- Highlights key syntax and examples for using the QUOTIENT function to calculate the integer portion of a division.

#### Content

##### Quartiles

The following table outlines the quartiles and the corresponding values returned:

| Quartile | Value Returned                  |
|----------|----------------------------------|
| 0        | Minimum value                   |
| 1        | First quartile (25th percentile) |
| 2        | Median value (50th percentile)  |
| 3        | Third quartile (75th percentile) |
| 4        | Maximum value                   |

##### 4.1.4.6.6.195 QUOTIENT

The QUOTIENT function returns the integer portion of a division between two given numbers. The returned value will be an integer value.

**Syntax**

The syntax of the QUOTIENT function is:

- =QUOTIENT (numerator, denominator)
- **Numerator** – Required.
- **Denominator** – Required.

**Remarks:**

- **#VALUE!** - Occurs if any of the given arguments are non-numeric.

**Example:**

| FORMULA          | RESULT |
|------------------|--------|
| = QUOTIENT (10,3) | 3      |

#### Code Examples (XML)

```xml
<!-- Example usage of the QUOTIENT function in a WinForms application -->
<ExampleOfQUOTIENTFunction>
    <QUOTIENTFunction>
        <Formula>=QUOTIENT(10,3)</Formula>
        <Result>3</Result>
    </QUOTIENTFunction>
</ExampleOfQUOTIENTFunction>
```

#### RAG Annotations
<!-- tags: [product, module, control, api, version?] keywords: [k1, k2, ...] -->
```