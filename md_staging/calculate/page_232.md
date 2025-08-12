```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_232.jpeg
document_name: calculate
page_number: 232
page_id: calculate#page_232
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:13:43Z
fidelity: lossless
-->

## Content

### TEXT

**Converts a value to text in a specific number format.**

#### Syntax

```markdown
TEXT(value, format_text)
```

**where:**

- `value` is a numeric value, a formula that evaluates to a numeric value or a reference to a cell containing a numeric value.
- `format_text` is a number format in text form in the Category box on the Number tab in the Format Cells dialog box.

### TIME

**Returns the decimal number for a particular time.**

The decimal number returned by TIME is a value ranging from 0 (zero) to 0.99999999, representing the times from 0:00:00 (12:00:00 A.M.) to 23:59:59 (11:59:59 P.M.).

#### Syntax

```markdown
TIME(hour, minute, second)
```

**where:**

- `hour` is a number from 0 (zero) to 23 representing the hour.
- `minute` is a number from 0 to 59 representing the minute.
- `second` is a number from 0 to 59 representing the second.

### TIMEVALUE

**Returns the decimal number of the time represented by a text string. The decimal number is a value ranging from 0 (zero) to 0.99999999, representing the times from 0:00:00 (12:00:00 A.M.) to 23:59:59 (11:59:59 P.M.).**

---

## API Reference

### Parameters

#### TEXT
- **value**: Numeric value or reference to a numeric value.
- **format_text**: String specifying the number format.

#### TIME
- **hour**: Integer representing the hour (0 to 23).
- **minute**: Integer representing the minute (0 to 59).
- **second**: Integer representing the second (0 to 59).

#### TIMEVALUE
- **text_string**: A string representing the time.

### Returns

- **TEXT**: A string representation of the number in the specified format.
- **TIME**: A floating-point number representing the given time as a decimal fraction of a day.
- **TIMEVALUE**: A floating-point number representing the given time as a decimal fraction of a day.

## Code Examples

### C#

```csharp
// Example using TEXT
string result = TEXT(1234.567, "#,##0.00");
// result: "1,234.57"

// Example using TIME
double timeDecimal = TIME(13, 45, 30); 
// timeDecimal: 0.572916667 (3:45:30 PM)

// Example using TIMEVALUE
double timeValue = TIMEVALUE("13:45:30"); 
// timeValue: 0.572916667 (3:45:30 PM)
```

---

## Tags and Keywords

<!-- tags: syncfusion, winforms, text, time, timevalue, datetime, numeric formatting, function, syntax, parameter, return value keywords: text, time, timevalue, format_text, hour, minute, second, decimal number, numeric value, function syntax -->
```