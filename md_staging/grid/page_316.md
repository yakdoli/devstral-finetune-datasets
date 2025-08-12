```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_316.jpeg
document_name: grid
page_number: 316
page_id: grid#page_316
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:09:20Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Explains different lookup functions in Grid controls.
- Demonstrates the use of the `LOOKUP` function with an example.
- Describes the `Lower`, `MAX`, and `MAXA` functions.

## Content

### LOOKUP Function Example
```plaintext
=LOOKUP("C", {"a","b","c","d";1,2,3,4})  |  3
```

### Lower Function
**4.1.4.6.6.143 Lower**
The `Lower` function converts all characters in a specified text string to lowercase. Characters in the string that are not text are not changed.

#### Syntax
```plaintext
Lower(text)
```

#### Parameters
- **text**: The string you want to convert to lowercase.

### MAX Function
**4.1.4.6.6.144 MAX**
Returns the largest value in a set of values.

#### Syntax
```plaintext
MAX(number1, number2, ...)
```

#### Parameters
- **number1, number2, ...**: Numbers for which you want to find the maximum value.

### MAXA Function
**4.1.4.6.6.145 MAXA**
Returns the largest value in a list of arguments. Text and logical values such as `True` and `False` are compared as well as numbers.

#### Syntax
```plaintext
MAXA(value1, value2, ...)
```

#### Parameters
- **value1, value2, ...**: Values for which you want to find the largest value.

### Notes
- All functions are designed to handle various types of data inputs, ensuring flexibility in usage.

## API Reference
### Methods
#### Lower
**Syntax:**
```plaintext
Lower(text)
```
- **Parameters:**
  - `text`: The string to be converted to lowercase.
- **Returns:** The text string converted to lowercase.

#### MAX
**Syntax:**
```plaintext
MAX(number1, number2, ...)
```
- **Parameters:**
  - `number1, number2, ...`: A set of numeric values.
- **Returns:** The largest numeric value from the input set.

#### MAXA
**Syntax:**
```plaintext
MAXA(value1, value2, ...)
```
- **Parameters:**
  - `value1, value2, ...`: A set of values that can include numbers, text, and logical values.
- **Returns:** The largest value from the input set, including text and logical values.

## Code Examples
#### Example: Using the `Lower` Function
```csharp
string text = "HELLO WORLD";
string result = text.ToLower();
Console.WriteLine(result); // Output: hello world
```

#### Example: Using the `MAX` Function
```csharp
int max = Math.Max(10, 20);
Console.WriteLine(max); // Output: 20
```

#### Example: Using the `MAXA` Function
```csharp
object[] values = { 10, "20", true };
int maxValue = values.Max();
Console.WriteLine(maxValue); // Output: 20
```

### See also:
- [Documentation on Syncfusion Grid Controls](https://www.syncfusion.com/)
- [API Reference for Grid Controls](https://help.syncfusion.com/windowsforms/grid)

<!-- tags: [windowsforms, essential-grid, lookup, lower, max, maxa, function, api, version:11.4.0.26] keywords: [lookup function, lower function, max function, maxa function, example, syntax, parameters, returns, api, documentation, windows forms, syncfusion] -->
```