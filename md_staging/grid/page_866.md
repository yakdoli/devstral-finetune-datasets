```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_866.jpeg
document_name: grid
page_number: 866
page_id: grid#page_866
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:48:41Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

![Figure: Format Cell Dialog](https://i.imgur.com/KQkjH.png)

## 4.3.4.5.3 Conditional Formatting

### Overview
- This section explains the feature of Conditional Formatting in Grid Grouping control.
- It details how to format grid cells based on specific conditions using the GridConditionalFormatDescriptor.
- It provides steps to specify filter criteria and styles for the filtered cells through the designer.

### Content

Grid Grouping control has in-built support for Conditional Formatting. This feature allows you to format grid cells based on a certain condition. This can be achieved by defining a **GridConditionalFormatDescriptor** for the grid. Using this descriptor, you can specify the filter criteria for the cells and the style to be applied for the filtered cells. Once these specifications are defined, then the given styles are applied to only those cells that satisfy the condition specified.

Conditional Formatting can be specified through the designer itself by accessing the **TableDescriptor.ConditionalFormats** property. This will open the **GridConditionalFormatDescriptor** editor wherein you can add as many formatters as you want. For each such formatter, you need to specify the filter criteria either by adding **RecordFilters** or by an **Expression**. The below property editor illustrates this process.

## API Reference

### Classes
#### ConditionalFormatting
- **Properties**
  - **ConditionalFormats**: Contains a collection of GridConditionalFormat descriptors.
  - **TableDescriptor**: Specifies the table for which conditional formatting is applied.

### Methods
- **ApplyFormatting()**: Applies the specified formatting to the grid cells based on the defined conditions.

## Code Examples

```csharp
// Example of applying conditional formatting
using Syncfusion.Windows.Forms.Grid;

// Assuming grid is an instance of GridDataBoundGrid
GridStyleInfo style = new GridStyleInfo();
style.TextColor = Color.Red;
style.BuiltInStyle = GridBuiltInStyle.Advanced;

grid.TableDescriptor.ConditionalFormats.Add(new GridConditionalFormatDescriptor()
{
    DisplayMembers = new string[] { "Grade" },
    FormatExpression = "Grade == 'A'",
    Style = style
});

// Apply the formatting
grid.ApplyFormatting();
```

## Page-level Navigation/TOC
- **4.3.4.5.3 Conditional Formatting**
  - Overview
  - Content
  - API Reference
  - Code Examples

## Cross References
- See also: Grid Grouping, Format Cell Dialog, Designer Support, TableDescriptor

## RAG Annotations
<!-- tags: [grid, conditional formatting, designer, winforms] keywords: [GridConditionalFormatDescriptor, TableDescriptor.ConditionalFormats, RecordFilters, Expression, ApplyFormatting, GridStyleInfo] -->
```