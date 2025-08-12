```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_033.jpeg
document_name: grid
page_number: 033
page_id: grid#page_033
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:18:21Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- The page provides details about enabling filters on specific columns in the Essential Grid for Windows Forms.
- It introduces the various types of filters available, including Excel-style, ordinary, filter by display member, and dynamic filters.
- It includes a sample link for accessing the demo code.

## Content

### Figure 3: Filters on Specific Columns

![](attachment:Figure_3_Filters_on_Specific_Columns.png)

#### Filter Types and Cell Types
- **Excel-Style Filter**
  - **Cell Type:** GridExcelFilterCell
- **Ordinary Filter**
  - **Cell Type:** No Cell Type Needed
- **Filter By Display Member**
  - **Cell Type:** FilterByDisplayMemberCell
- **Dynamic Filter**
  - **Cell Type:** DynamicFilterCell

### Sample Link
A sample is available in the following location:

```
[Installed Drive]\AppData\Local\Syncfusion\EssentialStudio\[Version]\Windows\Grid.Grouping.Windows\Sample\2.0\Filters and Expressions\Filter By DisplayMember Demo
```

### Enable Filters on Desired Columns
The following code is used to enable filters in specific columns:

#### C#
```csharp
GridDynamicFilter filter = new GridDynamicFilter();
filter.AllowIndividualColumnWiring = true;
filter.WireGrid(gridGroupingControl);
```

#### VB
```vb
Dim filter As New GridDynamicFilter()
filter.AllowIndividualColumnWiring = True
filter.WireGrid(gridGroupingControl);
```

#### Dynamic Filter Wired to Column 0
Dynamic filter is wired to column 0 by using the following code:

## API Reference
- None provided in this section.

## Code Examples
- The code examples are included above for both C# and VB.

## Page-level Navigation/TOC (if applicable)
- None provided in this section.

## Cross References
- None provided in this section.

<!-- tags: [EssentialGrid, WindowsForms, Filters, GridDynamicFilter, GridExcelFilterCell, FilterByDisplayMemberCell, DynamicFilterCell, FilterByDisplayMemberDemo] keywords: [grid, filters, columns, excel-style, ordinary filter, filter by display member, dynamic filter, windows forms] -->
```
