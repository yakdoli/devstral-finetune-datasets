```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_175.jpeg
document_name: calculate
page_number: 175
page_id: calculate#page_175
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:09:21Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Enables calculation of predicted exponential growth using existing data.
- Provides an array of values used for regression analysis.

## Content

### **4.7.62 GROWTH**

This feature enables you to calculate predicted exponential growth using existing data. This calculates and returns an array of values used for the regression analysis. Growth enables you to perform a regression analysis.

#### Table 13: Method Table

| Method | Description                          | Parameters             | Type     | Return Type | Reference links |
|--------|---------------------------------------|-------------------------|----------|--------------|-----------------|
| Growth() | Calculates the Growth for an array of cells. | Known y's, <br> Known x's, <br> new_x's | Method | String | N/A |

#### Syntax

The following is the formula to calculate Growth for an array of cells in a column:

```plaintext
=GROWTH(known_y's, [known_x's], [new_x's],
```

- **Known_y's**: A set of y-values you already know in a relationship, where \( y = b \cdot m^x \).
- **Known_x's**: An optional set of x-values that you may already know in the relationship, where \( y = b \cdot m^x \).
- **New_x's**: New x-values for which you want GROWTH to return corresponding y-values.

#### Code Example

```plaintext
=Growth(B2:B7,A2:A7,C6:C7)
```

### **4.7.63 HARMEAN**

---

## API Reference
- **Namespace**: N/A (Not explicitly mentioned in the provided page)
- **Class**: N/A (Not explicitly mentioned in the provided page)
- **Members**:
  - **Growth()**
    - **Parameters**:
      - Name | Type | Description | Default | Required
      - known_y's | Array | Known y-values | None | Yes
      - [known_x's] | Array | Known x-values (optional) | None | No
      - [new_x's] | Array | New x-values | None | No
    - **Returns**: String
    - **Description**: Calculates the predicted y-values for the given x-values using exponential growth.
    - **Exceptions**: None explicitly mentioned.

## Code Examples (multi-language supported)
The provided code example in the page demonstrates the use of the `Growth()` function:

```csharp
var growthResult = Growth(B2:B7, A2:A7, C6:C7);
```

In this example:
- `B2:B7` represents the known_y's.
- `A2:A7` represents the known_x's.
- `C6:C7` represents the new_x's for which the corresponding y-values are calculated.

---

## Cross References
- See also: `HARMEAN` for calculating the harmonic mean.

---

<!-- tags: [Syncfusion, Winforms, User Guide, Essential Calculate, GROWTH, HARMEAN, Exponential Growth, Regression Analysis] keywords: [exponential growth, regression analysis, GROWTH function, HARMEAN, known_y's, known_x's, new_x's, Syncfusion Winforms] -->
```