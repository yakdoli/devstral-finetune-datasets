```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_182.jpeg
document_name: calculate
page_number: 182
page_id: calculate#page_182
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:10:01Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Returns the internal rate of return for a series of cash flows represented by the numbers in values.
- Checks for blank or null values.
- Checks whether a value is an error.

## Content

### 4.7.74 IRR
Returns the internal rate of return for a series of cash flows represented by the numbers in values. The cash flows must occur at regular intervals such as monthly or annually.

#### Syntax
`IRR(values, guess)`

#### Parameters
- **values**: An array or a reference to cells that contain numbers for which you want to calculate the internal rate of return. Values must contain at least one positive value and one negative value to calculate the internal rate of return. IRR uses the order of values to interpret the order of cash flows. Be sure to enter your payment and income values in the sequence you want.
- **guess**: A number that you guess is close to the result of IRR. An iterative technique is used for calculating IRR. In most cases, you do not need to provide a guess for the IRR calculation. If a guess is omitted, it is assumed to be 0.1 (10 percent).

### 4.7.75 IsBlank
The IsBlank function checks for blank or null values.

#### Syntax
`IsBlank(value)`

#### Parameters
- **value**: The value that you want to test. If the value is blank, this function will return TRUE. If the value is not blank, the function will return FALSE.

### 4.7.76 IsErr
The IsErr function checks whether a value is an error.

#### Syntax
`IsErr(value)`

#### Parameters
- **value**: The value that you want to test. If the value is an error value (except #N/A), this function will return TRUE/FALSE to indicate whether a value is an error.

## API Reference
### Methods
- **IRR(values, guess)**: Returns the internal rate of return.
  - **Parameters**:
    - `values`: Array or reference to cells containing numbers.
    - `guess`: Optional guess for the result of IRR.
  - **Returns**: The internal rate of return.

- **IsBlank(value)**: Checks for blank or null values.
  - **Parameters**:
    - `value`: The value to test.
  - **Returns**: TRUE if the value is blank, FALSE otherwise.

- **IsErr(value)**: Checks whether a value is an error.
  - **Parameters**:
    - `value`: The value to test.
  - **Returns**: TRUE if the value is an error (except #N/A), FALSE otherwise.

## Code Examples
### Example 1: Calculating IRR
```csharp
double[] cashFlows = {-10000, 3000, 4200, 6800};
double guess = 0.1;

double irr = IRR(cashFlows, guess);
Console.WriteLine("IRR: " + irr);
```

### Example 2: Checking if a value is blank
```csharp
string value = "   "; // or any value

bool isBlank = IsBlank(value);
Console.WriteLine("Is Blank: " + isBlank);
```

### Example 3: Checking if a value is an error
```csharp
double value = double.NaN; // or any error value

bool isError = IsErr(value);
Console.WriteLine("Is Error: " + isError);
```

## RAG Annotations
<!-- tags: [Syncfusion, Winforms, Financial Functions, Error Checking, Blank Checks, Internal Rate of Return, IRR, IsBlank, IsErr] keywords: [IRR, cash flows, guess, blank values, error values, financial calculations, checking] -->
```