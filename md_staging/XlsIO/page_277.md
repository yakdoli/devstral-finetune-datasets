```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_277.jpeg
document_name: XlsIO
page_number: 277
page_id: XlsIO#page_277
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:06:52Z
fidelity: lossless
-->

## Working with Pivot Table Cache

### Overview
- This section describes the process of creating and configuring a pivot table with data sourced from a pivot cache in a spreadsheet using Syncfusion XlsIO.

### Content

#### Creating a Pivot Table Using a Pivot Cache

The following code snippet demonstrates how to create a pivot table in an Excel spreadsheet by adding a pivot cache and configuring its fields.

```csharp
//Step 1: Instantiate the spreadsheet creation engine.
ExcelEngine excelEngine = new ExcelEngine();
//Step 2: Instantiate the excel application object.
IApplication application = excelEngine.Excel;

//Set the default version as Excel 2010.
application.DefaultVersion = ExcelVersion.Excel2010;

IWorkbook workbook = application.Workbooks.Open("PivotCodeDate.xlsx");

// The first worksheet object in the worksheets collection is accessed.
IWorksheet worksheet = workbook.Worksheets[0];

//Access the worksheet to draw pivot table.
IWorksheet pivotSheet = workbook.Worksheets[1];

//Select the data to add in cache.
IPivotCache cache = workbook.PivotCaches.Add(worksheet["A1:H50"]);

//Insert the pivot table.
IPivotTable pivotTable = pivotSheet.PivotTables.Add("PivotTable1", pivotSheet["A1"], cache);
pivotTable.Fields[4].Axis = PivotAxisTypes.Page;

pivotTable.Fields[2].Axis = PivotAxisTypes.Row;
pivotTable.Fields[6].Axis = PivotAxisTypes.Row;
pivotTable.Fields[3].Axis = PivotAxisTypes.Column;

IPivotField field = pivotSheet.PivotTables[0].Fields[5];
pivotTable.DataFields.Add(field, "Sum of Units", PivotSubtotalTypes.Sum);

//Apply row field filter.
IPivotField rowField = pivotTable.Fields[2];
// Applying Label based row field filter
```

#### Explanation of Code

1. **Instantiating the Spreadsheet Engine**:
   - The `ExcelEngine` class is used to create an instance of the spreadsheet creation engine.
   - The `Excel` property of `ExcelEngine` provides an instance of the Excel application object.

2. **Setting the Default Version**:
   - The `DefaultVersion` property of the `IApplication` object is set to `ExcelVersion.Excel2010` to specify that the application will use the Excel 2010 format.

3. **Opening an Existing Workbook**:
   - The `Open` method is used to open the workbook named `PivotCodeDate.xlsx` for further processing.

4. **Accessing Worksheets**:
   - The first worksheet in the workbook is accessed using `workbook.Worksheets[0]`.
   - A second worksheet is accessed for drawing the pivot table using `workbook.Worksheets[1]`.

5. **Adding a Pivot Cache**:
   - The `PivotCaches.Add` method is used to create a pivot cache based on the data in the range `A1:H50` of the source worksheet.

6. **Creating the Pivot Table**:
   - The `PivotTables.Add` method is used to create a new pivot table named `PivotTable1` starting at cell `A1` on the pivot sheet.
   - The pivot table is associated with the previously created pivot cache.

7. **Configuring Pivot Table Fields**:
   - The `Fields` property of the pivot table is used to configure the axes for the pivot table:
     - Fields are assigned to the `Page`, `Row`, and `Column` axes of the pivot table.

8. **Adding Data Fields**:
   - A data field named "Sum of Units" is added to the pivot table using the `DataFields.Add` method.
   - The subtotal type for this data field is set to `PivotSubtotalTypes.Sum`.

9. **Applying Row Field Filter**:
   - A filter is applied to the row field to refine the data displayed in the pivot table based on specific labels.

This example demonstrates the complete process of creating and configuring a pivot table using pivot cache to manage and display data effectively.

#### Cross References
- Refer to the **pivot cache** section for more details on managing data in pivot tables.
- For advanced configuration options, see the **pivot table formatting** section.

### API Reference

#### Namespaces and Classes
- **Syncfusion.XlsIO**: Provides classes and methods for creating and manipulating Excel spreadsheets.
  - **ExcelEngine**: Core class for creating and managing Excel documents.
  - **IApplication**: Represents an instance of the Excel application.
  - **IWorkbook**: Represents a workbook in the Excel document.
  - **IWorksheet**: Represents a worksheet in the workbook.
  - **IPivotCache**: Represents a pivot cache used to store data for pivot tables.
  - **IPivotTable**: Represents a pivot table in the worksheet.
  - **IPivotField**: Represents a field in a pivot table.

#### Methods
- **ExcelEngine.Excel**: Provides an instance of the Excel application object.
- **IApplication.DefaultVersion**: Sets the default version of the Excel document.
- **IWorkbook.Open**: Opens an existing Excel workbook.
- **IWorkbook.Worksheets**: Collection of worksheets in the workbook.
- **IPivotCaches.Add**: Adds a new pivot cache based on a specified range of data.
- **IPivotTables.Add**: Adds a new pivot table to the worksheet.
- ** PivotTable.Fields**: Collection of fields in the pivot table.
- ** PivotTable.DataFields.Add**: Adds a new data field to the pivot table.

### Code Examples

#### Creating a Pivot Table with Customized Field Axes

This example demonstrates how to create a pivot table with customized field axes, adding a data field, and applying a filter.

```csharp
// Creating the pivot table
IPivotTable pivotTable = pivotSheet.PivotTables.Add("PivotTable1", pivotSheet["A1"], cache);

// Configuring the axes
pivotTable.Fields[4].Axis = PivotAxisTypes.Page; // Assigning to page axis
pivotTable.Fields[2].Axis = PivotAxisTypes.Row;  // Assigning to row axis
pivotTable.Fields[3].Axis = PivotAxisTypes.Column; // Assigning to column axis

// Adding a data field
IPivotField field = pivotSheet.PivotTables[0].Fields[5];
pivotTable.DataFields.Add(field, "Sum of Units", PivotSubtotalTypes.Sum);

// Applying a row field filter
IPivotField rowField = pivotTable.Fields[2];
```

### Tags and Keywords
<!-- tags: [pivot table, pivot cache, spreadsheet, data fields, pivot fields, Excel, Syncfusion, XlsIO] keywords: [pivot table, pivot cache, worksheet, data field, row axis, column axis, sum of units, filter, Excel 2010] -->
```
