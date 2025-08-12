```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_112.jpeg
document_name: calculate
page_number: 112
page_id: calculate#page_112
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:06:58Z
fidelity: lossless
-->

## Overview
- Explains how to remove functions from the Library.
- Describes the use of `CalcEngine.RemoveFunction` method to remove a single function.
- Includes examples in C# and VB for removing functions from the Library.
- Outlines the process for replacing a function with another implementation.

## Content

### Removing Functions from the Library

#### Clearing All Functions
```csharp
// Remove all functions from the Library.
engine.LibraryFunctions.Clear();
```

```vb
// Remove all functions from the Library.
engine.LibraryFunctions.Clear()
```

After clearing all functions, you can add a few functions that will be used often. To know how to add functions, see **Add Function**.

#### Removing a Single Function
To remove a single function from the Function Library, use the `CalcEngine.RemoveFunction` method, passing a "function name" as the string that references this function, from a formula.

```csharp
// Remove formula name MyMin from the Library.
engine.RemoveFunction("MyMin");
```

```vb
' Remove formula name MyMin from the Library.
engine.RemoveFunction("MyMin")
```

### Replace Function
To replace a function with another implementation, you must remove the original name, and add the same name again with a different delegate method.

### 4.5.3 Functions

Here is a list of the Function Library entries included with Essential Calculate which includes more than 150 entries. For detailed information on each function, see **Function Reference Section**.

#### 4.5.3.1 Logical
This section lists the logical functions included with Essential Calculate in the below table.

## Page-level Navigation/TOC (if applicable)
- 4.5.3 Functions
  - 4.5.3.1 Logical

## Cross References
See also:
- Add Function
- Function Reference Section

<!-- tags: [Product, Syncfusion, Winforms, Calculate, Functions, Library, Essential Calculate, CalcEngine, RemoveFunction, Logical Functions] keywords: [clear functions, remove function, replace function, function library, MyMin, removeFunction, logical functions, essential calculate, function reference, add function] -->
```