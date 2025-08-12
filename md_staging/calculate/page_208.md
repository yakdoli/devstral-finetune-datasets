```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_208.jpeg
document_name: calculate
page_number: 208
page_id: calculate#page_208
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:12:12Z
fidelity: lossless
-->


## EssentialCalculate

### Overview
- Explains the parameters and usage of the POISSON function, including details on how it calculates probabilities.
- Describes the syntax and functionality of the POW function, which raises a number to a specified power.

### Content

#### Poisson Function
The POISSON function is used to calculate probabilities based on the Poisson distribution.

**Parameters:**
- **x**: The number of events.
- **mean**: The expected numeric value.
- **cumulative**: A logical value that determines the form of the probability distribution returned. If True, it returns the cumulative Poisson probability; if False, it returns the Poisson probability mass function.

**Remarks:**
- **X**: Must be >= 0.
- **Mean**: Must be > 0.
- **POISSON Calculation**:
  - For **cumulative = False**:
    \[
    POISSON = \frac{e^{-\lambda} \lambda^x}{x!}
    \]
  - For **cumulative = True**:
    \[
    CUMPOISSON = \sum_{k=0}^{x} \frac{e^{-\lambda} \lambda^k}{k!}
    \]

#### 4.7.126 Pow

**The Pow Function**
The Pow function returns the result of a number raised to a power.

**Syntax:**
\[
\text{POW(number, power)}
\]

**Parameters:**
- **number**: The base number. It can be any real number.
- **power**: The exponent to which the base number is raised.

## API Reference (if applicable)

### Poisson Function

- **Parameters**:
  - Name | Type | Description | Default | Required
  - x | Numeric | Number of events | - | Yes
  - mean | Numeric | Expected numeric value | - | Yes
  - cumulative | Logical | Determines the type of probability distribution | - | Yes

### Pow Function

- **Parameters**:
  - Name | Type | Description | Default | Required
  - number | Numeric | Base number | - | Yes
  - power | Numeric | Exponent | - | Yes

Returns:
- **Type**: Numeric
- **Description**: The result of raising the base number to the specified power.

## Code Examples (multi-language supported)

```csharp
// Example of using the Poisson function with cumulative = False
double poissonResult = Math.Poisson(5, 3, false);

// Example of using the Pow function
double powerResult = Math.Pow(2, 3);
```

## Page-level Navigation/TOC (if applicable)
- 4.7.125 Poisson Function
- 4.7.126 Pow Function
- Additional relevant topics if applicable

## Cross References
- See also: Other functions related to statistical calculations and mathematical operations.

<!-- tags: [syncfusion, winforms, pow, poisson, function, probability, statistics] keywords: [poisson, pow, function, statistical, probability, mathematical] -->
```