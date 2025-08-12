```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_351.jpeg
document_name: grid
page_number: 351
page_id: grid#page_351
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:11:47Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Returns the skewness of a distribution, characterizing its degree of asymmetry around the mean.
- Includes functions such as `SKEW` and `SKEW.P`.
- Provides details about syntax, equations, and error handling for skewness calculations.

## Content

### SKEW Function

#### Overview
Returns the skewness of a distribution. Skewness characterizes the degree of asymmetry of a distribution around its mean.

#### Syntax
```plaintext
SKEW(number1, number2, ...)
```
where:

- `number1, number2, ...` are arguments for which you want to calculate the skewness. You can also use a single array or a reference to an array instead of arguments separated by commas.

#### Remarks
- The equation for skewness is defined as follows:
  \[
  \frac{n}{(n-1)(n-2)} \sum \left( \frac{x_i - \bar{x}}{s} \right)^3
  \]

### SKEW.P Function

#### Overview
Returns the skewness of a distribution based on a population: a characterization of the degree of asymmetry of a distribution around its mean.

#### Syntax
```plaintext
SKEW.P(number 1, [number 2], ...)
```
where:
- Number 1 is required, and subsequent numbers are optional. Number 2, ... up to 254 are numbers or names, arrays, or references that contain numbers for which you want the population skewness, can be used.

#### Remarks
- **#NUM!** - occurs if arguments do not have a valid value.
- **#VALUE!** - occurs if arguments do not have valid data types.
- **#DIV/0!** - occurs if there are fewer than three data points, or the sample standard deviation is zero.

### SLN Function

#### Overview
Returns the straight-line depreciation of an asset for one period.

#### Syntax
```plaintext
SLN
```

## API Reference

### SKEW
- **Namespace:** Syncfusion.Windows.Forms.Grid
- **Parameters:**
  - `number1`, `number2`, ...: Input numbers for which skewness is calculated.
- **Returns:** The skewness of the distribution.

### SKEW.P
- **Namespace:** Syncfusion.Windows.Forms.Grid
- **Parameters:**
  - `number 1`: Required input number.
  - `[number 2]`, ...: Optional input numbers.
- **Returns:** The population skewness of the distribution.
- **Exceptions:**
  - `#NUM!`
  - `#VALUE!`
  - `#DIV/0!`

### SLN
- **Namespace:** Syncfusion.Windows.Forms.Grid
- **Parameters:**
  - Not explicitly mentioned in the provided content.
- **Returns:** The straight-line depreciation of an asset for one period.

## Code Examples

### Example 1: Calculating Skewness
```csharp
using Syncfusion.Windows.Forms.Grid;

double[] numbers = {1, 2, 3, 4, 5};
double skewness = Grid.CalculateSkew(numbers);
Console.WriteLine("Skewness: " + skewness);
```

### Example 2: Population Skewness Calculation
```csharp
using Syncfusion.Windows.Forms.Grid;

double[] populationNumbers = {5, 6, 7, 8, 9};
double skewnessP = Grid.CalculateSKEW_P(populationNumbers);
Console.WriteLine("Population Skewness: " + skewnessP);
```

## Page-level Navigation/TOC
- SKEW Function
- SKEW.P Function
- SLN Function

## Cross References
- See also: `CalculateSkew` and `CalculateSKEW_P` methods in the `Syncfusion.Windows.Forms.Grid` namespace.

<!-- tags: [skewness, population skewness, straight-line depreciation, Essential Grid, Windows Forms] keywords: [skew, SKEW.P, SLN, distribution asymmetry, Windows Forms API] -->
```