```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_104.jpeg
document_name: calculate
page_number: 104
page_id: calculate#page_104
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:06:12Z
fidelity: lossless
-->

# Essential Calculate

- `>=` Greater Than Or Equal
- `<>` Not Equal

All operations are subject to the following hierarchy of operations. The level 1 operations are done first, followed by level 2, and so on. Within the same level, the operations are performed from left to right in the order in which they are encountered during the parsing of the formula.

1. - (Unary Minus)
2. `*` `/`
3. `+` `-`
4. `<` `>` `=` `<=` `>=` `<>`
5. `&` (Concatenation)

If you want to change the default operators precedence, then use parentheses to explicitly indicate the operation order.

## Examples

1. **Formulas** | **Computed Value**
   - `= 6 / 2 + 1` | 4
   - `= 6 / (2 + 1)` | 2
   - `= 2 + 4 / 2` | 4
   - `= (2 + 4) / 2` | 3

Logical operations return specific values: True or False. If you need specific numerical values associated with any logical expression, then use the logical expression as the first argument in the Formula Library IF-function, with the second argument being the numerical value of True and the third argument being the numerical value of False. If you use a well-formed logical expression in a larger calculation, True evaluates to numerical 1 and False evaluates to numerical 0 for use in the calculations.

## 4.4.2 Square Brackets in CalcQuickBase Formulas

If you are using a `CalcQuickBase` object to add calculation support to your business object, then you must use strings as indexers on the CalcQuickBase instance to get and set values. These strings are referred to as the value's Name. If you need to use a Name in a formula, then you should enclose the string within brackets, `[ ]`. In step three of the code below, four names A, B, C, and D are registered. Notice that the formula entered in step two uses the values from A and B by enclosing these names in brackets.

### Code Example

```csharp
// 1) Instantiates a CalcQuickBase object.
```
```html
<!-- tags: [product, module, control, api, version?] keywords: [calculate, operations, precedence, operators, logical operations, truth values, calcquickbase, square brackets, indexer strings, formula library, if function, true, false, numerical evaluation, business object, syncfusion winforms] -->
```