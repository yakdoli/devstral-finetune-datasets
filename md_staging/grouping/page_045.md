```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_045.jpeg
document_name: grouping
page_number: 045
page_id: grouping#page_045
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:00:45Z
fidelity: lossless
-->

# Essential Grouping

## Overview
- Demonstrates filtering data on the console based on specific conditions.
- Explains how to add algebraic expressions to data objects using ExpressionFieldDescriptor.

## Content

### Filtering on the Console

![](attachment:Figure_18_data_filtered.png)

**Figure 18:** Screen Showing Data Filtered on [D] LIKE 'd1' OR [B] = 2

Filtering is applied to the data displayed in the console.

#### 4.3.2 Expressions

You can add new properties to your data object that are algebraic expressions involving other properties of the object.

To add an expression, you need to create an `ExpressionFieldDescriptor` and add it to the `Engine.TableDescriptor.Expression.Fields` collection. Here we illustrate this process by adding an expression that computes 2.1 times the value of property B plus 3.2.

#### Steps to Add an Expression

1. In the Console Application, comment out all the code that is in the `Main` method and add this code to create a data object and set it into the `GroupingEngine`.

```csharp
// Create an arraylist of random MyObjects.
ArrayList list = new ArrayList();
```

## API Reference

### ExpressionFieldDescriptor

- **Name**: ExpressionFieldDescriptor
- **Usage**: Used to define algebraic expressions for data objects.

### Engine.TableDescriptor.Expression.Fields

- **Name**: Expression.Fields
- **Usage**: Collection to store ExpressionFieldDescriptor objects.

## Code Examples

### Adding an Expression to a Data Object

```csharp
// Sample code to create an ExpressionFieldDescriptor.
ExpressionFieldDescriptor expressionField = new ExpressionFieldDescriptor();
expressionField.Expression = "2.1 * B + 3.2";
expressionField.FieldName = "ExpressionField";
tableDescriptor.Expression.Fields.Add(expressionField);
```

## Cross References

- See also: [Creating a GroupingEngine](#groupingengine), [Defining Table Descriptors](#tabledescriptors)

### RAG Annotations

<!-- tags: WinForms, Grouping, ExpressionFieldDescriptor, TableDescriptor keywords: filtering, expressions, algebraic, GroupingEngine, TableDescriptor -->
```