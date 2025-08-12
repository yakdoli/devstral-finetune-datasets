```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_166.jpeg
document_name: calculate
page_number: 166
page_id: calculate#page_166
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:08:52Z
fidelity: lossless
-->

# Essential Calculate

## Content

### 4.7.45 EXP

Returns e raised to the power of the given number.

#### Syntax

`EXP(number)`

where:  
`number` is the exponent applied to the base e.

---

### 4.7.46 EXPONDIST

Returns the exponential distribution.

#### Syntax

`EXPONDIST(x, lambda, cumulative)`

where:  
- `x` is the value of the function.  
- `lambda` is the parameter value.  
- `cumulative` is a logical value that indicates which form of the exponential function is to be provided. If `cumulative` is `True`, `EXPONDIST` returns the cumulative distribution function; if `False`, it returns the probability density function.

#### Remarks

- The equation for the probability density function is:  
  \[ f(x; \lambda) = \lambda e^{-\lambda x} \]  
- The equation for the cumulative distribution function is:  

---

## API Reference

This section describes the `EXP` and `EXPONDIST` functions in detail.

### EXP

**Namespace**: Essential Calculate  
**Class**: `Math`  
**Method**: `EXP`

#### Parameters

| Name | Type | Description |
|------|------|-------------|
| `number` | Number | The exponent applied to the base e. |

#### Returns

| Type | Description |
|------|-------------|
| Double | The value of e raised to the power of the given number. |

---

### EXPONDIST

**Namespace**: Essential Calculate  
**Class**: `StatisticalFunctions`  
**Method**: `EXPONDIST`

#### Parameters

| Name | Type | Description |
|------|------|-------------|
| `x` | Double | The value of the function. |
| `lambda` | Double | The parameter value. |
| `cumulative` | Boolean | Indicates whether to return the cumulative distribution function (`True`) or the probability density function (`False`). |

#### Returns

| Type | Description |
|------|-------------|
| Double | The value of the exponential distribution based on the specified parameters. |

---

## Code Examples

### Example 1: Using EXP

```csharp
using EssentialCalculate.Math;

double exponent = 2;
double result = EXP(exponent);
// result will be e^2
```

### Example 2: Using EXPONDIST

```csharp
using EssentialCalculate.StatisticalFunctions;

double x = 1.5;
double lambda = 0.5;
bool cumulative = true;
double result = EXPONDIST(x, lambda, cumulative);
// result will be the cumulative exponential distribution for the given parameters
```

---

## Cross References

- See also: `EXP`, `EXPONDIST`

<!-- tags: [syncfusion-sdk, mathematical functions, probability distributions, user guide, version 11.4.0.26] keywords: [EXP, EXPONDIST, exponential distribution, probability density function, cumulative distribution function, essential calculate] -->
```