```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_187.jpeg
document_name: calculate
page_number: 187
page_id: calculate#page_187
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:10:04Z
fidelity: lossless
-->

## Essential Calculate

### LEFT(text, num_chars)

#### Parameters
- **text**: The text string that contains the characters you want to extract.
- **num_chars**: Specifies the number of characters which you want `LEFT` to extract.

#### Remarks
- `num_chars` must be greater than or equal to zero.
- If `num_chars` is greater than the length of `text`, `LEFT` returns all the text.
- If `num_chars` is omitted, it is assumed to be 1.

---

### 4.7.87 LN

#### Function
Returns the natural logarithm of a number. Natural logarithms are based on the constant \( e \) (2.718281828459...).

#### Syntax
```plaintext
LN(number)
```

#### Parameters
- **number**: The positive real number for which you want the natural logarithm.

#### Remarks
- `LN` is the inverse of the `EXP` function.

---

### 4.7.88 LEN

#### Function
`LEN` returns the length of a text string, including spaces.

#### Syntax
```plaintext
LEN(text)
```

---

## API Reference

### Namespace: System.String

#### Methods
- **LEFT(text, num_chars)**: Extracts the specified number of characters from the start of a text string.
- **LN(number)**: Computes the natural logarithm of a given number.
- **LEN(text)**: Returns the length of a text string.

---

## Cross References

See also:
- Previous section: [Other String Functions](#other-string-functions)
- Related documentation: [Mathematical Functions](#mathematical-functions)

---

## RAG Annotations
<!-- tags: [winforms, string-functions, mathematical-functions, synchronization-guide] keywords: [LEFT, LN, LEN, natural logarithm, character extraction, text length, API reference, Syncfusion] -->
```