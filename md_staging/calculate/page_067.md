```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_067.jpeg
document_name: calculate
page_number: 067
page_id: calculate#page_067
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:02:21Z
fidelity: lossless
-->

## EssentialCalculate

### Introduction

This page describes the functionality of using simple variables in the `CalcQuickBase` object, specifically focusing on how variables are managed and utilized in algebraic expressions.

#### Overview

- **Key Concepts**:
  - The `CalcQuickBase` object maintains a collection of variables.
  - Variables can be added or modified by assigning a name and a value.
  - Algebraic expressions can use these variables by enclosing their names in brackets.

---

### Simple Variables

#### Explanation

When a name is used as an indexer on the `CalcQuickBase` object, the object checks the collection of variables it maintains:

- **Adding New Variables**: If the name is not in the collection, it is added as a new item with the assigned value.
- **Modifying Existing Variables**: If the name is already in the collection, its assigned value is updated to the new value.

---

#### Parsing and Replacement

When a formula is parsed, the `CalcQuickBase` object replaces all occurrences of variable names with their current values. To use a named variable in a formula, enclose it within brackets, as shown in the following example:

```plaintext
[base]*[height]/2
```

This formula takes the value represented by the base and multiplies it by the height of the value divided by two.

---

### String Variables as Formulas

As a convention, if you want a variable to hold a string that is a formula and be treated as a formula, begin that string with a special character, the `CalcQuickBase.FormulaCharacter` (default value is `"="`). If you invoke the `ParseAndCompute` method directly, any string you pass will be treated as a formula, regardless of whether it begins with `FormulaCharacter`.

---

### The FormulaInfo Class

This section delves into the `FormulaInfo` class, which provides detailed information about the formula parsing and computation process.

---

### Example

The interface shown in **Figure 30** demonstrates the use of simple variables in the context of calculating a formula using the `CalcQuickBase` object.

#### Figure 30: Simple Variables

![Figure 30: Simple Variables](image.png)

This figure illustrates the process of entering an algebraic expression using variables and computing the result.

---

### Summary

- **Variables** are managed efficiently within the `CalcQuickBase` object.
- Variables are used in formulas by enclosing their names in brackets.
- The `FormulaInfo` class provides further insights into the parsing and computation of formulas.

---

## API Reference

### Namespace: Syncfusion.Windows.Forms.CalcEngine

#### Class: `CalcQuickBase`

##### Properties

- **FormulaCharacter**: Gets or sets the special character that denotes a formula.

##### Methods

- **ParseAndCompute(string formula)**: Parses and computes the given formula.

---

## Code Examples

### C#

```csharp
using Syncfusion.Windows.Forms.CalcEngine;

class Program
{
    static void Main()
    {
        // Create an instance of CalcQuickBase
        var calc = new CalcEngine.CalcQuickBase();

        // Set variables
        calc["base"] = 1.4;
        calc["height"] = 3.5;

        // Compute the formula
        var result = calc.ParseAndCompute("[base]*[height]/2");

        // Output the result
        System.Console.WriteLine("Computed value: " + result);
    }
}
```

---

## Page-level Navigation/TOC

- **Overview**
- **Simple Variables**
  - Explanation
  - Parsing and Replacement
- **String Variables as Formulas**
- **The FormulaInfo Class**
- **Summary**
- **API Reference**
- **Code Examples**

---

## Cross References

- Refer to the `CalcEngine` namespace documentation for complete details on the `CalcQuickBase` class and related methods.

---

### Note

This page provides detailed insights into handling and utilizing variables within algebraic expressions using the `CalcQuickBase` object in Syncfusion Winforms. It is part of the essential guide for developers working with dynamic computation features.

---

<!-- tags: [Syncfusion Winforms, CalcQuickBase, algebraic expressions, variables, parsing, computation, FormulaInfo Class, version] keywords: [simple variables, algebraic expressions, CalcQuickBase, variables, parsing, computation, FormulaCharacter, ParseAndCompute, C#, code examples] -->
```