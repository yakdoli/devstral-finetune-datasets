```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_839.jpeg
document_name: tools
page_number: 839
page_id: tools#page_839
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:38:56Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Explains the usage of various placeholder and literal symbols in mask strings for Windows Forms applications.
- Describes the behavior and purpose of different mask characters, such as decimal placeholders, thousands separators, time separators, and alphanumeric placeholders.
- Highlights how certain mask characters can be used to perform case conversion or ensure compatibility with other systems like Microsoft Access.

## Content

The following table outlines the essential placeholder and literal symbols used in mask strings for Windows Forms:

| Symbol | Description |
| --- | --- |
| `.` | Decimal placeholder. The actual character used is the one specified as the decimal placeholder in your international settings. This character is treated as a literal for masking purposes. |
| `,` | Thousands separator. The actual character used is the one specified as the thousands separator in your international settings. This character is treated as a literal for masking purposes. |
| `:` | Time separator. The actual character used is the one specified as the time separator in your international settings. This character is treated as a literal for masking purposes. |
| `/` | Date separator. The actual character used is the one specified as the date separator in your international settings. This character is treated as a literal for masking purposes. |
| `\` | Treat the next character in the mask string as a literal. This allows you to include the `"#"`, `"&"`, `"A"`, and `"?`" characters in the mask. This character is treated as a literal for masking purposes. |
| `;` | Character placeholder. Valid values for this placeholder are ANSI characters in the following ranges: 32-126 and 128-255. |
| `>` | Convert all the characters that follow to uppercase. |
| `<` | Convert all the characters that follow to lowercase. |
| `A` | Alphanumeric character placeholder (entry required). For example: a - z, A - Z, or 0 - 9. |
| `a` | Alphanumeric character placeholder (entry optional). |
| `9` | Digit placeholder (entry optional). For example: 0 - 9. |
| `C` | Character or space placeholder (entry optional). This operates exactly like the `"&"` placeholder and ensures compatibility with Microsoft Access. |
| `?` | Letter placeholder. For example: a - z or A - Z. |
| Literal | All other symbols are displayed as literals; that is, as themselves. |

## Code Examples

[C#]

This section is intended for code examples related to the use of mask strings in Windows Forms applications.

## Page-level Navigation/TOC (if applicable)
- No local Table of Contents present.

## Cross References
- None.

## RAG Annotations
<!-- tags: [product, module, control, api, version?] keywords: [Windows Forms, mask strings, placeholders, literals, international settings, alphanumeric, case conversion, Microsoft Access] -->
```