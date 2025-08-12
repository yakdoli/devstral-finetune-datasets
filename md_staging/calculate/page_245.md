```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_245.jpeg
document_name: calculate
page_number: 245
page_id: calculate#page_245
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:13:14Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Explains the use of logical expressions in calculations.
- Discusses how to handle and process calculations in the `CalcEngine` class.
- Provides an example of using logical conditions in calculations.

## Content

### 5.1.4 How To Use Logical Expressions In Other Calculated Expressions?

Logical expressions return a `True` or `False` value. If you use a logical expression as part of a calculation, then:

- A `True` is replaced with `1`.
- A `False` is replaced with `0` as the whole expression is evaluated.

This allows you to easily write and compute formulas that involve logical conditions.

Consider the following expression:

```
([Cost] < 100) * 1 + ([Cost] >= 100) * ([Cost] < 200) * 3 + ([Cost] >= 200) * ([Cost] < 300) * 5 + ([Cost > 300) * 7
```

Depending upon the value of `cost`, this expression returns `1, 3, 5` or `7`. This is an example of using a linear combination of logical expressions that times other values.

**Note:** The logical conditions are mutually exclusive, but, when taken as a whole, cover all possible values of `cost`. It has the effect of assigning a unique value depending upon the input value.

#### 5.2 CalcEngine

`CalcEngine` is the class that encapsulates all the calculation support in Essential Calculate. It has methods that parse and compute expressions and also contains many functions defining the calculations found in the Function Library that ships with Essential Calculate.

##### 5.2.1 How To Force Calculations To Be Processed After They Have Been Suspended?

No additional information provided in the image.

## API Reference (if applicable)
- No specific API reference is mentioned in the provided section.

## Code Examples (multi-language supported)
- No code examples are provided in the image.

## RAG Annotations
<!-- tags: [Syncfusion Winforms, Essential Calculate, CalcEngine, logical expressions, calculations] -->
```