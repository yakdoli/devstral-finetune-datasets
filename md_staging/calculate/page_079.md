```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_079.jpeg
document_name: calculate
page_number: 079
page_id: calculate#page_079
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:03:11Z
fidelity: lossless
-->

# Essential Calculate

## DataGrid with Calculation Support

The following figure illustrates the DataGrid with calculation support:

**Figure 34: Data Grid**

You can copy the code that defines the derived DataGrid object to your projects and have immediate support for calculations in a Data Grid using Data Table data sources. Before we begin with the details of this sample and the derived DataGrid class, we will discuss the ICalcData interface describing the purpose of its implementation details.

## 4.1.2.2.1 Using CalcDataGrid as a Single Spreadsheet

### Overview
- Demonstrates the usage of CalcDataGrid to support calculations in a Data Grid.
- Explains how to integrate CalcDataGrid with a User Control to perform calculations.

### Using CalcDataGrid as a Single Spreadsheet
Essential Calculate provides a derived DataGrid object that implements ICalcData to support calculations. But you need to know how to use such an object on a User Control. Essentially, you can drop an instance of the CalcDataGrid object onto your form, create an instance of CalcEngine by using your CalcDataGrid as its ICalcData object, and then calculate things so that the initial display shows the calculated values. The following code illustrates this.

### Code Example

```csharp
private Syncfusion.Calculate.CalcEngine engine;
private DataTable dt;
```

### Summary
- The derived DataGrid object supports calculations using Data Table data sources.
- Integration with User Controls is demonstrated.
- The code shows how to initialize the CalcEngine using CalcDataGrid.

## API Reference

### Class: CalcDataGrid
- **Namespace:** Syncfusion.Windows.Forms.Grid

### Methods
- **Calculate()**
  - Purpose: Performs calculations based on the formulas in the Data Grid.
  - Returns: bool indicating success or failure.

### Events
- **CalculationFailed**
  - Triggered when a calculation fails.
  - Parameters: object sender, CalculationFailedEventArgs e

### Properties
- **DataSource**
  - Type: object
  - Description: Gets or sets the data source for the Data Grid.
  - Default: null

## Code Examples

### Example: Integrating CalcDataGrid with a User Control

```csharp
// Initialize CalcDataGrid
CalcDataGrid grid = new CalcDataGrid();
grid.DataSource = dt;

// Initialize CalcEngine
CalcEngine engine = new CalcEngine();
engine.ICalcData = grid;

// Perform calculations
engine.Calculate();
```

## See also
- [DataGrid with Calculation Support](#)
- [Syncfusion Winforms Documentation](#)
- [CalcEngine API Reference](#)

<!-- tags: [syncfusion, data grid, calculation support, user control, calcengine, api, version:11.4.0.26] keywords: [data grid, calculation, calcdata, user control, calcengine, syncfusion] -->
```