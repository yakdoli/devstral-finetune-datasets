```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_244.jpeg
document_name: calculate
page_number: 244
page_id: calculate#page_244
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:14:32Z
fidelity: lossless
-->

## Content

### Example Code: Parsing and Computing Formulas

#### C#

```csharp
string result1 = this.calculate.ParseAndCompute("[Rate] * [Amount]");
```

#### VB

```vb
' Declares a CalcQuickBase object.
private calculate As CalcQuickBase

'...
' Creates an instance.
Me.calculate = New CalcQuickBase()
'... Sets up any variables you need in your calculation.
' Calls the ParseAndCompute method to compute formulas.
Dim result As String = Me.calculate.ParseAndCompute("4 * 5 + SQRT(3)")
Dim result1 As String = Me.calculate.ParseAndCompute("[Rate] * [Amount]")
```

### 5.1.3 How To Enter Vectors Of Numbers Into CalcQuickBase?

Some formulas, like Intercept, require you to enter the parameters as vectors of numbers. Other formulas, like Sum, accept number vectors as parameter arguments. To use such formulas through a CalcQuickBase object, you must enter the numbers by enclosing them in braces. The following code illustrates this.

#### C#

```csharp
// Sets the number vectors as parameters.
CalcQuickBase["known_Y"] = "{2,3,9,1,8}";
CalcQuickBase["known_X"] = "{6,5,11,7,5}";

// Computes the Intercept returned by these values.
this.textBox1.Text = 
CalcQuickBase.ParseAndCompute("Intercept([known_Y],[known_X])");
```

#### VB

```vb
' Sets the number vectors as parameters.
CalcQuickBase("known_Y") = "{2,3,9,1,8}"
CalcQuickBase("known_X") = "{6,5,11,7,5}"

' Computes the Intercept returned by these values.
Me.textBox1.Text =
```

### Summary

This section explains how to use the `ParseAndCompute` method of the `CalcQuickBase` object to compute formulas in both C# and VB. Additionally, it demonstrates how to handle number vectors as arguments for formulas that support them, such as the `Intercept` function.

### API Reference

#### Methods
- **ParseAndCompute(string formula): string**
  - **Parameters**: 
    - formula: `string` - The formula to compute.
  - **Returns**: `string` - The computed result of the formula.
  - **Description**: Parses and computes the given formula string.

### Code Examples

#### Example: Computing the Product of Rate and Amount

```csharp
string result1 = this.calculate.ParseAndCompute("[Rate] * [Amount]");
```

#### Example: Entering Number Vectors for the Intercept Formula

```csharp
CalcQuickBase["known_Y"] = "{2,3,9,1,8}";
CalcQuickBase["known_X"] = "{6,5,11,7,5}";
this.textBox1.Text = CalcQuickBase.ParseAndCompute("Intercept([known_Y],[known_X])");
```

### Tags and Keywords
<!-- tags: CalcQuickBase, ParseAndCompute, Intercept, number vectors, formula computation, C#, VB, Syncfusion Winforms keywords: CalcQuickBase, ParseAndCompute, Intercept, number vectors, formula computation, C#, VB, Syncfusion, Winforms -->
```