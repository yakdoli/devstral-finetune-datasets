```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_226.jpeg
document_name: calculate
page_number: 226
page_id: calculate#page_226
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:12:18Z
fidelity: lossless
-->

# Essential Calculate

## Remarks

- The equation for the standard error of the predicted \( y \) is:

\[
\sqrt{\frac{1}{(n-2)} \left[ \sum (y - \overline{y})^2 - \frac{\left[ \sum (x - \overline{x})(y - \overline{y}) \right]^2}{\sum (x - \overline{x})^2} \right]}
\]

  where:
  - \(\overline{x}\) and \(\overline{y}\) are the sample means AVERAGE(known_x's) and AVERAGE(known_y's).
  - \( n \) is the sample size.

## 4.7.157 SUBSTITUTE

Substitutes new_text for old_text in a text string. Use SUBSTITUTE when you want to replace specific text in a text string; use REPLACE when you want to replace any text that occurs in a specific location in a text string.

### Syntax

SUBSTITUTE(text, old_text, new_text, instance_num)

where:
- **Text** is the text or the reference to a cell containing text for which you want to substitute characters.
- **Old_text** is the text you want to replace.
- **New_text** is the text you want to replace old_text with.
- **Instance_num** specifies which occurrence of old_text you want to replace with new_text. If you specify instance_num, only that instance of old_text is replaced. Otherwise, every occurrence of old_text in text is changed to new_text.

For example:

The example may be easier to understand if you copy it to a blank worksheet.

<!-- tags: [Syncfusion Winforms, SUBSTITUTE, Text Manipulation, Standard Error Calculation] keywords: [SUBSTITUTE function, text substitution, standard error, sample mean, sample size, equation, text manipulation, Excel functions] -->
```