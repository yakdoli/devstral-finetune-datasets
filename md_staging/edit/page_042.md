```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_042.jpeg
document_name: edit
page_number: 042
page_id: edit#page_042
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:56:28Z
fidelity: lossless
-->

## Essential Edit for Windows Forms

| Syntax  | Description                                                                 |
|---------|-----------------------------------------------------------------------------|
| `\n`    | Matches a new line `\u000A`.                                               |
| `\e`    | Matches an escape `\u001B`.                                                |
| `\040`  | Matches an ASCII character as octal (exactly three digits). The character `\040` represents a space. |
| `\x20`  | Matches an ASCII character using hexadecimal representation (exactly two digits). |
| `\u0020` | Matches a Unicode character using hexadecimal representation (exactly four digits). |
| `\\`    | Matches a character when followed by a character that is not recognized as an escaped character. For example, `\*` is the same as `\x2A`. |

### Character Classes

A character class is a set of characters that will find a match if any one of the characters included in the set matches. The following table summarizes the character matching syntax.

| Character Class | Description                                                                 |
|-----------------|-----------------------------------------------------------------------------|
| `.`            | Matches any character except `\n`. When within a character class, the `.` will be treated as a period character. |
| `[aeiou]`      | Matches any single character included in the specified set of characters.    |
| `[^aeiou]`     | Matches any single character not in the specified set of characters.         |
| `[0-9a-fA-F]`  | Use of a hyphen (-) allows specification of contiguous character ranges.      |
| `\w`           | Matches any word character.                                               |
| `\W`           | Matches any non-word character.                                           |
| `\s`           | Matches any whitespace character.                                        |
| `\S`           | Matches any non-whitespace character.                                     |
| `\d`           | Matches any decimal digit.                                               |
```