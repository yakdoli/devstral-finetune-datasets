```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_286.jpeg
document_name: grid
page_number: 286
page_id: grid#page_286
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:06:40Z
fidelity: lossless
-->

### Essential Grid for Windows Forms

#### EXPONDIST(x, lambda, cumulative)

- **x** is the value of the function.
- **lambda** is the parameter value.
- **cumulative** is a logical value that indicates which form of the exponential function is to be provided. If cumulative is True, EXPONDIST returns the cumulative distribution function; if False, it returns the probability density function.

#### Remarks

The equation for the probability density function is:

- \( f(x; \lambda) = \lambda e^{-\lambda x} \)

- The equation for the cumulative distribution function is:

- \( F(x; \lambda) = 1 - e^{-\lambda x} \)

### Error Conditions

- **#NUM!** - occurs if \( x \) is less than zero.
- **#VALUE!** - occurs if \( x \) is non-numeric.
- **#VALUE!** - occurs if lambda is non-numeric.
- **#NUM!** - occurs if lambda is equal to or less than zero.

---

### 4.1.4.6.6.85 FACT

**Returns the factorial of a number.** The factorial of a number is the product of all positive integers \( \leq \) the given number.

#### Syntax

**FACT(number), where:**

- **number** is the non-negative number for which you want the factorial of. If the number is not an integer, it is truncated.

---

### 4.1.4.6.6.86 FACTDOUBLE

---

## API Reference (if applicable)

- **Namespace:** 
- **Class:**
- **Members (Methods/Properties/Events/Enums):**

### Code Examples (multi-language supported)

- Example code snippets using C#: 
```csharp
// Example C# implementation of EXPONDIST and FACT functions
```

- Example code snippets using VB.NET: 
```vb
' Example VB.NET implementation of EXPONDIST and FACT functions
```

## Cross References

See also: [Other related functions or references as mentioned on the page]

---

<!-- tags: [essential grid, windows forms, exponential distribution, factorial, probability density function, cumulative distribution function] keywords: [expondist, fact, factdouble, lambda, cumulative, probability density, factorial] -->
```