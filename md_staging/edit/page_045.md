```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_045.jpeg
document_name: edit
page_number: 045
page_id: edit#page_045
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:56:53Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- Regex patterns separated by the | (vertical bar) character.
- Example: cat|dog|tiger.
- The leftmost successful match wins.

## Content

### See Also
- **Lexical Macros**

---

#### 4.2.5.2 Lexical Macros

Edit Control allows you to define macros that represent regular expression elements. These macros are valid for use in any regular expression.

---

##### Usage

Using defined macros is easy. To reference a macro, simply type its name within curly braces ({}). The following examples illustrate this feature better:

- **This regular expression uses a macro that represents the character class [0-9] to build a decimal number regular expression.**
  ```
  {DigitMacro}+(\.{DigitMacro})+
  ```

- **This regular expression builds a C# identifier using two macros.**
  ```
  (_|\{AlphaMacro\})(\{WordMacro\})
  ```

##### Built-In Macros

Edit Control recognizes a number of built-in macros. If a language definition defines a lexical macro of the same name as a built-in lexical macro, the user's definition will override the system definition. The following table summarizes the built-in macros of Edit Control.

| Macro      | Description                                                                                       |
|------------|---------------------------------------------------------------------------------------------------|
| AllMacro   | Contains all Unicode characters. This is the same as [\u0000-\uFFFF]                         |
| AlphaMacro | Contains all Unicode alphanumeric digits. This is the same as: [a-zA-Z]                      |

---

## Cross References
- **See Also:**
  - Lexical Macros

<!-- tags: [windows forms, edit control, regular expressions, macros, built-in macros, lexical macros] keywords: [regex, macros, windows forms, edit control, allmacro, alphamacro] -->
```