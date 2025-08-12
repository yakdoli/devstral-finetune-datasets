```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_127.jpeg
document_name: calculate
page_number: 127
page_id: calculate#page_127
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:06:43Z
fidelity: lossless
-->

## Essential Calculate

The ROMAN function converts an Arabic number to a Roman numeral. This function returns a text string depicting the Roman numeral form of the given number.

### Syntax

The syntax of the ROMAN function is

```
=ROMAN( number, (form) )
```

- `number` – Required.
- `form` – Optional, this value will specify the style of the Roman numeral.

If `number` is not an integer, then it will be rounded down.

### Form Style Variations

| Form             | Type          |
|------------------|---------------|
| 0 or omitted     | Classic.      |
| 1                | More concise. See example below. |
| 2                | More concise. See example below. |
| 3                | More concise. See example below. |
| 4                | Simplified.   |

### Error Handling

**#VALUE!** - Occurs if any of the given values is non-numeric, or for values less than 0 and greater than 3999.

### Example

| FORMULA               | RESULT        |
|-----------------------|---------------|
| `=ROMAN(499, 0)`     | CDXCIX        |
| `=ROMAN(499, 1)`     | ID            |
| `=ROMAN(-100)`       | #VALUE!       |

## 4.5.6.16 IFERROR

The IFERROR function tests if an initial given value (or expression) returns an error, and if so, this function returns a second given argument. Otherwise, the function returns the initial tested value.

### Syntax

The syntax of the IFERROR function is

```
=IFERROR(value, value_error)
```

- `value` – Required. This is a value to check for the error.
- `value_error` – Required. This value will be returned if the `value` has an error.

## API Reference

### ROMAN Function

- **Parameters:**
  - `number`: Numerical value to convert to a Roman numeral.
  - `form`: Optional style specification for the Roman numeral.

### IFERROR Function

- **Parameters:**
  - `value`: The value to test for an error.
  - `value_error`: The value to return if an error is found.

## Code Examples

### Example 1: Using ROMAN Function

```csharp
// Convert an Arabic number to Roman numeral in Classic style
string result = ROMAN(499, 0); // Output: CDXCIX
```

### Example 2: Handling Errors with IFERROR Function

```csharp
// Using IFERROR to handle potential errors
object result = IFERROR(SQRT(-1), "Invalid Input"); // Output: "Invalid Input"
```

## Cross References

- For more information on error handling, see the documentation on error functions and their applications.
- For additional Roman numeral formatting styles, refer to the section on ROMAN numeral styles.

<!-- tags: Roman numeral, IFERROR, error handling, Roman numeral conversion, Roman numeral styles, WinForms. keywords: ROMAN function, IFERROR function, Roman numeral, numeric conversion, error handling, concise Roman numeral, simplified Roman numeral -->
```