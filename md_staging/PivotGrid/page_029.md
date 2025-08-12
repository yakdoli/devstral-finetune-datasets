```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_029.jpeg
document_name: PivotGrid
page_number: 029
page_id: PivotGrid#page_029
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:54:05Z
fidelity: lossless
-->

# Essential PivotGrid WindowsForms

## Overview
- Explains how to disable filtering using the Grouping Bar.
- Demonstrates the sorting indicator functionality in the PivotGrid.
- Provides code examples in C# and VB for disabling filtering in the PivotGrid.

## Content

### Filtering in the Grouping Bar

#### Figure 10: Filter Popup
![Figure 10: Filter Popup](https://example.com/filter_popup.png)

The following code example illustrates how to disable the filtering in the Grouping Bar.

#### C#
```csharp
// Disabling Filtering
pivotGridControl1.AllowFiltering = false;
```

#### VB
```vb
// Disabling Filtering
pivotGridControl1.AllowFiltering = False
```

#### 4.6.2 Sorting Indicator
The sort indicator in the item represents the sort type such as ascending order or descending order. By default, the PivotGrid will populate the data in ascending order. The sorting order can be changed by clicking on the item present in the row header area and column header area.

The following image illustrates the sort indicator with sort types:

#### Figure 11: Sort Indicator
![Figure 11: Sort Indicator](https://example.com/sort_indicator.png)

## Page-Level Navigation/TOC (if applicable)
- [4.6.2 Sorting Indicator](#4.6.2-Sorting-Indicator)

## Cross References
- Refer to the user guide for more information on PivotGrid features and functionalities.

<!-- tags: [PivotGrid, WinForms, filtering, sorting, indicator, Grouping Bar] keywords: [Disable Filtering, PivotGrid, Sorting Indicator, Ascending Order, Descending Order, Grouping Bar, Filter Popup, C#, VB] -->
```