---
title: "PivotGrid - Syncfusion SDK Documentation"
type: "api-documentation"
framework: "syncfusion"
version: "v11"
processing_mode: "Process Isolation (프로세스 격리)"
extracted_date: "1754726158.643018"
optimized_for: ["llm-training", "rag-retrieval"]
scaling_approach: "3"
---

<!-- 페이지 1 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_001.jpeg
document_name: PivotGrid
page_number: 001
page_id: PivotGrid#page_001
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:52:37Z
fidelity: lossless
-->

# Essential Studio 2013 Volume 4 - v.11.4.0.26

## Overview
- A technical documentation for Syncfusion's PivotGrid WindowsForms control.
- Provides comprehensive information on using the PivotGrid control for Windows Forms applications.
- Focuses on delivering innovation in pivot grid functionalities for developers.

## Content

### Key Features
- Robust data handling capabilities
- Advanced data manipulation options
- Customizable appearance and user experience
- Integration with various data sources

### Installation and Setup
- Step-by-step guide to installing the PivotGrid control
- Dependencies and requirements for Windows Forms applications
- Configuration options for optimal performance

### Usage Examples
- Code samples demonstrating common use cases
- Demonstrations of advanced functionalities
- Instructions on integrating PivotGrid into existing applications

### API Reference
Detailed documentation on the PivotGrid API:
- Namespace: Syncfusion.Windows.Forms.PivotGrid
- Classes: PivotGridControl, PivotGridRenderer, PivotGridModel
- Methods: BindData(), Refresh(), SetStyle()
- Properties: ColumnWidth, RowHeight, CellStyle

### Code Examples

```csharp
// Example of binding data to PivotGrid
using Syncfusion.Windows.Forms.PivotGrid;

public void BindDataSource()
{
    PivotGridControl pivotGrid = new PivotGridControl();
    pivotGrid.DataSource = new MyDataSource();
    pivotGrid.DataBind();
}
```

### Troubleshooting and Best Practices
- Common issues and solutions
- Performance optimization tips
- Debugging and error handling strategies

## RAG Annotations
<!-- tags: [PivotGrid, WindowsForms, Syncfusion, v.11.4.0.26] keywords: [PivotGridControl, WindowsForms, data handling, advanced features, code examples, API, troubleshooting] -->
```

---

<!-- 페이지 2 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_005.jpeg
document_name: PivotGrid
page_number: 005
page_id: PivotGrid#page_005
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:52:49Z
fidelity: lossless
-->

# Essential PivotGrid WindowsForms

## Overview
- **Overview** - This section gives a brief introduction to our product and its key features.
- **Deployment** - This section elaborates on the install location of the samples, license, and so on.
- **Getting Started** - This section guides you on getting started with a BI application, PivotGrid control, and so on.
- **Concepts and Features** - This section includes features of the PivotGrid control, which are illustrated with use-case scenarios, code examples, and screenshots.

## Document Conventions
The following conventions will help you quickly identify the important sections of information while using the content.

### Table 1: Conventions Table

| Convention             | Icon              | Description                                                                 |
|------------------------|-------------------|-----------------------------------------------------------------------------|
| Note                   | 📝 Note:         | Represents important information.                                      |
| Example                | Example           | Represents an example.                                                 |
| Tip                    | 💡                | Represents useful hints that will help you in using the controls/features. |
| Additional Information | ⓘ                | Represents additional information on the topic.                         |

### 1.2 IT Scenarios
The Essential PivotGrid for Windows Forms finds its main application in the financial domain, where it is used to organize and analyze business data.

### 1.3 Prerequisites and Compatibility
This section covers the requirements mandatory for using the PivotGrid control. It also lists operating systems and browsers compatible with the product.

#### Prerequisites
The prerequisites details are listed below:

### Table 2: Prerequisites Table

| Development Environments | • Visual Studio 2012<br>• Visual Studio 2010<br>• Visual Studio 2008 |
|--------------------------|-------------------------------------------------------------------------|

```markdown
<!-- tags: [syncfusion, winforms, pivotgrid, prerequisites, deployment, it scenarios, features] keywords: [BI application, use-case scenarios, code examples, screenshots, visual studio versions, financial domain, technical documentation] -->
```

---

<!-- 페이지 3 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_009.jpeg
document_name: PivotGrid
page_number: 009
page_id: PivotGrid#page_009
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:53:03Z
fidelity: lossless
-->

## Essential PivotGrid Windows Forms

### Overview
- Explore the Business Intelligence Edition of Essential Studio for Windows Forms applications.
- Utilize PivotGrid samples for analyzing cross-tabulated data.

### Content
#### Dashboard BI
- **Figure 2: Syncfusion Essential Studio Dashboard BI**
  ![Figure 2: Syncfusion Essential Studio Dashboard BI](./image.png)
  
**Instructions:**
1. In the Dashboard window, click **Run Samples** for Windows Forms under **BI Edition**.
  
**Note:** You can view the samples in any of the following three ways:
- **Run Samples** - Click to view the locally installed samples.
- **Online Samples** - Click to view online samples.
- **Explore Samples** - Explore UI Windows Forms on disk.

2. Click **PivotGrid**. The Pivot Grid samples are displayed.

```html
<!-- tags: [pivotgrid, dashboard, windowsforms, essentialstudio, runsamples, onlinesamples, exploresamples] keywords: [pivotgrid, windowsforms, dashboard, essential studio, business intelligence] -->
```

---

<!-- 페이지 4 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_013.jpeg
document_name: PivotGrid
page_number: 013
page_id: PivotGrid#page_013
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:53:12Z
fidelity: lossless
-->

## Essential PivotGrid WindowsForms

### Overview

- Explains the process of populating data to PivotGrid in Windows Forms environment.
- Demonstrates how to configure PivotGrid with data sources and calculations using C#.

## Content

### 3.2 Populating Data to PivotGrid

The PivotGrid requires the following information in order to populate data:

- **ItemSource** - The data source for the pivot table. This object should be either an IEnumerable list or a DataTable.
- **PivotRows** - Elements that need to be added in PivotGrid rows.
- **PivotColumns** - Elements that need to be added in PivotGrid columns.
- **PivotCalculations** - Calculation values that appear as value cells in PivotGrid.

To populate a PivotGrid with the sample IList data, refer to the code below.

#### Code Example

```csharp
protected void Form1_Load(object sender, System.EventArgs e)
{
    // Code to populate PivotGrid with sample IList data would go here.
}
```

## Page-level Navigation/TOC

- [Essential PivotGrid WindowsForms](#essential-pivotgrid-windowsforms)

## Cross References

- See also: [如何在 Windows Forms 中配置 PivotGrid](#如何在-windows-forms-中配置-pivotgrid)

### RAG Annotations

<!-- tags: [PivotGrid, WindowsForms, DataSources, Calculations, SyncfusionWinforms, 11.4.0.26] keywords: [PivotGrid, ItemSource, PivotRows, PivotColumns, PivotCalculations, Windows Forms, C#] -->
```

---

<!-- 페이지 5 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_017.jpeg
document_name: PivotGrid
page_number: 017
page_id: PivotGrid#page_017
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:53:23Z
fidelity: lossless
-->

# Essential PivotGrid WindowsForms

## Concepts and Features

### 4.1 PivotItem

PivotItem is an item in a PivotTable field. It provides the information needed to define a pivot item for either a row or column. It consists of the following fields.

#### Table 5: Properties Table for PivotItem

| Property Name | Description | Type | Value it Accepts | Reference link |
|---------------|-------------|------|------------------|----------------|
| Comparer      | Gets or sets the IComparer object used for sorting. If this value is null, then sorting will be performed under the assumption that this field is IComparable. | IComparer | - | - |
| FieldHeader   | Gets or sets the title you want to see in the header for this pivot item. | string | - | - |
| FieldMappingName | Gets or sets the property's mapping name. | string | - | - |
| Format | Gets or sets the format item for the specified field. | string | - | - |
| TotalHeader | Gets or sets the string you want to append to the pivot item's summary cells. | string | - | - |

#### 4.1.1 Defining PivotItem in Code-Behind

The PivotItem can be defined in code-behind. The following code example illustrates this.

```csharp
<!-- code example would go here -->
```
<!-- tags: [winforms, pivotgrid, pivotitem, code-behind, syncfusion, windowsforms, pivottable, fieldheader, fieldmappingname, format, totalheader] keywords: [pivotitem, code-behind, pivotgrid, pivottable, fieldmappingname, format, totalheader, fieldheader] -->
```

---

<!-- 페이지 6 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_021.jpeg
document_name: PivotGrid
page_number: 021
page_id: PivotGrid#page_021
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:53:36Z
fidelity: lossless
-->

## Understanding SummaryType and Summary Properties

### Overview
- The SummaryType and Summary properties are crucial for defining calculation types in PivotGrid.
- SummaryType allows selection from predefined calculation options such as Sum, Average, etc., and can also be customized.
- Summary is automatically set for non-custom SummaryType values, requiring a custom SummaryBase-derived object for Custom.

### Detailed Description

| Property         | Description                                                                                                                                                                                                                                                                                                                                 | Enumerations                                                    | Value        |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|--------------|
| SummaryType      | Gets or sets the SummaryType enumeration for this calculation. Setting it to any value other than Custom will also properly set Summary.                                                                                                                                                                      | DoubleTotal Sum<br>DoubleAverage<br>DoubleMaximum<br>DoubleMinimum<br>DoubleStandardDeviation<br>DoubleVariance<br>Count<br>DecimalTotalSum<br>IntTotalSum<br>Custom | -          |
| Summary          | The Summary property is used to perform specific calculations. This value is automatically set when you specify any non-custom value of SummaryType; if you specify SummaryType.Custom, then you are required to set Summary to be an instance of your custom SummaryBase-derived object. |

## Defining PivotComputationInfo and Code-Behind

### Overview
- The PivotComputationInfo can be defined in C# or VB code.

### 4.2.1 Defining PivotComputationInfo and Code-Behind

#### The PivotComputationInfo can be defined in C# or VB code.

##### C#
```csharp
// Defining PivotComputationInfo
PivotComputationInfo m_PivotComputationInfo = new PivotComputationInfo() { CalculationName="Amount", FieldName="Amount", };
```

### API Reference

#### Naming Properties
- **CalculationName**: Specifies the calculation name to be displayed in the PivotGrid. Example value: "Amount".
- **FieldName**: Specifies the field name to be used in the calculation. Example value: "Amount".

### Code Examples (C#)

```csharp
// Example: Defining a PivotComputationInfo
PivotComputationInfo m_PivotComputationInfo = new PivotComputationInfo() {
    CalculationName = "Amount",
    FieldName = "Amount"
};
```

<!-- tags: [PivotGrid, SummaryType, Summary, PivotComputationInfo, WinForms] keywords: [SummaryType, Summary, Calculation, Custom, DoubleTotalSum, DoubleAverage, DoubleMaximum, DoubleMinimum, DoubleStandardDeviation, DoubleVariance, Count, DecimalTotalSum, IntTotalSum, Custom] -->
```

---

<!-- 페이지 7 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_025.jpeg
document_name: PivotGrid
page_number: 025
page_id: PivotGrid#page_025
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:53:51Z
fidelity: lossless
-->

# Essential PivotGrid WindowsForms

```vb
#endregion
}
```

### Adding Pivot Rows to Grid with FieldMappingName, TotalHeader and Comparer

```vb
[VB]
' Adding Pivot Rows to Grid with FieldMappingName, TotalHeader and Comparer
Me.PivotGridControl1.PivotRows.Add(New PivotItem With
{.FieldMappingName = "Product", .TotalHeader = "Total", .Comparer = New ReverseOrderComparer()})
'''

''' <summary>
''' Reverse Order Comparer for sorting data in Descending order
''' </summary>
public class ReverseOrderComparer : IComparer
'    #Region "IComparer Members"

    public Integer Compare(Object x, Object y)
        If x Is Nothing AndAlso y Is Nothing Then
            Return 0
        ElseIf y Is Nothing Then
            Return 1
        ElseIf x Is Nothing Then
            Return -1
        Else
            Return -x.ToString().CompareTo(y.ToString())
        End If
'
'    #End Region
```

