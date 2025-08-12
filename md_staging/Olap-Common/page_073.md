```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_073.jpeg
document_name: Olap Common
page_number: 073
page_id: Olap Common#page_073
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:19:39Z
fidelity: lossless
-->

# Essential OlapCommon

```csharp
1,
    [Date].[Fiscal].CurrentMember
)
)
Then 0

When VBA!Abs
(
(
[Measures].[Reseller Sales Amount] -
(
[Measures].[Reseller Sales Amount],
ParallelPeriod
(
[Date].[Fiscal].[Fiscal Year],
1,
[Date].[Fiscal].CurrentMember
)
)
)
/
(
[Measures].[Reseller Sales Amount],
ParallelPeriod
(
[Date].[Fiscal].[Fiscal Year],
1,
[Date].[Fiscal].CurrentMember
)
)
) <=.02
Then 0
```

## Example Explanation

The provided code snippet is an MDX (Multidimensional Expressions) statement, commonly used in OLAP (Online Analytical Processing) systems to query and manipulate multidimensional data. Here's a breakdown of the key components:

- **`[Date].[Fiscal].CurrentMember`**: This refers to the currently selected fiscal date member. It's a dimension member that helps in specifying a particular period in the fiscal calendar.

- **`[Measures].[Reseller Sales Amount]`**: This measures the amount of sales made by resellers. It's a quantitative measure in the cube.

- **`ParallelPeriod` Function**: This function retrieves the corresponding member in a parallel period relative to the current member. In the given code, it references the fiscal year one period before the current fiscal period.

- **`ABS` Function**: This function computes the absolute value of the difference between the current fiscal year's reseller sales amount and the reseller sales amount in the parallel period.

- **Conditional Statement (`Then 0`)**: The `When` clause checks a condition and sets the result to `0` when the condition is met. Specifically, it checks if the absolute percentage change in reseller sales is less than or equal to 2%.

This MDX statement is used to calculate and compare reseller sales amounts for the current fiscal period and the previous fiscal year's equivalent period. It ensures that if the change is minimal (less than or equal to 2%), the result is set to `0`, indicating no significant change.

## Related Topics

For further details on MDX and its components, refer to:
- MDX Functions (e.g., `ABS`, `ParallelPeriod`)
- Dates and Times in MDX
- Conditional Expressions in MDX

<!-- tags: [syncfusion, winforms, olap, mdx, essentials] keywords: [mdx, fiscal period, reseller sales amount, parallel period, absolute change, conditional statements] -->
```