```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_089.jpeg
document_name: Olap Common
page_number: 089
page_id: Olap Common#page_089
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:21:06Z
fidelity: lossless
-->

## Olap Common

### Overview

- **OlapDataManager** and **OlapReport** are used to create and configure Online Analytical Processing (OLAP) reports.
- Demonstrates specifying dimensions and measures for a report, specifically targeting the "Adventure Works" cube.

### Content

#### Creating an OLAP Report

In this example, we create an OLAP report named "Customer Report" that targets the "Adventure Works" cube. We define dimensions and measures to fetch relevant data.

#### Steps to Create the Report

1. **Initialize the OLAP Data Manager:**
   ```csharp
   OlapDataManager OlapDataManager = new OlapDataManager
   (@DataSource=hosts: Initial Catalog=Adventure Works DW;);
   ```

2. **Create a New OLAP Report:**
   ```csharp
   OlapReport olapReport = new OlapReport();
   olapReport.Name = "Customer Report";
   olapReport.CurrentCubeName = "Adventure Works";
   ```

3. **Define Column Members (Dimension Elements):**
   ```csharp
   DimensionElement dimensionElementColumn = new DimensionElement();
   dimensionElementColumn.Name = "Customer";
   dimensionElementColumn.AddLevel("Customer Geography", "Country");
   ```

4. **Define Measure Element:**
   ```csharp
   MeasureElements measureElementColumn = new MeasureElements();
   measureElementColumn.Elements.Add(new MeasureElement
   {
       Name = "Internet Sales Amount"
   });
   ```

5. **Define Row Members (Dimension Elements):**
   ```csharp
   DimensionElement dimensionElementRow = new DimensionElement();
   dimensionElementRow.Name = "Date";
   dimensionElementRow.AddLevel("Fiscal", "Fiscal Year");
   ```

6. **Add Elements to the Report:**
   ```csharp
   ////Adding Column Members
   olapReport.CategoricalElements.Add(dimensionElementColumn);
   ////Adding Measure Element
   olapReport.CategoricalElements.Add(measureElementColumn);
   ////Adding Row Members
   olapReport.SeriesElements.Add(dimensionElementRow);
   ```

#### VB.NET Equivalent

The same functionality can be achieved in VB.NET as shown below:

```vb
Dim OlapDataManager As OlapDataManager = New OlapDataManager
("DataSource=localhost; Initial Catalog=Adventure Works DW")
Dim olapReport1 As OlapReport = New OlapReport()
olapReport1.Name = "Customer Report"
olapReport1.CurrentCubeName = "Adventure Works"
Dim dimensionElementColumn As DimensionElement =
New DimensionElement()
'Specifying the Name for the Dimension Element
dimensionElementColumn.Name = "Customer"
dimensionElementColumn.AddLevel("Customer Geography", "Country")

Dim measureElementColumn As MeasureElements = New MeasureElements()
'Specifying the Name for the Measure Element
measureElementColumn.Elements.Add(New MeasureElement With {.Name = "Internet Sales Amount"})
```

### Summary

This example demonstrates the creation of an OLAP report in both C# and VB.NET. It involves initializing the `OlapDataManager`, configuring the `OlapReport`, and specifying dimension and measure elements to define the report layout. The example targets a specific cube ("Adventure Works") and illustrates how to add categorical elements and series elements to the report.

### .NET References

Ensure the following references are included in your project:
- `Syncfusion.Olap.Windows.Forms.dll`
- `Syncfusion.Olap.DataManager.dll`

### Cross References

- **See also:**  
  - [OlapReport Documentation](https://docs.syncfusion.com/windowsforms/olapreport/getting-started)  
  - [OlapDataManager](https://docs.syncfusion.com/windowsforms/olap/Base/olap-data-manager)

<!-- tags: [Microsoft, C#, VB.NET, OLAP, OLAP Report, Dimension Element, Measure Element, Adventure Works, WinForms, Syncfusion] keywords: [OlapReport, OlapDataManager, DimensionElement, MeasureElements, C#, VB.NET, WinForms] -->
```