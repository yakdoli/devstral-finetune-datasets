```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_914.jpeg
document_name: tools
page_number: 914
page_id: tools#page_914
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:42:43Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### 3.5.8.11.1 Properties Deprecated

| **Property**         | **Alternatives**                                       | **Comments**                                                                 |
|-----------------------|-------------------------------------------------------|-----------------------------------------------------------------------------|
| `NullState`          | `IsNull`                                               | Deprecated as it should have Getter alone.                                  |
| `UseNullString`      | `AllowNull`                                            | This behavior is incorporated with `AllowNull`; previously both `AllowNull` and `UseNullString` existed. Removed for better clarity. |
| `IsNullValue`        | `IsNull`                                               | `IsNullValue` means the same as `NullState` and `IsNull`, and it has been deprecated for better clarity.                              |
| `MaxLength`          | `MaxValue`, <br> `NumberDecimalDigits`                 | `Max` length is removed as there is a conflict. Hence use `MaxValue` and `NumberDecimalDigits` as alternatives.                     |
| `EnforceMinMaxDuringValidating` | `OnValidationFailed.KeepFocus`              | No need for a separate property as `MinMaxValidation` already exists. The same behavior can be achieved with the alternative.     |

### 3.5.8.11.2 Newly Added API's

| **Property**         | **Description**                                        | **Behavior**                                                             |
|-----------------------|-------------------------------------------------------|-----------------------------------------------------------------------------|
| `IsNull` (Read Only) | Returns a Boolean specifying the `NullState` of the control | True when `Control.Text` equals `String.Empty` or `NullString`.         |
| `AllowNull`          | Specifies whether the field can be nulled.             | Related to `NullString`. `NullString` will be set when the ``organized.``|

## Page-level Navigation/TOC (if applicable)
- 3.5.8.11.1 Properties Deprecated
- 3.5.8.11.2 Newly Added API's

### Cross References
See also: additional relevant sections or external references (if provided on the page).

<!-- tags: [syncfusion, winforms, api-deprecation, new-apis, version 11.4.0.26] keywords: [nullable, nullstate, usenullstring, isnullvalue, maxlength, enforceminmaxduringvalidating, nullability, booleantype, allownull] -->
```