```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_214.jpeg
document_name: calculate
page_number: 214
page_id: calculate#page_214
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:11:45Z
fidelity: lossless
-->

## Essential Calculate

### 4.7.136 RATE

Returns the interest rate per period of an annuity. RATE is calculated by iteration and may not converge to a unique solution.

#### Syntax

```plaintext
RATE(nper, pmt, pv, fv, type, guess)
```

#### where:

- **nper** is the total number of payment periods in an annuity.
- **pmt** is the payment made for each period and cannot change over the life of the annuity. Typically, pmt includes the principal and interest but, no other fees or taxes. If pmt is omitted, you must include the fv argument.
- **pv** is the present value— the total amount that a series of future payments is worth now.
- **fv** is the future value or a cash balance that you want to attain after the last payment is made. If fv is omitted, it is assumed to be 0 (the future value of a loan, for example, is 0).
- **type** is the number 0 or 1 and indicates when payments are due. If type equals:
  - 0 - Payments are due at the end of the period.
  - 1 - Payments are due at the beginning of the period.
- **guess** is your guess for what the rate will be. If you omit guess, it is assumed to be 10 percent. If RATE does not converge, try different values for guess. RATE usually converges if guess is between 0 and 1.

### 4.7.137 RIGHT

RIGHT returns the last character or characters in a text string, based on the number of characters you specify.

#### Syntax

```plaintext
RIGHT(text, num_chars)
```

#### where:

- **text** is the text string containing the characters you want to extract.
- **num_chars** specifies the number of characters you want RIGHT to extract.

```html
<!-- tags: [rate, annuity, interest, right, text manipulation, financial function, iteration, present value, future value, payment, syncfusion winforms] keywords: [rate, financial functions, right function, string extraction, financial calculations, iteration, pv, fv, pmt, type, guess, text processing] -->
```