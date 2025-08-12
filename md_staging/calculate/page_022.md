```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_022.jpeg
document_name: calculate
page_number: 022
page_id: calculate#page_022
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T02:59:49Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- A comprehensive guide to using the Essential Calculate tool for ASP.NET.
- Demonstrates setting up forms with calculation dependencies for custom business objects.
- Explains function libraries, dependencies, and custom function implementation.

## Content

### Calculate Description

Essential Calculate for ASP.NET allows you to add extensive calculation support to your own business objects. Easily set up forms that have calculation dependencies among various controls on the form.

Essential Calculate comes with a function library of more than 150 entries. It supports cross sheet references. When used in conjunction with Essential XlsIO, you can fully load, manipulate, and compute Excel spreadsheets without any dependency upon Excel. Function implementation is extensible, and you can easily add your own custom functions.

### Featured Samples

#### Figure 8: Calculate samples displayed in the ASP.NET Sample Browser

The image shows the "Calculate" feature within the ASP.NET Sample Browser interface. The main navigation panel on the left lists categories like "Calculate," "Reports," and "Business Intelligence," indicating the user can explore various sample applications.

#### Sample Browsing

1. **Navigation**
   - The interface allows users to select and explore different sample code snippets for "Calculate."

2. **Demonstration**
   - The featured samples showcase how to implement dynamic calculations in forms using Essential Calculate.

3. **Selection and Browsing**
   - Select any sample and browse through the features.

### Source Code Location

#### Windows Forms Source Code
The default location of the Windows Forms Calculate source code is:

```
[System Drive]:\Program Files\Synfusion\Essential Studio\[Version Number]\Windows\Calculate.Windows\Src
```

#### ASP.NET Source Code
The default location of the ASP.NET Calculate source code is:

```
[System Drive]:\Program Files\Synfusion\Essential Studio\[Version Number]\Web\Calculate.Web\Src
```

## API Reference

### Namespaces and Classes
- **Namespace:** `Syncfusion.Calculate`
- **Class:** `CalculateEngine`
- **Members:**
  - **Methods:**
    - `Evaluate(string expression)`
    - `AddFunction(string name, Func<object, object>)`
  - **Properties:**
    - `Result`
    - `Error`

### Parameters
| Name       | Type               | Description                    | Required |
|------------|--------------------|--------------------------------|----------|
| `expression`  | `string`         | The formula to evaluate.      | Yes      |
| `name`      | `string`         | The name of the custom function.| Yes      |
| `function`  | `Func<object, object>` | The implementation of the custom function. | Yes      |

## Code Examples

### Example 1: Using the CalculateEngine

```csharp
using Syncfusion.Calculate;

var engine = new CalculateEngine();
engine.AddFunction("CustomSum", (params object[] args) =>
{
    var sum = 0;
    foreach (var arg in args)
    {
        if (arg is int) sum += (int)arg;
    }
    return sum;
});

var result = engine.Evaluate("CustomSum(10, 20, 30)");
Console.WriteLine(result); // Output: 60
```

## Page-Level Navigation/TOC

- **Calculate**
- **Source Code Location**
  - Windows Forms Source Code
  - ASP.NET Source Code

## RAG Annotations

<!-- tags: [syncfusion, calculate, asp.net, windows forms, api reference] keywords: [calculate engine, custom functions, source code location, windows forms, asp.net, dynamic calculations] -->
```