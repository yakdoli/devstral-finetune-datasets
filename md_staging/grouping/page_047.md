```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_047.jpeg
document_name: grouping
page_number: 047
page_id: grouping#page_047
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:00:28Z
fidelity: lossless
-->

# Essential Grouping

## Overview
- This page describes how to add an expression property to a table descriptor using C# and VB.NET in the context of Syncfusion Winforms.
- Highlights the process of displaying records before and after adding an expression property.
- Demonstrates creating and adding an expression field descriptor to the `ExpressionFields` collection of the table descriptor.

## Content

### Adding an Expression Property

#### Adding before Filtering

In the following code snippets, the process of displaying the data before filtering, adding an expression property, and then displaying the data after adding the field is outlined.

#### C# Code

```csharp
// Pause
Console.ReadLine();

// Add an expression property.
ExpressionFieldDescriptor efd = new ExpressionFieldDescriptor("MultipleOfB", "2.1 * [B] + 3.2");
groupingEngine.TableDescriptor.ExpressionFields.Add(efd);

// Display the data after adding the field.
foreach (Record rec in groupingEngine.Table.FilteredRecords)
{
    Console.WriteLine(rec.GetValue("MultipleOfB"));
}

// Pause
Console.ReadLine();
```

#### VB.NET Code

```vb
' Display the data before filtering.
Dim rec As Record
For Each rec In groupingEngine.Table.FilteredRecords
    Dim obj As MyObject = CType(rec.GetData(), MyObject)
    If Not (obj Is Nothing) Then
        Console.WriteLine(obj)
    End If
Next rec

' Pause
Console.ReadLine()

' Add an expression property.
Dim efd As New ExpressionFieldDescriptor("MultipleOfB", "2.1 * [B] + 3.2")
groupingEngine.TableDescriptor.ExpressionFields.Add(efd)

' Display the data after adding the field.
For Each rec In groupingEngine.Table.FilteredRecords
    Console.WriteLine(rec.GetValue("MultipleOfB"))
Next rec
```

## API Reference

### Methods/Properties Used

- `ExpressionFieldDescriptor`
  - `ExpressionFieldDescriptor(String name, String expression)`
    - Creates a new expression field descriptor with the specified name and expression.
  - `ExpressionFields.Add(ExpressionFieldDescriptor)`
    - Adds an expression field descriptor to the table descriptor.

### Parameters

- `name`: The name of the expression field.
- `expression`: The mathematical expression to evaluate.

### Returns

- No explicit return value for the methods used in the context.

## Cross References

- See also: [Expression Fields in Syncfusion Winforms](#expression-fields-in-syncfusion-winforms)

<!-- tags: [Syncfusion, Winforms, ExpressionFieldDescriptor, TableDescriptor, Grouping, Version: 11.4.0.26] keywords: [ExpressionFieldDescriptor, TableDescriptor, Filtering, Winforms, C#, VB.NET] -->
```