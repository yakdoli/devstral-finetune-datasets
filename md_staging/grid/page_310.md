<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_310.jpeg
document_name: grid
page_number: 310
page_id: grid#page_310
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:08:21Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Returns the natural logarithm of a number.
- Natural logarithms are based on the constant e (2.718281828459...).

### Content

#### LN
**Syntax**
- `LN(number)`, where:
  - `number` is the positive real number for which you want the natural logarithm.

**Remarks**
- LN is the inverse of the EXP function.

---

#### LEN
**Syntax**
- `Len(text)`, where:
  - `text` is the text string whose length is to be determined.

**Description**
- LEN returns the length of a text string, including spaces.

---

#### LOG
**Syntax**
- `LOG(number, base)`, where:
  - `number` is the positive real number for which you want the logarithm.
  - `base` is the base of the logarithm. If base is omitted, it is assumed to be 10.

## API Reference
- `LN`: Returns the natural logarithm of a number.
- `LEN`: Returns the length of a text string, including spaces.
- `LOG`: Returns the logarithm of a number to the base that you specify.

## Code Examples
- **C# Example for LN:**
  ```csharp
  double result = Math.Log(10);  // Natural logarithm of 10
  ```

- **C# Example for LEN:**
  ```csharp
  string text = "Hello World";
  int length = text.Length;  // Length of the string
  ```

- **C# Example for LOG:**
  ```csharp
  double result = Math.Log(100, 10);  // Logarithm of 100 to the base 10
  ```

## Cross References
- See also: EXP, Math library functions, string manipulation in WinForms.

<!-- tags: [logarithm, exp, len, string length, windows forms, syncfusion] keywords: [natural logarithm, base logarithm, string length, text, mathematics, ln, exp, log] -->