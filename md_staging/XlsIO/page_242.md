```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_242.jpeg
document_name: XlsIO
page_number: 242
page_id: XlsIO#page_242
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:03:32Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Demonstrates filtering series and categories in XlsIO.
- Illustrates how to customize and manipulate data visualizations programmatically.

## Content

### Filtering Series and Categories in XlsIO

#### First Chart: XlsIO with First Series and Second Category Filtered

![Figure 79: XlsIO with First Series and Second Category Filtered](figure.png)

- The chart shows sales data for four products (Product-A, Product-B, Product-C, Product-D) across five months (Jan, Mar, Apr, May).
- The **SERIES** section allows filtering specific product data, with options for selecting individual products or grouping all into a single series.
- The **CATEGORIES** section filters months, with checkboxes enabling the selection of individual months or grouping into a single category.
- Key features:
  - **Series Filtering**: The first series (Product-A) is excluded from the displayed data, while the rest are visible.
  - **Category Filtering**: The second category (Mar) is filtered out, showing only Jan, Apr, and May.
  - **Legend**: Reflects the filtered data, showing only the remaining three products.
  - **Dynamic Update**: The chart updates dynamically based on the selected filters.

#### Second Chart: XlsIO Series and Categories Customization

![Figure: XlsIO Series and Categories Customization](figure2.png)

- This chart demonstrates more advanced filtering and customization options.
- **SERIES** section:
  - Allows selection of specific series (Series2, Series3, Series4).
  - The **Row 1** option aggregates all products into a single series, applicable when no individual filter is selected.
- **CATEGORIES** section:
  - Offers filtering by specific months.
  - The **Column A** option aggregates months into a single category when no individual month is selected.
- Key features:
  - **Dynamic Filtering**: Users can apply custom filters to focus on specific series and categories.
  - **Dynamic Update**: The chart dynamically updates to reflect the selected filters.
  - **Legend and Data**: The legend and data are dynamically adjusted to reflect the filtered data.

### Code Examples

```csharp
// Example of applying filters programmatically
using Syncfusion.XlsIO;

// Create a new Excel application instance
ExcelEngine engine = new ExcelEngine();
IApplication application = engine.Excel;

// Open an existing worksheet
IWorkbook workbook = application.Workbooks.Open("SalesData.xlsx");
IWorksheet worksheet = workbook.Worksheets["SalesData"];

// Apply filters
worksheet.Charts[0].Series[0].Visible = false; // Hide Series 1 (Product-A)
worksheet.Charts[0].Categories[1].Visible = false; // Hide Category 2 (March)

// Save the modified workbook
workbook.Save("FilteredSalesData.xlsx");
engine.Dispose();
```

## API Reference

### Methods
- **Workbook.Sheets[worksheetName].Charts[chartIndex].Series[seriesIndex].Visible**
  - Sets the visibility of a specific series in the chart.
  - **Parameters**:
    - `seriesIndex`: The index of the series to modify.
    - `visible`: Boolean value indicating whether the series should be visible (`true`) or hidden (`false`).
- **Workbook.Sheets[worksheetName].Charts[chartIndex].Categories[categoryIndex].Visible**
  - Sets the visibility of a specific category in the chart.
  - **Parameters**:
    - `categoryIndex`: The index of the category to modify.
    - `visible`: Boolean value indicating whether the category should be visible (`true`) or hidden (`false`).

## Page-level Navigation/TOC
- **Figure 79: XlsIO with First Series and Second Category Filtered**
- **Second Chart: XlsIO Series and Categories Customization**
- **API Reference**

## Cross References
- See also: XlsIO Series and Categories Customization Guide, Advanced Filtering Techniques in XlsIO.

<!-- tags: [XlsIO, Syncfusion, Winforms, Excel, Filtering, Charting, Series, Categories] keywords: [filtering, chart, series, categories, customization, XlsIO, Excel, filtering techniques, visible, hidden] -->
```