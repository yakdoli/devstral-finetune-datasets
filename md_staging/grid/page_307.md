```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_307.jpeg
document_name: grid
page_number: 307
page_id: grid#page_307
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:09:03Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Describes various functions like IsText, IsNonText, and KURT in the Essential Grid for Windows Forms.
- Provides syntax and usage examples for each function.

## Content

### Example

| FORMULA                        | RESULT  |
|-------------------------------|---------|
| =ISREF("Region1")             | FALSE   |
| =ISREF(=ISLOGICAL(TRUE))     | TRUE    |

#### 4.1.4.6.6.125 IsText

The IsText function returns a boolean value after determining that the provided value is a string.

**Syntax:**

```plaintext
IsText(text)
```

**Where:**

- `text` is the value you want to check whether it is a string or not.

#### 4.1.4.6.6.126 IsNonText

The IsNonText function returns the boolean value after determining that the provided value is not a string.

**Syntax:**

```plaintext
IsNonText(text)
```

**Where:**

- `text` is the value you want to check whether it is a string or not.

#### 4.1.4.6.6.127 KURT

Returns the kurtosis of a data set. Kurtosis characterizes the relative peakedness or flatness of a distribution compared with the normal distribution. Positive kurtosis indicates a relatively peaked distribution. Negative kurtosis indicates a relatively flat distribution.

**Syntax:**

```plaintext
KURT(number1, number2, ...), where:
```

- `number1, number2, ...` are arguments for which you want to calculate kurtosis. You can also use a single array or a reference to an array instead of arguments separated by commas.

## Code Examples (multi-language supported)
- Inline code in text should be wrapped with backticks.
  
<details>
  <summary>View additional formatting options</summary>
  
- Code blocks with language identifiers: ```csharp, ```vb, ```xml, ```xaml, ```js, ```css, ```ts, ```python.

</details>

### Cross References
- Refer to the API Reference for more details on function parameters and return types.

<!-- tags: [Essential Grid, Windows Forms, IsText, IsNonText, KURT] keywords: [kurtosis, boolean, string, distribution, peakedness, flatness] -->
```