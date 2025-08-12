```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_244.jpeg
document_name: grid
page_number: 244
page_id: grid#page_244
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:05:07Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Introduces the Formula Library feature in the `Essential Grid` for Windows Forms.
- Highlights the integration with .NET Framework's `System.Math` class for mathematical functions.
- Describes additional functionalities such as `Sum` and `Avg`, and the ability to add custom functions.

## Content

### 4.1.4.6.2 Using the Formula Library

Essential Grid's Formula Library contains the mathematical functions that are available in the .NET Framework's `System.Math` class. In addition, there are `Sum` and `Avg` members. You can also add additional functions to this library by using your own code.

#### Sample Formula Library Usage

![Figure 132: Sample Formula Library Usage](#)

In the above screenshot, cell A2 has a formula that uses four different library functions: `Sqrt`, `Pow`, `Cos`, and `Sin`.

**Note:** For a complete list of these library functions, refer to the Class Reference for "GridFormulaEngine".

---

### 4.1.4.6.3 Supported Arithmetic Operators and Calculation Precedence

The current formula support will let you enter well-formed parenthetical algebraic expressions with operators and operands. The nine supported operators are shown in the following precedence table, with operators on the same level being calculated as encountered when the expression is scanned from left to right.

#### Code Tables

| Operation                                | Symbol          | Calculation Precedence |
|------------------------------------------|-----------------|-------------------------|
| Multiplication, Division                | `/` `*`         | 1st                     |
| Addition, Subtraction                   | `+` `-`         | 2nd                     |
| Less Than, Greater Than, Equal, Less Than Or Equal, Greater Than Or Equal, Not Equal | `<` `>` `=` `<=` `>=` `<>` | 3rd                     |

## API Reference

This section focuses on the `GridFormulaEngine` class reference for the supported library functions.

## Code Examples

None provided in this section.

## Cross References

See also:
- Class Reference for `GridFormulaEngine`

---

<!-- tags: [syncfusion, winforms, grid, essential grid, formula library, gridformulaengine, mathematical functions, arithmetic operators, calculation precedence] keywords: [essential grid, formula library, sum, avg, system.math, operators, precedence, gridformulaengine, sweaty programmer] -->
```