## API Reference
- **Class**: ReverseOrderComparer
  - Implements: IComparer
  - **Method**:
    - **Compare(Object x, Object y)**:
      - **Parameters**:
        - `x`: Object
        - `y`: Object
      - **Return**: Integer
      - **Description**: Compare method for sorting data in descending order.

## Code Examples

### VB.NET Example

```vb
' Adding Pivot Rows with Custom Comparer
Me.PivotGridControl1.PivotRows.Add(New PivotItem With
{.FieldMappingName = "Product", .TotalHeader = "Total", .Comparer = New ReverseOrderComparer()})
```

### ReverseOrderComparer Class

```vb
public class ReverseOrderComparer : IComparer
    ' Implementation of Compare method
    public Integer Compare(Object x, Object y)
        If x Is Nothing AndAlso y Is Nothing Then
            Return 0
        ElseIf y Is Nothing Then
            Return 1
        ElseIf x Is Nothing Then
            Return -1
        Else
            Return -x.ToString().CompareTo(y.ToString())
        End If
```

<!-- tags: PivotGrid, WindowsForms, Fields, Mapping, TotalHeader, Comparer keywords: PivotGrid, WindowsForms, ReverseOrderComparer, TotalHeader, FieldMappingName, IComparer, Compare -->
```

---

<!-- 페이지 8 -->

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

---

<!-- 페이지 9 -->

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

---

<!-- 페이지 10 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_037.jpeg
document_name: PivotGrid
page_number: 037
page_id: PivotGrid#page_037
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:54:40Z
fidelity: lossless
-->

# Essential PivotGrid WindowsForms

```csharp
PivotWordExport wordExport = new PivotWordExport();
wordExport.pivotGridToWord(savedialog.FileName, pivotGridControl1);
```

```vb
Dim wordExport As New PivotWordExport()
wordExport.pivotGridToWord(savedialog.FileName, pivotGridControl1)
```

Merging is applied to all the cells and the exported file is as same as that of the original PivotGrid. The formatting is applied based on the visual styles of the grid.

The below image depicts the conversion of PivotGrid content to a Word file:

|             | Canada                                                                                                     |                                                                                                                       |
|-------------|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
|             | Alberta                                                                                                    |                                                                                                                       |
|             | 1                                                                                                         | 10                                                                                                                    |
|             | Quantity                                      | Year                                                                                   | Quantity                                                  | Year                |
| Bike        | FY 2005                                       | 25                                                                                   | 25                                                         | 28                  |
|             | FY 2006                                       | 9                                                                                    | 9                                                          | 11                  |
|             | FY 2007                                       | 4                                                                                    | 4                                                          | 4                   |
| Bike Total  | 38                                            | 38                                                                                   | 43                                                         | 43                  |
| Car         | FY 2005                                       | 6                                                                                    | 6                                                          | 4                   |
|             | FY 2006                                       | 1                                                                                    | 1                                                          | 1                   |
|             | FY 2007                                       | 1                                                                                    | 1                                                          | 2                   |
| Car Total   | 8                                             | 8                                                                                    | 7                                                          | 7                   |
| Grand Total | 46                                            | 46                                                                                   | 50                                                         | 50                  |

## Exporting to PDF:

Essential Grid control supports conversion of PivotGrid content to a PDF file. Data in the PivotGrid control can be converted to a PDF document for offline verification and/or computation. This can be achieved by making use of the `PivotPdfExport` class. The PDF libraries are used to support the conversion of PivotGrid content to a PDF page.

While exporting to PDF, PivotGrid is read row by row and exported into the PDF document.

The `Export` method is used to export PivotGrid content to a PDF file. The following sample code illustrates how to convert the PivotGrid content to PDF.

```csharp
PivotPdfExport pdfExport = new PivotPdfExport(pivotGridControl1);
pdfExport.Export(savedialog.FileName);
```

<!-- tags: [syncfusion, winforms, pivotgrid, pdf export, word export, essential grid, pdf, offline verification, data export, version 11.4.0.26, word document, merging, formatting, visual styles, sample code] -->
```

---

<!-- 페이지 11 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_041.jpeg
document_name: PivotGrid
page_number: 041
page_id: PivotGrid#page_041
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:54:57Z
fidelity: lossless
-->

# Essential PivotGrid Windows Forms

## Index

### Overview
- **1 Overview** 4
  - **1.1 Introduction to Essential PivotGrid Windows Forms** 4
  - **1.2 IT Scenarios** 5
  - **1.3 Prerequisites and Compatibility** 5
  - **1.4 Documentation** 6

### Installation and Deployment
- **2 Installation and Deployment** 8
  - **2.1 Installation** 8
  - **2.2 Samples and Location** 8
  - **2.3 Deployment Requirements** 10
  - **2.4 Properties Table for PivotGrid** 11

### Getting Started
- **3 Getting Started** 12
  - **3.1 Creating PivotGrid through Visual Studio** 12
  - **3.2 Populating Data to PivotGrid** 13
  - **3.3 Class Diagram** 16

### Concepts and Features
- **4 Concepts and Features** 17
  - **4.1 PivotItem** 17
    - **4.1.1 Defining PivotItem in Code-Behind** 17
    - **4.1.2 Sorting Using PivotItem** 18
  - **4.10 Print Option** 38
  - **4.2 PivotComputationInfo** 20
    - **4.2.1 Defining PivotComputationInfo and Code-Behind** 21
    - **4.2.2 Format String in PivotComputationInfo** 22
  - **4.3 SummaryType** 23
  - **4.4 Sorting** 24
  - **4.5 Freezing Headers** 26
  - **4.6 Grouping Bar** 26
    - **4.6.1 Filtering in Grouping Bar** 28
    - **4.6.2 Sorting Indicator** 29
  - **4.7 Cell Selection** 30
  - **4.8 Subtotal Hiding** 32
    - **4.8.1 Showing or Hiding Subtotals in PivotGrid** 34
  - **4.9 Exporting Pivot Grid to Excel, Word, and PDF** 35

## Page-level Navigation/TOC (if applicable)
- The page contains a hierarchical index for essential features and topics related to the PivotGrid control in Syncfusion's WinForms library. It covers installation, deployment, getting started, and various concepts and features of the PivotGrid, including sorting, filtering, and exporting functionalities.

### Cross References
- **See also:**
  - Code-Behind implementation
  - Data population in PivotGrid
  - Freezing headers
  - Subtotal showing/hiding

<!-- tags: csharp, syncfusion, winforms, pivotgrid, exporting, filtering, sorting, subtotal hiding, documentation, tutorial -->
```

---

<!-- 페이지 12 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_002.jpeg
document_name: PivotGrid
page_number: 002
page_id: PivotGrid#page_002
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:52:37Z
fidelity: lossless
-->

# Contents

## 1 Overview
1.1 Introduction to Essential PivotGrid Windows Forms
1.2 IT Scenarios
1.3 Prerequisites and Compatibility
1.4 Documentation

## 2 Installation and Deployment
2.1 Installation
2.2 Samples and Location
2.3 Deployment Requirements
2.4 Properties Table for PivotGrid

## 3 Getting Started
3.1 Creating PivotGrid through Visual Studio
3.2 Populating Data to PivotGrid
3.3 Class Diagram

## 4 Concepts and Features
4.1 PivotItem
4.1.1 Defining PivotItem in Code-Behind
4.1.2 Sorting Using PivotItem
4.2 PivotComputationInfo
4.2.1 Defining PivotComputationInfo and Code-Behind
4.2.2 Format String in PivotComputationInfo
4.3 SummaryType
4.4 Sorting
4.5 Freezing Headers
4.6 Grouping Bar
4.6.1 Filtering in Grouping Bar
4.6.2 Sorting Indicator
4.7 Cell Selection
4.8 Subtotal Hiding
4.8.1 Showing or Hiding Subtotals in PivotGrid

## Additional Information
© 2013 Syncfusion. All rights reserved.
```

<!-- tags: [PivotGrid, Windows Forms, Installation, Deployment, Getting Started, Concepts, Features, Syncfusion Winforms, version: 11.4.0.26] keywords: [Essential PivotGrid, IT Scenarios, Prerequisites, Compatibility, Documentation, Installation, Samples, Deployment Requirements, Properties Table, PivotGrid, Visual Studio, Data Population, Class Diagram, PivotItem, PivotComputationInfo, SummaryType, Sorting, Freezing Headers, Grouping Bar, Filtering, Sorting Indicator, Cell Selection, Subtotal Hiding, Showing or Hiding Subtotals] -->

---

<!-- 페이지 13 -->

```markdown
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_006.jpeg
document_name: PivotGrid
page_number: 006
page_id: PivotGrid#page_006
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:52:50Z
fidelity: lossless
-->

# Essential PivotGrid Windows Forms

| .NET Framework Versions | .NET 4.5 RTM<br>.NET 4.0<br>.NET 3.5 SP1 |
|---|---|

## Compatibility

The compatibility details are listed below:

### Table 3: Compatibility Table

| Operating Systems | - Windows 8 (32 bit and 64 bit)<br>- Windows Server 2008 (32 bit and 64 bit)<br>- Windows Server 2003 (32 bit and 64 bit)<br>- Windows 7 (32 bit and 64 bit)<br>- Windows Vista (32 bit and 64 bit)<br>- Windows XP |
|---|---|

## 1.4 Documentation

Syncfusion provides the following documentation sections to provide all the necessary information pertaining to the PivotGrid control.

### Documentation Locations

| Type of Documentation | Location |
|---|---|
| Read Me | `[drive:]\Program Files\Syncfusion\Essential Studio\<version number>\Infrastructure\Read Me\BI_Windows.html` |
| Release Notes | `[drive:]\Program Files\Syncfusion\Essential Studio\<version number>\Infrastructure\Release Notes\BI.html` |
| User Guide (this document) | **Online**<br>`http://help.syncfusion.com/resources` (Navigate to the Pivot Analyses for Windows Forms User Guide.)<br>Note: Click Download as PDF to access a PDF version.<br>**Installed Documentation**<br>Dashboard -> Documentation -> Installed Documentation. |
| Class Reference | **Online**<br>`http://help.syncfusion.com/resources` (Navigate to the Windows Forms User Guide. Select Pivot Grid, and then click the Class Reference link found in the upper right section of the page.) |

---

<!-- tags: [Syncfusion Winforms, PivotGrid, Documentation, Compatibility, User Guide, Class Reference, Version 11.4.0.26] keywords: [Essential PivotGrid Windows Forms, .NET Framework Versions, Operating Systems, Read Me, Release Notes, User Guide, Class Reference, Version] -->
```

---

<!-- 페이지 14 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_010.jpeg
document_name: PivotGrid
page_number: 010
page_id: PivotGrid#page_010
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:53:03Z
fidelity: lossless
-->

# Essential PivotGrid Windows Forms

## Overview
- Demonstrates the features of Syncfusion Essential PivotGrid.
- Explains how to extract and summarize data from large lists.
- Highlights applications in the financial domain for organizing and analyzing business data.

## Content

### Featured Samples

**Figure 3: PivotGrid samples**

The PivotGrid samples showcase various features and functionalities:

- **Tool Tip Demo**: Displays tooltips for additional information.
- **Visual Style Demo**: Demonstrates the customization of visual styles.
- **GroupingBar Demo**: Illustrates the use of GroupingBar for filtering and grouping.
- **PivotGridDemo**: Provides a comprehensive example of PivotGrid usage.
- **Cell Selection Demo**: Shows how to select and highlight cells.
- **HyperlinkCell Demo**: Demonstrates linking cells.
- **New Samples**: Introduces additional sample demonstrations.

#### Instructions
4. Select any sample and browse through the features.

### Source Code Location

The default location of the PivotGrid source code is:

```
[System Drive]\Program Files\Syncfusion\Essential Studio\[Version Number]\BL\PivotGrid\Src
```

### Deployment Requirements

The following assemblies need to be referenced in your application to use Essential PivotGrid for WF:

- Syncfusion.Core
- Syncfusion.Grid.Base
- Syncfusion.Grid.Windows
- Syncfusion.Shared.Base
- Syncfusion.Linq.Base
- Syncfusion.Shared.Windows
- Syncfusion.PivotAnalysis.Base
- Syncfusion.PivotAnalysis.Windows

## API Reference

Not explicitly detailed in this section of documentation. However, the required assemblies and their roles are listed above for integration purposes.

## Code Examples

No specific code examples are provided in this section. For detailed implementation examples, refer to the referenced samples and documentation.

## Cross References
- **See also:** Essential PivotGrid documentation, Windows Forms examples, and Syncfusion support for additional details and deeper insights.

<!-- tags: [Essential PivotGrid, Windows Forms, Syncfusion SDK, Deployment, Samples, Version 11.4.0.26] keywords: [PivotGrid, GroupingBar, Visual Style, Tool Tip, Cell Selection, HyperlinkCell, Source Code Location, Assembly References, Deployment Requirements] -->
```

