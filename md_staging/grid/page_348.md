```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_348.jpeg
document_name: grid
page_number: 348
page_id: grid#page_348
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:11:42Z
fidelity: lossless
-->

### Essential Grid for Windows Forms

The correlation coefficient \( r \) is defined as:

\[
r = \frac{\sum(x - \bar{x})(y - \bar{y})}{\sqrt{\sum(x - \bar{x})^2 \sum(y - \bar{y})^2}}
\]

where:

- \( x\)-bar and \( y\)-bar are the sample means \( \text{AVERAGE(known_x's)} \) and \( \text{AVERAGE(known_y's)} \).
- \( \text{RSQ} \) returns \( r^2 \), which is the square of this correlation coefficient.

### 4.1.4.6.6.208 SEARCH

The SEARCH function returns the location of a substring in a string. This function is **NOT** case-sensitive.

#### Syntax

SEARCH(substring, string, [start_position])

- **substring**: Required. The text to be found.
- **string**: Required. The text in which to search for the value of the substring.
- **start_position**: Optional. The starting position for searching in the string.

#### Notes

- If the value of `find_text` is not found, the `#VALUE!` error value is returned.
- If the `start_position` argument is omitted, it is assumed to be 1.
- If `start_position` is not greater than 0, or is greater than the length of the string argument, the `#VALUE!` error value is returned.

#### Example

| **FORMULA**                         | **RESULT** |
|-------------------------------------|------------|
| `=SEARCH("base", "database")`       | 5          |

---

### 4.1.4.6.6.209 SEC

The SEC function returns the secant of an angle.

#### Syntax

SEC(number) where:

- **number**: angle in radians for which you want the secant.

#### Remarks

This function calculates the secant of an angle, which is the reciprocal of the cosine of the angle.

---

<!-- tags: [product, syncfusion sdk, winforms, grid, essential grid, 11.4.0.26] keywords: [search function, secant, correlation coefficient, substring search, angle radian, rsq, essential grid, windows forms] -->
```