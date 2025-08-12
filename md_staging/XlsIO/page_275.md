```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_275.jpeg
document_name: XlsIO
page_number: 275
page_id: XlsIO#page_275
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:06:40Z
fidelity: lossless
-->

## Overview
- This section provides a detailed explanation of how to create and configure a pivot table in Excel using XlsIO.
- The process includes selecting data for the pivot table, inserting the pivot table, setting field axes, applying filters, and applying built-in styles.

## Content

### Creating and Configuring a Pivot Table

This example demonstrates how to create a pivot table and customize its fields and filtering options.

1. **Access the worksheet to draw pivot table.**
   ```vb
   Dim pivotSheet As IWorksheet = workbook.Worksheets(1)
   ```

2. **Select the data to add in cache.**
   ```vb
   Dim cache As IPivotCache =
       workbook.PivotCaches.Add(worksheet("A1:H50"))
   ```

3. **Insert the pivot table.**
   ```vb
   Dim pivotTable As IPivotTable =
       pivotSheet.PivotTables.Add("PivotTable1", pivotSheet("A1"), cache)
   ' Set field axis to page.
   pivotTable.Fields(4).Axis = PivotAxisTypes.Page
   ```

4. **Set field axis to row.**
   ```vb
   pivotTable.Fields(2).Axis = PivotAxisTypes.Row
   pivotTable.Fields(6).Axis = PivotAxisTypes.Row
   ```

5. **Set field axis to column.**
   ```vb
   pivotTable.Fields(3).Axis = PivotAxisTypes.Column
   ```

6. **Add data fields with summaries.**
   ```vb
   Dim field As IPivotField = pivotSheet.PivotTables(0).Fields(5)
   pivotTable.DataFields.Add(field, "Sum of Units", PivotSubtotalTypes.Sum)
   ```

7. **Apply page field filter.**
   ```vb
   Dim pageField As IPivotField = pivotTable.Fields(4)
   ' Select multiple items in page field to filter.
   pageField.Items(1).Visible = False
   pageField.Items(2).Visible = False
   ```

8. **Apply built-in style.**
   ```vb
   pivotTable.BuiltInStyle = PivotBuiltInStyles.PivotStyleMedium2
   ```

9. **Activate the pivot worksheet.**

## Cross References

- For more detailed information on pivot tables and their configuration options, refer to the [official XlsIO documentation](https://help.syncfusion.com/xlsio).
- Additional examples and tutorials can be found in the Syncfusion [code gallery](https://www.syncfusion.com/code-gallery).

<!-- tags: [xlsio, pivot_table, filtering, built-in_styles, winforms] keywords: [pivot_table, data_cache, field_axes, page_filter, style] -->
```