---

<!-- 페이지 15 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_014.jpeg
document_name: PivotGrid
page_number: 014
page_id: PivotGrid#page_014
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:53:17Z
fidelity: lossless
-->

# Essential PivotGrid WindowsForms

```csharp
{
    // Specifying the ItemSource for Pivot Grid
    this.PivotGridControl.ItemsSource = ProductSales.GetSalesData();

    // Adding Pivot Rows to Grid
    this.PivotGridControl.PivotRows.Add(new PivotItem { FieldMappingName = "Product", TotalHeader = "Total" });
    this.PivotGridControl.PivotRows.Add(new PivotItem { FieldMappingName = "Year", TotalHeader = "Total" });

    // Adding Pivot Columns to Grid
    this.PivotGridControl.PivotColumns.Add(new PivotItem { FieldMappingName = "Country", TotalHeader = "Total" });
    this.PivotGridControl.PivotColumns.Add(new PivotItem { FieldMappingName = "State", TotalHeader = "Total" });

    // Adding Pivot Calculations to Grid
    this.PivotGridControl.PivotCalculations.Add(new PivotComputationInfo { FieldName = "Amount", Format = "C", SummaryType = SummaryType.DoubleTotalSum });
    this.PivotGridControl.PivotCalculations.Add(new PivotComputationInfo { FieldName = "Quantity", Format = "#,#0" });
}
```

### [VB]

```vb
Protected Sub Form1_Load(ByVal sender As Object, ByVal e As System.EventArgs)
    ' Specifying the ItemSource for Pivot Grid
    Me.PivotGridControl1.ItemSource = ProductSales.GetSalesData()

    ' Adding Pivot Rows to Grid
    Me.PivotGridControl1.PivotRows.Add(New PivotItem With {.FieldMappingName = "Product", .TotalHeader = "Total"})
    Me.PivotGridControl1.PivotRows.Add(New PivotItem With {.FieldMappingName = "Year", .TotalHeader = "Total"})

    ' Adding Pivot Columns to Grid
    Me.PivotGridControl1.PivotColumns.Add(New PivotItem
```

## API Reference

- **Namespace**: Syncfusion.Windows.Forms.PivotGrid
- **Class**: PivotGridControl
  - **Properties**:
    - `ItemSource`: Specifies the data source for the Pivot Grid.
    - `PivotRows`: Collection of `PivotItem` for rows.
    - `PivotColumns`: Collection of `PivotItem` for columns.
    - `PivotCalculations`: Collection of `PivotComputationInfo` for calculations.
  - **Methods**:
    - `Add(PivotItem)`: Adds a pivot item to the collection.
    - `GetSalesData()`: Retrieves sales data.

## Code Examples

### C#

```csharp
this.PivotGridControl.ItemsSource = ProductSales.GetSalesData();
this.PivotGridControl.PivotRows.Add(new PivotItem { FieldMappingName = "Product", TotalHeader = "Total" });
this.PivotGridControl.PivotRows.Add(new PivotItem { FieldMappingName = "Year", TotalHeader = "Total" });
this.PivotGridControl.PivotColumns.Add(new PivotItem { FieldMappingName = "Country", TotalHeader = "Total" });
this.PivotGridControl.PivotColumns.Add(new PivotItem { FieldMappingName = "State", TotalHeader = "Total" });
this.PivotGridControl.PivotCalculations.Add(new PivotComputationInfo { FieldName = "Amount", Format = "C", SummaryType = SummaryType.DoubleTotalSum });
this.PivotGridControl.PivotCalculations.Add(new PivotComputationInfo { FieldName = "Quantity", Format = "#,#0" });
```

### VB

```vb
Me.PivotGridControl1.ItemSource = ProductSales.GetSalesData()
Me.PivotGridControl1.PivotRows.Add(New PivotItem With {.FieldMappingName = "Product", .TotalHeader = "Total"})
Me.PivotGridControl1.PivotRows.Add(New PivotItem With {.FieldMappingName = "Year", .TotalHeader = "Total"})
Me.PivotGridControl1.PivotColumns.Add(New PivotItem With {.FieldMappingName = "Country", .TotalHeader = "Total"})
Me.PivotGridControl1.PivotColumns.Add(New PivotItem With {.FieldMappingName = "State", .TotalHeader = "Total"})
Me.PivotGridControl1.PivotCalculations.Add(New PivotComputationInfo With {.FieldName = "Amount", .Format = "C", .SummaryType = SummaryType.DoubleTotalSum})
Me.PivotGridControl1.PivotCalculations.Add(New PivotComputationInfo With {.FieldName = "Quantity", .Format = "#,#0"})
```

<!-- tags: [pivotgrid, windowsforms, itemsource, pivotrows, pivotcolumns, pivotcalculations, syncfusion, winforms, 11.4.0.26] keywords: [pivot grid, item source, pivot rows, pivot columns, pivot calculations, sales data, product, year, country, state, amount, quantity, format, summary type] -->
```

---

<!-- 페이지 16 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_018.jpeg
document_name: PivotGrid
page_number: 018
page_id: PivotGrid#page_018
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:53:44Z
fidelity: lossless
-->

## Content

### Adding PivotItems to the PivotGrid

#### C#

```csharp
// Defining PivotItem
PivotItem m_PivotItem = new PivotItem() { FieldHeader="Product", 
   FieldMappingName ="Product", TotalHeader ="Total" };
// Adding PivotItem to PivotRows
this.PivotGridControl1.PivotRows.Add(m_PivotItem);
```

#### VB

```vb
' Defining PivotItem
Dim m_PivotItem As PivotItem = New PivotItem() With
{.FieldHeader="Product", .FieldMappingName ="Product", .TotalHeader ="Total"}
' Adding PivotItem to PivotRows
Me.PivotGridControl1.PivotRows.Add(m_PivotItem)
```

### 4.1.2 Sorting Using PivotItem

By default, the PivotGrid will sort data in ascending order. The sorting order can be changed using the `Comparer` field of `PivotItem`.

```csharp
// Adding Pivot Rows to Grid with FieldMappingName, TotalHeader and Comparer
this.PivotGridControl1.PivotRows.Add(new PivotItem { FieldMappingName = "Product", TotalHeader = "Total", Comparer = new ReverseOrderComparer() });

