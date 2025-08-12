```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_752.jpeg
document_name: grid
page_number: 752
page_id: grid#page_752
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:38:10Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

```csharp
Me.gridGroupingControl1.TableDescriptor.SummaryRows.AddRange(New GridSummaryRowDescriptor() { srd1, srd2 })
```

### Overview
- Demonstrates the addition of multi-row summaries in an Essential Grid.
- Example screenshot of multi-row summaries for sports data.
- Explains summaries for nested tables and groups using `ChildTableDescriptor`.

## Content

### Summaries for Nested Tables and Groups

#### Background
Given below is a sample screenshot.

![Multi Row Summaries](https://example.com/multiscreen.png)
*Figure 301: Multi Row Summaries*

**Summaries for Nested Tables and Groups**

Say your datasource has two tables nested, Orders and Order Details, with summaries for the parent table. The summaries that are set for the top level table are sufficient enough for the groups. You need to define summary rows only for the child tables. It can be achieved by creating summaries through the ChildTableDescriptor. The following code illustrates this process.

#### Code Example
```csharp
// Adding Summaries for the Parent Table(Orders).
GridSummaryColumnDescriptor scd = new GridSummaryColumnDescriptor("Sum", SummaryType.DoubleAggregate, "Freight", "{Sum:#}");
GridSummaryRowDescriptor srd = new GridSummaryRowDescriptor("Sum", "$", scd);
srd.Appearance.AnyCell.HorizontalAlignment = GridHorizontalAlignment.Right;
srd.Appearance.AnyCell.BackColor = Color.FromArgb(255, 231, 162);
this.gridGroupingControl.TableDescriptor.SummaryRows.Add(srd);

// Adding Summaries for the Child Table(Order Details).
```

### Conclusion
This section highlights how to handle summaries for nested tables and groups in Essential Grid for Windows Forms, emphasizing the importance of configuring summaries based on the table hierarchy.

## API Reference

- **GridSummaryRowDescriptor**:
  - Constructor: `new GridSummaryRowDescriptor(name, description, columnDescriptor)`
  - Properties:
    - `Appearance`: Specifies the appearance of the summary row.
      - `HorizontalContentAlignment`: Setting the horizontal alignment of the content.
      - `BackColor`: Setting the background color for the row.

## Code Examples

The provided C# code illustrates how to define and add summaries for both parent and child tables in an Essential Grid.

## Page-level Navigation/TOC (if applicable)

- Summaries for Nested Tables and Groups
  - Code Example
  - Background Information

## Cross References

- Related topics: Adding Summaries, Handling Nested Tables, Grid Summary Rows

<!-- tags: [syncfusion, winforms, grid, essential grid, summaries, nested tables, groups, parent tables, child tables, gridsummaryrowdescriptor, appearance, .net] keywords: [nested tables, summaries, row descriptors, grid summary, gridgroupingcontrol, parent table, child table, alignment, backcolor, appearance properties] -->
```