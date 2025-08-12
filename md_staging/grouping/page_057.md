```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_057.jpeg
document_name: grouping
page_number: 057
page_id: grouping#page_057
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:01:26Z
fidelity: lossless
-->

## Essential Grouping

- `<`, `>`, `=`, `<=`, `>=`, `<>`: less than, greater than, equal, less than or equal, greater than or equal, not equal
- match, like, in, between
- or, and, or

### Note

1. **Alpha constants used with `match` and `like` should be enclosed in apostrophes (`'`).**
2. **Logical operators return "1", if the logical expression is True and return "0", if the logical expression is False.**

Given below is some more information on special logical operators:

- **Match**  
  - Returns `1` if there is any occurrence of the right-hand argument in the left-hand argument.  
  **Example**  
  `[Company_Name]` match `'RTR'` returns `0` for any record whose CompanyName field does not contain `RTR` anywhere in the string.

- **Like**  
  - Checks if the field starts exactly as specified in the right-hand argument.  
  **Example**  
  `[Company_Name]` like `'RTR'` returns `1` for any record whose CompanyName field is exactly `'RTR'`.  
  You can use an asterisk as a wildcard.  
  `[Company_Name]` like `'RTR*'` returns `1` for any record whose CompanyName field starts with `'RTR'`.  
  `[Company_Name]` like `'*RTR'` returns `1` for any record whose CompanyName field ends with `'RTR'`.

- **In**  
  - Checks if the field value is any of the values listed in the right-hand operand. The collection of items used as the right-hand should be separated by commas and enclosed within braces `{ }`.  
  **Example**  
  `[code]` in `{1,10,21}` returns `1` for any record whose code field contains `1` or `10` or `21`.  
  `[Company_Name]` in `{RTR,MAS}` returns `1` for any record whose CompanyName field is `RTR` or `MAS`.

### Note
Spaces that are significant in the list, i.e., `{RTR,MAS}` is not the same as `{RTR, MAS}`.

```html
```