/// <summary>
/// Reverse Order Comparer for sorting data in Descending order
/// </summary>
public class ReverseOrderComparer : IComparer
{
```

## Page-level Navigation/TOC (if applicable)
- [4.1.2 Sorting Using PivotItem](#4.1.2-sorting-using-pivotitem)

## Cross References
See also:  
- [Defining PivotItem](#defining-pivotitem)
- [Adding PivotItem to PivotRows](#adding-pivotitem-to-pivotrows)

<!-- tags: [pivotgrid, winform, sort, pivotitem, comparer, reverseordercomparer] keywords: [pivotgrid, wiforms, pivotitem, data sorting, reverse order comparer, total header, field mapping name] -->
``` 


---

<!-- 페이지 17 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_022.jpeg
document_name: PivotGrid
page_number: 022
page_id: PivotGrid#page_022
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:53:57Z
fidelity: lossless
-->

## Content

### Adding PivotComputationInfo to PivotCalculations

```csharp
SummaryType = SummaryType.Count;
// Adding PivotComputationInfo to PivotCalculations
this.pivotGrid1.PivotCalculations.Add(m_PivotComputationInfo);
```

```vb
' Defining PivotComputationInfo
Dim m_PivotComputationInfo As PivotComputationInfo = New PivotComputationInfo() With {.CalculationName="Amount", .FieldName="Amount", .SummaryType= SummaryType.Count}
' Adding PivotComputationInfo to PivotCalculations
Me.pivotGrid1.PivotCalculations.Add(m_PivotComputationInfo)
```

### 4.2.2 Format String in PivotComputationInfo

The `PivotComputationInfo` property replaces each format specification in a specified string with the textual equivalent of a corresponding value.

#### Decimal Format

```csharp
// Decimal Format
PivotComputationInfo m_PivotComputationInfo = new PivotComputationInfo() { CalculationName="Total", FieldName="Quantity", SummaryType= SummaryType.Count, Format="0.00"};
```

```vb
' Decimal Format
Dim m_PivotComputationInfo As PivotComputationInfo = New PivotComputationInfo() With {.CalculationName="Total", .FieldName="Quantity", .SummaryType= SummaryType.Count, .Format="0.00"}
```

## Page-level Navigation/TOC (if applicable)
- 4.2.2 Format String in PivotComputationInfo

## Cross References
- See also: [PivotGrid calculations, format strings, value conversion]

<!-- tags: [Syncfusion Winforms, PivotGrid, calculations, format strings, PivotComputationInfo, SummaryType, value conversion] keywords: [C#, VB, decimal format, textual equivalent, calculation name, field name, summary type, format string, value replacement] -->
```

---

<!-- 페이지 18 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_026.jpeg
document_name: PivotGrid
page_number: 026
page_id: PivotGrid#page_026
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:54:10Z
fidelity: lossless
-->

## Freezing Headers

The PivotGrid for Windows Forms provides built-in support for freezing column and row headers. This is achieved by setting the `FreezeHeaders` property of `PivotGrid` to `True`. This feature also enables scrolling through the value cells.

### Code Examples

#### C# Code

```csharp
// To Freeze Grid Headers
this.PivotGridControl1.FreezeHeaders = true;
```

#### VB Code

```vb
' To Freeze Grid Headers
Me.PivotGridControl1.FreezeHeaders = True
```

### Figure: PivotGrid with Frozen Headers
![PivotGrid with Frozen Headers](https://via.placeholder.com/800x400)

## Grouping Bar

The PivotGrid Grouping Bar enables the drag-and-drop feature of fields between different areas such as column, row, value, and filter. By using the Grouping Bar, you can add, rearrange, or remove fields to show data in the PivotGrid exactly the way you want.

### Description of Grouping Bar

The Grouping Bar has field headers that identify fields in the pivot grid. One field header contains:

- **Caption string** - Identifies the field's content
- **Sort indicator** - Identifies the sort order applied to the field's values

---

### Summary

- The PivotGrid provides built-in support for freezing headers, which helps when scrolling through the value cells.
- The Grouping Bar enables flexible manipulation of fields in the PivotGrid for precise data display.

### Copyright

© 2013 Syncfusion. All rights reserved.
```

---

<!-- 페이지 19 -->

<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_030.jpeg
document_name: PivotGrid
page_number: 030
page_id: PivotGrid#page_030
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:54:21Z
fidelity: lossless
-->

# Essential PivotGrid WindowsForms

## Overview
- Demonstrates disabling sorting in the Grouping Bar.
- Explains cell selection in PivotGrid for Windows Forms and how it can be customized.
- Provides code examples in C# and VB.

## Content

The following code example illustrates how to disable sorting in the Grouping Bar.

### Disabling Sorting

#### C#
```csharp
[C#]
// Disabling Sorting.
pivotGridControl1.AllowSorting = false;
```

#### VB
```vb
[VB]
// Disabling Sorting.
pivotGridControl1.AllowSorting = False
```

### 4.7 Cell Selection

The PivotGrid for Windows Forms supports cell selection, similar to Microsoft Excel. On cell selection, an event called `PivotGridSelectionChanged` will be triggered, and the `PivotGridSelectionChangedEventArgs` will return an `IEnumerable` collection of column, row, and value of the corresponding selected cell.

#### Use Case Scenarios
Using the cell selection support, you can select cells that can be copied to clipboard or notepad. You can perform custom operations on cell selection and also bind any control based on the selected cell values.

#### Adding Cell Selection
The following code snippets show how to create a PivotGrid and specify cell selection.

```csharp
[C#]
// Instantiating PivotGridControl
PivotGridControl pivotGridControl1 = new PivotGridControl();
// Adding PivotRows
pivotGridControl1.PivotRows.Add(new PivotItem { FieldHeader = "Product" });
pivotGridControl1.PivotColumns.Add(new PivotItem { FieldHeader = "Date" });
// Adding PivotColumns
pivotGridControl1.PivotColumns.Add(new PivotItem { FieldHeader = 
```

## Page-level Navigation/TOC (if applicable)

## RAG Annotations
<!-- tags: [PivotGrid, WindowsForms, Sorting, CellSelection] keywords: [Disable Sorting, Grouping Bar, PivotGridSelectionChanged, IEnumerable, Custom Operations, Cell Selection, Clipboard, Notepad, PivotGridControl, PivotRows, PivotColumns, FieldHeader] -->

---

<!-- 페이지 20 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_034.jpeg
document_name: PivotGrid
page_number: 034
page_id: PivotGrid#page_034
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:54:35Z
fidelity: lossless
-->

# Essential PivotGrid WindowsForms

| SubTotalsRendering | Handles rendering of cells(showing or hiding the cells) by calculating the cell range values in the Pivot Engine based on the ShowSubTotals property value in the control | - | Void | - |
|--------------------|----------------------------------------------------------------------------------------------------|---|-----|---|

## Sample Link

Follow the steps given below to view a sample of this feature:

1. Select Start > Programs > Syncfusion > Essential Studio x.x.x.x -> Dashboard.
2. Click Run Samples under UI edition.
3. Select PivotGrid.
4. Navigate to Selection > Cell Selection Demo.

## 4.8.1 Showing or Hiding Subtotals in PivotGrid

The user can show or hide the PivotGrid subtotals using `ShowSubTotals` property. To show subtotals, set this property to `true`. To hide subtotals, set this property to `false`. By default, the value of the `ShowSubTotals` property is set to `true`.

The following code example illustrates how to set values for the `ShowSubTotals` property to show the subtotals.

### Code Example

```csharp
this.pivotGridControl1.ShowSubTotals = true;
```

```vb
Me.pivotGridControl1.ShowSubTotals = True
```

The following code example illustrates how to set values for the `ShowSubTotals` property to hide the subtotals.

<!-- tags: [PivotGrid, windowsforms, subtotals, showsubtotals, property, rendering, cell selection] keywords: [showsubtotals, pivotgrid, windowsforms, subtotals, property, cell selection, demo, c#, vb] -->
```

---

<!-- 페이지 21 -->

```html
<!--  
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_038.jpeg
document_name: PivotGrid
page_number: 038
page_id: PivotGrid#page_038
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:54:46Z
fidelity: lossless
-->

# Essential PivotGrid WindowsForms

```vb
Dim pdfExport As New PivotPdfExport(pivotGridControl1)
pdfExport.Export(savedialog.FileName)
```

The below image depicts the conversion of PivotGrid content to a PDF file:

|               | Canada                                      |                                  |                                  |                                  |                                  |                                  |                                  |                                  |                                  |                                  |                                  |                                  |                                  |                                  |                                  |
|---------------|---------------------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|
|               | **Alberta**                                 |                                  |                                  |                                  |                                  |                                  |                                  |                                  |                                  |                                  |                                  |                                  |                                  |                                  |
|               | **1**                                      | **10**                          | **11**                          | **2**                          | **3**                          | **4**                          | **5**                          |                                  |                                  |                                  |                                  |                                  |                                  |                                  |                                  |
|               | **Quantity**                               | **Year**                        | **Quantity**                    | **Year**                        | **Quantity**                    | **Year**                        | **Quantity**                    | **Year**                        | **Quantity**                    | **Year**                        | **Quantity**                    | **Year**                        | **Quantity**                    | **Year**                        |
| **Bike**      | FY 2005                                    | 25                              | 28                              | 28                              | 39                              | 39                              | 32                              | 32                              | 38                              | 38                              | 47                              | 47                              | 43                              | 43                              |
|               | FY 2006                                    | 9                               | 11                              | 11                              | 8                               | 8                               | 14                              | 14                              | 15                              | 15                              | 8                               | 8                               | 15                              | 15                              |
|               | FY 2007                                    | 4                               | 4                               | 4                               | 2                               | 2                               | 6                               | 6                               | 6                               | 6                               | 4                               | 4                               | 5                               | 5                               |
| **Bike Total**| 38                                         | 38                              | 43                              | 43                              | 49                              | 49                              | 52                              | 52                              | 59                              | 59                              | 59                              | 59                              | 63                              | 63                              |
| **Car**       | FY 2005                                    | 6                               | 6                               | 4                               | 4                               | 10                              | 10                              | 9                               | 9                               | 4                               | 4                               | 9                               | 9                               | 8                               | 8                               |
|               | FY 2006                                    | 1                               | 1                               | 1                               | 2                               | 2                               | 1                               | 1                               | 4                               | 4                               | 1                               | 1                               | 1                               | 1                               |
|               | FY 2007                                    | 1                               | 2                               | 2                               | 1                               | 1                               | 1                               | 1                               | 1                               | 1                               | 1                               | 1                               | 1                               | 1                               |
| **Car Total** | 8                                          | 8                               | 7                               | 7                               | 13                              | 13                              | 10                              | 10                              | 9                               | 9                               | 10                              | 10                              | 10                              | 10                              |
| **Grand Total**| 46                                         | 46                              | 50                              | 50                              | 62                              | 62                              | 62                              | 62                              | 68                              | 69                              | 69                              | 73                              | 73                              | 73                              |

## Sample Location
A sample is placed in the following location:

`<Installed Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\PivotGrid.Windows\Samples\2.0\Exporting\Export Demo`

### 4.10 Print Option
The print option is extended for the PivotGrid control to allow users to preview the contents before the contents are printed on paper.

This feature is used to print the PivotGrid control in landscape and portrait views. This feature has overridden the GridPrintDocumentAdv from Syncfusion.GridHelperClasses.Windows.

The pivot grid visual style color is automatically applied in the printed document based on the visual styles of the grid.

The print functionality can be invoked using the following code:

```csharp
private void button1_Click_1(object sender, EventArgs e)
{
    try
    {
        PivotGridPrintDocumentAdv pd = new PivotGridPrintDocumentAdv(this.pivotGridControl1);
    }
}
```

<!-- tags: [WinForms, PivotGrid, Exporting, Printing, GridPrintDocument, Syncfusion] keywords: [export, pdf, print, preview, landscape, portrait, visual style, color, PivotGridPrintDocument] -->
```

---

<!-- 페이지 22 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_003.jpeg
document_name: PivotGrid
page_number: 003
page_id: PivotGrid#page_003
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:52:37Z
fidelity: lossless
-->

# Essential PivotGrid WindowsForms

## Overview
- **Exporting Pivot Grid to Excel, Word, and PDF**: This section explains how to export PivotGrid data into Excel, Word, and PDF formats.
- **Print Option**: Provides details on the printing functionality of the PivotGrid control.

## Content

### Exporting Pivot Grid to Excel, Word, and PDF
1. **Overview**: Learn how to export data from PivotGrid to Excel, Word, and PDF formats effortlessly.
2. **Process**: Step-by-step guide to configuring and executing the export operations.
3. **Features**: Overview of features supported during the export process, such as formatting and data details.

### Print Option
1. **Overview**: Understanding the printing capabilities of the PivotGrid control.
2. **Configuration**: Instructions on setting up printing options for the PivotGrid.
3. **Usage**: Examples and best practices for utilizing the print options effectively.

## API Reference

### Methods
- **ExportToExcel()**: Exports the PivotGrid data to an Excel format.
- **ExportToWord()**: Exports the PivotGrid data to a Word document.
- **ExportToPdf()**: Exports the PivotGrid data to a PDF format.
- **Print()**: Triggers the printing of the PivotGrid content.

## Code Examples

### Exporting to Excel
```csharp
// C# Example
PivotGridControl pivotGrid = new PivotGridControl();
pivotGrid.ExportToExcel("output.xlsx");
```

### Print Option Usage
```csharp
// C# Example
PivotGridControl pivotGrid = new PivotGridControl();
pivotGrid.Print();
```

## Cross References
See also: **Getting Started with PivotGrid**, **Data Binding in PivotGrid**, **Performance Optimization in PivotGrid**

<!-- tags: [pivotgrid, export, print, windowsforms, syncfusion] keywords: [exporting, printing, windowsforms, pivotgrid, pdf, excel, word] -->
```

---

<!-- 페이지 23 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_007.jpeg
document_name: PivotGrid
page_number: 007
page_id: PivotGrid#page_007
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:52:50Z
fidelity: lossless
-->

# Essential PivotGrid WindowsForms

## Overview
- Installed Documentation path: `Dashboard -> Documentation -> Installed Documentation`.

## Content

### Documentation Path
The documentation path for the installed documentation is as follows:
- **Dashboard** -> **Documentation** -> **Installed Documentation**

This path directs users to the installed documentation, providing easy access to the essential guides and references for working with the Essential PivotGrid in Windows Forms.

## RAG Annotations
<!-- tags: [product, module, control, api, version?] keywords: [Uncle Pasta, Essential PivotGrid, Windows Forms, Documentation, Installed Documentation, Dashboard] -->
```

---

<!-- 페이지 24 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_011.jpeg
document_name: PivotGrid
page_number: 011
page_id: PivotGrid#page_011
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:52:57Z
fidelity: lossless
-->

# Essential PivotGrid Windows Forms

## 2.4 Properties Table for PivotGrid

### Table 4: Properties Table

| Property Name          | Type          | Description                                                                                                                                                     |
|------------------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DeferLayoutUpdate      | bool          | Gets or sets a value to specify whether the layout should be updated immediately after updating the pivoting info, or if it should wait for a Refresh() call. |
| FreezeHeaders          | bool          | Gets or sets a value to specify whether headers of a grid has to be frozen or not.                                                                            |
| DataSource             | object        | Gets or sets the source of data for a pivot table. This object should be an IEnumerable or IQueryable list.                                                 |
| PivotCalculations       | Hashtable     | Gets the collection of Pivot Calculations.                                                                                                                    |
| PivotColumns           | Hashtable     | Gets the collection of pivot columns.                                                                                                                          |
| PivotEngine            | PivotEngine   | Gets or sets the pivot engine for a grid.                                                                                                                      |
| PivotRows              | Hashtable     | Gets the collection of pivot rows.                                                                                                                              |
| ShowCalculationsAsColumns | bool       | Gets or sets a value to specify whether calculations should appear as rows or columns. The default behavior is for calculations to appear as columns.        |
| ShowGrandTotals        | bool          | Gets or sets a value to specify whether grand total calculations should be computed by the engine.                                                       |
| PivotCellInfo          | PivotCellInfo | Gets or sets the PivotCellInfo in order to check the cell type.                                                                                               |

## Page-level Navigation/TOC (if applicable)
- If the body contains a local Table of Contents for this page, keep it as a bullet/numbered list with links/texts as shown.
- Ignore global site TOC or breadcrumbs unless the page explicitly describes them.

<!-- tags: [PivotGrid, Windows Forms, properties, table, Syncfusion, version] keywords: [Property Name, Type, Description, DeferLayoutUpdate, FreezeHeaders, DataSource, PivotCalculations, PivotColumns, PivotEngine, PivotRows, ShowCalculationsAsColumns, ShowGrandTotals, PivotCellInfo] -->
```

---

<!-- 페이지 25 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_015.jpeg
document_name: PivotGrid
page_number: 015
page_id: PivotGrid#page_015
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:53:11Z
fidelity: lossless
-->

# Essential PivotGrid Windows Forms

```vb
With {.FieldMappingName = "Country", .TotalHeader = "Total"}
            Me.PivotGridControl1.PivotColumns.Add(New PivotItem With {.FieldMappingName = "State", .TotalHeader = "Total"})
            ' Adding PivotCalculations to Grid
            Me.PivotGridControl1.PivotCalculations.Add(New PivotComputationInfo With {.FieldName = "Amount", .Format = "C", .SummaryType = SummaryType.DoubleTotalSum})
            Me.PivotGridControl1.PivotCalculations.Add(New PivotComputationInfo With {.FieldName = "Quantity", .Format = "#,#0"})
End Sub
```

## Overview

- The `PivotGrid` control is demonstrated with data manipulation capabilities.
- The code example shows field mapping and computation information for pivot reporting.
- The output pivot grid includes totals and summaries for pivoted data.

## Content

When the code above runs, the following output will be generated.

### Pivoted Data Output

|  | Canada | Total |  |  |
| --- | --- | --- | --- | --- |
|  |  | Canada Total |  | Grand Total |
|  | Amount | Quantity | Amount | Quantity | Amount | Quantity | Amount | Quantity |
| Bike | FY 2005 | $5,409,300.00 | 34 | $4,605,600.00 | 29 | $5,583,000.00 | 32 | $15,597,900.00 | 95 | $15,597,900.00 | 95 |
| FY 2006 | $1,595,900.00 | 11 | $2,647,200.00 | 15 | $1,948,500.00 | 10 | $6,291,600.00 | 35 | $6,291,600.00 | 36 |
| FY 2007 | $1,126,500.00 | 6 | $1,349,200.00 | 8 | $812,700.00 | 6 | $3,488,400.00 | 20 | $3,488,400.00 | 20 |
| Bike Total |  | $8,231,700.00 | 51 | $8,802,000.00 | 52 | $8,344,200.00 | 48 | $25,377,900.00 | 151 | $25,377,900.00 | 151 |
| Car | FY 2005 | $1,410,300.00 | 8 | $1,482,900.00 | 10 | $958,500.00 | 5 | $3,851,700.00 | 23 | $3,851,700.00 | 23 |
| FY 2006 | $1,003,500.00 | 4 | $629,700.00 | 3 | $584,100.00 | 4 | $2,217,300.00 | 11 | $2,217,300.00 | 11 |
| FY 2007 |  |  | $87,300.00 | 1 | $660,000.00 | 3 | $747,300.00 | 4 | $747,300.00 | 4 |
| Car Total |  | $2,413,800.00 | 12 | $2,199,900.00 | 14 | $2,202,500.00 | 12 | $6,816,300.00 | 38 | $6,816,300.00 | 38 |
| Grand Total |  | $10,645,500.00 | 63 | $11,001,900.00 | 66 | $10,546,800.00 | 60 | $32,194,200.00 | 189 | $32,194,200.00 | 189 |

**Figure 6: Pivot Grid Control with Pivoted Data**

## Page-level Navigation/TOC (if applicable)

- [Top of Page](#PivotGrid)
- [Overview](#overview)
- [Content](#content)

## Cross References

- See also:
  - C# and VBNet Code Examples
  - Related Features and Properties in the `PivotGrid` Control

## RAG Annotations

<!-- tags: [PivotGrid, Windows Forms, Control, Data Reporting, Version: 11.4.0.26] keywords: [PivotGrid, PivotCalculations, FieldMapping, SummaryType, DoubleTotalSum, Quantity] -->
```

---

<!-- 페이지 26 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_019.jpeg
document_name: PivotGrid
page_number: 019
page_id: PivotGrid#page_019
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:53:43Z
fidelity: lossless
-->

# Essential PivotGrid WindowsForms

## Overview
- Demonstrates how to implement a custom `IComparer` for sorting Pivot Grid data in descending order.
- Includes C# and VB.NET code examples for adding `PivotItem` with custom `FieldMappingName`, `TotalHeader`, and `Comparer`.
- Explains the functionality of the `ReverseOrderComparer` class.

## Content

### Implementing a Custom Comparer

#### C# Code Example

```csharp
#region IComparer Members

public int Compare(object x, object y)
{
    if (x == null && y == null)
        return 0;
    else if (y == null)
        return 1;
    else if (x == null)
        return -1;
    else
        return -x.ToString().CompareTo(y.ToString());
}

#endregion
}
```

#### VB.NET Code Example

```vb
' Adding Pivot Rows to Grid with FieldMappingName, TotalHeader and Comparer
Me.PivotGridControl1.PivotRows.Add(New PivotItem With
{
    .FieldMappingName = "Product", .TotalHeader = "Total", .Comparer = New ReverseOrderComparer()
})

''' <summary>
''' Reverse Order Comparer for sorting data in Descending order
''' </summary>
public class ReverseOrderComparer : IComparer
    ' #Region "IComparer Members"

    public Integer Compare(Object x, Object y)
        If x Is Nothing AndAlso y Is Nothing Then
            Return 0
        ElseIf y Is Nothing Then
```

## API Reference

### Classes

- **ReverseOrderComparer**
  - Implements `IComparer` for sorting in descending order.
  - **Parameters:**
    - `x`: The first object to be compared.
    - `y`: The second object to be compared.
  - **Returns:** An integer indicating the relative order of the two objects.

### Properties and Methods

- **`PivotItem.FieldMappingName`**
  - Type: `String`
  - Description: The field mapping name for the Pivot Grid.
- **`PivotItem.TotalHeader`**
  - Type: `String`
  - Description: The header name for the total row.
- **`PivotItem.Comparer`**
  - Type: `IComparer`
  - Description: The custom comparer used for sorting.

## Code Examples

### C# Example

```csharp
// Adding a PivotItem with custom settings
pivotGridControl1.PivotRows.Add(new PivotItem
{
    FieldMappingName = "Product",
    TotalHeader = "Total",
    Comparer = new ReverseOrderComparer()
});
```

### VB.NET Example

```vb
' Adding a PivotItem with custom settings
Me.PivotGridControl1.PivotRows.Add(New PivotItem With
{
    .FieldMappingName = "Product",
    .TotalHeader = "Total",
    .Comparer = New ReverseOrderComparer()
})
```

## Cross References
- See also: [Syncfusion PivotGrid Documentation](https://help.syncfusion.com/windowsforms/pivotgrid)

<!-- tags: [PivotGrid, WindowsForms, CustomComparer, SyncfusionWinforms, Sorting, IComparer, ReverseOrderComparer] keywords: [PivotItem, FieldMappingName, TotalHeader, CustomComparer, ReverseOrder, DescendingSort] -->
```

---

<!-- 페이지 27 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_023.jpeg
document_name: PivotGrid
page_number: 023
page_id: PivotGrid#page_023
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:54:04Z
fidelity: lossless
-->

# Essential PivotGrid WindowsForms

The following table lists the different types of format settings.

## Overview
- Lists various format settings for data presentation.
- Explains SummaryType, which determines field summary calculations.
- Includes descriptions of summary operations such as SUM, AVERAGE, and other statistical computations.

## Content

### Table 7: Types of format settings
| Format          | Description         |
|------------------|---------------------|
| 0.00            | Decimal             |
| C               | Currency            |
| #,##0           | Thousand Separator   |
| #' degrees'     | Literal String Specifier |
| D               | Long Date           |

### 4.3 SummaryType
**SummaryType** determines the type of field summary such as count, sum, average, etc. It is an enumerator that should be defined in the PivotComputationInfo class. It contains the following types for performing calculations.

#### Table 8: Summary Type
| Summary Type          | Description                               |
|------------------------|-------------------------------------------|
| DoubleTotalSum        | Computes the sum of double or integer values. |
| DoubleAverage         | Computes the simple average of double or integer values. |
| DoubleMaximum         | Computes the maximum of double or integer values. |
| DoubleMinimum         | Computes the minimum of double or integer values. |
| DoubleStandardDeviation | Computes the standard deviation of double or integer values. |
| DoubleVariance        | Computes the variance of double or integer values. |
| Count                 | Computes the count of double or integer values. |
| DecimalTotalSum       | Computes the sum of decimal values. |

## API Reference (if applicable)
Not explicitly defined in this section. This content focuses on format settings and summary calculations without referencing specific APIs.

## Code Examples (multi-language supported)
Not explicitly provided in the current content.

## Page-level Navigation/TOC (if applicable)
Not explicitly included in this section.

## Cross References
Not explicitly mentioned in this content.

## RAG Annotations
<!-- tags: PivotGrid, FormatSettings, SummaryType, WindowsForms, Syncfusion, ComputationInfo keywords: format, decimal, currency, thousand separator, literal string specifier, long date, summary type, double total sum, double average, double maximum, double minimum, double standard deviation, double variance, count, decimal total sum -->
```

---

<!-- 페이지 28 -->

<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_027.jpeg
document_name: PivotGrid
page_number: 027
page_id: PivotGrid#page_027
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:54:20Z
fidelity: lossless
-->

# Essential PivotGrid Windows Forms

## Overview
- Filter button - end-users can use it to filter field values

## Content

### Header Areas

The headers of all visible fields are contained within header areas. The headers of row and column fields are displayed within the row header and column header areas, respectively. The headers of data fields are displayed within the data header area.

### Use Case Scenarios

At times, you may expect the Grid to perform sorting and filtering at run-time.

### Adding Grouping Bar

By default, Grouping Bar is enabled. It can be disabled by setting the `ShowGroupBar` property of `PivotGrid` to `False`.

#### Code Examples

##### C#

```csharp
// Instantiating PivotGridControl
PivotGridControl pivotGridControl1 = new PivotGridControl();

// Adding PivotRows
pivotGridControl1.PivotRows.Add(new PivotItem { FieldHeader = "Product" });
pivotGridControl1.PivotColumns.Add(new PivotItem { FieldHeader = "Date" });

// Adding PivotColumns
pivotGridControl1.PivotColumns.Add(new PivotItem { FieldHeader = "Country" });
pivotGridControl1.PivotColumns.Add(new PivotItem { FieldHeader = "State" });

// Adding PivotCalculations
pivotGridControl1.PivotCalculations.Add(new PivotComputationInfo { FieldName="Amount", Format="C" });
pivotGridControl1.PivotCalculations.Add(new PivotComputationInfo { FieldName = "Quantity", Format = "#,##0" });
```

##### VB

```vb
' Instantiating PivotGridControl
Dim pivotGridControl1 As PivotGridControl = New PivotGridControl()

' Adding PivotRows
pivotGridControl1.PivotRows.Add(New PivotItem With {.FieldHeader = "Product"})
pivotGridControl1.PivotColumns.Add(New PivotItem With {.FieldHeader = "Date"})

' Adding PivotColumns
pivotGridControl1.PivotColumns.Add(New PivotItem With {.FieldHeader = "Country"})
pivotGridControl1.PivotColumns.Add(New PivotItem With {.FieldHeader = "State"})

' Adding PivotCalculations
pivotGridControl1.PivotCalculations.Add(New PivotComputationInfo With {.FieldName = "Amount", .Format = "C"})
pivotGridControl1.PivotCalculations.Add(New PivotComputationInfo With {.FieldName = "Quantity", .Format = "#,##0"})
```

## Page-level Navigation/TOC (if applicable)

This section is not present on the page.

## Cross References

This section is not present on the page.

<!-- tags: [pivotgrid, windowsforms, filterbutton, groupingbar, usecasescenario] keywords: [pivotgrid, windowsforms, filterbutton, groupingbar, sorting, filtering] -->

---

<!-- 페이지 29 -->

<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_031.jpeg
document_name: PivotGrid
page_number: 031
page_id: PivotGrid#page_031
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:54:36Z
fidelity: lossless
-->

# Essential PivotGrid WindowsForms

## Content

Here is the C# code snippet for setting up a PivotGrid control:

```csharp
"Country" }));
pivotGridControl1.PivotColumns.Add(new PivotItem { FieldHeader = "State" });

// Adding PivotCalculations
pivotGridControl1.PivotCalculations.Add(new PivotComputationInfo { FieldName="Amount", Format="C"});
pivotGridControl1.PivotCalculations.Add(new PivotComputationInfo { FieldName = "Quantity", Format = "#,##0" });

// Enabling cell selection
this.pivotGridControl1.AllowSelection = false;
```

### VB

Here is the VB code snippet for setting up a PivotGrid control:

```vb
' Instantiating PivotGridControl
Dim pivotGridControl1 As PivotGridControl = New PivotGridControl()
' Adding PivotRows
pivotGridControl1.PivotRows.Add(New PivotItem With {.FieldHeader = "Product"})
pivotGridControl1.PivotColumns.Add(New PivotItem With {.FieldHeader = "Date"})
' Adding PivotColumns
pivotGridControl1.PivotColumns.Add(New PivotItem With {.FieldHeader = "Country"})
pivotGridControl1.PivotColumns.Add(New PivotItem With {.FieldHeader = "State"})
' Adding PivotCalculations
pivotGridControl1.PivotCalculations.Add(New PivotComputationInfo With {.FieldName="Amount", .Format="C"})
pivotGridControl1.PivotCalculations.Add(New PivotComputationInfo With {.FieldName = "Quantity", .Format = "#,##0"})
' Enabling cell selection
Me.pivotGridControl1.AllowSelection = False
```

## API Reference

### Properties
- `PivotRows`: Collection of PivotItem for rows.
- `PivotColumns`: Collection of PivotItem for columns.
- `PivotCalculations`: Collection of PivotComputationInfo for calculations.
- `AllowSelection`: Boolean property to enable or disable cell selection.

### Methods
- `Add(PivotItem)`: Adds a PivotItem to the specified collection.
- `Add(PivotComputationInfo)`: Adds a PivotComputationInfo to the calculations.

## Code Examples

### C#
```csharp
pivotGridControl1.PivotRows.Add(new PivotItem { FieldHeader = "Product" });
pivotGridControl1.PivotColumns.Add(new PivotItem { FieldHeader = "Date" });

// Adding PivotColumns
pivotGridControl1.PivotColumns.Add(new PivotItem { FieldHeader = "Country" });
pivotGridControl1.PivotColumns.Add(new PivotItem { FieldHeader = "State" });

// Adding PivotCalculations
pivotGridControl1.PivotCalculations.Add(new PivotComputationInfo { FieldName="Amount", Format="C" });
pivotGridControl1.PivotCalculations.Add(new PivotComputationInfo { FieldName = "Quantity", Format = "#,##0" });
```

### VB
```vb
pivotGridControl1.PivotRows.Add(New PivotItem With {.FieldHeader = "Product"})
pivotGridControl1.PivotColumns.Add(New PivotItem With {.FieldHeader = "Date"})

' Adding PivotColumns
pivotGridControl1.PivotColumns.Add(New PivotItem With {.FieldHeader = "Country"})
pivotGridControl1.PivotColumns.Add(New PivotItem With {.FieldHeader = "State"})

' Adding PivotCalculations
pivotGridControl1.PivotCalculations.Add(New PivotComputationInfo With {.FieldName="Amount", .Format="C"})
pivotGridControl1.PivotCalculations.Add(New PivotComputationInfo With {.FieldName = "Quantity", .Format = "#,##0"})
```

### RAG Annotations
<!-- tags: [PivotGrid, WindowsForms, syncing data, display settings, cell selection] -->
<!-- keywords: [PivotGrid, PivotRows, PivotColumns, PivotItem, PivotComputationInfo, FieldName, Format, AllowSelection] -->

---

<!-- 페이지 30 -->

```html
<!--  
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_035.jpeg
document_name: PivotGrid
page_number: 035
page_id: PivotGrid#page_035
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:54:56Z
fidelity: lossless
-->

## Essential PivotGrid Windows Forms

### Code Examples

```csharp
this.pivotGridControl1.ShowSubTotals = false;
```

```vb
Me.pivotGridControl1.ShowSubTotals = False
```

### 4.9 Exporting Pivot Grid to Excel, Word, and PDF

The PivotGrid is exported into different formats and the formatting styles are applied as per the visual style of PivotGrid.

There are three options to export PivotGrid:

1.  Export to Excel
2.  Export to Word
3.  Export to PDF

#### Export to Excel:

Exporting data to an Excel spreadsheet is one of the most commonly preferred features in the .NET world. Essential Grid control has an in-built support to export an Excel spreadsheet. The class **ExcelExport** provides support for exporting data from the PivotGrid control to an Excel spreadsheet for verification and/or computation.

This class automatically copies a grid's styles and formats to an Excel spreadsheet. This enables you to export PivotGrid to an Excel document.

The following code illustrates exporting PivotGrid to an Excel:

```csharp
ExcelExport excelExport = new ExcelExport(pivotGridControl1,
Syncfusion.XlsIO.ExcelVersion.Excel2010);

excelExport.ExportMode = (ExportAsPivotTable) ? ExportModes.PivotTable
: ExportModes.Cell;

excelExport.Export(FileName);
```

#### Export to Excel provides two options:

1.  Cell-by-Cell Export
2.  Pivot Table Export
```

---

<!-- 페이지 31 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_039.jpeg
document_name: PivotGrid
page_number: 039
page_id: PivotGrid#page_039
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:55:07Z
fidelity: lossless
-->

# Essential PivotGrid Windows Forms

## Content

### Printing Overview

Here are some code examples for configuring print settings and handling print previews in a `PivotGrid` control:

#### C#

```csharp
pd.DefaultPageSettings.Margins = new
System.Drawing.Printing.Margins(25, 25, 25, 25);
PrintPreviewDialog previewDialog = new PrintPreviewDialog();
previewDialog.Document = pd;
previewDialog.Show();
}
catch (Exception ex)
{
MessageBox.Show("Error while print preview" + ex.ToString());
}
}
```

#### VB

```vb
Private Sub button1_Click(ByVal sender As Object, ByVal e As EventArgs)

Try

Dim pd As New PivotGridPrintDocumentAdv(Me.pivotGridControl1)

pd.DefaultPageSettings.Margins = New
System.Drawing.Printing.Margins(25, 25, 25, 25)
Dim previewDialog As New PrintPreviewDialog()
previewDialog.Document = pd
previewDialog.Show()

Catch ex As Exception
MessageBox.Show("Error while print preview" & ex.ToString())

End Try

End Sub
```

#### Headers and Footers

Headers and footers can also be added by using the `DrawGridPrintHeader` and `DrawGridPrintFooter` events. The following code illustrates how to add the header and footer:

#### C#

```csharp
pd.DrawGridPrintHeader += new
GridPrintDocumentAdv.DrawGridHeaderFooterEventHandler(pd_DrawGridPrintHeader);
```

## API Reference

### Methods and Events

- `DefaultPageSettings.Margins`: Configures page margins for printing.
- `PrintPreviewDialog`: A dialog for previewing the printed content.
- `PivotGridPrintDocumentAdv`: A document class for handling PivotGrid printing.
- `DrawGridPrintHeader`: Event to draw a custom header for printed content.
- `DrawGridPrintFooter`: Event to draw a custom footer for printed content.

## Code Examples

The provided examples demonstrate how to set up print settings, handle errors in the print preview process, and customize headers and footers for printed output.

---

<!-- tags: [syncfusion, windowsforms, pivotgrid, printing, header, footer, exceptions] keywords: [margins, printpreviewdialog, drawgridprintheader, drawgridprintfooter, errors, customization] -->
```

---

<!-- 페이지 32 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_004.jpeg
document_name: PivotGrid
page_number: 004
page_id: PivotGrid#page_004
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:52:37Z
fidelity: lossless
-->

# 1 Overview

This section covers information on Essential PivotGrid for Windows Forms, its key features, prerequisites for using the control, its compatibility with various operating systems, and finally, documentation details complimentary with the product. It comprises the following subsections:

## 1.1 Introduction to Essential PivotGrid Windows Forms

Essential PivotGrid for Windows Forms is a powerful cell-oriented, extensible grid control. It simulates the pivot table feature of Excel. The PivotGrid, as the name implies, pivots data to organize the data in a cross-tabulated form. The major advantage with a pivot grid is that you can extract the desired information from a large list within seconds. Along with presenting the data, a pivot grid also enables you to summarize and group data.

### Figure 1: PivotGrid Control

![PivotGrid Control](http://)

**Key Features**

Important features of the PivotGrid control are listed below:

- Multilevel drill up/down capability—row drill-down, column drill-down, multilevel row/column drill-down
- Data-binding support
- Auto Calculation of total summary
- Filters
- Grouping support
- Sorting

### User Guide Organization

This product comes with numerous samples as well as an extensive documentation to guide you. This User Guide provides detailed information on the features and functionalities of the PivotGrid control. It is organized into the following sections:

---

<!-- tags: [pivotgrid, windows forms, syncfusion, user guide, essential pivotgrid] keywords: [user guide organization, key features, multilevel drill, data binding, auto calculation, filters, grouping, sorting, samples, extensive documentation] -->
```

---

<!-- 페이지 33 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_008.jpeg
document_name: PivotGrid
page_number: 008
page_id: PivotGrid#page_008
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:52:49Z
fidelity: lossless
-->

# Essential PivotGrid Windows Forms

This section covers information on the install location, samples, licensing, patch updates, and updates of the current version of Essential Studio. It is comprised of the following subsections:

## 2.1 Installation

For step-by-step installation procedures for installing Essential Studio, refer to the **Installation** topic under **Installation and Deployment** in the **Common UG**.

### See Also
For licensing, patches, and information on adding or removing selective components, refer to the following topics in **Common UG** under **Installation and Deployment**:

- Licensing
- Patches
- Add/Remove Components

## 2.2 Samples and Location

This section covers the location of the installed samples and describes the procedure to run the samples through the Sample Browser and online. It also provides the location of the source code.

### Samples Installation Location

The PivotGrid samples are installed in the following location, locally on the disk:

#### Windows XP:
```plaintext
C:\Syncfusion\Essential Studio<version number>\Windows\PivotGrid.Windows\Samples
```

#### Windows 8/7/Vista:
```plaintext
C:\Users\<user name>\AppData\Local\Syncfusion\EssentialStudio\<version number>\Windows\PivotGrid.Windows\Samples
```

### Viewing Samples
To view the samples, follow the steps below:

1. Click **Start → All Programs → Syncfusion → Essential Studio <version number> → Dashboard**.

## Page-level Navigation/TOC (if applicable)

<!-- tags: [syncfusion-windows-forms, essential-studio, installation, deployment, samples, location] keywords: [installation procedures, licensing, patches, selective components, samples location, PivotGrid, local disk path, source code, Sample Browser] -->
```

---

<!-- 페이지 34 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_012.jpeg
document_name: PivotGrid
page_number: 012
page_id: PivotGrid#page_012
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:53:03Z
fidelity: lossless
-->

# Getting Started

## Creating PivotGrid through Visual Studio

To create the PivotGrid through Visual Studio:

1. Open the Start menu, and then click Microsoft Visual Studio 2008.
2. On the File menu, click New Project. The New Project dialog box appears as follows.

![New Project Dialog Box](https://example.com/image-url-for-dialog-box.png "Figure 4: New Project Dialog Box")

3. Select WindowsForms Application, and then click OK.
4. Drag the PivotGridControl control from the Toolbox to the Design page.

## Overview
- Describes the initial setup process for creating a PivotGrid application using Visual Studio.
- Guides users through selecting project templates and dragging controls to the design surface.

## Content
### WinForms-specific conventions
The instructions detail how to use Visual Studio 2008 for setting up a PivotGrid project in the Windows Forms environment. This involves creating a new Windows Forms application and adding the PivotGridControl to the design surface.

• **Project Creation**:
    1. Open Microsoft Visual Studio 2008.
    2. Initiate a new project by navigating through the Start menu and selecting "New Project."

• **Template Selection**:
    - Choose "Windows Forms Application" from the available project templates.

• **Design Surface Integration**:
    - Drag and drop the PivotGridControl from the Toolbox onto the Design page to begin building the application interface.

## API Reference (if applicable)
- Namespace: `Syncfusion.Windows.Forms.PivotGrid`
- Class: `PivotGridControl`
- Properties: `DataSource`, `ColumnHeaders`, `RowHeaders`
- Methods: `LoadDataSource()`, `SetEmptyString()`
- Events: `DataBound`, `CellDoubleClick`

## Code Examples (multi-language supported)
```csharp
using Syncfusion.Windows.Forms.PivotGrid;

// Initialize the PivotGridControl
PivotGridControl pivotGrid = new PivotGridControl();
pivotGrid.DataSource = yourDataSource;
pivotGrid.loadDataSource();
```

```vb
Imports Syncfusion.Windows.Forms.PivotGrid

' Initialize the PivotGridControl
Dim pivotGrid As New PivotGridControl()
pivotGrid.DataSource = yourDataSource
pivotGrid.loadDataSource()
```

<!-- tags: PivotGrid, WindowsForms, VisualStudio2008, SyncfusionWinforms, control, properties, methods, events -->
```

---

<!-- 페이지 35 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_016.jpeg
document_name: PivotGrid
page_number: 016
page_id: PivotGrid#page_016
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:53:18Z
fidelity: lossless
-->

# Essential PivotGrid WindowsForms

## Overview
- Provides an overview of the class diagram for the `PivotGrid` control.
- Explains the relationship between `PivotGrid Control`, its base class, and its components.

## Content

### 3.3 Class Diagram

The class diagram for the `PivotGrid WF` control is shown below:

```plaintext
+---------------------------+
| PivotGrid Control        |
+---------------------------+
         ↑
+---------------------------+
| PivotGridControlBase     |
+---------------------------+
         ↑
+------------------------+   +--------------------+
| Pivot Rows           |   | Pivot Columns      |
+------------------------+   +--------------------+
                           ↓                         ↓
+---------------------------+   +--------------------+
| Pivot Calculation Values |   | Filters           |
+---------------------------+   +--------------------+
```

#### Explanation:
- **`PivotGrid Control`**: The main control that implements the `IPivotControl` interface.
- **`IPivotControl`**: The interface that defines the behavior and methods of the pivot grid.
- **`PivotGridControlBase`**: The base class for the pivot grid control, which contains shared functionality.
- **`Pivot Rows`**: Represents the rows in the pivot grid.
- **`Pivot Columns`**: Represents the columns in the pivot grid.
- **`Pivot Calculation Values`**: Defines the calculation values for the pivot grid.
- **`Filters`**: Handles filtering functionality in the pivot grid.

### Figure 7: PivotGrid WF Class Diagram

The diagram illustrates the structure and hierarchy of the `PivotGrid` control, showing how it is composed of various components and interfaces.

## API Reference (if applicable)
- This section details the classes, methods, properties, and events related to the `PivotGrid` control.
- For example:
  - `IPivotControl`: Interface defining the control's behavior.
  - `PivotGridControlBase`: Base class for the pivot grid control.
  - `Pivot Rows`, `Pivot Columns`, `Pivot Calculation Values`, `Filters`: Components of the pivot grid.

## Code Examples
Example code demonstrating how to use the `PivotGrid` control in a Windows Forms application:
```csharp
using Syncfusion.Windows.Forms.PivotGrid;

public class PivotGridExample
{
    private PivotGridControl pivotGrid;

    public void InitializePivotGrid()
    {
        // Create an instance of PivotGridControl
        pivotGrid = new PivotGridControl();

        // Add rows, columns, and calculation values
        pivotGrid.PivotRows.Add(new PivotRowField("Category"));
        pivotGrid.PivotColumns.Add(new PivotColumnField("Product"));
        pivotGrid.PivotCalculationValues.Add(new PivotValueField("Sales", "Total Sales", CalculationMode.Sum));

        // Apply a filter
        pivotGrid.PivotFilters.Add(new PivotFilterField("Region", "North"));
    }
}
```

## Cross References
- See also:
  - [PivotGrid Control Documentation](#pivotgrid-control-documentation)
  - [Working with PivotGrid in Windows Forms](#working-with-pivotgrid-in-windows-forms)

<!-- tags: PivotGrid, WindowsForms, Class Diagram, IPivotControl, PivotGridControlBase keywords: PivotRows, PivotColumns, PivotCalculationValues, Filters, Windows Forms, class diagram, control interface -->
```

---

<!-- 페이지 36 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_020.jpeg
document_name: PivotGrid
page_number: 020
page_id: PivotGrid#page_020
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:53:36Z
fidelity: lossless
-->

# Essential PivotGrid WindowsForms

```vb
Return 1
ElseIf x Is Nothing Then
    Return -1
Else
    Return -x.ToString().CompareTo(y.ToString())
End If
' #End Region
```

## 4.2 PivotComputationInfo

This class holds the information needed for calculations that appear in PivotGrid. For each calculation, there is an associated `PivotComputationInfo` object that is added to the `PivotCalculations` collection. The properties available in the `PivotComputationInfo` are listed in the following table.

### Table 6: Properties Table for PivotComputationInfo

| Property Name | Description | Type | Value it Accepts | Reference link |
|---------------|-------------|------|------------------|----------------|
| CalculationName | Gets or sets what is displayed in the pivot table if more than one calculation is included in the PivotGrid. | string | - | - |
| Description | Gets or sets a description of the calculation. | string | - | - |
| FieldName | Gets or sets the name of the property to be used in this calculation. | string | - | - |
| Format | Gets or sets the format string to be used to format the calculation results in the PivotGrid. | string | - | - |
| Summary | Gets or sets the SummaryBase object that is used to define this | SummaryBase | - | - |

## API Reference (if applicable)

### System.ComponentModel.ISupportInitialize

This section can be added if specific API references are provided in the actual documentation.

## Code Examples (multi-language supported)

### C# Example
```csharp
// Example usage of PivotComputationInfo
PivotComputationInfo computationInfo = new PivotComputationInfo();
computationInfo.CalculationName = "Total Sales";
computationInfo.Description = "Calculates the total sales for each item.";
computationInfo.FieldName = "SalesAmount";
computationInfo.Format = "C2";
computationInfo.Summary = new SummaryBase(); // Initialize appropriate summary type

pivotGridModel.PivotCalculations.Add(computationInfo);
```

### VB.NET Example
```vb.net
' Example usage of PivotComputationInfo
Dim computationInfo As New PivotComputationInfo()
computationInfo.CalculationName = "Total Sales"
computationInfo.Description = "Calculates the total sales for each item."
computationInfo.FieldName = "SalesAmount"
computationInfo.Format = "C2"
computationInfo.Summary = New SummaryBase() ' Initialize appropriate summary type

pivotGridModel.PivotCalculations.Add(computationInfo)
```

## Page-level Navigation/TOC (if applicable)
- [4.2 PivotComputationInfo](#4.2-pivotcomputationinfo)

## Cross References
- See also: Related sections or pages can be added here if they exist in the documentation.

<!-- tags: [pivotgrid, calculation, pivotgridcalculations, winforms, computationinfo] keywords: [pivotgrid, computation, pivot, sum, aggregation, calculation, data] -->
```

---

<!-- 페이지 37 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_024.jpeg
document_name: PivotGrid
page_number: 024
page_id: PivotGrid#page_024
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:53:53Z
fidelity: lossless
-->

## 4.4 Sorting

Sorting enables you to quickly visualize and understand the data in a better way, organize and find the data that you want, and ultimately make more effective decisions. By default, the PivotGrid will populate the data in ascending order. The sorting order can be changed using the Comparer field of PivotItem.

### Overview
- Sorting helps in organizing and visualizing data effectively.
- By default, data is sorted in ascending order.
- Sorting order can be customized using a custom Comparer.

### Content
#### Sorting in PivotGrid
Sorting in the PivotGrid enables users to restructure the data according to their requirements. By default, the data is organized in ascending order. However, this behavior can be adjusted by utilizing a custom Comparer class. Below is an example demonstrating how to achieve this:

```csharp
this.PivotGridControl.PivotRows.Add(new PivotItem
{
    FieldMappingName = "Product",
    TotalHeader = "Total",
    Comparer = new ReverseOrderComparer()
});
```

#### Custom Comparer Example

```csharp
/// <summary>
/// Reverse Order Comparer for sorting data in Descending order
/// </summary>
public class ReverseOrderComparer : IComparer
{
    #region IComparer Members

    public int Compare(object x, object y)
    {
        if (x == null && y == null)
            return 0;
        else if (y == null)
            return 1;
        else if (x == null)
            return -1;
        else
            return -x.ToString().CompareTo(y.ToString());
    }

    #endregion
}
```

This custom Comparer class, `ReverseOrderComparer`, implements the `IComparer` interface and provides a mechanism to sort data in descending order.

---

``` 
``` 
<!-- tags: [pivotgrid, sorting, windowsforms, syncfusion, asc, desc, comparer] keywords: [pivotitem, totals, totalheader, reverseordercomparer, iComparer, sortingorder, ascendingorder, descendingorder] -->
``` 


---

<!-- 페이지 38 -->

<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_028.jpeg
document_name: PivotGrid
page_number: 028
page_id: PivotGrid#page_028
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:54:07Z
fidelity: lossless
-->

## Essential PivotGrid Windows Forms

### Setting Up the PivotGrid

Here is a code snippet demonstrating how to set up the PivotGrid:

```csharp
"Product"})
pivotGridControl1.PivotColumns.Add(New PivotItem With {.FieldHeader = "Date"})
' Adding PivotColumns
pivotGridControl1.PivotColumns.Add(New PivotItem With {.FieldHeader = "Country"})
pivotGridControl1.PivotColumns.Add(New PivotItem With {.FieldHeader = "State"})
' Adding PivotCalculations
pivotGridControl1.PivotCalculations.Add(New PivotComputationInfo With {.FieldName="Amount", .Format="C"})
pivotGridControl1.PivotCalculations.Add(New PivotComputationInfo With {.FieldName = "Quantity", .Format = "#,#0"})
```

### PivotGrid Grouping Bar

The PivotGrid Grouping Bar is a feature that allows users to group data by specific fields. Here is an explanation of the key areas in the Grouping Bar:

- **Filter Button**: Indicates the option to filter data.
- **Filter Header Area**: Displays the fields that can be filtered.
- **Sort Indicator**: Shown when data is sorted by a specific field.
- **Column Header Area**: Lists the fields in the columns.
- **Data Area**: Displays the actual data grouped by the specified fields.
- **Row Header Area**: Lists the fields in the rows.

### Figure 9: PivotGrid Grouping Bar

![Figure 9: PivotGrid Grouping Bar](https://example.com/figure9.png)

### 4.6.1 Filtering in Grouping Bar

#### Overview
- Filtering allows users to display only a subset of data that meets specified criteria, hiding irrelevant data.
- Runtime filtering is a key feature, represented by a funnel symbol.
- Clicking the funnel opens a filter popup, allowing users to select specific elements to filter by.

#### Detailed Explanation
Data filtering displays only a subset of data that meets criteria specified by you and hides data that you don't want to be displayed. The items present in the filter header area, column header area, and row header area provide the option of runtime filtering, which is represented as a funnel symbol on it. On clicking the symbol, it opens a filter popup which displays a list of elements through which filtering can be applied.

## References

- **Syncfusion WinForms Documentation**: [Syncfusion WinForms PivotGrid Documentation](https://www.syncfusion.com/documentation/windowsforms/pivotgrid/)

### Figure 9: PivotGrid Grouping Bar
This figure illustrates the layout of the PivotGrid Grouping Bar, highlighting key interactive elements such as the filter button, sort indicators, and headers/rows.

## Additional Notes
- The PivotGrid control supports various calculations and formatting options, which are configured using `PivotComputationInfo`.
- Filtering enhances the user experience by allowing them to focus on relevant data subsets.

<!-- tags: [syncfusion, pivotgrid, filtering, winforms, data grouping, runtime filtering] keywords: [pivotgrid, grouping, filtering, runtime filtering, filter button, filter header, filter popup, data area, row header, column header] -->

---

<!-- 페이지 39 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_032.jpeg
document_name: PivotGrid
page_number: 032
page_id: PivotGrid#page_032
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:54:26Z
fidelity: lossless
-->

# Essential PivotGrid Windows Forms

## Overview

- The PivotGrid control with detailed cell selection and subtotal hiding functionality.
- Data visualization and manipulation in PivotGrid using cells and subtotals.
- Example scenarios demonstrating the use of PivotGrid features.

## Content

### PivotGrid Cell Selection

**Figure 12: PivotGrid Cell Selection**

The PivotGrid control displays financial data for different countries and fiscal years. The data is organized into rows for "Bike" and "Car" categories, with columns for Canada, France, Germany, the United Kingdom, the United States, and a Grand Total.

#### Bike Category

| Year   | Canada         | France         | Germany         | United Kingdom | United States | Grand Total    |
|--------|----------------|----------------|----------------|----------------|----------------|----------------|
| FY 2005 | $28,042,200.00 | $26,531,700.00 | $28,022,100.00 | $29,365,200.00 | $33,896,700.00 | $145,857,900.00 |
| FY 2006 | $13,699,800.00 | $13,812,300.00 | $13,020,300.00 | $9,955,500.00  | $12,009,300.00 | $62,497,200.00  |
| FY 2007 | $6,795,000.00  | $7,396,800.00  | $8,487,600.00  | $6,083,400.00  | $7,078,500.00  | $35,841,300.00  |
| FY 2008 | $3,612,600.00  | $3,812,100.00  | $3,933,000.00  | $3,421,500.00  | $3,315,300.00  | $18,094,500.00  |
| FY 2009 | $1,490,400.00  | $2,655,900.00  | $2,169,000.00  | $2,543,700.00  | $1,161,300.00  | $10,020,300.00  |
| Bike Total | $53,640,000.00 | $54,208,800.00 | $55,632,000.00 | $51,369,300.00 | $57,461,100.00 | $272,311,200.00 |

#### Car Category

| Year   | Canada         | France         | Germany         | United Kingdom | United States | Grand Total    |
|--------|----------------|----------------|----------------|----------------|----------------|----------------|
| FY 2005 | $5,514,600.00  | $6,982,200.00  | $5,710,800.00  | $5,500,800.00  | $6,949,800.00  | $30,658,200.00  |
| FY 2006 | $2,439,900.00  | $2,606,700.00  | $1,287,000.00  | $2,762,400.00  | $2,304,900.00  | $11,400,900.00  |
| FY 2007 | $1,137,900.00  | $2,750,100.00  | $1,619,100.00  | $1,176,300.00  | $2,483,400.00  | $9,166,800.00   |
| FY 2008 | $1,151,400.00  | $767,400.00    | $408,900.00    | $740,700.00    | $777,600.00    | $3,846,000.00   |
| FY 2009 | $58,800.00     | $270,000.00    | $404,400.00    | $293,700.00    | $1,026,900.00  | $1,026,900.00   |
| Car Total | $10,302,600.00 | $13,106,400.00 | $9,295,800.00  | $10,584,600.00 | $12,809,400.00 | $56,098,800.00  |
| Grand Total | $63,942,600.00 | $67,315,200.00 | $64,927,800.00 | $61,953,900.00 | $70,270,500.00 | $328,410,000.00 |

### 4.8 Subtotal Hiding

#### Overview

The subtotal hiding feature is used to show or hide the subtotals in the PivotGrid. In the case of larger data tables, this feature enables the user to have an abstract view of the data by hiding subtotals using the `ShowSubTotals` property.

#### Use Case Scenarios

When the user has more computational fields with subtotals in each group of their PivotGrid, the user might find it difficult to view all the data. In that case, the user can hide the subtotals and make it visible when required.

The following screenshots show the PivotGrid with shown and hidden subtotals.

## API Reference

- **`ShowSubTotals`** property: Controls whether subtotals are shown or hidden in the PivotGrid.

## Code Examples

```csharp
using Syncfusion.Windows.Forms.PivotGrid;
// Example to hide subtotals
pivotGridControl1.ShowSubTotals = false;
```

## Page-level Navigation/TOC

- [Subtotal Hiding](#4.8-subtotal-hiding)

## Cross References

- See also: [PivotGrid Overview](#overview), [PivotGrid Cell Selection](#pivotgrid-cell-selection)

<!-- tags: [syncfusion-windowsforms, pivotgrid, subtotalhiding, showsubtotals, datavisualization, financialdata] keywords: [subtotal, hiding, subtotals, pivotgrid, data, visualization, financial, cell selection, grand total] -->
```

---

<!-- 페이지 40 -->

```html
<!-- {{page_id}} -->
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_036.jpeg
document_name: PivotGrid
page_number: 036
page_id: PivotGrid#page_036
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:55:08Z
fidelity: lossless
-->

# Essential PivotGrid WindowsForms

## Cell-by-Cell Export

**Overview**
- In cell-by-cell export, the contents are exported cell by cell with applied formatting.
- The formatting includes all styles applied to the data.

### Implementation Details
The following image shows the cell-by-cell export:

| A    | B    | C      | D      | E       | F       | G       | H       | I       | J      | K      | L      | M      | N      | O      |
|------|------|--------|--------|---------|---------|---------|---------|---------|--------|--------|--------|--------|--------|--------|
| 1    |      | Canada  |        |         |         |         |         |         |        |        |        |        |        |        |
| 2    |      | Alberta |        |         |         |         |         |         |        |        |        |        |        |        |
| 3    |      | 1       |        | 11      |         | 2       |         | 3       |        | 4      |        | 5      |        |        |
| 4    |      | Quantity | Year   | Quantity | Year     | Quantity | Year     | Quantity | Year   | Quantity | Year   | Quantity |        |        |
| 5    | Bike | FY 2005 | 25     | 25      | 28      | 39      | 39      | 32      | 32     | 38     | 38     | 47     | 47     | 43     |
| 6    |      | FY 2006 | 9      | 11      | 11      | 8       | 8       | 14      | 14     | 15     | 15     | 8      | 8      | 15     |
| 7    |      | FY 2007 | 4      | 4       | 4       | 2       | 2       | 6       | 6      | 6      | 6      | 4      | 4      | 5      |
| 8    | Bike Total | 38 | 38  | 43  | 43  | 49  | 49  | 52  | 52  | 59  | 59  | 59  | 59  | 63 |
| 9    | Car | FY 2005 | 6      | 6       | 4      | 10      | 10      | 9       | 9      | 4      | 4      | 9      | 9      | 8      |
| 10   |      | FY 2006 | 1      | 1       | 1      | 2       | 2      | 1       | 1      | 4      | 4      | 1      | 1      | 1      |
| 11   |      | FY 2007 | 1      | 1       | 2      | 2       | 1       | 1       |        | 1      | 1      |        |        | 1      |
| 12   | Car Total | 8     | 8      | 7      | 7      | 13      | 13      | 10      | 10     | 9      | 9      | 10     | 10     | 10     |
| 13   | Grand Total | 46   | 46  | 50  | 50  | 62  | 62  | 62  | 62  | 68  | 68  | 68  | 69  | 69 |

## Pivot Table Export

**Overview**
- In PivotTable export, users can export the entire PivotGrid with its functionalities, including sorting and filtering.
- The PivotGrid allows data manipulation via drag-and-drop to organize data into a cross-tabulated format.

### Features
- Extract desired information quickly.
- Summarizes and groups data.
- Primary application in the financial domain for organizing and analyzing business data.

### Implementation Details
The following image depicts the exported PivotTable:

| A | B    | C       | D       | E       | F       | G       | H       | I       | J     |
|---|------|---------|---------|---------|---------|---------|---------|---------|-------|
| 1 |      | Country | State   | Quantity | Values  |         |         |         |       |
| 2 |      | Canada  |         | Quantity | Values  |         |         |         |       |
| 3 |      | Alberta |         | Quantity | Values  |         |         |         |       |
| 4 |      | Product | Year    | Quantity | Year    | Quantity | Year    | Quantity | Year  |
| 5 |      | Bike    | FY 2005 | 25      | 25      | 32      | 32      | 38      | 38    |
| 6 |      | FY 2006 | 9       | 14      | 14      | 15      | 15      | 8       | 8     |
| 7 |      | FY 2007 | 4       | 6       | 6       | 6       | 6       | 4       | 4     |
| 8 | Bike Total | 38  | 38  | 52  | 52  | 59  | 59  | 59  | 59 |
| 9 |      | Car | FY 2005 | 6       | 9       | 4       | 4       | 9       | 9     |
| 10 |       | FY 2006 | 1       | 1       | 4       | 4       | 1       | 1       | 1     |
| 11 |       | FY 2007 | 1       | 1       | 1       | 1       |        |        | 1     |
| 12 | Car Total | 8      | 8      | 10      | 10      | 9       | 9       | 10      | 10    |
| 13 | Grand Total | 46  | 46  | 62  | 62  | 62  | 62  | 68  | 69 |

## Export to Word

**Overview**
- Essential Grid provides built-in support to export data to Word.
- Users can download data from the PivotGrid into a Word document for offline verification and computation.
- Achieved using the `PivotWordExport` class.

### Code Example
The following code snippet demonstrates exporting PivotGrid to Word:

```csharp
[PivotWordExport]
```

## API Reference

- **PivotWordExport**: Exports PivotGrid data to Word.

## RAG Annotations
<!-- tags: [essential-pivotgrid, synchronization-api, cell-by-cell-export, pivottable-export, data-export, windowsforms] keywords: [pivotgrid, cell-by-cell, pivottable, data-export, word-export, syncfusion, windowsforms] -->
```

---

<!-- 페이지 41 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_040.jpeg
document_name: PivotGrid
page_number: 040
page_id: PivotGrid#page_040
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:55:46Z
fidelity: lossless
-->

## Essential PivotGrid WindowsForms

```csharp
pd.DrawGridPrintFooter += new GridPrintDocumentAdv.DrawGridHeaderFooterEventHandler(pd_DrawGridPrintFooter);
```

### [VB]

```vb
AddHandler pd.DrawGridPrintHeader, AddressOf pd_DrawGridPrintHeader
AddHandler pd.DrawGridPrintFooter, AddressOf pd_DrawGridPrintFooter
```

The following image shows the printed output of the pivot grid:

![Pivot Grid in Print Preview](https://i.imgur.com/unclear.jpg)

**Figure 15: Pivot Grid in Print Preview**

### Sample Link

A sample is available in the following location:

```
<Installed Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\PivotGrid.Windows\Samples\1.0\Pivot\Print\Print Grid Demo
```

## API Reference

### Namespace: Syncfusion.Windows.Forms.PivotGrid

#### Methods
- `DrawGridPrintHeader()`
- `DrawGridPrintFooter()`

### Properties
- `DrawGridPrintHeader`
- `DrawGridPrintFooter`

## Code Examples

### C#

```csharp
pd.DrawGridPrintFooter += new GridPrintDocumentAdv.DrawGridHeaderFooterEventHandler(pd_DrawGridPrintFooter);
```

### VB.NET

```vb
AddHandler pd.DrawGridPrintHeader, AddressOf pd_DrawGridPrintHeader
AddHandler pd.DrawGridPrintFooter, AddressOf pd_DrawGridPrintFooter
```

## Cross References

See also:

- [PivotGrid Documentation](https://www.syncfusion.com/documentation/windowsforms/pivotgrid)
- [EssentialStudio Samples](https://www.syncfusion.com/downloads/community-edition/latest)

<!-- tags: PivotGrid, WindowsForms, Print, Grid, Syncfusion, 11.4.0.26 keywords: PivotGrid, Print, DrawGridPrintFooter, DrawGridPrintHeader -->
```