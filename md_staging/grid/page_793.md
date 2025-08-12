```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_793.jpeg
document_name: grid
page_number: 793
page_id: grid#page_793
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:40:10Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates filtering by display member in a Grid control.
- Explains how filter expressions can be used to manipulate grid data.
- Provides detailed information on setting and validating filter expressions.

## Content

### Filtering By Display Member

#### Figure 317: Filtering By Display Member
- The figure shows a grid with columns: Orders, OrderID, Customers, Quantity, and Price ($).
- The Customers column has a dropdown filter with options like "(All)," "William Wordsworth," "Mark Twain," etc.
- The filter functionality allows users to apply display member filters to filter rows based on customer names.

#### Note
For more details, refer the following browser sample:

```plaintext
<Install Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Grouping.Windows\Samples\2.0\Filters and Expressions\Filter By DisplayMember Demo
```

##### 4.3.4.3.4.2.5 List of Filter Expressions
- Filter expressions can be set and added to `RecordFilters` collection through a textual string.
- The string should adhere to the syntax to be followed and must be valid.

The following table lists tokens used in Expression Filters and their descriptions:

| Syntax | Expression                          | Description                                 |
|--------|-------------------------------------|---------------------------------------------|
| *      | `[columnname] * 'anynumber'`      | Filters grid based on the multiplied value computed. |

## API Reference (if applicable)

- **Namespace**: Syncfusion.Windows.Forms.Grid
- **Class/Control**: GridControl
- **Members**:
  - **Properties**:
    - `RecordFilters`: Collection of filters applied to grid rows.
    - `FilterByDisplayMember`: Method or property related to display member filtering.
  - **Methods**:
    - `AddFilter`: Adds a filter expression to the grid.
    - `ApplyFilter`: Applies a filter to the grid.
  - **Events**:
    - `FilterApplied`: Triggered when a filter is applied to the grid.

## Code Examples (multi-language supported)

#### C# Example
```csharp
// Adding a filter by display member
gridControl.RecordFilters.Add("Customers", "James Dickey");

// Applying the filter
gridControl.ApplyFilter();
```

## Cross References
- Refer to the browser sample provided for practical implementation examples.
- See also: Grid Control Overview, Expression Filters, Filter Collection Management, and Grid Customization.

<!-- tags: [product, module, control, api, version?] keywords: [filter expression, display member, grid control, windows forms, record filters, filtering, essential grid] -->
```