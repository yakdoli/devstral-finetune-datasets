```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_319.jpeg
document_name: grid
page_number: 319
page_id: grid#page_319
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:09:46Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## MINA Function Overview

### Overview
- **Purpose**: Finds the smallest value among the provided arguments.
- **Arguments**: Can include numeric values, logical values, and text. Logical values and text are evaluated according to specific rules.

### Function Definition
**MINA(value1, value2, …)**, where:

- **value1, value2, …**: Values for which you want to find the smallest value.

### Remarks
- **Logical Evaluation**:
  - Arguments that contain `True` evaluate as `1`.
  - Arguments that contain text or `False` evaluate as `0` (zero).

---

## MINUTE Function Overview

### Overview
- **Purpose**: Returns the minutes of a time value, expressed as an integer ranging from `0` to `59`.

#### Function Identifier
**4.1.4.6.6.151 MINUTE**

### Syntax
**MINUTE(serial_number)**, where:

- **serial_number**: The time that contains the minute you want to find. This can be entered as:
  - Text strings within quotation marks (e.g., `"6:00 PM"`),
  - Decimal numbers (e.g., `0.75`, representing `6:00 PM`), or
  - Results of other formulas or functions (e.g., `TIMEVALUE("6:00 PM")`).

### Remarks
- **Time Representation**: Time values are a portion of a date value and are represented by a decimal number. For example, `12:00 PM` is represented as `0.5`.

---

## MINVERSE Function Overview

### Overview
- **Purpose**: Retrieves the inverse matrix for the matrix stored in an array.

#### Function Identifier
**4.1.4.6.6.152 MINVERSE**

### Syntax
**MINVERSE(array)**, where:

- **array**: An numeric array with an equal number of rows and columns.

### Remarks
- **Error Handling**: `#VALUE!` occurs if any cells in the array are empty or contain a string.

---

## API Reference

### Parameters
- **MINA**:
  - **value1, value2, …**:
    - Type: Mixed (numeric, logical, or text values).
    - Description: Values to evaluate for the smallest value.
    - Default: None.
    - Required: Yes.
- **MINUTE**:
  - **serial_number**:
    - Type: Time or decimal representation of time.
    - Description: Time value to extract the minute from.
    - Default: None.
    - Required: Yes.
- **MINVERSE**:
  - **array**:
    - Type: Numeric array with equal rows and columns.
    - Description: Matrix for which the inverse is to be calculated.
    - Default: None.
    - Required: Yes.

### Returns
- **MINA**: Smallest value from the provided arguments.
- **MINUTE**: Integer representing the minute from the time value.
- **MINVERSE**: Inverse matrix for the input array.

### Exceptions
- **MINVERSE**:
  - `#VALUE!`: Occurs if cells in the array are empty or contain non-numeric data.

---

## Code Examples

### Example 1: Using MINA Function
```csharp
double[] values = { 10, 20, 30, 40, 50 };
double min = MINA(10, 20, 30, 40, 50);
Console.WriteLine($"The minimum value is: {min}");
```

### Example 2: Using MINUTE Function
```csharp
double serialTime = DateTime.Parse("6:30 PM").TimeOfDay.TotalDays;
int minutes = (int)(serialTime * 24 * 60);
Console.WriteLine($"The minute is: {minutes}");
```

### Example 3: Using MINVERSE Function
```csharp
double[,] matrix = {
    { 1, 2 },
    { 3, 4 }
};

// Calculate inverse
double[,] inverseMatrix = Matrix.Inverse(matrix);

Console.WriteLine("Inverse Matrix:");
for (int i = 0; i < inverseMatrix.GetLength(0); i++)
{
    for (int j = 0; j < inverseMatrix.GetLength(1); j++)
    {
        Console.Write($"{inverseMatrix[i, j]}\t");
    }
    Console.WriteLine();
}
```

---

## Cross References
- See also: Documentation for additional matrix operations and time-value manipulation functions.

<!-- tags: [syncfusion, winforms, grid, mina, minute, minverse, matrix operations, time functions] keywords: [MINA, MINUTE, MINVERSE, smallest value, time, inverse matrix, numeric array, error handling, decimal representation] -->
```