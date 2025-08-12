<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_769.jpeg
document_name: grid
page_number: 769
page_id: grid#page_769
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:38:48Z
fidelity: lossless
-->

## Match Operators in Syncfusion Grid for Windows Forms

### Match

| Keyword | Operator | Description | Example |
|---------|----------|-------------|---------|
| Match   | match    | Returns 1 if there is any occurrence of the right-hand argument in the left-hand argument. For example, `[Company] match 'RTR'` returns 0 for any record whose CompanyName field does not contain RTR anywhere in the string. | `[Company] match 'Syncfusion'` |

### Like

| Keyword | Operator | Description | Example |
|---------|----------|-------------|---------|
| Like    | like     | Checks if the field starts exactly as specified in the right-hand argument. For example, `[Company] like 'RTR'` returns 1 for any record whose CompanyName field is exactly RTR. You can use an asterisk as a wildcard. `[Company] like 'RTR*'` returns 1 for any record whose CompanyName field starts with RTR. `[Company] like '*RTR'` returns 1 for any record whose CompanyName field ends with RTR. | `[Sport] like 'Basket*'` |

### In

| Keyword | Operator | Description | Example |
|---------|----------|-------------|---------|
| In      | in       | Checks if the field value is any of the values listed in the right-hand operand. The collection of items used as the right-hand should be separated by commas and enclosed with brackets({}). For example, `[code] in` | `[Country] in {"USA", "UK"}` |

## Summary

- The `match` operator checks for any occurrence of a substring within a field.
- The `like` operator checks if a field starts or ends with a specific pattern, using asterisks as wildcards.
- The `in` operator checks if a field value is one of the specified values in a list.

<!-- tags: [Syncfusion, WinForms, Grid, Match, Like, In, Operators] keywords: [match, like, in, filter, search, string comparison, substring, wildcard, list, value checking] -->