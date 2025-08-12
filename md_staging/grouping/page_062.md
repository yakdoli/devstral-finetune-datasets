```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_062.jpeg
document_name: grouping
page_number: 062
page_id: grouping#page_062
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:01:31Z
fidelity: lossless
-->

# Essential Grouping

## Overview
- ComputeFunc:
  - Explains how to compute functions for grouping.
- Expression Fields:
  - Details the process of adding expression fields to data records.

## Content

### 5.3 How to Add Expression Fields?

To add an expression field to the data in the Grouping Engine, you must first create an instance of an `ExpressionFieldDescriptor` and add it to the `ExpressionFields` collection in the `TableDescriptor`. The `ExpressionFieldDescriptor` will allow you to specify a string that holds an algebraic expression using any of the other fields that are in the record.

The following code snippet illustrates this.

#### [C#]

```csharp
// Add an expression property that multiplies field B by 2.1 and adds 3.2
ExpressionFieldDescriptor efd = new ExpressionFieldDescriptor("MultipleOfB", "2.1 * [B] + 3.2");
this.groupingEngine.TableDescriptor.ExpressionFields.Add(efd);

// Assumes the datasource to be an IList, holding objects of type MyClass.
MyClass o = this.groupingEngine.Table.Records[2].GetData() as MyClass;

// MultipleOfB is an expression field name and B is a property in MyClass.
object someValue = this.groupingEngine.Table.Records[2].GetValue("B");
object someExpressionValue =
this.groupingEngine.Table.Records[2].GetValue("MultipleOfB");
```

#### [VB.NET]

```vb
' Add an expression property that multiplies field B by 2.1 and adds 3.2
Dim efd As New ExpressionFieldDescriptor("MultipleOfB", "2.1 * [B] + 3.2")
Me.groupingEngine.TableDescriptor.ExpressionFields.Add(efd)

' Assumes the datasource to be an IList, holding objects of type MyClass.
Dim o As MyClass = CType(Me.groupingEngine.Table.Records(2).GetData(), MyClass)

' MultipleOfB is an expression field name and B is a Property in MyClass.
Dim someValue As Object = Me.groupingEngine.Table.Records(2).GetValue("B")
Dim someExpressionValue As Object =
Me.groupingEngine.Table.Records(2).GetValue("MultipleOfB")
```

## API Reference

The `ExpressionFieldDescriptor` class is used to define a descriptor for an expression field. It allows specifying an algebraic expression that can be evaluated over the fields in the records.

- **Constructor**: 
  - `ExpressionFieldDescriptor(string name, string expression)`: Creates a new instance of the `ExpressionFieldDescriptor` with the specified name and expression.

## Code Examples

The provided code examples demonstrate how to:
- Create an `ExpressionFieldDescriptor` object.
- Add it to the `TableDescriptor`'s `ExpressionFields` collection.
- Retrieve the values of both regular fields and expression fields.

## Page-level Navigation/TOC
- [5.3 How to Add Expression Fields?]

## Cross References
See also:
- Grouping Engine
- TableDescriptor
- ExpressionFieldDescriptor

<!-- tags: [Essential Grouping, Expression Fields, Grouping Engine, TableDescriptor, ExpressionFieldDescriptor] keywords: [ExpressionFieldDescriptor, algebraic expression, ExpressionFields, TableDescriptor, Grouping Engine, MyClass, records, GetValue] -->
```
