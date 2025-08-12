```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_040.jpeg
document_name: calculate
page_number: 040
page_id: calculate#page_040
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:00:30Z
fidelity: lossless
-->

# Essential Calculate

## Overview

- Learn to create a Windows Application that allows you to register variables with a `CalcQuick` object and use these variables in algebraic expressions.
- Understand how to compute quantities represented by formulas like `Rate * Amount` or `(1 + Rate) * Amount`.

## Content

### 3.5.2 Windows Application Using Variables and CalcQuickBase

In this section, you will learn how to create a Windows Application that allows you to register variables with a `CalcQuick` object and then use these variables in algebraic expressions. For example, you might register a variable named `Rate` to be `0.07` and a variable named `Amount` to be `1500`, and then compute a quantity represented by the formula `Rate * Amount` or by `(1 + Rate) * Amount`.

#### 3.5.2.1 Windows Forms CalcQuickBase

1. **In Visual Studio, use `File | New | Project` to create a new Windows Forms Application. Right-click the `References` in Solution Explorer and add a reference to `Syncfusion.Calculate.Base`.**

    **Figure 17: Essential Calculate Reference Being Added to the Project**
    ![Add Reference Dialog](https://i.imgur.com/additional_image_link_here.png)

    - The **Add Reference** dialog shows various components, and you need to select `Syncfusion.Calculate.Base` version `5.202.0.25` and add it to your project.

2. **Using the designer, drop three text boxes, three labels, two buttons, and one list box onto the form as shown in the picture below.**

## Code Examples

No specific code examples provided in this section, but you can add any relevant C# or XAML code snippets here.

## API Reference

### Namespace: Syncfusion.Calculate.Base

#### Class: `CalcQuick`

- **Properties:**
  - `RegisterVariable(String name, Object value)` — Registers a variable with the given name and value.
  - `Compute(String formula)` — Computes the result of the given formula.

## RAG Annotations

<!-- tags: windows application, calcquick, windows forms, algebraic expressions, variables, reference addition keywords: calculate, essential calculate, winforms, algebra, formulas, register variables -->
```