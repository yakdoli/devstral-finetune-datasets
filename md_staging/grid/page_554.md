```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_554.jpeg
document_name: grid
page_number: 554
page_id: grid#page_554
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:24:09Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Explains how to bind a grid to a `DataTable` and use the `DataView.RowFilter` property to restrict shown rows.
- Discusses using `RowFilter` similar to SQL `WHERE` clause with examples.
- References detailed syntax in .NET Frameworks online help for `DataColumn.Expression`.

## Content

### Binding Grid to DataTable with Row Filtering

Assume that you are binding a grid to a `DataTable`. In this case, you will have to use the `DataView.RowFilter` property to restrict the rows that appear in your Grid Data Bound Grid. The syntax for the `RowFilter` clause is very similar to the SQL `WHERE` clause. You will be able to see a full description of this in the .NET Frameworks online help for the `DataColumn.Expression`, which uses the same syntax.

#### Example `RowFilter` Strings

| RowFilter String         | Result                                                                 |
|---------------------------|------------------------------------------------------------------------|
| `[City Area] = Center`   | Shows only rows where the `City Area` column is `center`.            |
| `rate > 10`              | Shows only rows where the `rate` column is greater than `10`.         |
| `Name LIKE a*`           | Shows only rows where the `Name` column begins with `*a`.             |
| `Name LIKE *a`           | Shows only rows where the `Name` column ends with `*a`.               |

---

### Sample Grid Filtering Demonstration

#### Screenshot: Grid with Filtering

![Grid on Right is Filtered Version of Grid on Left](https://example.com/image-url)

**Figure 217: Grid on Right is Filtered Version of Grid on Left**

The filtered grid is created by setting the `RowFilter` property of it to a default view. If you change the `RowFilter` property, then the grid's contents will change to reflect the new filter.

---

### C# Code Example

```csharp
// Example code block will be placed here after additional OCR processing.
```

### Notes

- The `RowFilter` property allows dynamic filtering without fetching data from the database again.
- The `LIKE` operator supports pattern matching with wildcards (`*`).

---

## Page-level Navigation/TOC (if applicable)
- None found on this page.

## Cross References
- Refer to .NET Frameworks online help for `DataColumn.Expression`.
- Related topics may include grid binding and SQL query-like functionalities.

## RAG Annotations
<!-- tags: [grid, dataview, rowfilter, windows forms, datatABLE, sql where clause] keywords: [rowfilter, dataview, grid, filtering, c#, datatable, sql_where, LIKE, filter strings] -->
```