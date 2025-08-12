```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_981.jpeg
document_name: grid
page_number: 981
page_id: grid#page_981
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:52:35Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Describes the use of ExpressionFields to display calculated values based on other fields in the same record.
- Explains how ExpressionFields can be created using the TableDescriptor.ExpressionFields property.
- Highlights the editor where you can add multiple expression fields with their own expressions.

## Content

When there is a need to display calculated values based on the values on other fields in the same record, ExpressionFields would be the right choice to use. ExpressionFields can be created by using the TableDescriptor.ExpressionFields property. This will open an editor wherein you can add any number of expression fields each with its own expression used to calculate the results.

### Example: Adding an Expression Field

The following example demonstrates how to add an Expression Field to calculate the Winning Percentage for basketball teams.

#### Figure 376: Adding an Expression Field

The image shows the `ExpressionFieldDescriptor Collection Editor` in use, where the following settings are configured:

- **Name**: `Winning %`
- **Result Type**: `System.Double`
- **Expression**: `([wins]*100)/([wins]+[ties]+[losses])`
- **AllowTrimEnd**: `False`
- **FieldPropertyType**: `System.Double`
- **ForceIntermediate**: `False`
- **Hide**: `False`
- **ReferencedField**: `losses,ties,wins`

This setup allows the grid to dynamically calculate and display the winning percentage for each team based on their wins, ties, and losses.

## Code Example

Here is an example of how you can configure an ExpressionField programmatically:

```csharp
// Setting up the ExpressionField
TableDescriptor tableDesc = new TableDescriptor();

// Define an ExpressionField
ExpressionFieldDescriptor exprField = new ExpressionFieldDescriptor();
exprField.Name = "Winning %";
exprField.Type = typeof(double);
exprField.Expression = "([wins]*100)/([wins]+[ties]+[losses])";

// Add the ExpressionField to the table descriptor
tableDesc.ExpressionFields.Add(exprField);

// Apply the table descriptor to the grid control
gridGroupingControl1.TableDescriptor = tableDesc;
```

## API Reference

### Namespace: Syncfusion.Grouping

#### Class: ExpressionFieldDescriptor

##### Properties
- **Name**: Gets or sets the name of the ExpressionField.
- **Type**: Gets or sets the type of the ExpressionField.
- **Expression**: Gets or sets the mathematical expression used to calculate the field value.
- **ReferencedFields**: Gets or sets the fields that are referenced in the calculation.

#### Members
- **ExpressionFieldDescriptor()**: The default constructor.
- **ExpressionFieldDescriptor(string name, Type type, string expression)**: Constructs a new instance with a specified name, type, and expression.

##### Methods
- **GetReferencedFields()**: Gets the list of fields referenced in the expression.

##### Example Usage
```csharp
// Creating a new ExpressionFieldDescriptor
ExpressionFieldDescriptor exprField = new ExpressionFieldDescriptor("Winning %", typeof(double), "([wins]*100)/([wins]+[ties]+[losses])");
```

### TableOptions

- **ExpressionFields**: Allows the addition and management of calculated fields in the grid.

## Cross References
- [TableDescriptor Properties](#tabledescriptor-properties)
- [Row Operations](#row-operations)

### Figure: Adding an Expression Field

The figure shows the setup of an ExpressionFieldDescriptor in the grid control, illustrating how to create and configure an ExpressionField.

## Page-level Navigation/TOC
- [ExpressionFields Overview](#expressionfields-overview)
- [Adding an Expression Field](#adding-an-expression-field)
- [API Reference](#api-reference)

### Tags and Keywords
<!-- tags: [expressionfields, gridgroupingcontrol, calculatedfields, windowsforms] keywords: [calculation, dynamicfield, percentagemetric, gridcontrol] -->
```