```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_287.jpeg
document_name: grid
page_number: 287
page_id: grid#page_287
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:07:46Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Detailed explanation of the FACTDOUBLE function and its usage in calculating the double factorial of a given integer.
- Information on handling errors in function inputs.
- Explanation of the False function for evaluating logical values.

## Content

### FACTDOUBLE Function

#### Overview
The FACTDOUBLE function returns the double factorial of a given value. The given value must be an integer value.

#### Syntax
The syntax of the FACTDOUBLE function is:
```
= FACTDOUBLE (number).
```
- **number** – Required.

#### Remarks
- **#NUM!** - If the number is less than zero (0).
- **#VALUE!** - Occurs if any of the given arguments are non-numeric.

#### Example

| FORMULA          | RESULT    |
|------------------|-----------|
| = FACTDOUBLE(6)  | 48        |
| = FACTDOUBLE(-2) | #NUM!     |

### False Function

#### Overview
The False function returns a logical value when the given string value is false.

#### Syntax
```
False(stringvalue)
```
- **stringvalue** – is to provide any text value or empty string.

### FDIST Function

#### Overview
The FDIST function returns the F probability distribution.

#### Syntax
```
FDIST(x, degrees_freedom1, degrees_freedom2), where:
```
- **x** is the value at which to evaluate the function.

---

## API Reference

### Methods

#### `FACTDOUBLE(number)`
**Parameters:**
- **number** (integer) - The integer value for which the double factorial is calculated.

**Returns:**
- The double factorial of the given number.

**Exceptions:**
- **#NUM!** - If the number is less than zero (0).
- **#VALUE!** - If the argument is non-numeric.

#### `False(stringvalue)`
**Parameters:**
- **stringvalue** (string) - The string value to evaluate.

**Returns:**
- A logical value of `False`.

#### `FDIST(x, degrees_freedom1, degrees_freedom2)`
**Parameters:**
- **x** (float) - The value at which to evaluate the F probability distribution.
- **degrees_freedom1** (float) - The degrees of freedom for the numerator.
- **degrees_freedom2** (float) - The degrees of freedom for the denominator.

**Returns:**
- The F probability distribution value.

---

## Code Examples

```csharp
public void CalculateDoubleFactorial()
{
    double result = FACTDOUBLE(6); // Returns 48
    Console.WriteLine(result);
}

public void EvaluateFalse()
{
    bool result = False("any text"); // Returns False
    Console.WriteLine(result);
}

public void CalculateFDist()
{
    double x = 5;
    double degreesOfFreedom1 = 10;
    double degreesOfFreedom2 = 20;
    double result = FDIST(x, degreesOfFreedom1, degreesOfFreedom2);
    Console.WriteLine(result);
}
```

---

<!-- tags: [syncfusion, winforms, grid, factdouble, false, fdist] keywords: [double factorial, logical value, f probability distribution, syntax, remarks, example] -->
```