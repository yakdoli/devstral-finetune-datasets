```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_060.jpeg
document_name: grouping
page_number: 060
page_id: grouping#page_060
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:01:11Z
fidelity: lossless
-->

# Essential Grouping

1. The `groupingEngine.Table.Records` collection will give you access to the raw data in your datasource through the `GroupingEngine`.

2. If you have applied filters or have sorted the data and want to access the sorted or filtered data, then you must use the `GroupingEngine.Table.FilteredRecords` collection.

3. This collection reflects the visible state of the data in the `GroupingEngine`.

## 5.2 How to Add Custom Calculations to Expression Fields?

Essential Grouping lets you add your own functions to a function library which can be used in an expression field. In this manner, you can do custom calculations in expressions. This is a two-step process which is given below:

1. Register the function name and a delegate with the grouping engine.
2. Implement a method that does your calculation.

In the code given below, we add a method named 'Func' that takes two arguments and performs a certain calculation on those arguments.

```csharp
// Step 1
// Add function named Func that uses a delegate named ComputeFunc to define a custom calculation.
ExpressionFieldEvaluator evaluator = 
    this.groupingEngine.TableDescriptor.ExpressionFieldEvaluator;
evaluator.AddFunction("Func", new 
    ExpressionFieldEvaluator.LibraryFunction(ComputeFunc));

// Sample usage in an Expression column.
this.groupingEngine.TableDescriptor.ExpressionFields.Add("test");
this.groupingEngine.TableDescriptor.ExpressionFields["test"].Expression = 
    "Func([Col1], [Col2])";

//...
```

```csharp
// Step 2
// Define ComputeFunc that returns the absolute value of the 1st arg minus 2 * the 2nd arg.
public string ComputeFunc(string s)
{
    // Get the list delimiter (for en-us, it is a comma).
    char comma = 
        Convert.ToChar(this.gridGroupingControl1.Culture.TextInfo.ListSeparator);
}
```

<!-- tags: [product, module, control, api, version?] keywords: [grouping, filtering, sorting, data access, custom calculations, expression fields, grouping engine, function library, delegate, ComputeFunc, FilteredRecords, TableDescriptor] -->
```