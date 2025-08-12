```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_033.jpeg
document_name: PivotGrid
page_number: 033
page_id: PivotGrid#page_033
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:54:17Z
fidelity: lossless
-->

# Essential PivotGrid WindowsForms

## Overview
- Displays the functionality of the PivotGrid control with detailed fields and subtotals.
- Highlights the use of filter fields and subtotals in PivotGrid data presentation.

## Content

### Figures

#### Figure 13: PivotGrid with Subtotals

**Description**: The PivotGrid with subtotals displayed, showing detailed data for various categories like countries, states, and products, along with their amounts and quantities.

| Field         | Data                                                                                          |
|---------------|-----------------------------------------------------------------------------------------------|
| **Country**   | Canada, France, Germany                                                                      |
| **State**     | Charente-Maritime, Essonne, Garonne (Haute), Gers, Bayern                                    |
| **Prod...**   | Bike, Car                                                                                    |
| **FY...**     | FY 2005, FY 2006, FY 2007, FY 2008, FY 2009                                                 |
| **Amount**    | Specific monetary values for each year and category                                         |
| **Quantity**  | Specific quantity values for each year and category                                         |
| **Grand Total** | Consolidated amounts and quantities across all categories and years                         |

#### Figure 14: PivotGrid with Subtotals Hidden

**Description**: The PivotGrid with subtotals hidden, displaying only the overall data without intermediate subtotals for comparison.

| Field         | Data                                                                                          |
|---------------|-----------------------------------------------------------------------------------------------|
| **Country**   | Canada, France                                                                                |
| **State**     | British Columbia, Manitoba, Ontario, Quebec, Charente-Mar                                   |
| **Prod...**   | Bike, Car                                                                                    |
| **FY...**     | FY 2005, FY 2006, FY 2007, FY 2008, FY 2009                                                 |
| **Amount**    | Specific monetary values for each year and category                                         |
| **Quantity**  | Specific quantity values for each year and category                                         |
| **Grand Total** | Consolidated amounts and quantities across all categories and years                         |

### Properties

#### Table 9: Property Table

| Property       | Description                  | Data Type | Reference links |
|----------------|------------------------------|-----------|-----------------|
| ShowSubTotals  | Shows or hides the subtotals | Boolean   | -               |

### Methods

#### Table 10: Method Table

| Method        | Description | Parameters                                         | Return Type | Reference links |
|---------------|-------------|----------------------------------------------------|-------------|-----------------|
| -             | -           | -                                                  | -           | -               |

## API Reference

### Namespace

```csharp
namespace Syncfusion.Windows.Forms.Grid
{
```

### Class

```csharp
    public class PivotGridControl
    {
```

#### Properties

| Property       | Description                  | Data Type | Reference links |
|----------------|------------------------------|-----------|-----------------|
| ShowSubTotals  | Shows or hides the subtotals | Boolean   | -               |

#### Methods

| Method        | Description | Parameters | Return Type | Reference links |
|---------------|-------------|------------|-------------|-----------------|
| AddSubTotal() | Adds a subtotal to the PivotGrid | - | void | - |
| RemoveSubTotal() | Removes a subtotal from the PivotGrid | - | void | - |

## Page-level Navigation/TOC

- Properties
- Methods

## Cross References

- See also: for detailed usage examples of **ShowSubTotals** property, refer to the *API Reference* section.
- Additional pivot grid functionalities and configurations can be explored in the main documentation of Syncfusion PivotGrid.

### RAG Annotations

<!-- 
tags: [pivotgrid, winforms, subtotals, properties, methods, api reference, synfusion winforms]
keywords: [PivotGrid, ShowSubTotals, Filter Fields, Subtotals, Grand Total, Data Representation]
 -->
```