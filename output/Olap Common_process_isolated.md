---
title: "Olap Common - Syncfusion SDK Documentation"
type: "api-documentation"
framework: "syncfusion"
version: "v11"
processing_mode: "Process Isolation (프로세스 격리)"
extracted_date: "1754724220.8886807"
optimized_for: ["llm-training", "rag-retrieval"]
scaling_approach: "3"
---

<!-- 페이지 1 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_001.jpeg
document_name: Olap Common
page_number: 001
page_id: Olap Common#page_001
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:14:30Z
fidelity: lossless
-->

# Olap Common

## Overview
- Comprehensive guide to using the Essential OlapCommon feature.
- Detailed documentation on the latest version, v.11.4.0.26.
- Focus on delivering innovation with ease in Essential Studio 2013 Volume 4.

## Content

### Introduction to OlapCommon
The **OlapCommon** component is a powerful tool within the Syncfusion Winforms library, designed to simplify and enhance the implementation of OLAP (Online Analytical Processing) functionalities. This section provides an overview of the component and its integration with the broader Essential Studio framework.

### Key Features
- **Advanced OLAP Support**: Handles data cube processing and multidimensional analysis effectively.
- **Intuitive Design**: Features a user-friendly API to simplify development and deployment.
- **Seamless Integration**: Works in conjunction with other Syncfusion Winforms components for holistic application development.

#### Usage and Implementation
Users can leverage the **OlapCommon** component to build robust applications that support business intelligence and data analytics. The component includes detailed examples and best practices for integration, ensuring a smooth development experience.

---

### API Reference
#### Namespace: `Syncfusion.OlapCommon`
- **Classes and Types**: Detailed explanation of the classes and types available within the `OlapCommon` namespace.
- **Properties**: List of properties available for customization and querying.
- **Methods**: Describes the methods for performing OLAP-specific operations.
- **Events**: Listing of events triggered during operations for monitoring and customization.

#### Properties
- `DataSource`: Specifies the data source for OLAP operations.
- `DimensionAxis`: Configures the dimensions for multidimensional analysis.

#### Methods
- `PerformAnalysis`: Executes OLAP analysis based on defined parameters.
- `GetDataCube`: Retrieves the resulting data cube after analysis.

#### Events
- `AnalysisCompleted`: Raised when the analysis operation is completed.
- `ErrorOccurred`: Triggered when an error occurs during analysis.

---

### Code Examples

#### Example: Basic Usage of OlapCommon
```csharp
// Import necessary namespace
using Syncfusion.OlapCommon;

// Initialize the OlapCommon component
OlapCommon olapCommon = new OlapCommon();

// Set up the data source
olapCommon.DataSource = new OlapDataSource("exampleSource");

// Configure dimensions
olapCommon.DimensionAxis.Add(new Dimension("Time"));
olapCommon.DimensionAxis.Add(new Dimension("Location"));

// Perform OLAP analysis
DataTable result = olapCommon.PerformAnalysis();

// Handle the result
if (result != null)
{
    foreach (DataRow row in result.Rows)
    {
        Console.WriteLine(row["Value"]);
    }
}
```

#### XML Configuration Example
```xml
<olapCommon>
    <dataSource>exampleSource</dataSource>
    <dimensionAxis>
        <dimension name="Time" />
        <dimension name="Location" />
    </dimensionAxis>
</olapCommon>
```

---

### Troubleshooting and Support
For further assistance or inquiries, visit the [Syncfusion Documentation](https://help.syncfusion.com/) or contact support via the [Syncfusion Support Portal](https://www.syncfusion.com/support/).

---

### Cross References
- **See also**:  
  - [Essential Studio Documentation](https://help.syncfusion.com/)
  - [OLAP Concepts](https://help.syncfusion.com/olap-concepts)
  - [Syncfusion Support](https://www.syncfusion.com/support)

---

<!-- tags: [OlapCommon, OLAP, Syncfusion Winforms, Essential Studio, version 11.4.0.26] keywords: [OlapCommon, OLAP, multidimensional analysis, data cube, business intelligence, Essential Studio, Syncfusion] -->
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
document_name: Olap Common
page_number: 005
page_id: Olap Common#page_005
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:14:53Z
fidelity: lossless
-->

# 1 Business Intelligence (BI)

## Overview
- This section defines Business Intelligence (BI), emphasizes its importance, and discusses recent advancements in BI technologies.
- It highlights the use of Online Analytical Processing (OLAP) as the standard for persisting and accessing BI data.
- It covers the evolution of BI implementation costs and introduces Microsoft's SQL Server Analysis Services (SSAS) as a cost-effective OLAP solution.

## Content

### 1.1 What is BI?
Business Intelligence (BI) simplifies information to enable all decision makers of an organization to access information easily. This helps the decision makers at all levels to understand, analyze, collaborate, and act on information anytime, anywhere.

Here is how Wikipedia defines [BI](https://en.wikipedia.org/wiki/Business_intelligence).

### 1.2 Why to use BI?
It is hard to overemphasize the importance of Business Intelligence (BI) in today's world. It is impossible to make strategic business decisions without analyzing the past business performance. Businesses are increasingly investing heavily in tools and services that let decision makers visually analyze data in myriad ways.

Several products and solutions have emerged to cater to the Business Intelligence market. Lessons have been learned, and currently Online Analytical Processing (OLAP) is the de facto standard for persisting and accessing BI data. Applications built using OLAP include sales reports, executive reports, forecasting, and so on.

### 1.3 What's new in BI?
While BI has been an expensive affair in the past, requiring several thousands of dollars in investment for integrating a solution into an enterprise, recent technological developments have considerably reduced the cost to implement and own an OLAP-based BI solution.

Microsoft's SQL Server Analysis Services (SSAS) is one such solution, which is a set of OLAP services provided as part of Microsoft SQL Server. The SSAS is available for almost a decade, is a mature, very cost-effective solution for maintaining multidimensional (also called cube) data. With an efficient OLAP storage mechanism in place, you only need another efficient OLAP visualization tool set to complete your BI needs. This is where Syncfusion OLAP controls come into place.

#### 1.3.1 Multi-dimensional Data
Multi-dimensional structure is defined as "a variation of the relational model that uses multidimensional structures to organize data and express the relationships between data." The structure is broken into cubes which are able to store and access data within the confines of each cube. Each cell within a multidimensional structure contains aggregated data related to elements along each of its dimensions. Even when data is manipulated, it is still easy to access as well as be a compact type of database. The data still remains interrelated. Multidimensional structure is quite popular for analytical databases that use OLAP applications. Analytical databases use these databases because of their ability to deliver answers quickly to complex business queries. Data can be seen through different ways, which gives a broader picture of a problem unlike other models.

## RAG Annotations
<!-- tags: [Olap, Business Intelligence, SQL Server Analysis Services, OLAP, BI, multidimensional data, cubes] keywords: [BI, decision makers, simplified information, strategic business decisions, analytical data, cost-effective solution, OLAP, SQL Server Analysis Services, cubes, multidimensional structure, complex queries] -->
```

---

<!-- 페이지 3 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_009.jpeg
document_name: Olap Common
page_number: 009
page_id: Olap Common#page_009
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:15:11Z
fidelity: lossless
-->

## OLAP Base

### Overview
- The OLAP Base is a class library that provides essential data processing capabilities required by OLAP controls.
- It serves as the processing unit for Syncfusion OLAP controls, managing tasks such as establishing connections, retrieving data, processing, and formatting input.
- Communication between Syncfusion OLAP controls and the OLAP cube is handled through the OlapDataManager class within the Syncfusion.Olap.Base namespace.

### Content

#### 3.1 OLAP Base
The OLAP Base is a class library that contains several namespaces and classes to perform data processing operations required by OLAP controls. OLAP base is the processing unit of all Syncfusion OLAP controls. From establishing the connection and retrieving the data, processing it and providing the formatted input for each control, everything is taken care by the OLAP base. Syncfusion OLAP controls communicate to the OLAP cube through the OlapDataManager class available in Syncfusion.Olap.Base namespace.

#### Figure 2: OLAP Base Architecture

![OLAP Base Architecture](#)

**Figure 2: OLAP Base Architecture**

---

## API Reference

### Namespaces and Classes Mentioned
- `OlapBase`
- `OlapDataManager`
- `MDXQuery`
- `OlapDataProvider`
  - `ExecuteCellSet`
  - `GetCubeSchema`
- `PivotEngine`
- `QueryEngine`
  - `MDXQuerySpecification`
    - `SELECT`
    - `WHERE`
  - `QueryEngineVersion3`

### Key Interaction Flow
- **User Input**: Through elements like `Reports`, `MDXQuery`, and `ItemSource`, user inputs are processed.
- **MDX Query Specification**: Constructs the MDX query using `SELECT` and `WHERE` clauses.
- **Query Execution**: The query is executed via `OlapDataManager` to fetch data and schema information from the cube.
- **Pivot Engine**: Processes the fetched data for visualization.
- **UI Controls**: Displays the processed data to the user.

---

<!-- tags: [syncfusion, winforms, olap, olap-base, olap-data-manager, mdx-query] keywords: [olap base, syncfusion winforms, pivot engine, ui controls, data processing, mdx query, item source] -->
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
document_name: Olap Common
page_number: 013
page_id: Olap Common#page_013
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:15:25Z
fidelity: lossless
-->

# Essential OlapCommon

## Overview
- Describes methods related to executing MDX queries, retrieving cube schemas, and managing member relationships in OLAP environments.
- Focuses on data retrieval and manipulation within multidimensional cubes.

## Content

### Table 2: Methods

| Method Name         | Description                                                                                                                                                                                                                     | Parameters                                                                                         | Return Type           | Reference Link |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|-----------------------|----------------|
| ExecuteCellSet     | Four arguments should be given to invoke this method. The arguments are MDX query as string, drill down state of result set as bool, query append info as bool and finally get the OlapReport. This method will generate the CellSet for the given query or OlapReport. | MDx Query as string, drill down state as bool, Property append status as bool and Current OlapReort of OlapDataManager | CellSet               | -              |
| GetCubeSchema      | This method will get the cube name and intersect the cube to get all the information about the cube and return an object of type CubeSchema, which will contain all the information. CubeSchema is a class in Data namespace. | Cube Name as string                                                                                     | CubeSchema            | -              |
| GetChildMembers    | This method will get the member element and the expander state and return the child members of the given member as MemberCollection.                                                                                     | Parent member as Member and drill down state as bool                                                  | MemberCollection      | -              |
| GetLevelMembers    | This method will get the level element as argument and return the member elements of that level as MemberCollection.                                                                                                       | Level                                                                                               | MemberCollection      | -              |
| GetParentMember    | This method is used to find the parent member of a member element. By passing a member element as an argument, this element will return its parent.                                                                            | Member                                                                                                | Member                | -              |

## Code Examples

Here is an example of how the `ExecuteCellSet` method might be used in C#:

```csharp
using Syncfusion.Olap;

// Assuming OlapReport and OlapDataManager are initialized
string mdxQuery = "SELECT ..."; // Your MDX query
bool drillDownState = true;
bool queryAppendInfo = false;
bool propertyAppendStatus = false;
var cellSet = manager.ExecuteCellSet(mdxQuery, drillDownState, queryAppendInfo, propertyAppendStatus, olapReport);
```

## API Reference

### Methods

#### ExecuteCellSet
- **Parameters:**
  - **Mdx Query as string**: The MDX query to execute.
  - **Drill down state of result set as bool**: Whether to drill down the results.
  - **Query append info as bool**: Whether to append query information.
  - **Property append status as bool**: Whether to include property append status.
  - **Current OlapReort of OlapDataManager**: The current Olap report.
- **Return Type**: CellSet
- **Description**: Executes the given MDX query and returns a CellSet for the given query or OlapReport.

#### GetCubeSchema
- **Parameters**: Cube Name as string
- **Return Type**: CubeSchema
- **Description**: Retrieves the schema of the specified cube.

#### GetChildMembers
- **Parameters**:
  - **Parent member as Member**: The parent member to get child members from.
  - **Drill down state as bool**: Whether to drill down to get child members.
- **Return Type**: MemberCollection
- **Description**: Retrieves the child members of the given member.

#### GetLevelMembers
- **Parameters**: Level
- **Return Type**: MemberCollection
- **Description**: Retrieves the member elements of the specified level.

#### GetParentMember
- **Parameters**: Member
- **Return Type**: Member
- **Description**: Finds the parent member of the given member element.

## Cross References

- See also:
  - [CubeSchema Documentation](#cube-schema)
  - [OlapReport Documentation](#olap-report)

<!-- tags: [Olap, MDX, CubeSchema, Member, OlapReport, CellSet] keywords: [ExecuteCellSet, GetCubeSchema, GetChildMembers, GetLevelMembers, GetParentMember] -->
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
document_name: Olap Common
page_number: 017
page_id: Olap Common#page_017
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:15:47Z
fidelity: lossless
-->

# Essential OlapCommon

## Overview
- Connecting to the **Active Pivot Server** using **C#** and **VB** code examples.
- Detailed explanation of properties and their descriptions in a table format.

## Content

### Connecting to Active Pivot Server

#### C#
```csharp
// Connecting to Active Pivot Server
OlapDataManager DataManager = new
OlapDataManager(@"Data Source=http://localhost:8081/var_s/xmla;
Initial Catalog=VarCubes;
User ID=; Password=; Transport Compression=None;");
DataManager.DataProvider.ProviderName = Syncfusion.Olap.DataProvider.Providers.ActivePivot;
```

#### VB
```vb
' Connecting to Active Pivot Server
Dim DataManager As OlapDataManager = New OlapDataManager("Data
Source=http://localhost:8081/var_s/xmla;  Initial Catalog=VarCubes;
User ID=; Password=; Transport Compression=None;")
DataManager.DataProvider.ProviderName = Syncfusion.Olap.DataProvider.Providers.ActivePivot
```

Click [here](#) for more information on Active Pivot server.

### 4.2.1 Properties and Methods

#### Properties

The properties and their descriptions are tabulated below:

| Property Name   | Description                                                                 | Type       | Value it Accepts | Reference Link |
|-----------------|------------------------------------------------------------------------------|------------|------------------|----------------|
| **ConnectionString** | Used to pass the connection string to establish the connection.<br>The user can also get the connection string using this property. | string     | String          | -              |
| **CurrentCellSet**   | The user can get the CellSet of their input from                             | CellSet    | -               | -              |

<!-- tags: [Olap, Active Pivot, C#, VB, Properties, Methods, ConnectionString, CurrentCellSet] keywords: [Syncfusion, OLAP, connection, properties, methods, string, cellset, data] -->
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
document_name: Olap Common
page_number: 021
page_id: Olap Common#page_021
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:16:00Z
fidelity: lossless
-->

## Overview

- Details the methods related to managing and manipulating reports in the Essential OlapCommon framework.
- Describes how to trigger events, remove, rename, save, and set reports.
- Focuses on the UseWhereClauseForSlicing property and its role in handling data slicing in MDX queries.

## Content

### Methods in OlapCommon

The following table outlines the methods available in the Essential OlapCommon framework for managing reports:

| Method Name          | Description                                                                 | Parameters                                 | Return Type | Reference Link         |
|----------------------|-----------------------------------------------------------------------------|--------------------------------------------|--------------|------------------------|
| NotifyReportChanged  | Used to trigger the ReportChanged event.                                    | -                                          | Void         | -                      |
| RemoveReport         | Used to get the report name as input and remove that report from report collection. | string                                     | Void         | RemoveReport           |
| RenameReport         | Used to rename the current report of OlapDataManager.                       | Index as int and new Report Name as string | Void         | RenameReport           |
| SaveReport           | Used to get the file name and store the current report collection along with the current state of the OlapDataManager as an Xml file. | string                                     | Void         | SaveReport             |
| SetCurrentReport     | Used to set an OlapReport as the current report of the OlapDataManager. This method is the initial method that will start data processing. | OlapReport                                | Void         | SetCurrentReport       |

### 4.2.2 UseWhereClauseForSlicing

The UseWhereClauseForSlicing property facilitates the user to decide whether the MDX query parser engine should consider 'Where' or 'Select' clause for slicing data.

#### Use Case Scenarios

While slicing dimensions with a specific range of measures using the 'Select' clause in MDX query, an exception is thrown. This can be resolved by using the 'Where' clause for slicing.

#### Example

Slicing the Date dimension from months of 2002 to months of 2003 will throw an exception when the 'Select' clause is used.

### Properties

#### Table 6: Property Table

| Property          | Description | Type     | Data Type | Reference links |
|-------------------|-------------|----------|-----------|-----------------|
| UseWhereClauseForSlicing | Specifies whether the MDX query parser engine should consider 'Where' or 'Select' clause for slicing data. | -         | -         | -           |

## API Reference

### Methods Summary

- **NotifyReportChanged**
  - **Purpose:** Used to trigger the ReportChanged event.
  - **Parameters:** None
  - **Return Type:** Void

- **RemoveReport**
  - **Purpose:** Used to remove a report from the collection based on the report name.
  - **Parameters:** string (report name)
  - **Return Type:** Void

- **RenameReport**
  - **Purpose:** Used to rename the current report.
  - **Parameters:** Index as int and new Report Name as string
  - **Return Type:** Void

- **SaveReport**
  - **Purpose:** Used to save the current report as an Xml file.
  - **Parameters:** string (file name)
  - **Return Type:** Void

- **SetCurrentReport**
  - **Purpose:** Used to set the current report and start data processing.
  - **Parameters:** OlapReport
  - **Return Type:** Void

## Code Examples

Example usage of the SetCurrentReport method:

```csharp
OlapReport report = new OlapReport();
OlapDataManager.SetCurrentReport(report);
```

## Page-level Navigation/TOC (if applicable)

- Methods in OlapCommon
- UseWhereClauseForSlicing
  - Use Case Scenarios
  - Example

## Cross References

See also:
- [OlapDataManager Class Reference](#)
- [MDX Query Handling in Olap Applications](#)

<!-- tags: [syncfusion-sdk, olap, mdx-query, report-management, syncfusion-winforms] keywords: [notifyreportchanged, removereport, renamereport, savereport, setcurrentreport, usewhereclauseforslicing, mdx, report, synchronization, data-processing] -->
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
document_name: Olap Common
page_number: 025
page_id: Olap Common#page_025
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:16:24Z
fidelity: lossless
-->

# Essential OlapCommon

## Content

### Dimension Element

#### Overview
A `dimension` object is a fundamental component in OLAP reporting, composed of basic information such as **Name, Hierarchy, Level, and Members**. This section details how to create and understand the structure of a dimension element, emphasizing its hierarchical organization and properties.

#### Description
A simple `dimension` object contains basic attributes such as name, hierarchy, level, and members. By specifying the hierarchy and level name, the dimension element can be created. The dimension element includes hierarchical details and information about each level and member within that hierarchy.

---

#### Hierarchical Details
- **Hierarchy Element**:  
  Each element of a dimension can be summarized using a **hierarchy**. A hierarchy represents a parent-child relationship, where a parent member consolidates its child members. Parent members can be further aggregated, forming a hierarchy that can be summarized at various levels.  
  **Example**:  
  - May 2005 → Second Quarter 2005 → Year 2005.

- **Level Element**:  
  A level element is a child of the hierarchy element and contains a set of members that share the same rank within the hierarchy.  
  **Example**: May 2005, June 2005, etc., are members at the same level (months).

- **Member Element**:  
  A member element represents a member of a specific level in a cube and is a child of a hierarchy element. Each member has properties that describe its details.

---

#### Member Properties
Member properties encapsulate basic information about each member in a tuple. This includes the member name, parent level, the number of children, and other metadata. These properties are available for all members at a given level.

---

### Table of Dimensional Properties

| Name          | Description                                                                 | Type | Value it accepts | Reference Link                                     |
|---------------|-----------------------------------------------------------------------------|------|------------------|-----------------------------------------------------|
|               | collection of elements that comes under the categorical axis.              |      |                  |                                                     |
| TogglePivot   | Used to swap the elements in the column axis and row axis.                | bool | True/False      | -                                                   |
| Tag           | Holds the backup information of the OLAP Report.                           | CLR. | String          | [Tag property in OlapReport](#)                   |

---

## Cross References

- **See also**: Hierarchy Overview, OLAP Report Tag Reference

---

### RAG Annotations

<!-- tags: [olap, dimension, hierarchy, level, member, WinForms, Syncfusion] keywords: [dimension object, hierarchy, level element, member element, toggle pivot, backup information, olap report] -->
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
document_name: Olap Common
page_number: 029
page_id: Olap Common#page_029
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:16:40Z
fidelity: lossless
-->

## Key Performance Indicator (KPI) Element

### Overview
- Key Performance Indicators (KPIs) are collections of calculations associated with a measure group in a cube, used to evaluate business success.
- KPIs typically use MDX expressions or calculated members.
- Metadata is included to guide client application display of KPI results.
- Types include KPI Goal, Status, Trend, and Value.
- KPI elements are created by specifying details like name and the indicators included.

### Content

#### Key Performance Indicator (KPI) Element
Key Performance Indicator (KPI) is a collection of calculations that are associated with a measure group in a cube that are used to evaluate business success. Typically, these calculations are a combination of Multidimensional Expressions (MDX) or calculated members. The KPIs also have an additional metadata that provides information about how client applications should display the results of the KPI's calculations.

The different types of KPI Indicators are:

- KPI Goal
- KPI Status
- KPI Trend
- KPI Value

We can create a KPI element by specifying its name and giving details of the indicator that are included in the element.

#### Code Example in C#

```csharp
KpiElements kpiElement = new KpiElements();

// Specifying the KPI Element name and configuring its Indicators
kpiElement.Elements.Add(new KpiElement { Name = "Internet Revenue", ShowKPIGoal = true, ShowKPIStatus = true, ShowKPIValue = true, ShowKPITrend = true });
```

#### Code Example in VB

```vb
Dim kpiElement As KpiElements = New KpiElements()

' Specifying the KPI Element name and configuring its Indicators
kpiElement.Elements.Add(New KpiElement With { .Name = "Internet Revenue", .ShowKPIGoal = True, .ShowKPIStatus = True, .ShowKPIValue = True, .ShowKPITrend = True })
```

### NamedSet Element

#### Overview
- A named set is a collection of tuples and members defined and saved as part of the cube definition.
- Named sets reside inside the sets folder under a dimension.
- They can be dragged to Categories/Series/Slicer axes in Axes Element Builder.
- MDX allows defining named sets for easier handling of complex expressions.

### Content

#### NamedSet Element
A named set is a collection of tuples and members, which can be defined and saved as a part of the cube definition. Named set records reside inside the sets folder, which is under a dimension element. These elements can be dragged to Categories/Series/Slicer axis of Axes Element Builder. To help make working with a lengthy, complex, or commonly used expression easier, Multidimensional Expressions (MDX) lets you to define a named set.

The following code will describe the creation of a Named set Element:

## Page-level Navigation/TOC (if applicable)
- If the body contains a local Table of Contents for this page, keep it as a bullet/numbered list with links/text as shown. Do not create links that don’t exist.
- Ignore global site TOC or breadcrumbs unless the page explicitly describes them.

## Cross References
- If other pages or sections are referenced in the text, maintain those links or anchor text.
- If cross-referencing is not possible, note explicit links or text references.

## RAG Annotations
<!-- tags: [syncfusion, olap, namedset, kpi, mdx, cubes, winforms, 11.4.0.26] keywords: [key performance indicators, named set, multidimensional expressions, cube, kpi goal, kpi status, kpi trend, kpi value, axes element builder] -->
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
document_name: Olap Common
page_number: 033
page_id: Olap Common#page_033
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:17:00Z
fidelity: lossless
-->

## Essential OlapCommon

```csharp
SubsetElement subSetElementRow = new SubsetElement(3);
subSetElementRow.Name = "Top 3 Elements";
olapReport.CategoricalElements.SubSetElement = subSetElementColumn;
olapReport.SeriesElements.SubSetElement = subSetElementRow;
```

```vb
[VB]
Dim subSetElementColumn As SubsetElement = New SubsetElement(5)
subSetElementColumn.Name = "Top 5 Elements"
Dim subSetElementRow As SubsetElement = New SubsetElement(3)
subSetElementRow.Name = "Top 3 Elements"
olapReport.CategoricalElements.SubSetElement = subSetElementColumn
olapReport.SeriesElements.SubSetElement = subSetElementRow
```

### 4.3.9 Summary Elements

**Summary elements come when the base deals with Non-OLAP data. This is similar to the measure element in the OLAP data. This element will be considered as the measure and this value will be displayed in the value cell.**

The following codes will describe the creation of the Summary elements:

```csharp
// Specifying the Summary Elements
SummaryElements summaries = new SummaryElements();
summaries.Add(new SummaryInfo { Column = "Quantity", Key = "Quantity", Type = SummaryType.Sum });
summaries.Add(new SummaryInfo { Column = "Amount", Key = "Amount", Type = SummaryType.Sum, FormatString = "{0:c}" });
```

```vb
[VB]
' Specifying the Summary Elements
Dim summaries As SummaryElements = New SummaryElements()
summaries.Add(New SummaryInfo With {.Column = "Quantity", .Key = "Quantity", .Type = SummaryType.Sum})
summaries.Add(New SummaryInfo With {.Column = "Amount", .Key = "Amount", .Type = SummaryType.Sum, .FormatString = "{0:c}"})
```
```html
<!-- tags: [OlapCommon, subsetElement, summaryElements, OLAPdata, measureElement, NonOLAPdata, SummaryInfo, SummaryElements, Quantity, Amount] keywords: [subsetElement, SummaryElements, SummaryInfo, OLAPdata, NonOLAPdata, measureElement, Top3Elements, Top5Elements, Quantity, Amount, FormatString] -->
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
document_name: Olap Common
page_number: 037
page_id: Olap Common#page_037
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:17:14Z
fidelity: lossless
-->

## Content

### 4.3.11.1.1 Simple Report

[C#]

```csharp
OlapReport olapReport = new OlapReport();
olapReport.Name = "Customer Report";
olapReport.CurrentCubeName = "Adventure Works";

DimensionElement dimensionElementColumn = new DimensionElement();
//Specifying the Name for the Dimension Element
dimensionElementColumn.Name = "Customer";
dimensionElementColumn.HierarchyName = "Customer Geography";
dimensionElementColumn.AddLevel("Customer Geography", "Country");

MeasureElements measureElementColumn = new MeasureElements();
measureElementColumn.Elements.Add(new MeasureElement { Name = "Internet Sales Amount" });

DimensionElement dimensionElementRow = new DimensionElement();
//Specifying the Dimension Name
dimensionElementRow.Name = "Date";
dimensionElementRow.AddLevel("Fiscal", "Fiscal Year");

//// Adding Column Members
olapReport.CategoricalElements.Add(dimensionElementColumn);
//// Adding Measure Element
olapReport.CategoricalElements.Add(measureElementColumn);
//// Adding Row Members
olapReport.SeriesElements.Add(dimensionElementRow);
```

[VB]

```vb
Dim olapReport As OlapReport = New OlapReport()
olapReport.Name = "Customer Report"
olapReport.CurrentCubeName = "Adventure Works"

Dim dimensionElementColumn As DimensionElement = New DimensionElement()
' Specifying the Name for the Dimension Element
dimensionElementColumn.Name = "Customer"
dimensionElementColumn.HierarchyName = "Customer Geography"
dimensionElementColumn.AddLevel("Customer Geography", "Country")

Dim measureElementColumn As MeasureElements = New MeasureElements()
measureElementColumn.Elements.Add(New MeasureElement With {.Name = "Internet Sales Amount"})
```

---

## API Reference

### Namespaces and Classes

- **Namespace**: `OlapReport`
- **Class**: `OlapReport`
- **Properties**:
  - `Name`: Specifies the name of the report.
  - `CurrentCubeName`: Specifies the name of the current cube.
- **Methods**:
  - `AddLevel(hierarchyName, levelName)`: Adds a specific level to the dimension element.
  - `CategoricalElements.Add(dimensionElement)`: Adds column or measure elements to the report.
  - `SeriesElements.Add(dimensionElement)`: Adds row elements to the report.

### Parameters

- **Name**: 
  - **Type**: `string`
  - **Description**: The name of the report.
  - **Default**: None
  - **Required**: Yes
- **CurrentCubeName**: 
  - **Type**: `string`
  - **Description**: The name of the cube used in the report.
  - **Default**: None
  - **Required**: Yes

### Exceptions

- None explicitly listed. Ensure proper handling of null or invalid inputs.

---

## Code Examples (continued)

The above code samples demonstrate how to set up a simple report using the `OlapReport` class in both C# and VB. These examples illustrate how to specify the cube name, dimension elements, measure elements, and row/column configurations required for generating the report.

---

## Cross References

- For detailed information about OLAP concepts and terminology, refer to the official documentation or related sections in this guide.
- Additional examples and advanced configurations can be found in the API reference and examples provided with Syncfusion WinForms.

<!-- tags: [Syncfusion, Winforms, OLAP, Report, Dimension, Measure] keywords: [OlapReport, DimensionElement, MeasureElements, CurrentCubeName, AddLevel, CategoricalElements, SeriesElements] -->
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
document_name: Olap Common
page_number: 041
page_id: Olap Common#page_041
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:17:33Z
fidelity: lossless
-->

# Essential OlapCommon

## Overview
- Demonstrates specifying excluded row elements in an OLAP report.
- Adding the date dimension element with fiscal year, month, fiscal quarter, and fiscal semester hierarchy levels.
- Creating column and measure elements.
- Adding row members to the report.

## Content

### Specifying Excluded Row Elements

The following code snippet demonstrates how to specify excluded row elements in an OLAP report:

```csharp
// Specifying the Excluded row elements
DimensionElement excludedRowElement = new DimensionElement();
excludedRowElement.Name = "Date";
excludedRowElement.AddLevel("Fiscal", "Fiscal Year");
excludedRowElement.AddLevel("Fiscal", "Month");
excludedRowElement.AddLevel("Fiscal", "Fiscal Quarter");
excludedRowElement.AddLevel("Fiscal", "Fiscal Semester");
excludedRowElement.Hierarchy.LevelElements["Fiscal Year"].Add("FY 2002");
excludedRowElement.Hierarchy.LevelElements["Fiscal Year"].Add("FY 2004");
excludedRowElement.Hierarchy.LevelElements["Fiscal Year"].Add("FY 2005");
excludedRowElement.Hierarchy.LevelElements["Fiscal Semester"].Add("H2 FY 2003");
excludedRowElement.Hierarchy.LevelElements["Month"].Add("August 2002");
excludedRowElement.Hierarchy.LevelElements["Month"].Add("September 2002");
excludedRowElement.Hierarchy.LevelElements["Fiscal Quarter"].Add("Q2 FY 2003");
excludedRowElement.Hierarchy.LevelElements["Fiscal Quarter"].Add("Q2 FY 2003");

/// Adding Column Members
olapReport.CategoricalElements.Add(dimensionElementColumn, excludedColumn);
/// Adding Measure Element
olapReport.CategoricalElements.Add(measureElementColumn);
/// Adding Row Members
olapReport.SeriesElements.Add(dimensionElementRow, excludedRowElement);
```

### VB Example

The following Visual Basic code snippet demonstrates the configuration of an OLAP report, similar to the above example:

```vb
[VB]

Dim olapReport As OlapReport = New OlapReport()
olapReport.Name = "Customer Report"
olapReport.CurrentCubeName = "Adventure Works"
Dim dimensionElementColumn As DimensionElement = New DimensionElement()
' Specifying the Name for the Dimension Element
dimensionElementColumn.Name = "Customer"
' Specifying the Hierarchy Name
dimensionElementColumn.HierarchyName = "Customer Geography"
dimensionElementColumn.AddLevel("Customer Geography", "Country")
```

## API Reference

### Methods
- `AddLevel(hierarchyName, levelName)`: Adds a level to the specified hierarchy.
- `Add`: Adds elements to the `CategoricalElements` or `SeriesElements` collections.

## Code Examples

### C# Example
```csharp
DimensionElement excludedRowElement = new DimensionElement();
excludedRowElement.Name = "Date";
excludedRowElement.AddLevel("Fiscal", "Fiscal Year");
excludedRowElement.AddLevel("Fiscal", "Month");
excludedRowElement.Hierarchy.LevelElements["Fiscal Year"].Add("FY 2002");
// ... other level additions
olapReport.SeriesElements.Add(dimensionElementRow, excludedRowElement);
```

### VB Example
```vb
Dim olapReport As OlapReport = New OlapReport()
Dim dimensionElementColumn As DimensionElement = New DimensionElement()
dimensionElementColumn.HierarchyName = "Customer Geography"
dimensionElementColumn.AddLevel("Customer Geography", "Country")
```

## Cross References

- Refer to the main OLAP documentation for detailed explanations on hierarchy and element configurations.

<!-- tags: [Olap, OLAPReport, DimensionElement, Hierarchy, Level, MeasureElement, SeriesElements] keywords: [Fiscal Year, Month, Fiscal Quarter, Fiscal Semester, Customer Geography, Country, Customer, Report] -->
```

---

<!-- 페이지 12 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_045.jpeg
document_name: Olap Common
page_number: 045
page_id: Olap Common#page_045
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:17:54Z
fidelity: lossless
-->

## Essential OlapCommon

```vb
' Specifying the Dimension Name
dimensionElementRow.Name = "Date"
dimensionElementRow.AddLevel("Fiscal", "Fiscal Year")

Dim sortElement As SortElement = New SortElement(AxisPosition.Categorical, SortOrder.BDESC, True)
sortElement.Element.UniqueName = "[Measures].[Internet Sales Amount]"

''' Adding Column Members
olapReport.CategoricalElements.Add(dimensionElementColumn)

''' Adding Measure Element
olapReport.CategoricalElements.Add(measureElementColumn)

' Adding Sort Element
olapReport.CategoricalElements.Add(sortElement)

''' Adding Row Members
olapReport.SeriesElements.Add(dimensionElementRow)
```

## 4.3.11.1.5 Report with Filter

### [C#]

```csharp
OlapReport olapReport = new OlapReport();

olapReport.Name = "Customer Report";
olapReport.CurrentCubeName = "Adventure Works";

DimensionElement dimensionElementColumn = new DimensionElement();
// Specifying the Name for the Dimension Element
dimensionElementColumn.Name = "Customer";
dimensionElementColumn.AddLevel("Customer Geography", "Country");

// Creating Measure Element
MeasureElements measureElementColumn = new MeasureElements();
measureElementColumn.Elements.Add(new MeasureElement { Name = "Internet Sales Amount" });

DimensionElement dimensionElementRow = new DimensionElement();
// Specifying the Dimension Name
```
```

---

<!-- 페이지 13 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_049.jpeg
document_name: Olap Common
page_number: 049
page_id: Olap Common#page_049
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:18:05Z
fidelity: lossless
-->

## Essential OlapCommon

```vb
dimensionElementColumn.Name = "Customer"

' Specifying the Hierarchy Name
dimensionElementColumn.HierarchyName = "Customer Geography"
dimensionElementColumn.AddLevel("Customer Geography", "Country")

Dim measureElementColumn As MeasureElements = New MeasureElements()
measureElementColumn.Elements.Add(New MeasureElement With {.Name = "Internet Sales Amount"})

Dim dimensionElementRow As DimensionElement = New DimensionElement()
' Specifying the Dimension Name
dimensionElementRow.Name = "Date"
dimensionElementRow.AddLevel("Fiscal", "Fiscal Year")

' Specifying the SubsetElement
' Specify the start index and end index to retrieve the records.
Dim subSetElementColumn As SubsetElement = New SubsetElement(5)
subSetElementColumn.Name = "Top 5 Elements"

Dim subSetElementRow As SubsetElement = New SubsetElement(3)
subSetElementRow.Name = "Top 3 Elements"

''' Adding Column Members
olapReport.CategoricalElements.Add(dimensionElementColumn)
''' Adding Measure Element
olapReport.CategoricalElements.Add(measureElementColumn)
olapReport.CategoricalElements.SubSetElement = subSetElementColumn
''' Adding Row Members
olapReport.SeriesElements.Add(dimensionElementRow)
olapReport.SeriesElements.SubSetElement = subSetElementRow
```

## 4.3.11.1.7 Drill down report

---

```html
© 2013 Syncfusion. All rights reserved. | Page 49
```

<!-- tags: [OlapCommon, WinForms, Version 11.4.0.26] keywords: [dimensionElementColumn, measureElementColumn, subsetElementColumn, subsetElementRow, olapReport, categorical elements, series elements, drill down report] -->
```

---

<!-- 페이지 14 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_053.jpeg
document_name: Olap Common
page_number: 053
page_id: Olap Common#page_053
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:18:17Z
fidelity: lossless
-->

# Essential OlapCommon

## Overview
- Demonstrates filtering the top 5 elements of "Internet Sales Amount" in an OLAP report.
- Constructs a report with categorized elements and series elements for specific dimensions and measures.

## Content

### Example Code in C#

```csharp
//Filter the top 5 elements of "Internet Sales Amount".
TopCountElement topCountElement = new TopCountElement(AxisPosition.Categorical, 5);
topCountElement.MeasureName = "Internet Sales Amount";

//// Adding Column Members
olapReport.CategoricalElements.Add(dimensionElementColumn);
////Adding Measure Element
olapReport.CategoricalElements.Add(measureElementColumn);
////Adding Measure Element
olapReport.CategoricalElements.Add(topCountElement);
////Adding Row Members
olapReport.SeriesElements.Add(dimensionElementRow);
```

### Example Code in VB

```vb
[VB]

Dim olapReport As OlapReport = New OlapReport()
olapReport.Name = "Customer Report"
olapReport.CurrentCubeName = "Adventure Works"

Dim dimensionElementColumn As DimensionElement = New DimensionElement()
' Specifying the Name for the Dimension Element
dimensionElementColumn.Name = "Customer"
dimensionElementColumn.AddLevel("Customer Geography", "Country")

' Creating Measure Element
Dim measureElementColumn As MeasureElements = New MeasureElements()
measureElementColumn.Elements.Add(New MeasureElement With {.Name = "Internet Sales Amount"})

Dim dimensionElementRow As DimensionElement = New DimensionElement()
' Specifying the Dimension Name
dimensionElementRow.Name = "Date"
dimensionElementRow.AddLevel("Fiscal", "Fiscal Year")

' Filter the top 5 elements of "Internet Sales Amount".
```

## Page-level Navigation/TOC (if applicable)
- This page focuses on using `TopCountElement` to filter elements in an OLAP report.

<!-- tags: [product, module, control, api, version?] keywords: [Olap Common, TopCountElement, OLAP report, filtering, VB, C#] -->
```

---

<!-- 페이지 15 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_057.jpeg
document_name: Olap Common
page_number: 057
page_id: Olap Common#page_057
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:18:30Z
fidelity: lossless
-->

# Essential OlapCommon

## Overview

- Adding calculated members in a collection using C# code.
- Demonstrating the configuration of categorical and series elements for reports.

## Content

### Adding Calculated Members in Calculated Member Collection

The following C# code snippet shows how to add calculated members to the `CalculatedRouteMembers` collection.

```csharp
//// Adding Calculated members in calculated member collection
olapReport.CalculatedMembers.Add(calculatedMeasure1);
olapReport.CalculatedMembers.Add(calculateDimension);
olapReport.CalculatedMembers.Add(calculatedMeasure2);

//// Adding Column Members
olapReport.CategoricalElements.Add(dimensionElementColumn);
olapReport.CategoricalElements.Add(calculateDimension);
//// Adding Measure Element
olapReport.CategoricalElements.Add(measureElementColumn);
olapReport.CategoricalElements.Add(calculatedMeasure1);
olapReport.CategoricalElements.Add(calculatedMeasure2);

//// Adding Row Members
olapReport.SeriesElements.Add(dimensionElementRow);
```

### VB Code Implementation

The following VB code snippet provides details on configuring dimension elements and adding calculated measures.

```vb
[VB]

Dim dimensionElementColumn As DimensionElement = New DimensionElement()
' Specifying the Name for the Dimension Element
dimensionElementColumn.Name = "Customer"
dimensionElementColumn.HierarchyName = "Customer Geography"
dimensionElementColumn.AddLevel("Customer Geography", "Country")

Dim internalDimension As DimensionElement = New DimensionElement()
internalDimension.Name = "Product"
internalDimension.AddLevel("Product Categories", "Category")

' Calculated Measure
Dim calculatedMeasure1 As CalculatedMember = New CalculatedMember()
calculatedMeasure1.Name = "Oder on Discount"
calculatedMeasure1.Expression = "[Measures].[Order Quantity] + ([Measures].[Order Quantity] * 0.10)"
calculatedMeasure1.AddElement(New MeasureElement With {.Name = "Order Quantity"})
```

### Explanation of the Code

- **DimensionElement Column**: Configures the dimension element for "Customer," specifying the hierarchy and level.
- **DimensionElement Row**: Configures the dimension element for "Product," specifying another hierarchy and level.
- **Calculated Measure**: Defines a calculated member named "Oder on Discount," calculating the order quantity plus 10% of the order quantity.

## API Reference

### Namespaces and Classes Used

- `DimensionElement`: Represents a dimension element for configuring categorical elements.
- `CalculatedMember`: Represents a calculated member for adding to the `CalculatedMembers` collection.

### Methods Used

- `Add(...)`:
  - Adds elements to the collection.
  - Parameters include `DimensionElement` or `CalculatedMember` objects based on context.

### Properties Set

- `Name`: Specifies the name of the dimension element or calculated member.
- `HierarchyName`: Specifies the hierarchy associated with the dimension element.
- `AddLevel(...)`: Associates a hierarchy level with the dimension element.
- `Expression`: Specifies the formula for calculating the value of a calculated member.

## Code Examples

### C# Example

```csharp
olapReport.CalculatedMembers.Add(calculatedMeasure1);
olapReport.CategoricalElements.Add(dimensionElementColumn);
olapReport.SeriesElements.Add(dimensionElementRow);
```

### VB Example

```vb
Dim dimensionElementColumn As DimensionElement = New DimensionElement()
internalDimension.Name = "Product"
calculatedMeasure1.Expression = "[Measures].[Order Quantity] + ([Measures].[Order Quantity] * 0.10)"
calculatedMeasure1.AddElement(New MeasureElement With {.Name = "Order Quantity"})
```

---

<!-- tags: [OLAP, dimension elements, calculated members, VB, C#] keywords: [calculated members, dimension elements, hierarchy, level, expression, calculated measures] -->
```

---

<!-- 페이지 16 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_061.jpeg
document_name: Olap Common
page_number: 061
page_id: Olap Common#page_061
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:18:53Z
fidelity: lossless
-->

# Essential OlapCommon

## Code Examples

```csharp
' Adding Column Members
olapReport.CategoricalElements.Add(dimensionElementColumn)
olapReport.CategoricalElements.Add(kpiElement)
' Adding Measure Elements
olapReport.CategoricalElements.Add(measureElementColumn)
' Adding Row Members
olapReport.SeriesElements.Add(dimensionElementRow)
```

## Content

### Report with member properties

```csharp
[C#]

OlapReport olapReport = new OlapReport();
olapReport.Name = "Employee Sales Report";
// Specifying the current cube name
olapReport.CurrentCubeName = "Adventure Works";

MeasureElements measureElementColumn = new MeasureElements();
// Specifying the Name for the Measure Element
measureElementColumn.Elements.Add(new MeasureElement { Name = "Sales Amount Quota" });

DimensionElement dimensionElementRow = new DimensionElement();
// Specifying the Dimension Name
dimensionElementRow.Name = "Employee";
// Specifying the Hierarchy and level name for the Dimension Element
dimensionElementRow.AddLevel("Employees", "Employee Level 02");
dimensionElementRow.Hierarchy.LevelElements["Employee Level 02"].IncludeAvailableMembers = true;

// Adding the Member properties to the Dimension Element
dimensionElementRow.MemberProperties.Add(new MemberProperty("Title", "[Employee].[Employees].[Title]"));
dimensionElementRow.MemberProperties.Add(new MemberProperty("Phone", "[Employee].[Employees].[Phone]"));
dimensionElementRow.MemberProperties.Add(new MemberProperty("Email Address",
```

## Page-level Navigation/TOC (if applicable)

- **Report with member properties**

## Cross References

- See also: [previous section on adding column, measure, and row members]

<!-- tags: [OlapReport, DimensionElement, MeasureElements, MemberProperty, Syncfusion Winforms] keywords: [OlapReport properties, DimensionElementRow, IncludeAvailableMembers, MemberProperties, Employee Sales Report] -->
```

---

<!-- 페이지 17 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_065.jpeg
document_name: Olap Common
page_number: 065
page_id: Olap Common#page_065
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:19:05Z
fidelity: lossless
-->

## Content

### 4.3.12 Binding the OlapReport to OlapDataManager

#### Overview
- Specifies the process of binding the created report to the OlapDataManager.
- Sets the report to the current report property of OlapDataManager for processing, querying, and cell set creation.

```vb
' Specifying the Column Dimension Element
Dim dimensionElementColumn As DimensionElement = New DimensionElement ()
dimensionElementColumn.Name = "Geography"
dimensionElementColumn.Hierarchy = New HierarchyElement () With { .Name = "Geography Hierarchy" }

dimensionElementColumn.Hierarchy.LevelElements.Add(New LevelElement () With { .Name = "Country" })
dimensionElementColumn.Hierarchy.LevelElements.Add(New LevelElement () With { .Name = "State" })

' Specifying the Summary Elements
Dim summaries As SummaryElements = New SummaryElements ()
summaries.Add(New SummaryInfo With { .Column = "Quantity", .Key = "Quantity", .Type = SummaryType.Sum })
summaries.Add(New SummaryInfo With { .Column = "Amount", .Key = "Amount" , .Type = SummaryType.Sum, .FormatString = "{0:c}" })

' Adding the Row Elements
olapReport.SeriesElements.Add(New Item With { .ElementValue = summaries })
```

Once the report is created, the report is set to the current report property of the OlapDataManager. Further data processing, query creation, and cell set creation starts from the OlapDataManager.

### 4.3.13 Paging
#### Overview
- Enables the user to view large records by breaking them into smaller segments.
- Demonstrates how to enable paging in a report using the `EnablePaging` property.

#### Enabling Paging

##### C#
```csharp
olapDataManager.CurrentReport.EnablePaging = true;
```

##### VB
```vb
olapDataManager.CurrentReport.EnablePaging = True
```

The user can customize the page settings such as current page, page size (for both row and column).

---

## API Reference

- **Namespace**: `Syncfusion.Olap.Manager`
- **Class**: `OlapDataManager`
  - **Property**:
    - `CurrentReport`: Used to set the report to the current report property.
  - **Method**:
    - `GetCurrentReport()`: Retrieves the currently set report.
- **Class**: `OlapReport`
  - **Property**:
    - `EnablePaging`: Enables paging for the report.

---

## Code Examples

#### Sample C# Code for Enabling Paging

```csharp
using Syncfusion.Olap.Manager;

// Assuming olapDataManager is an instance of OlapDataManager
olapDataManager.CurrentReport.EnablePaging = true;
```

#### Sample VB Code for Enabling Paging

```vb
Imports Syncfusion.Olap.Manager

' Assuming olapDataManager is an instance of OlapDataManager
olapDataManager.CurrentReport.EnablePaging = True
```

---

## Page-level Navigation/TOC

### 4.3.12 Binding the OlapReport to OlapDataManager
- Specifying the Column Dimension Element
- Specifying the Summary Elements
- Adding the Row Elements

### 4.3.13 Paging
- Enabling Paging
- Customizing Page Settings

---

## Cross References

- See also:
  - [Geography Hierarchy]
  - [Summary Elements]
  - [OlapDataManager]
  - [OlapReport]
  - [Paging Feature]

---

<!-- tags: [syncfusion, winforms, olap, olapreport, olapdatamanager, paging, enablepaging, reportbinding] keywords: [OlapReport, OlapDataManager, enablepaging, summary, geography, hierarchy, pagingfunctionality] -->
```

---

<!-- 페이지 18 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_069.jpeg
document_name: Olap Common
page_number: 069
page_id: Olap Common#page_069
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:19:25Z
fidelity: lossless
-->

## Essential OlapCommon

```csharp
olapDataManager.MdxQuery = "MDX Query Here"
olapDataManager.ExecuteCellSet()
```

### 4.3.17 Virtual KPI Element

Key performance indicators can be virtually defined during run time. This feature enables users to create KPIs without storing them in SSAS (SQL Server Analysis Services). This feature is very useful when users want to define KPIs at run time and also minimize the time necessary to create KPIs.

#### 4.3.17.1 Properties

**Table 12: VirtualKpiElement Class Properties**

| Property             | Description                                    | Type | Data Type |
|----------------------|------------------------------------------------|------|-----------|
| Name                 | Gets or sets the name for VirtualKpiElement.  | CLR  | String    |
| KpiValueExpression   | Gets or sets the value which indicates the value expression for VirtualKpiElement. | CLR  | String    |
| KpiGoalExpression    | Gets or sets the value which indicates the goal expression for VirtualKpiElement. | CLR  | String    |
| KpiStatusExpression  | Gets or sets the value which indicates the status expression for VirtualKpiElement. | CLR  | String    |
| KpiTrendExpression   | Gets or sets the value which indicates the trend expression for VirtualKpiElement. | CLR  | String    |
| KpiTrendGraphic      | Gets or sets the name of the graphic used to represent the result of the trend expression. | CLR  | String    |
| KpiStatusGraphic     | Gets or sets the name of the graphic used to represent the result of the status expression. | CLR  | String    |

**Table 13: OlapReport Class Properties**

<!-- tags: [syncfusion, winforms, olap, kpi, virtual kpi, mdx query, sql server analysis services, ssas, essential olapcommon] keywords: [kpi, runtime, mdx, ssas, virtual, data type, expression, status, trend, graphic, asynchronous, essential olap] -->
```

---

<!-- 페이지 19 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_073.jpeg
document_name: Olap Common
page_number: 073
page_id: Olap Common#page_073
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:19:39Z
fidelity: lossless
-->

# Essential OlapCommon

```csharp
1,
    [Date].[Fiscal].CurrentMember
)
)
Then 0

When VBA!Abs
(
(
[Measures].[Reseller Sales Amount] -
(
[Measures].[Reseller Sales Amount],
ParallelPeriod
(
[Date].[Fiscal].[Fiscal Year],
1,
[Date].[Fiscal].CurrentMember
)
)
)
/
(
[Measures].[Reseller Sales Amount],
ParallelPeriod
(
[Date].[Fiscal].[Fiscal Year],
1,
[Date].[Fiscal].CurrentMember
)
)
) <=.02
Then 0
```

## Example Explanation

The provided code snippet is an MDX (Multidimensional Expressions) statement, commonly used in OLAP (Online Analytical Processing) systems to query and manipulate multidimensional data. Here's a breakdown of the key components:

- **`[Date].[Fiscal].CurrentMember`**: This refers to the currently selected fiscal date member. It's a dimension member that helps in specifying a particular period in the fiscal calendar.

- **`[Measures].[Reseller Sales Amount]`**: This measures the amount of sales made by resellers. It's a quantitative measure in the cube.

- **`ParallelPeriod` Function**: This function retrieves the corresponding member in a parallel period relative to the current member. In the given code, it references the fiscal year one period before the current fiscal period.

- **`ABS` Function**: This function computes the absolute value of the difference between the current fiscal year's reseller sales amount and the reseller sales amount in the parallel period.

- **Conditional Statement (`Then 0`)**: The `When` clause checks a condition and sets the result to `0` when the condition is met. Specifically, it checks if the absolute percentage change in reseller sales is less than or equal to 2%.

This MDX statement is used to calculate and compare reseller sales amounts for the current fiscal period and the previous fiscal year's equivalent period. It ensures that if the change is minimal (less than or equal to 2%), the result is set to `0`, indicating no significant change.

## Related Topics

For further details on MDX and its components, refer to:
- MDX Functions (e.g., `ABS`, `ParallelPeriod`)
- Dates and Times in MDX
- Conditional Expressions in MDX

<!-- tags: [syncfusion, winforms, olap, mdx, essentials] keywords: [mdx, fiscal period, reseller sales amount, parallel period, absolute change, conditional statements] -->
```

---

<!-- 페이지 20 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_077.jpeg
document_name: Olap Common
page_number: 077
page_id: Olap Common#page_077
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:19:57Z
fidelity: lossless
-->

# Essential Olap Common

## Steps in Establishing a Connection and Processing Data

### Overview
- Establish a connection to the specified data source using a connection string containing details about the data source.
- Connect to a server or an offline cube.
- Provide input for data processing using either MDX Query or OlapReport.
- Process the data based on the input type, where the method differs for OLAP base.
- Execute the MDX query or generate an MDX query from the OlapReport.
- Format the result set for the controls and display the output.

### Detailed Steps

1. **Get the input to establish a connection to the specified data source**:
   - The connection information is provided as a connection string that includes details about the data source.
   - Example connection string: `"DataSource = localhost; Initial Catalog = Adventure Works DW";`

2. **Connect to a server or an offline cube**:
   - Establish a connection to the desired data source.

3. **Provide input for data processing**:
   - Once the connection is established, input two types of inputs to process the OLAP data:
     - **MDX Query**: Write an MDX Query for the database and use that query as input.
     - **OlapReport**: Create an OLAP report and provide that report as input to the OlapDataManager.

4. **Output based on input type**:
   - The output will be the same regardless of the input type.
   - However, the processing method will differ in the OLAP base depending on the input type.

5. **Execute the MDX query**:
   - If an MDX query is given as input, the query will be executed on the connected database.

6. **Process the OlapReport**:
   - If an OlapReport is given as input:
     - **a.** An MDX query specification will be created based on the OlapReport.
     - **b.** The MDX query will be generated using the OlapQueryBuilderEngine.
     - **c.** The generated query will be executed on the connection database.

7. **Obtain the result**:
   - Once the query is executed, either from the MDX query input or the OlapReport input, the result is obtained.

8. **Format the result**:
   - The result set will be formatted to provide input for the controls.
   - The formatted input will be passed to the controls.

9. **Display the output**:
   - The output will be displayed in the controls.

### In Silverlight

1. **Requirements for OlapDataManager**:
   - The OlapDataManager requires an OlapReport and a Virtual Channel in the form of OlapDataManager.

2. **Data Binding**:
   - The OlapDataManager is a set to control, and in the `DataBind` method, the control makes an asynchronous call with the help of a virtual channel provided in OlapDataManager.

3. **Communication via WCF Service**:
   - With the help of WCF Service, the control communicates with the Olap base to retrieve the CellSet.

4. **Control-OlapDataManager Communication**:
   - The control passes the obtained CellSet to the OlapDataManager.
   - In turn, the OlapDataManager returns the PivotEngine to the control.

5. **Displaying the Output**:
   - The output will be reflected in the controls.

## 4.5.2 Steps in processing Non-OLAP data

### Overview
- Process the Non-OLAP data (such as IEnumerable, IList, DataTable, DataView, etc.) to provide the specified formatted input to the controls.
- For Non-OLAP data, no connection needs to be established.

### Processing Non-OLAP data

To process the Non-OLAP data:
1. Give the two inputs.

## API Reference (if applicable)
- [Details to be added as per the documentation]

## Code Examples (multi-language supported)
- [Code examples to be added as per the documentation]

<!-- tags: [Syncfusion Winforms, OLAP, Non-OLAP, OlapDataManager, OlapReport, MDX Query, WCF Service, CellSet, PivotEngine, Silverlight] keywords: [data processing, connection string, query execution, result formatting, output display, virtual channel, asynchronous call, data controls] -->
```

---

<!-- 페이지 21 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_081.jpeg
document_name: Olap Common
page_number: 081
page_id: Olap Common#page_081
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:20:19Z
fidelity: lossless
-->

## Essential OlapCommon

### Code Example: Connecting to Mondrian Server

```vb
' Connecting to Mondrian Server
Dim DataManager As OlapDataManager = New OlapDataManager("Datasource = http://bi.syncfusion.com:8080/mondrian/xmla; Initial Catalog=FoodMart;")
DataMgr.DataProvider.ProviderName = Syncfusion.Olap.DataProvider.Providers.Mondrian
```

Click [here](#more-information-about-mondrian-xmla-configurations) for more information about Mondrian XMLA configurations.

### 5.5 Connect ActivePivot Server through XMLA

The user can connect the Active Pivot server through XMLA (XML for Analysis) services using the OlapDataManager in our OLAP controls.

The following code illustrates how to connect to Active Pivot server:

#### C#

```csharp
// Connecting to Active Pivot Server
OlapDataManager DataManager = new OlapDataManager(@"Data Source=http://localhost:8081/var_s/xmla; Initial Catalog=VaRCubes; User ID=; Password=; Transport Compression=None;");
DataManager.DataProvider.ProviderName = Syncfusion.Olap.DataProvider.Providers.ActivePivot;
```

#### VB

```vb
' Connecting to Active Pivot Server
Dim DataManager As OlapDataManager = New OlapDataManager("Data Source=http://localhost:8081/var_s/xmla; Initial Catalog=VaRCubes; User ID=; Password=; Transport Compression=None;")
DataMgr.DataProvider.ProviderName = Syncfusion.Olap.DataProvider.Providers.ActivePivot
```

Click [here](#more-information-about-active-pivot-server) for more information about Active Pivot server.

### 5.6 Create a WCF Service for Silverlight OLAP Control

The following steps will define the adding of WCF Service to the Web project and configuring it with `IOLapDataProvider`:

## API Reference

### WinForms-specific conventions

Namespaces, Classes, Members (Methods/Properties/Events/Enums) in subsections.
- Parameters table: Name | Type | Description | Default | Required
- Returns: Type + description.
- Exceptions: bullet list.

## Code Examples

Extract all code exactly. Use fenced blocks with language: `csharp`, `vb`, `xml`, `xaml`, `js`, `css`, `ts`, `python`.

## Cross References

See also:موندريان، إيس بي، XMLA، بروسرس، مشيف وشقف للو想到了

## RAG Annotations

Tags: [Syncfusion Winforms, Olap Common, Mondrian Server, XMLA, ActivePivot, WCF Service, Silverlight OLAP Control]
Keywords: [OlapDataManager, ProviderName, DataProvider, Mondrian, ActivePivot, WCF Service, Silverlight, OLAP]
```

<!-- tags: [Syncfusion Winforms, Olap Common, Mondrian Server, XMLA, ActivePivot, WCF Service, Silverlight OLAP Control] keywords: [OlapDataManager, ProviderName, DataProvider, Mondrian, ActivePivot, WCF Service, Silverlight, OLAP] -->
```

---

<!-- 페이지 22 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_085.jpeg
document_name: Olap Common
page_number: 085
page_id: Olap Common#page_085
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:20:39Z
fidelity: lossless
-->

## Overview

- Implements functionality to execute OLAP reports with various parameters.
- Closes the provider connection after report execution.
- Demonstrates both C# and VB.NET implementations.
- Utilizes `Syncfusion.OlapSilverlight.Common.SerializableDictionary` for returning results.
- Includes handling for levels and total count in reports.

## Content

### C#

```csharp
return resultSet;
}

/// <summary>
/// Executes the olap report with total count.
/// </summary>
/// <param name="report">The report.</param>
/// <returns></returns>
public Syncfusion.OlapSilverlight.Common.SerializableDictionary<string, object>
ExecuteOlapReportWithTotalCount(OlapReport report)
{
    Syncfusion.OlapSilverlight.Common.SerializableDictionary<string, object>
    dict = this._dataManager.ExecuteOlapReportWithTotalCount(report);
    // Closing the Provider Connection
    this._dataManager.DataProvider.CloseConnection();
    return dict;
}
}
#endregion
```

### VB.NET

```vb
[VB]

<AspNetCompatibilityRequirements(RequirementsMode := _ 
AspNetCompatibilityRequirementsMode.Allowed)> _
<ServiceBehavior(IncludeExceptionDetailInFaults := True)> _
Public Class OlapManager
    Implements IOlapDataProvider

#Region "Member"
    Private ReadOnly _dataManager As OlapDataProvider
#End Region

#Region "Constructor"
    Public Sub New()
        _dataManager = New OlapDataProvider("DataSource=localhost;Initial Catalog=Adventure Works DW")
    End Sub
#End Region

#Region "IOLapDataProvider Members"

    Public Function ExecuteOlapReportWithLevelsTypeAll(ByVal report As OlapReport, ByVal showLevelsTypeAll As Boolean) As CellSet
        Dim cellSet As CellSet = 
        _dataManager.ExecuteOlapReportWithLevelsTypeAll(report, showLevelsTypeAll)
        _dataManager.DataProvider.CloseConnection()
        Return cellSet
    End Function
```

### Explanation

- **C# Implementation**:
  - The `ExecuteOlapReportWithTotalCount` method executes an OLAP report with the specified report object and returns a dictionary containing the results.
  - It ensures that the provider connection is closed after the report execution.
  
- **VB.NET Implementation**:
  - The `OlapManager` class implements the `IOlapDataProvider` interface.
  - The constructor initializes the `_dataManager` with a connection to a data source.
  - The `ExecuteOlapReportWithLevelsTypeAll` method executes the report and returns a `CellSet` object, also closing the provider connection after execution.

## API Reference

### Class: `OlapManager`

#### Methods

- **`ExecuteOlapReportWithTotalCount(OlapReport report)`**
  - **Parameters**:
    - `report`: The report to execute.
    - Type: `OlapReport`
  - **Returns**:
    - A `SerializableDictionary<string, object>` containing the results of the OLAP report.
  - **Description**:
    - Executes the OLAP report with the specified total count and closes the provider connection after execution.

- **`ExecuteOlapReportWithLevelsTypeAll(OlapReport report, Boolean showLevelsTypeAll)`**
  - **Parameters**:
    - `report`: The report to execute.
    - Type: `OlapReport`
    - `showLevelsTypeAll`: A boolean indicating whether to show all levels.
    - Type: `Boolean`
  - **Returns**:
    - A `CellSet` containing the results of the OLAP report.
  - **Description**:
    - Executes the OLAP report with the specified parameters and closes the provider connection after execution.

### Namespace: `Syncfusion.OlapSilverlight.Common`

- **SerializableDictionary<TKey, TValue>**
  - A dictionary that can be serialized, used to store key-value pairs of results from OLAP reports.

## Code Examples

### C# Example

```csharp
// Example usage of ExecuteOlapReportWithTotalCount
OlapReport report = new OlapReport();
var result = olapManager.ExecuteOlapReportWithTotalCount(report);
// Handle the result dictionary
```

### VB.NET Example

```vb
' Example usage of ExecuteOlapReportWithLevelsTypeAll
Dim report As New OlapReport()
Dim cellSet As CellSet = olapManager.ExecuteOlapReportWithLevelsTypeAll(report, True)
' Handle the CellSet result
```

<!-- tags: [Syncfusion, OLAP, WinForms, Report, OLAP Silverlight, SerializableDictionary] keywords: [execute, report, total count, levels, provider connection, close, dictionary, cellset, data provider, data manager, olap report] -->
```

---

<!-- 페이지 23 -->

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

---

<!-- 페이지 24 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_093.jpeg
document_name: Olap Common
page_number: 093
page_id: Olap Common#page_093
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:21:29Z
fidelity: lossless
-->

# Essential OlapCommon

OlapDataManager will accept the MDX query in the string format through any one of this and process the data based on the query. Once the connection is established you can pass the MDX query in string format.

The following code will illustrate the passing of the MXD query as input:

### [C#]

```csharp
OlapDataManager olapDataManager = new OlapDataManager("DataSource=localhost; Initial Catalog=Adventure Works DW");
string mdxQuery =
@"SELECT NON EMPTY ({{Hierarchy. ( [DrilldownLevel(( [Customer].[Customer Geography].[All Customers] ) ) ) } } * 
{ [MEASURES].[Internet Sales Amount]}}) dimension properties member_type ON COLUMNS, NON EMPTY ({{Hierarchy. ( 
[DrilldownLevel(({ [Date].[Fiscal].[All Periods]} ) ) ) } ) } } ) 
dimension properties member_type ON ROWS
FROM [Adventure Works] CELL PROPERTIES 
VALUE, FORMAT_STRING, FORMATTED_VALUE";
olapDataManager.MdxQuery = mdxQuery;
olapDataManager.ExecuteCellSet();
```

### [VB]

```vb
Dim olapDataManager As OlapDataManager = New 
OlapDataManager("DataSource=localhost; Initial Catalog=Adventure Works DW") 
Dim mdxQuery As String = "SELECT NON EMPTY ({{Hierarchy. ( [DrilldownLevel(( [Customer].[Customer Geography].[All Customers] ) ) ) } } * 
{ [MEASURES].[Internet Sales Amount]}}) dimension properties member_type ON COLUMNS, NON EMPTY ({{Hierarchy. ( 
[DrilldownLevel(({ [Date].[Fiscal].[All Periods]} ) ) ) } ) } ) } ) 
dimension properties member_type ON ROWS
FROM [Adventure Works]     CELL PROPERTIES 
VALUE, FORMAT_STRING, FORMATTED_VALUE"
olapDataManager.MdxQuery = mdxQuery
olapDataManager.ExecuteCellSet()
```

This will accept the MDX query as a string and assign it to the OlapDataManager's mdxQuery property and invoke the data process.

<!-- tags: [Olap Common, OlapDataManager, MDX, Query, C#, VB] keywords: [OlapDataManager, MDX, Query, Connection, Data Processing] -->
```

---

<!-- 페이지 25 -->

<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_097.jpeg
document_name: Olap Common
page_number: 097
page_id: Olap Common#page_097
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:21:43Z
fidelity: lossless
-->

## Essential OlapCommon

```csharp
dlg.Filter = "XML files (*.xml)|*.xml";

bool? b = dlg.ShowDialog();

if (b.HasValue && b.Value)
{
    using (Stream stream = dlg.OpenFile())
    {
        System.Xml.Serialization.XmlSerializer serializer = new System.Xml.Serialization.XmlSerializer(typeof(OlapReport));
        serializer.Serialize(stream, this.olapDataManager.CurrentReport);
    }
}
}
```

### [VB]

```vb
Private Sub SaveReport()
    Dim dlg As SaveFileDialog = New SaveFileDialog()
    dlg.Filter = "XML files (*.xml)|*.xml"

    Dim b As Nullable(Of Boolean) = dlg.ShowDialog()

    If b.HasValue AndAlso b.Value Then
        Using stream As Stream = dlg.OpenFile()
            Dim serializer As System.Xml.Serialization.XmlSerializer = New System.Xml.Serialization.XmlSerializer(GetType(OlapReport))
            serializer.Serialize(stream, Me.olapDataManager.CurrentReport)
        End Using
    End If
End Sub
```

## 5.12 Load xml report file

You can load the xml report set by using the `LoadReport` method.  
The following code snippet will illustrate the loading of the report:

---

<!-- tags: [syncfusion, winforms, olap, report, serialization, xml, load, save, api] keywords: [essential olapcommon, xml report, loadreport method, oleblob result, grid, table, size] -->

---

<!-- 페이지 26 -->

```html
<!--  
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_101.jpeg
document_name: Olap Common
page_number: 101
page_id: Olap Common#page_101
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:21:54Z
fidelity: lossless
-->

## Essential OlapCommon

### 5.16 Add the elements to an Axis

After creating the element, add the element to the specific axis. The `OlapReport` contains the axis as `CategoricalElements`, `SeriesElement` and `SliceElements`. By adding the created elements to any of these elements group, you can specify the axis position of the elements.

The following codes will describe the adding of the elements to categorical, series element:

```csharp
// Adding Column Members
olapReport.CategoricalElements.Add(dimensionElementColumn);
// Adding Measure Element
olapReport.CategoricalElements.Add(measureElementColumn);

// Adding Row Members
olapReport.SeriesElements.Add(dimensionElementRow);
```

```vb
'''Adding Column Members
olapReport.CategoricalElements.Add(dimensionElementColumn)
'''Adding Measure Element
olapReport.CategoricalElements.Add(measureElementColumn)

'''Adding Row Members
olapReport.SeriesElements.Add(dimensionElementRow)
```

### 5.17 Apply the Filter through filter element

The filter element will get information such as filter condition and filter value from the user, from the filter expression and then get the elements on which the filter has to apply.

The following codes describe the creation of the filter element and its application:

```csharp
DimensionElement dimensionElementColumn = new DimensionElement();
//Specifying the Name for the Dimension Element
dimensionElementColumn.Name = "Customer";
```

---
© 2013 Syncfusion. All rights reserved.
```

<!-- tags: [OlapCommon, Winforms, OlapReport, SliceElements, C# code, VB code, filter condition] keywords: [element, specific axis, categorical elements, series element, applying filter, filter condition, user input, grid, reporting, olap, data analysis] -->
```

---

<!-- 페이지 27 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_105.jpeg
document_name: Olap Common
page_number: 105
page_id: Olap Common#page_105
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:22:06Z
fidelity: lossless
-->

## Overview
- Describes the functionality of the "drill-down" button in the context of `OlapDataManager`.
- Explains the sequence of method calls when drill-down is triggered, focusing on recursion, member creation, and query generation.

## Content

### Overview of Drill-Down Functionality

Whenever the drill-down button is clicked, the `ToggleExpandableState()` method in the `OlapDataManager` will be invoked by the control. From there, the `UpdateDrillDowItems` will be called by passing the arguments, and there it checks the unique name and calls the `DrillUpDown()` method, which accepts the hierarchy element as an argument. This method is a recursive method and has an overload method that accepts the member element as an argument. By recursively iterating the drill-down level, all the members in that level will be created and added with its parent for the query creation.

Once the drill-down member is updated, the `NotifyElementModified()` will be invoked to generate the new query.

### Sequential Diagrams

#### Explanation of the Sequential Diagram for Drill-Down Process

The following screenshot explains the sequential diagram for the drill-down process:

![OLAP base sequential diagram](#)
**Figure 12: OLAP base sequential diagram**

The diagram illustrates the following steps in the drill-down process:

1. **User Trigger**: The user initiates a drill-up/down action.
2. **OlapDataManager Handling**: The `OlapDataManager` processes the drill-up/down request.
3. **Update Member**: The `Update DrillDown member` action updates the relevant member.
4. **Data Flow**: The data flows through `DataProvider`, `QuerySpecification`, `QueryBuilder`, `QueryBuilderHelper`, and `PivotEngine`.
5. **Recursive Drill-Down**: The `DrillUpDown` method is called recursively, handling `DrillDownHierarchy` and `DrillDownMember`.
6. **Query Execution**: The `GetQueryEx` method retrieves the query, which is then executed to generate the appropriate `CellSet`.
7. **Result Execution**: The `ExecuteOlapTable` ensures the query results are rendered correctly.

This diagram provides a comprehensive understanding of how the drill-down functionality is implemented and executed within the context of the `OlapDataManager` and related components.

## API Reference

### Methods

#### `ToggleExpandableState()`
- Invoked when the drill-down button is clicked.
- Triggers the `UpdateDrillDowItems` method.

#### `UpdateDrillDowItems`
- Accepts arguments and checks for unique names.
- Calls the `DrillUpDown()` method.

#### `DrillUpDown()`
- A recursive method that accepts a hierarchy element.
- Overloaded to accept a member element.
- Creates and adds members at the drill-down level and their parents for query creation.

#### `NotifyElementModified()`
- Called after updating the drill-down member to generate a new query.

## Code Examples

```csharp
// Example of handling drill-down in C#
public class OlapDataProcessor
{
    public void ToggleExpandableState()
    {
        // Implementation logic for toggling expandable state
        UpdateDrillDowItems();
    }

    public void UpdateDrillDowItems()
    {
        // Logic to update drill-down items
        DrillUpDown();
    }

    private void DrillUpDown()
    {
        // Recursive logic for drill-up/down
    }

    public void NotifyElementModified()
    {
        // Logic to generate new query after member update
    }
}
```

## Cross References

- See also: Other sections or reference materials relevant to the `OlapDataManager` and hierarchical queries.

<!-- tags: [OlapCommon, OlapDataProcessor, drill-down, recursion, query generation, WinForms] keywords: [toggleExpandableState, updateDrillDowItems, drillUpDown, notifyElementModified, sequential diagram, hierarchical queries] -->
```

---

<!-- 페이지 28 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_109.jpeg
document_name: Olap Common
page_number: 109
page_id: Olap Common#page_109
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:22:27Z
fidelity: lossless
-->

# Essential OlapCommon

```vb
Dim currentMdxQuery As String
'Invoke the service call to retrieve the MDX query from the Server based on current report.
_olapDataManager.GetMdxQuery(_olapDataManager.CurrentReport)
_olapDataManager.MdxQueryObtained += Function()
'MDX Query retrieved.
currentMdxQuery = _olapDataManager.CurrentReport.CurrentMdxQuery
End Function
```

## 5.23 Add UseWhereClauseForSlicing to an Application

The user can add the UseWhereClauseForSlicing property to an application by setting the property to a Boolean value. To perform the slicing operation using the ‘Where’ clause, set the property to `true`. To perform the slicing operation using the ‘Select’ clause, set the property to `false`. By default, the value of the UseWhereClauseForSlicing property is `true`.

### To perform slicing operation using ‘Where’ clause:

```csharp
OlapDataManager.UseWhereClauseForSlicing = true;
```

```vb
OlapDataManager.UseWhereClauseForSlicing = True
```

### To perform slicing operation using ‘Select’ clause:

```csharp
this.olapGridControl1.OlapDataManager.UseWhereClauseForSlicing = false;
```

```vb
Me.olapGridControl1.OlapDataManager.UseWhereClauseForSlicing = False
```

<!-- tags: [syncfusion, winforms, olap, slicing, mdx, where clause, select clause] keywords: [UseWhereClauseForSlicing, MDX query, slicing operation, boolean property, default value] -->
```

---

<!-- 페이지 29 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_113.jpeg
document_name: Olap Common
page_number: 113
page_id: Olap Common#page_113
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:22:38Z
fidelity: lossless
-->

# Essential OlapCommon

## Overview

- Explains the usage of the OlapGrid control.
- Demonstrates dragging and dropping the OlapGrid control into the MainPage.xaml.
- Guides through setting up an XAML application using the designer page.

## Content

### Working with OlapGrid

In this guide, you will learn how to integrate the OlapGrid control into your XAML application using Microsoft Visual Studio.

#### Using the Designer Page

Figure 16: Designer Page illustrates how to set up the environment for using the OlapGrid control. The Designer Page provides a graphical interface for designing XAML-based user interfaces.

**Figure 16: Designer Page**

To use the OlapGrid control, follow these steps:

1. Open the `MainPage.xaml` file in the designer.
2. Ensure the `Solution Explorer` is visible to manage project files.
3. Locate the `OlapGrid` control in the toolbox.

#### Dragging and Dropping the OlapGrid Control

5. Drag and drop the **OlapGrid** from the toolbox to the `MainPage.xaml`.

This step ensures that the OlapGrid control is added to your user interface design, enabling you to configure and utilize it within your application.

### Additional Information

To complete the setup and start working with the OlapGrid, refer to the documentation or API reference for further details on configuring properties, events, and methods.

## API Reference

For a comprehensive list of properties, methods, and events available for the OlapGrid, consult the Syncfusion OlapGrid API documentation:

- **Namespace**: Syncfusion.Olap_GRID
- **Class**: OlapGrid

### Example Code

Here’s an example of how to add the OlapGrid to your XAML:

```xml
<UserControl x:Class="SilverlightMVCSample.MainPage"
             xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
             xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
             mc:Ignorable="d"
             d:DesignHeight="300" d:DesignWidth="400">
    <Grid>
        <!-- Add OlapGrid here -->
        <syncfusion:OlapGrid x:Name="olapGrid" Height="200" Width="300" />
    </Grid>
</UserControl>
```

## Cross References

- Refer to the Syncfusion documentation for more detailed information on the OlapGrid control: [OlapGrid Documentation](#).

<!-- tags: OlapGrid, XAML, Designer Page, Syncfusion WinForms, version: 11.4.0.26 -->
```

---

<!-- 페이지 30 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_117.jpeg
document_name: Olap Common
page_number: 117
page_id: Olap Common#page_117
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:22:55Z
fidelity: lossless
-->

# Essential OlapCommon

```csharp
// Closing the provider connection.
this.dataManager.DataProvider.CloseConnection();
return cellSet;
}
```

### Members
```csharp
public MemberCollection GetChildMembers(string memberUniqueName, string cubeName)
{
    throw new NotImplementedException();
}
public CubeSchema GetCubeSchema(string cubeName)
{
    throw new NotImplementedException();
}
public CubeInfoCollection GetCubes()
{
    throw new NotImplementedException();
}
public MemberCollection GetLevelMembers(string levelUniqueName, string cubeName)
{
    throw new NotImplementedException();
}
#endregion
```

### VB Implementation
```vb
[VB]
Public Class OlapManager
    Implements IOlapDataProvider
    Private dataManager As Syncfusion.OlapSilverlight.Manager.OlapDataProvider
    ''' <summary>
    ''' Initializes a new instance of the <see cref="OlapManager"/> class.
    ''' </summary>
End Class
```

---

<!-- tags: [Olap Common, data provider, cube schema, member collection, VB.NET] keywords: [memberUniqueName, cubeName, levelUniqueName, membercollection, cubeschema, cubes, cubinfocollection, synchronization, exception handling, interface implementation, Winforms] -->
```

---

<!-- 페이지 31 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_121.jpeg
document_name: Olap Common
page_number: 121
page_id: Olap Common#page_121
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:23:05Z
fidelity: lossless
-->

# Essential Olap Common

## Content

### Initializing the Service Connection

#### C#

```csharp
Binding new BinaryMessageEncodingBindingElement(), new HttpTransportBindingElement { MaxReceivedMessageSize = 2147483647 };
EndpointAddress address = new EndpointAddress(new Uri(App.Current.Host.Source + "../../OlapManager.svc/binary"));
ChannelFactory<IOLapDataProvider> clientChannel = new ChannelFactory<IOLapDataProvider>(customBinding, address);
DataProvider = clientChannel.CreateChannel();
```

#### VB

```vb
Private Sub InitializeConnection()
    Dim customBinding As System.ServiceModel.Channels.Binding = New CustomBinding(New BinaryMessageEncodingBindingElement(), New HttpTransportBindingElement With {.MaxReceivedMessageSize = 2147483647})
    Dim address As EndpointAddress = New EndpointAddress(New Uri(App.Current.Host.Source & "../../OlapManager.svc/binary"))
    Dim clientChannel As ChannelFactory(Of IOLapDataProvider) = New ChannelFactory(Of IOLapDataProvider)(customBinding, address)
    DataProvider = clientChannel.CreateChannel()
End Sub
```

### Creating the Report

17. **Create the Report.**

For creating reports, there is a report object called `OlapReport`. The `OlapReport` object contains CategoricalItems, SeriesItems, SlicerItems, and FilterItems.

The `OlapReport` is associated with the `OlapDataManager` as the current report property. When a report is set to the current report, an event triggers, and the control renders based on the current report that is set.

### Binding the Data to OlapGridData

18. **Bind the data to OlapGridData.**

```csharp
private void MainPage_Loaded(object sender, RoutedEventArgs e)
{
    // Initialize the service connection.
    this.InitializeConnection();
    // Instantiating the OlapDataManager.
    OlapDataManager m_OlapDataManager = new OlapDataManager();
}
```

## Cross References

See also:
- [OlapReport](#OlapReport)
- [OlapDataManager](#OlapDataManager)

<!-- tags: [olap, report, datamanagement, wcf, syncfusion] keywords: [OlapReport, OlapDataManager, InitConnection, BinaryMessageEncodingBindingElement, HttpTransportBindingElement, DataProvider, Report, SeriesItems, FilterItems] -->
```

---

<!-- 페이지 32 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_125.jpeg
document_name: Olap Common
page_number: 125
page_id: Olap Common#page_125
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:23:19Z
fidelity: lossless
-->

# Essential Olap Common

## Overview
- Explains OLAP data processing and details the steps for handling both OLAP and non-OLAP data.
- Outlines the process of connecting to SSAS servers and cube files for OLAP reporting.
- Covers the functionality of OlapDataManager and its binding with OlapReport.

## Content

### 4.5 OLAP Data Processing
#### 4.5.1 Steps in processing OLAP Data
#### 4.5.2 Steps in processing Non-OLAP data

### 5 How To
#### 5.1 Establish the connection for an SSAS Server
- **5.10** Bind the Non-OLAP data to OlapDataManager
- **5.11** Save the report as xml file
- **5.12** Load xml report file
- **5.13** Rename and remove a report
  - **5.13.1** RenameReport
  - **5.13.2** RemoveReport
- **5.14** Get the reports in the OlapDataManager as a stream
- **5.15** Communicate the OLAP control with the base
- **5.16** Add the elements to an Axis
- **5.17** Apply the Filter through filter element
- **5.18** Show/hide the Expander buttons in OLAP controls
- **5.19** Process OlapReport Internally
#### 5.2 Establish the connection for a Cube file
- **5.20** Handle Drill Down/Up Process
- **5.21** Connect WCF Service by an additional Binding Type in Silverlight application
- **5.22** Retrieve the MDX Query of a CurrentReport
- **5.23** Add UseWhereClauseForSlicing to an Application
- **5.24** Edit MDX Query before Its Execution
- **5.25** Host BI Silverlight component in ASP.NET MVC Web Project
#### 5.3 Establish Role-based Connection
#### 5.4 Connecting to Mondrian Server through XMLA
#### 5.5 Connect ActivePivot Server through XMLA

### 5.6 Create a WCF Service for Silverlight OLAP control
### 5.7 Connect WCF Service in Silverlight application
### 5.8 Bind an OlapReport with OlapDataManager
- **5.8.1** CurrentReport
- **5.8.2** SetCurrentReport
- **5.8.3** LoadOlapDataManager
- **5.8.4** LoadReportDefinitionFile
- **5.8.5** LoadReportDefinitionFromStream
### 5.9 Bind the MDX query to OlapDataManager

## Page-level Navigation/TOC
- 4.5 OLAP Data Processing
  - 4.5.1 Steps in processing OLAP Data
  - 4.5.2 Steps in processing Non-OLAP data
- 5 How To
  - 5.1 Establish the connection for an SSAS Server
  - 5.2 Establish the connection for a Cube file
  - 5.3 Establish Role-based Connection
  - 5.4 Connecting to Mondrian Server through XMLA
  - 5.5 Connect ActivePivot Server through XMLA
  - 5.6 Create a WCF Service for Silverlight OLAP control
  - 5.7 Connect WCF Service in Silverlight application
  - 5.8 Bind an OlapReport with OlapDataManager
  - 5.9 Bind the MDX query to OlapDataManager

## RAG Annotations
<!-- tags: [syncfusion, winforms, olap, olapdatacommon, wcf, ssas, cubes] keywords: [olap data processing, ssas server, cube file, olap report, mdx query, silverlight application, xmla, mondrian server, activepivot server] -->
```


---

<!-- 페이지 33 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_002.jpeg
document_name: Olap Common
page_number: 002
page_id: Olap Common#page_002
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:14:30Z
fidelity: lossless
-->

# Contents

## Business Intelligence (BI)

- 1.1 What is BI? .....5
- 1.2 Why use BI? .....5
- 1.3 What's new in BI? .....5
  - 1.3.1 Multi-dimensional Data .....5

## Online Analytical Processing (OLAP)

- 2.1 ADOMD.NET .....7
- 2.2 ADOMD.NET assembly and setup files information .....7

## Syncfusion OLAP Architecture

### 3. OLAP Base
- OLAP Silverlight Base .....9
- OLAP Silverlight Base Wrapper .....10
  - 3.3.1 WCF Service .....11

### 4. Concepts

#### OlapDataProvider
- 4.1.1 AdomdDataProvider .....12

#### OlapDataManager
- 4.2.1 Properties and Methods .....14
- 4.2.2 UseWhereClauseForSlicing .....17
- 4.2.3 Drill Through .....21

#### OlapReport
- Properties and Methods .....22
  - 4.3.2 Dimension Element .....22
  - 4.3.3 Measure Element .....23
  - 4.3.4 Key Performance Indicator (KPI) Element .....25
  - 4.3.5 NamedSet Element .....25
  - 4.3.6 Sort Element .....28
  - 4.3.7 Calculated Member .....29
  - 4.3.8 Subset Element .....30
  - 4.3.9 Summary Elements .....32

## Page-level Navigation/TOC (if applicable)

This section provides a detailed table of contents for the reference guide, covering topics from Business Intelligence (BI) basics, Online Analytical Processing (OLAP), Syncfusion's OLAP Architecture, and key concepts related to the OlapDataProvider, OlapDataManager, and OlapReport components. It includes specific elements such as AdomdDataProvider, properties and methods, slicing options, and various report elements like Dimension, Measure, KPI, NamedSet, Sort, Calculated Member, Subset, and Summary elements.

## Cross References

- **See also**: AdomdDataProvider, OlapDataManager, OLAP, Business Intelligence, Multi-dimensional Data, OLAP Architecture, Syncfusion Winforms

## RAG Annotations

<!-- tags: [Olap Common, Winforms, Business Intelligence, OLAP, Syncfusion, OLAP Architecture, OlapDataProvider, OlapDataManager, OlapReport] keywords: [Business Intelligence, OLAP, Syncfusion OLAP Architecture, OlapDataProvider, OlapDataManager, OlapReport, Dimension Element, Measure Element, KPI Element, NamedSet Element, Sort Element, Calculated Member, Subset Element, Summary Elements, WCF Service, ADOMD.NET] -->
```

---

<!-- 페이지 34 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_006.jpeg
document_name: Olap Common
page_number: 006
page_id: Olap Common#page_006
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:14:47Z
fidelity: lossless
-->

# Essential OlapCommon

## Overview
- Multi-dimensional database products are popularized as OLAP systems for decision support on large historical data.
- Provides a multidimensional view of data with categorical and numeric attributes forming dimensions and measures, respectively.
- Supports hierarchical aggregation and interactive exploration of data cubes.

## Content

### Core Concepts
- **OLAP Systems**: Facilitate decision support by exposing a multidimensional view of data.
- **Multidimensional View**:
  - Categorical attributes (e.g., Products, Stores) form dimensions.
  - Numeric attributes (e.g., Sales, Revenue) form measures or cells of the multidimensional cube.
- **Hierarchies**:
  - Dimensions are associated with hierarchies that define aggregation levels.
  - Example: store-name -> city -> state for the Store dimension.
- **Aggregation**:
  - Measure attributes are aggregated using functions like sum, average, count, and variance.
  - Aggregation is performed at various levels of detail based on combinations of dimension attributes.

### Data Exploration Tools
- **Navigational Operators**:
  - Provide tools for exploring data cubes using operations such as select, drill-down, roll-up, and pivot.
- **Interactive Analysis**:
  - Analysts can interactively explore data by invoking sequences of operations.
  - Visualization of measures across various combinations of dimensions and aggregation levels.

### Syncfusion's OLAP Architecture
- Offers the easiest way to perform extreme analysis of data.
- Aligns with the multidimensional view and interactive exploration needs.

## RAG Annotations
<!-- tags: [OLAP, multidimensional database, decision support, hierarchical aggregation, navigation operators, interactive analysis, Syncfusion Winforms, version 11.4.0.26] keywords: [OLAP, multidimensional view, aggregation, hierarchy, data cube, pivot, drill-down, roll-up, analysis, Syncfusion] -->
```

---

<!-- 페이지 35 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_010.jpeg
document_name: Olap Common
page_number: 010
page_id: Olap Common#page_010
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:15:00Z
fidelity: lossless
-->

# Essential OlapCommon

## Overview
- This page describes the OLAP Silverlight Base and its wrapper, focusing on data processing and conversion features.
- Highlights the role of namespaces and classes in performing data conversion between OLAP Silverlight Base and OLAP Base.
- Explains the flow of data in Silverlight applications.

## Content

### 3.2 OLAP Silverlight Base
OLAP Silverlight Base is a class library containing several namespaces and classes to perform data processing operations required by OLAP Silverlight controls. The `OlapDataManager` retrieves OLAP data and binds the result to an OLAP Control.

#### Note:
This class library was organized under `Syncfusion.Olap.Base` assembly.

### 3.3 OLAP Silverlight Base Wrapper
The OLAP Silverlight Base Wrapper is a class library containing several namespaces and classes. This library helps perform data conversion between OLAP Silverlight Base and OLAP Base. The Data Conversion process is used to achieve the following features:

1. Establishing the connection and retrieving data by converting OLAP Silverlight Base information to OLAP Base information.
2. Sending retrieved data to OLAP Silverlight Base by converting OLAP Base data to OLAP Silverlight Base data.

#### Dataflow in Silverlight

![Dataflow in Silverlight](attachment)

### Diagram Explanation
- **OlapReport**: Serves as the starting point for reporting operations.
- **OlapDataManager**: Manages data retrieval and binding to the OLAP Control.
- **Control**: The UI component that interacts with the user.
- **CellSet Pivot Engine**: Handles cell set and pivot operations.
- **Virtual Channel (IOLapDataProvider)**: Acts as a middleware for asynchronous calls.
- **Olap Base**: Includes components like `MDX Query Specification`, `QueryBuilderEngine`, and `Data Provider` for query processing.

#### Note:
This class library was organized under `Syncfusion.OlapSilverlight.Base` assembly.

### Key Components
- **OlapReport**: Facilitates reporting operations.
- **OlapDataManager**: Manages data operations and binds data to the OLAP Control.
- **Control**: The user interface component for data interaction.
- **CellSet Pivot Engine**: Handles data pivoting and cell operations.
- **Virtual Channel (IOLapDataProvider)**: Middleware for asynchronous communication.
- **Olap Base**: Includes components like `MDX Query Specification`, `QueryBuilderEngine`, and `Data Provider`.

## API Reference

### namespaces
- `Syncfusion.Olap.Base`
- `Syncfusion.OlapSilverlight.Base`

### Classes
- `OlapDataManager`
- `OlapReport`
- `Control`
- `CellSet`
- `PivotEngine`
- `Virtual Channel (IOLapDataProvider)`
- `MDX Query Specification`
- `QueryBuilderEngine`
- `Data Provider`

## Code Examples

### C#
```csharp
// Sample code for retrieving OLAP data
using Syncfusion.Olap.Base;

public class DataRetriever
{
    public void RetrieveData()
    {
        var olapDataManager = new OlapDataManager();
        var cellSet = olapDataManager.GetData(); // Retrieve data from OLAP Base
        // Further processing and binding logic
    }
}
```

## Page-level Navigation/TOC
- 3.2 OLAP Silverlight Base
- 3.3 OLAP Silverlight Base Wrapper

## Cross References
- Refer to the `OlapDataManager` documentation for more details on data retrieval.
- See the `OlapBase` section for insights into query processing components.

<!-- tags: [Syncfusion, OLAP, Silverlight, Winforms, Base] keywords: [OlapDataManager, DataConversion, OLAP, Silverlight, Winforms, Dataflow] -->
```

---

<!-- 페이지 36 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_014.jpeg
document_name: Olap Common
page_number: 014
page_id: Olap Common#page_014
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:15:22Z
fidelity: lossless
-->

# Essential OlapCommon

| Method Name             | Description                                                                 | Parameters | Return Type | Reference Link |
|-------------------------|-----------------------------------------------------------------------------|------------|--------------|----------------|
|                         | member.                                                                     | -          | -            | -              |
| ValidateConnectionString | This method will validate the specified connection string in the data manager or in the data provider and return the validated status. | -          | bool         | -              |

## OlapDataManager

OlapDataManager is the most important class in the whole OLAP Base. All the information transfers from the control to OLAP base will happen through this class and this will retain the current state of the base objects. The connection is established in the Data provider of the OLAP Base, but the information required in establishing the connection is given to the data provider through the OlapDataManager.

### Table 3: Constructors

| Constructors                         | Description                                                                 | Parameters              | Return Type | Reference Link |
|--------------------------------------|-----------------------------------------------------------------------------|--------------------------|--------------|----------------|
| OlapDataManager()                   | Default constructor                                                      | -                        | Void         | -              |
| OlapDataManager(string)             | Accepts the connection string as argument and passes it to the Data Provider to establish the connection with data source. | String                 | Void         | -              |
| OlapDataManager(AdomdDataProvider)  | Accepts the Data Provider as argument and processes the cube that is connected with the given data provider.          | AdomdDataProvider      | Void         | -              |

### Establishing connection with the SSAS server

The following code snippet describes establishing connection with the server:

```csharp
OlapDataManager olapDataManager = new OlapDataManager("DataSource=local
```

## Code Examples

### C#

```csharp
OlapDataManager olapDataManager = new OlapDataManager("DataSource=local);
```

<!-- tags: [olapcommon, olapdata-manager, object-oriented-programming, cis, sql server] keywords: [essentials, connection string, data manager, constructor, adomd-data-provider, ssas server] -->
```

---

<!-- 페이지 37 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_018.jpeg
document_name: Olap Common
page_number: 018
page_id: Olap Common#page_018
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:15:36Z
fidelity: lossless
-->

# Essential OlapCommon

## Overview
- Describes the essential properties and their functionalities in the OlapCommon namespace.
- Provides details on how to set or retrieve properties related to cube names, schemas, reports, data providers, and more.
- Includes references to additional resources for specific properties.

## Content

### Property Description Table

| Property Name                   | Description                                                                                                             | Type                      | Value it Accepts         | Reference Link           |
|---------------------------------|-------------------------------------------------------------------------------------------------------------------------|---------------------------|--------------------------|--------------------------|
|                               | here.                                                                                                                   |                           |                          |                          |
| CurrentCubeName                | Used to set or get the current cube name. When set, the whole data process will change to the specified cube name. | String                    | String                   |                          |
| CurrentCubeSchema              | The user can get the CubeSchema of the currently connected cube.                                                        | CubeSchema                |                          |                          |
| CurrentReport                  | Used to load an OlapReport or get the currently loaded report.                                                          | OlapReport                | OlapReport               | OlapReport                |
| DataProvider                   | Used to set a data provider and get the existing data provider.                                                          | IDataProvider              | IDataProvider            | DataProvider               |
| IsCurrentReportModified        | Used to get or set the modified status of the currently loaded report.                                                  | bool                      | True/False               |                          |
| Itemsource                     | Used to bind the Non-OLAP data to OlapDataManager.                                                                      | Object                    | Enumerable collection/ ITyped List |                          |
| MdxQuery                       | Used to pass the MDX query as input.                                                                                   | string                    | String                   | MdxQuery                  |
| PivotEngine                    | Used to get the PivotEngine for the given input.                                                                       | PivotEngine               | PivotEngine              |                          |
| QuerySpecification              | Used to get the MDXQuerySpecification for the given OlapReport.                                                         | MDXQuerySpecification      |                          | QuerySpecification         |
| ReportPath                     | Used to get or set the report path to store the report as an XML file.                                                  | string                    |                          |                          |
| Reports                        | Contains the report collection of the OlapReportCollection.                                                            | OlapReportCollection      | OlapReportCollection     |                          |

## API Reference

- **Properties**
  - `CurrentCubeName`: Allows setting or retrieving the current cube name.
  - `CurrentCubeSchema`: Provides access to the `CubeSchema` of the currently connected cube.
  - `CurrentReport`: Facilitates loading or retrieving the current `OlapReport`.
  - `DataProvider`: Sets or retrieves the data provider.
  - `IsCurrentReportModified`: Indicates whether the current report has been modified.
  - `Itemsource`: Binds Non-OLAP data to the `OlapDataManager`.
  - `MdxQuery`: Passes an MDX query for processing.
  - `PivotEngine`: Retrieves the `PivotEngine` for the given input.
  - `QuerySpecification`: Retrieves the `MDXQuerySpecification` for the current `OlapReport`.
  - `ReportPath`: Sets or retrieves the report's storage path as an XML file.
  - `Reports`: Contains the collection of reports in the `OlapReportCollection`.

## Code Examples

### Sample Code Using `CurrentCubeName`

```csharp
using Syncfusion.OlapCommon;

var olapCommon = new OlapCommon();
// Set the current cube name.
olapCommon.CurrentCubeName = "SalesCube";

// Get the current cube name.
string currentCubeName = olapCommon.CurrentCubeName;
```

### Sample Code Using `MdxQuery`

```csharp
using Syncfusion.OlapCommon;

var olapCommon = new OlapCommon();
// Set the MDX query.
olapCommon.MdxQuery = "SELECT NON EMPTY Measures.[Sales Amount] ON COLUMNS, NON EMPTY [Product].[Product Category] ON ROWS FROM [SalesCube]";

// Execute the query.
var pivotEngine = olapCommon.PivotEngine;
pivotEngine.Refresh();
```

### Sample Code Using `CurrentReport`

```csharp
using Syncfusion.OlapCommon;

var olapCommon = new OlapCommon();

// Load an OlapReport.
olapCommon.CurrentReport = new OlapReport();
olapCommon.CurrentReport.Load("report.xml");

// Get the current report.
OlapReport currentReport = olapCommon.CurrentReport;
```

## Page-level Navigation/TOC

- [x] Property Description Table
- [x] API Reference
- [x] Code Examples

## Cross References

See also:
- MDXQuery
- OlapReport
- QuerySpecification
- DataProvider

## RAG Annotations

<!-- tags: [OlapCommon, MDXQuery, OlapReport, DataProvider, PivotEngine, OlapDataManager] keywords: [cube name, cube schema, report path, modified status, MDX query, PivotEngine] -->
```

---

<!-- 페이지 38 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_022.jpeg
document_name: Olap Common
page_number: 022
page_id: Olap Common#page_022
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:16:03Z
fidelity: lossless
-->

## Overview
- Explains the `UseWhereClauseForSlicing` property in MDX queries and how it affects slicing operations.
- Demonstrates using the `Drill Through` feature to explore data within the cube.
- Introduces the `OlapReport` object, which contains information about cube elements for processing with filters and sorting constraints.

## Content

### UseWhereClauseForSlicing
| Property Name          | Description                                                                                                                                 | Server side | Type    | Default |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|-------------|---------|---------|
| UseWhereClauseForSlicing | Enables the user to decide whether the MDX Query Parser Engine should consider the 'Where' or 'Select' clause for slicing operation. | Server side | Boolean | ----    |

#### Adding UseWhereClauseForSlicing property to an Application:
Refer to 5.22

### 4.2.3 Drill Through
This feature enables the user to drill through any value and see the data which formed the value.

The following code snippet illustrates how to drill through using MDX Query in OlapDataManager:

#### C# Implementation:
```csharp
string query = @"drillthrough Select { [Customer].[Customer Geography].[Country].[Australia] } on 0, { [Date].[Fiscal].[Fiscal Year].[2002] } on 1 from [Adventure Works] Where [Internet Sales Amount]";
// executing the drill-through operation.
olapDataManager.Execute(query);
```

#### VB Implementation:
```vb
Dim query As String = "drillthrough Select { [Customer].[Customer Geography].[Country].[Australia] } on 0, { [Date].[Fiscal].[Fiscal Year].[2002] } on 1 from [Adventure Works] Where [Internet Sales Amount]"
' Executing the drill-through operation.
olapDataManager.Execute(query)
```

### 4.3 OlapReport
**OlapReport** is an object that contains information about the cube element that has to be included for processing along its axis position and filter and sorting constraints. OlapReport has categorized the elements based on their characteristics as below:
- **Dimension Element**
  - Hierarchy Element
  - Level Element
  - Member Elements
- **Measure Element**
- **KPI Element**
- **NamedSet Element**

## Page-level Navigation/TOC (if applicable)
- Adding UseWhereClauseForSlicing property to an Application
- 4.2.3 Drill Through
- 4.3 OlapReport

## Cross References
- Refer to 5.22 for more details on the `UseWhereClauseForSlicing` property.

<!-- tags: [OlapCommon, MDX Queries, Drill Through, OlapReport, Filters, Sorting Constraints, Dimension Elements, Measure Elements, KPI Elements, NamedSet Elements, Syncfusion Winforms, 11.4.0.26] keywords: [MDX, Cube, Drill Through, OlapDataManager, OlapReport, Dimension Element, Measure Element, KPI, NamedSet Element] -->
```

---

<!-- 페이지 39 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_026.jpeg
document_name: Olap Common
page_number: 026
page_id: Olap Common#page_026
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:16:20Z
fidelity: lossless
-->

# Essential OlapCommon

## Overview
- Explains the hierarchical structure of a dimension.
- Demonstrates the creation of simple dimension elements using code.
- Illustrates the relationship between dimension elements, hierarchy elements, and level elements.

## Content

### Hierarchical Structure of a Dimension

![Figure 5: Hierarchical structure of a dimension](#)  
Figure 5: Hierarchical structure of a dimension

The following code will illustrate the creation of different types of dimensions:

#### Creating Simple Dimension Element

[C#]

```csharp
DimensionElement dimensionElementColumn = new DimensionElement();
// Specifying the Name for Column Dimension Element
dimensionElementColumn.Name = "Customer";
// Specifying the Hierarchy and Level Element Name
dimensionElementColumn.AddLevel("Customer Geography", "Country");
```

## API Reference (if applicable)
- Methods such as `AddLevel()` are used to define the hierarchy and levels within a dimension.

## Code Examples (multi-language supported)
- Provided C# code snippet for creating a simple dimension element.

## Page-level Navigation/TOC (if applicable)
- Refer to the "Hierarchical structure of a dimension" for visual representation.

## Cross References
- See also: Documentation for `DimensionElement`, `AddLevel()` method, and other relevant classes and methods.

<!-- tags: [Olap Common, dimension structure, dimension element, hierarchy, level element, code example, Winforms, version: 11.4.0.26] keywords: [dimension, hierarchy, level, element, structure, creation, code example, C#] -->
```

---

<!-- 페이지 40 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_030.jpeg
document_name: Olap Common
page_number: 030
page_id: Olap Common#page_030
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:16:31Z
fidelity: lossless
-->

## Essential OlapCommon

### Code Example: Creating a NamedSetElement

```csharp
NamedSetElement dimensionElementRow = new NamedSetElement();
// Specifying the dimension name
dimensionElementRow.Name = "Negative Margin Products";
```

```vb
Dim dimensionElementRow As NamedSetElement = New NamedSetElement()
' Specifying the dimension name
dimensionElementRow.Name = "Negative Margin Products"
```

### 4.3.6 Sort Element

The result set can be sorted by using the `SortElement`. We can create Sort elements and add it to the `OlapReport`. There are four types of sorting orders. They are:

- **ASC** – Sort the elements in ascending order.
- **BASC** – Sort the elements in ascending order by breaking the Hierarchy.
- **DESC** – Sort the elements in Descending order.
- **BDESC** – Sort the elements in Descending order by breaking the Hierarchy.

The following report will illustrate the creation of Sort element:

```csharp
SortElement sortElement = new SortElement(AxisPosition.Categorical, SortOrder.BDESC, true);
sortElement.Element.UniqueName = "[Measures].[Internet Sales Amount]";
```

```vb
Dim sortElement As SortElement = New SortElement(AxisPosition.Categorical, SortOrder.BDESC, True)
sortElement.Element.UniqueName = "[Measures].[Internet Sales Amount]"
```

### 4.3.7 Calculated Member

Calculated Members are the customized measures or dimension members created with the cube. The values are calculated at run-time. It is a user defined Element. The two types of calculated members are as follows:

1. **Calculated Measure** – Calculated member created from a measure element
2. **Calculated Dimension** – Calculated member created from a dimension

### Summary
- The page discusses sorting and filtering capabilities in OLAP reports, focusing on the `SortElement` and `Calculated Member`.
- It provides examples in both C# and VB.NET.
- The `SortElement` can be configured with different sorting orders, including ASC, BASC, DESC, and BDESC.
- `Calculated Members` allow for dynamic calculations at runtime, categorized as either Calculated Measure or Calculated Dimension.

### Code References
- `SortElement`
- `NamedSetElement`
- `OlapReport`

### Additional Notes
- The examples show how to create and configure these elements for OLAP reports in Syncfusion Winforms.

<!-- tags: [olap, report, calculated member, sort element, winforms, syncfusion] keywords: [measures, dimensions, sorting, calculated, runtime, cubes] -->
```

---

<!-- 페이지 41 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_034.jpeg
document_name: Olap Common
page_number: 034
page_id: Olap Common#page_034
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:16:47Z
fidelity: lossless
-->

## Filtering slicer elements by range

### Overview
- This feature allows you to specify a range for filter elements in the slicer field by setting a start and end value.
- Multiple ranges can be added to the filter elements in the slicer field.
- It eliminates the need to manually enter each member, making filtering easier.

### Content

#### Use Case Scenarios
It is not required to enter each member manually. This makes filtering easy.

#### Class

| Name                    | Description                                                                                                                                                                                                                      |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SlicerRangeFiltersInfo  | Used to filter values from one range to another. Unique name of the member element for start and end value need to be specified. The name of the member element can also be specified for start and end value when customer builds the unique name*. |

*Note: The name of the member element can be specified only when the name is formed with the dimension name, hierarchy name, and level name.*

#### Constructor

| Syntax                                                                      | Description                                                                                   | Parameter                                                                                       |
|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| SlicerRangeFiltersInfo(string startValueUniqueName, string endValueUniqueName) | Initializes SlicerRangeFiltersInfo with unique name as star and end values.                | Unique name for start and end value.                                                           |
| SlicerRangeFiltersInfo(string dimensionName, string hierarchyName, string levelName, string startValueName, string endValueName) | Initializes SlicerRangeFiltersInfo with name of dimension, hierarchy, level, star value and end value. | Name for dimension, hierarchy, level, start value and end value. |

#### Properties

The following table consists of the SlicerRangeFiltersInfo class's properties:

| Property     | Description | Type    | Data Type | Reference links |
|--------------|-------------|---------|-----------|-----------------|
|              |             |         |           |                 |

## Page-level Navigation/TOC (if applicable)
- [ ] None explicitly mentioned on the page.

## Cross References
- See also: None explicitly mentioned on the page.

<!-- tags: [Olap Common, filtering, slicer, WinForms,-range, ranges, SlicerRangeFiltersInfo] keywords: [slicer elements, range filtering, unique name, dimension name, hierarchy name, level name, SlicerRangeFiltersInfo, properties] -->
```

---

<!-- 페이지 42 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_038.jpeg
document_name: Olap Common
page_number: 038
page_id: Olap Common#page_038
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:17:01Z
fidelity: lossless
-->

# Essential OlapCommon

```csharp
ernet Sales Amount"})

Dim dimensionElementRow As DimensionElement = New DimensionElement()
// Specifying the Dimension Name
dimensionElementRow.Name = "Date"
dimensionElementRow.AddLevel("Fiscal", "Fiscal Year")

''' Adding Column Members
olapReport.CategoricalElements.Add(dimensionElementColumn)
''' Adding Measure Element
olapReport.CategoricalElements.Add(measureElementColumn)
''' Adding Row Members
olapReport.SeriesElements.Add(dimensionElementRow)
```

## 4.3.11.1.2 Report with slicing operation

[C#]

```csharp
OlapReport olapReport = new OlapReport();
olapReport.Name = "Customer Report";
olapReport.CurrentCubeName = "Adventure Works";

DimensionElement dimensionElementColumn = new DimensionElement();
// Specifying the dimension Name
dimensionElementColumn.Name = "Customer";
// Adding the Level Name along with the Hierarchy Name
dimensionElementColumn.AddLevel("Customer Geography", "Country");

DimensionElement dimensionElementRow = new DimensionElement();
// Specifying the dimension Name
dimensionElementRow.Name = "Date";
// Adding the Level Name along with the Hierarchy Name
dimensionElementRow.AddLevel("Fiscal", "Fiscal Year");

DimensionElement dimensionElementSlicer = new DimensionElement();
dimensionElementSlicer.Name = "Sales Channel";
dimensionElementSlicer.AddLevel("Sales Channel", "Sales Channel");

MeasureElements measureElementRow = new MeasureElements();
measureElementRow.Elements.Add(new MeasureElement { Name = "Internet Sa les Amount" });
```

## API Reference (if applicable)
- Refer to the relevant namespaces and classes pertaining to `OlapReport`, `DimensionElement`, `MeasureElement`, and related methods used in the examples above.

## Code Examples (straddle user context controls)
- Ensure that any code examples provided in this section integrate properly with the Syncfusion.Winforms framework and comply with the specified configurations and version constraints.

<!-- tags: [Olap, Report, Slicing, DimensionElement, MeasureElement, WinForms, Syncfusion] keywords: [OlapReport, DimensionElement, MeasureElements, Fiscal, Customer Report, Adventure Works, Sales Channel] -->
```

---

<!-- 페이지 43 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_042.jpeg
document_name: Olap Common
page_number: 042
page_id: Olap Common#page_042
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:17:16Z
fidelity: lossless
-->

# Essential OlapCommon

```vb
Dim measureElementColumn As MeasureElements = New MeasureElements()
measureElementColumn.Elements.Add(New MeasureElement { Name = "Internet Sales Amount" })
measureElementColumn.Elements.Add(New MeasureElement With {.Name = "Internet Sales Amount"})

Dim dimensionElementRow As DimensionElement = New DimensionElement()
'Specifying the Dimension Name
dimensionElementRow.Name = "Date"
dimensionElementRow.HierarchyName = "Fiscal"
dimensionElementRow.AddLevel("Fiscal", "Fiscal Year")

'Specifying Excluded column elements
Dim excludedColumnElement As DimensionElement = New DimensionElement()
excludedColumnElement.Name = "Customer"
excludedColumnElement.HierarchyName = "Customer Geography"
excludedColumnElement.AddLevel("Customer Geography", "Country")
excludedColumnElement.Hierarchy.LevelElements("Country").Add("Canada")
excludedColumnElement.Hierarchy.LevelElements("Country").Add("France")
excludedColumnElement.Hierarchy.LevelElements("Country").Add("United Kingdom")
excludedColumnElement.Hierarchy.LevelElements("Country").Add("United States")

'Specifying the Excluded row elements
Dim excludedRowElement As DimensionElement = New DimensionElement()
excludedRowElement.Name = "Date"
excludedRowElement.AddLevel("Fiscal", "Fiscal Year")
excludedRowElement.AddLevel("Fiscal", "Month")
excludedRowElement.AddLevel("Fiscal", "Fiscal Quarter")
excludedRowElement.AddLevel("Fiscal", "Fiscal Semester")
excludedRowElement.Hierarchy.LevelElements("Fiscal Year").Add("FY 2002")
excludedRowElement.Hierarchy.LevelElements("Fiscal Year").Add("FY
```

## API Reference (if applicable)

```vb
Namespace:
- MeasureElements
- MeasureElement
- DimensionElement
- Hierarchy
- LevelElements
```

## Code Examples

### Example 1: Defining Measure Elements

```vb
Dim measureElementColumn As MeasureElements = New MeasureElements()
measureElementColumn.Elements.Add(New MeasureElement { Name = "Internet Sales Amount" })
measureElementColumn.Elements.Add(New MeasureElement With {.Name = "Internet Sales Amount"})
```

### Example 2: Specifying a Dimension Row

```vb
Dim dimensionElementRow As DimensionElement = New DimensionElement()
dimensionElementRow.Name = "Date"
dimensionElementRow.HierarchyName = "Fiscal"
dimensionElementRow.AddLevel("Fiscal", "Fiscal Year")
```

### Example 3: Specifying Excluded Column Elements

```vb
Dim excludedColumnElement As DimensionElement = New DimensionElement()
excludedColumnElement.Name = "Customer"
excludedColumnElement.HierarchyName = "Customer Geography"
excludedColumnElement.AddLevel("Customer Geography", "Country")
excludedColumnElement.Hierarchy.LevelElements("Country").Add("Canada")
excludedColumnElement.Hierarchy.LevelElements("Country").Add("France")
excludedColumnElement.Hierarchy.LevelElements("Country").Add("United Kingdom")
excludedColumnElement.Hierarchy.LevelElements("Country").Add("United States")
```

### Example 4: Specifying Excluded Row Elements

```vb
Dim excludedRowElement As DimensionElement = New DimensionElement()
excludedRowElement.Name = "Date"
excludedRowElement.AddLevel("Fiscal", "Fiscal Year")
excludedRowElement.AddLevel("Fiscal", "Month")
excludedRowElement.AddLevel("Fiscal", "Fiscal Quarter")
excludedRowElement.AddLevel("Fiscal", "Fiscal Semester")
excludedRowElement.Hierarchy.LevelElements("Fiscal Year").Add("FY 2002")
excludedRowElement.Hierarchy.LevelElements("Fiscal Year").Add("FY")
```

### Notes
- The code examples demonstrate how to define various elements in an OLAP context, such as Measure Elements, Dimension Elements, and specifying excluded elements for both rows and columns.
- The examples use VB.NET, which is consistent with Syncfusion WinForms development.
- The Hierarchy and LevelElements are used to specify the structure and levels within dimensions.

<!-- tags: [OlapCommon, WinForms, MeasureElements, DimensionElement, Hierarchy, LevelElements, UserGuide] keywords: [MeasureElement, DimensionElement, Hierarchy, LevelElements, excluded elements, OLAP context, VB.NET] -->
```

---

<!-- 페이지 44 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_046.jpeg
document_name: Olap Common
page_number: 046
page_id: Olap Common#page_046
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:17:38Z
fidelity: lossless
-->

# Essential OlapCommon

```csharp
dimensionElementRow.Name = "Date";
dimensionElementRow.AddLevel("Fiscal", "Fiscal Year");

FilterElement filterElement = new FilterElement(AxisPosition.Categorical);
filterElement.Elements.Add(measureElementColumn);
filterElement.Elements.Add(dimensionElementColumn);
filterElement.FilterCase = FilterCase.GreaterThan;
filterElement.FilterValue.Add(new MeasureElement { Name = "Internet Sales Amount", Visible = true });
filterElement.FilterValue.Add(new FilterValue { Filter_Value = 2700000.00 });
filterElement.IsFilterCondition = true;
// Adding Column Members
olapReport.CategoricalElements.Add(new Item { ElementValue = dimensionElementColumn });
olapReport.CategoricalElements.IsFilterOrSortOn = true;
olapReport.FilterElements.Add(new Item { ElementValue = filterElement });

olapReport.SeriesElements.Add(dimensionElementRow);
```

### VB

```vb
Dim olapReport As OlapReport = New OlapReport()
olapReport.Name = "Customer Report"
olapReport.CurrentCubeName = "Adventure Works"

Dim dimensionElementColumn As DimensionElement = New DimensionElement()
'Specifying the Name for the Dimension Element
dimensionElementColumn.Name = "Customer"
dimensionElementColumn.AddLevel("Customer Geography", "Country")

'Creating Measure Element
Dim measureElementColumn As MeasureElements = New MeasureElements()
measureElementColumn.Elements.Add(New MeasureElement With {.Name = "Internet Sales Amount"})

Dim dimensionElementRow As DimensionElement = New DimensionElement()
```

## API Reference (if applicable)
- **Namespace**: OlapCommon
- **Class**: OlapReport
  - **Properties**
    - `Name`: String
    - `CurrentCubeName`: String
    - `CategoricalElements`: ICollection(Of Item)
    - `FilterElements`: ICollection(Of Item)
    - `SeriesElements`: ICollection(Of DimensionElement)
  - **Methods**
    - `AddLevel(levelName, levelDescription)`: Adds a level to a dimension.
    - `AddItem(elementValue)`: Adds a categorical item.
    - `AddFilterElement(filterElement)`: Adds a filter condition.
  - **Events**
    - `FilterConditionChanged`: Triggered when the filter condition changes.
    - `SeriesElementAdded`: Triggered when a new series element is added.

## Code Examples (multi-language supported)

### C#
```csharp
dimensionElementRow.Name = "Date";
dimensionElementRow.AddLevel("Fiscal", "Fiscal Year");
```

### VB
```vb
Dim dimensionElementColumn As DimensionElement = New DimensionElement()
dimensionElementColumn.Name = "Customer"
dimensionElementColumn.AddLevel("Customer Geography", "Country")
```

<!-- tags: [OlapCommon, OlapReport, DimensionElement, MeasureElements, FilterElements, C#, VB] keywords: [dimension, level, filter, measure, series, addition, categorical, elements, report] -->
```

---

<!-- 페이지 45 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_050.jpeg
document_name: Olap Common
page_number: 050
page_id: Olap Common#page_050
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:17:54Z
fidelity: lossless
-->

# Essential OlapCommon

## Overview
- Demonstrates creating an OLAP report with customized dimensions and measures.

## Content

### Creating an OLAP Report with Custom Dimension and Measure Elements

```csharp
[C#]

OlapReport olapReport = new OlapReport();
olapReport.Name = "Customer Report";
olapReport.CurrentCubeName = "Adventure Works";
DimensionElement dimensionElementColumn = new DimensionElement();
// Specifying the Name for the Dimension Element
dimensionElementColumn.Name = "Customer";
// Specifying the Hierarchy Name
dimensionElementColumn.HierarchyName = "Customer Geography";
dimensionElementColumn.AddLevel("Customer Geography", "Country");

MeasureElements measureElementColumn = new MeasureElements();
measureElementColumn.Elements.Add(new MeasureElement { Name = "Internet Sales Amount" });

DimensionElement dimensionElementRow = new DimensionElement();
// Specifying the Dimension Name
dimensionElementRow.Name = "Date";
dimensionElementRow.HierarchyName = "Fiscal";
dimensionElementRow.AddLevel("Fiscal", "Fiscal Year");
dimensionElementRow.Hierarchy.LevelElements["Fiscal Year"].Add("FY 2002");
dimensionElementRow.Hierarchy.LevelElements["Fiscal Year"].MemberElements[0].ShowChildMembers = true;
dimensionElementRow.Hierarchy.LevelElements["Fiscal Year"].MemberElements[0].Add("H1 FY 2002");
dimensionElementRow.Hierarchy.LevelElements["Fiscal Year"].MemberElements[0].ChildMemberElements[0].ShowChildMembers = true;
dimensionElementRow.Hierarchy.LevelElements["Fiscal Year"].MemberElements[0].ChildMemberElements[0].Add("Q1 FY 2002");
dimensionElementRow.Hierarchy.LevelElements["Fiscal Year"].MemberElements[0].ChildMemberElements[0].ChildMemberElements[0].ShowChildMembers = true;
dimensionElementRow.Hierarchy.LevelElements["Fiscal Year"].MemberElements[0].ChildMemberElements[0].ChildMemberElements[0].ChildMemberElements[0].ShowChildMembers = true;
dimensionElementRow.Hierarchy.LevelElements["Fiscal Year"].MemberElements[0].ChildMemberElements[0].ChildMemberElements[0].ChildMemberElements[0].Add("July 2001");
``` 

### Sample Code Explanation
- **Creating a Report**: Initializes an `OlapReport` object, sets its name, and specifies the cube to use.
- **Customizing Dimensions**: Defines different dimensions such as "Customer" and "Date" with their respective hierarchies and levels.
- **Adding Measures**: Specifies a measure column with a single measure, "Internet Sales Amount".
- **Hierarchy and Levels**: Configures the "Date" dimension with a fiscal hierarchy, adding fiscal years, half-years, and quarters, and setting flags for showing child members.

### Custom Dimension and Measure Setup
- **DimensionElement**: Represents a dimension in the OLAP report.
- **HierarchyName**: Specifies the hierarchy name for that dimension.
- **AddLevel**: Adds levels to the hierarchy, defining the granularity of the dimension.
- **MeasureElements**: Defines columns for measures in the report.
- **ShowChildMembers**: Controls whether child members of a level are shown in the report.

## Code Examples

```csharp
[C#]
OlapReport olapReport = new OlapReport();
// Additional code as shown above...

[VB]
```

## Cross References
- Refer to the OLAP Report documentation for more details on hierarchy and level configurations.

<!-- tags: [olapreport, dimensionelement, measureelements, fiscalhierarchy, customergeography] keywords: [olap report, dimension, measure, hierarchy, level] -->
```

---

<!-- 페이지 46 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_054.jpeg
document_name: Olap Common
page_number: 054
page_id: Olap Common#page_054
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:18:17Z
fidelity: lossless
-->

# Essential OlapCommon

```vb
Dim topCountElement As TopCountElement = New TopCountElement(AxisPosition.Categorical, 5)
topCountElement.MeasureName = "Internet Sales Amount"

'' Adding Column Members
olapReport.CategoricalElements.Add(dimensionElementColumn)

'' Adding Measure Element
olapReport.CategoricalElements.Add(measureElementColumn)

'' Adding Measure Element
olapReport.CategoricalElements.Add(topCountElement)

'' Adding Row Members
olapReport.SeriesElements.Add(dimensionElementRow)
```

### 4.3.11.1.9 Report with Named set

#### [C#]

```csharp
OlapReport olapReport = new OlapReport();
olapReport.Name = "Customer Report";
olapReport.CurrentCubeName = "Adventure Works";

DimensionElement dimensionElementColumn = new DimensionElement();
// Specifying the dimension Name
dimensionElementColumn.Name = "Customer";
// Specifying the Hierarchy Name
dimensionElementColumn.HierarchyName = "Customer Geography";
dimensionElementColumn.AddLevel("Customer Geography", "Country");

MeasureElements measureElementColumn = new MeasureElements();
// Specifying the measure elements
measureElementColumn.Elements.Add(new MeasureElement { Name = "Internet Sales Amount" });

// Specifying the NamedSet Element
NamedSetElement dimensionElementRow = new NamedSetElement();
// Specifying the dimension name
dimensionElementRow.Name = "Core Product Group";

/// Adding the Column members
olapReport.CategoricalElements.Add(dimensionElementColumn);
/// Adding the Measure elements
olapReport.CategoricalElements.Add(measureElementColumn);
/// Adding the Row members
```

<!-- tags: [product, module, control, api, version?] keywords: [OlapReport, DimensionElement, MeasureElements, NamedSetElement, AxisPosition, Categorical, TopCountElement, Customer Geography, Core Product Group, Internet Sales Amount] -->
```

---

<!-- 페이지 47 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_058.jpeg
document_name: Olap Common
page_number: 058
page_id: Olap Common#page_058
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:18:29Z
fidelity: lossless
-->

Essential OlapCommon

```vb
'// Calculated Measure
Dim calculatedMeasure2 As CalculatedMember = New CalculatedMember()
calculatedMeasure2.Name = "Sales Range"
calculatedMeasure2.AddElement(New MeasureElement With {.Name = "Sales Amount"})
calculatedMeasure2.Expression = "IIF([Measures].[Sales Amount]>200000,""High"",""Low"")"

' Calculated Dimension
Dim calculateDimension As CalculatedMember = New CalculatedMember()
calculateDimension.Name = "Bikes & Components"
calculateDimension.Expression = "([Product].[Product Categories].[Category].[Bikes] + [Product].[Product Categories].[Category].[Components] )"
calculateDimension.AddElement(internalDimension)

Dim measureElementColumn As MeasureElements = New MeasureElements()
measureElementColumn.Elements.Add(New MeasureElement With {.Name = "Sales Amount"})
measureElementColumn.Elements.Add(New MeasureElement With {.Name = "Order Quantity"})

Dim dimensionElementRow As DimensionElement = New DimensionElement()
'Specifying the Dimension Name
dimensionElementRow.Name = "Date"
dimensionElementRow.AddLevel("Fiscal", "Fiscal Year")

'// Adding Calculated members in calculated member collection
olapReport.CalculatedMembers.Add(calculatedMeasure1)
olapReport.CalculatedMembers.Add(calculateDimension)
olapReport.CalculatedMembers.Add(calculatedMeasure2)

''' Adding Column Members
olapReport.CategoricalElements.Add(dimensionElementColumn)
olapReport.CategoricalElements.Add(calculateDimension)
```

---

© 2013 Syncfusion. All rights reserved.  
```

---

<!-- 페이지 48 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_062.jpeg
document_name: Olap Common
page_number: 062
page_id: Olap Common#page_062
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:18:41Z
fidelity: lossless
-->

# Essential OlapCommon

```cs
"[Employee].[Employees].[Email Address]"
);

DimensionElement dimensionElementColumn = new DimensionElement();
// Specifying the Dimension Name
dimensionElementColumn.Name = "Product";
// Specifying the Hierarchy and level name for the Dimension Element
dimensionElementColumn.AddLevel("Product Categories", "Category");
dimensionElementColumn.MemberProperties.Add(new MemberProperty("Dealer Price", "[Product].[Product Categories].[Dealer Price]"));
dimensionElementColumn.MemberProperties.Add(new MemberProperty("Standard Cost", "[Product].[Product Categories].[Standard Cost]"));

// Adding Row Members
olapReport.SeriesElements.Add(dimensionElementRow);

///Adding Column Members
olapReport.CategoricalElements.Add(measureElementColumn);
```

### VB

```vb
Dim olapReport As OlapReport = New OlapReport()
olapReport.Name = "Employee Sales Report"
' Specifying the current cube name
olapReport.CurrentCubeName = "Adventure Works"

Dim measureElementColumn As MeasureElements = New MeasureElements()
' Specifying the Name for the Measure Element
measureElementColumn.Elements.Add(New MeasureElement With {.Name = "Sales Amount Quota"})

Dim dimensionElementRow As DimensionElement = New DimensionElement()
' Specifying the Dimension Name
dimensionElementRow.Name = "Employee"
' Specifying the Hierarchy and level name for the Dimension Element
dimensionElementRow.AddLevel("Employees", "Employee Level 02")
dimensionElementRow.Hierarchy.LevelElements("Employee Level 02").
```

## API Reference (if applicable)
- None specific to this page.

## Code Examples (multi-language supported)
- C# Example:
```cs
"[Employee].[Employees].[Email Address]"
);
DimensionElement dimensionElementColumn = new DimensionElement();
// Specifying the Dimension Name
dimensionElementColumn.Name = "Product";
// Specifying the Hierarchy and level name for the Dimension Element
dimensionElementColumn.AddLevel("Product Categories", "Category");
dimensionElementColumn.MemberProperties.Add(new MemberProperty("Dealer Price", "[Product].[Product Categories].[Dealer Price]"));
dimensionElementColumn.MemberProperties.Add(new MemberProperty("Standard Cost", "[Product].[Product Categories].[Standard Cost]"));

// Adding Row Members
olapReport.SeriesElements.Add(dimensionElementRow);

///Adding Column Members
olapReport.CategoricalElements.Add(measureElementColumn);
```

- VB Example:
```vb
Dim olapReport As OlapReport = New OlapReport()
olapReport.Name = "Employee Sales Report"
' Specifying the current cube name
olapReport.CurrentCubeName = "Adventure Works"

Dim measureElementColumn As MeasureElements = New MeasureElements()
' Specifying the Name for the Measure Element
measureElementColumn.Elements.Add(New MeasureElement With {.Name = "Sales Amount Quota"})

Dim dimensionElementRow As DimensionElement = New DimensionElement()
' Specifying the Dimension Name
dimensionElementRow.Name = "Employee"
' Specifying the Hierarchy and level name for the Dimension Element
dimensionElementRow.AddLevel("Employees", "Employee Level 02")
dimensionElementRow.Hierarchy.LevelElements("Employee Level 02").
```

<!-- tags: [product, olap, syncfusion, winforms, reporting, dimension, hierarchy, elements, measure, element, property] keywords: [OlapReport, DimensionElement, MeasureElements, SeriesElements, CategoricalElements, MemberProperty, LevelElements] -->
```

---

<!-- 페이지 49 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_066.jpeg
document_name: Olap Common
page_number: 066
page_id: Olap Common#page_066
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:18:59Z
fidelity: lossless
-->

Essential OlapCommon

## Overview

- Explains how to customize currentPage and pageSize settings in OlapReport.
- Demonstrates how to implement drill position and drill replace functionalities using MDX queries.
- Provides examples in both C# and VB.NET.

## Content

### 4.3.14 Drill Position

Drill position enables the user to drill into the current position of a selected member in the OlapReport. This excludes the drilled data of the selected member in other positions by using MDX queries.

The following code illustrates how to achieve drill position support in the current report:

**C#**

```csharp
olapDataManager.CurrentReport.PagerOptions.CategoricalCurrentPage = 1;
olapDataManager.CurrentReport.PagerOptions.SeriesCurrentPage = 2;
olapDataManager.CurrentReport.PagerOptions.CategoricalPageSize = 50;
olapDataManager.CurrentReport.PagerOptions.SeriesPageSize = 50;
```

**VB.NET**

```vb
olapDataManager.CurrentReport.PagerOptions.CategoricalCurrentPage = 1
olapDataManager.CurrentReport.PagerOptions.SeriesCurrentPage = 2
olapDataManager.CurrentReport.PagerOptions.CategoricalPageSize = 50
olapDataManager.CurrentReport.PagerOptions.SeriesPageSize = 50
```

### 4.3.15 Drill Replace

Drill Replace displays only the immediate child members and ancestors on drill-down and drill-up respectively.

The following code illustrates how to achieve drill replace support in a current report:

**C#**

```csharp
olapDataManager.CurrentReport.DrillType = DrillType.DrillReplace;
```

**VB.NET**

```vb
olapDataManager.CurrentReport.DrillType = DrillType.DrillReplace
```

<!-- tags: [product, module, control, api, version?] keywords: [OlapReport, PagerOptions, DrillPosition, DrillReplace, MDX, C#, VB.NET] -->
```

---

<!-- 페이지 50 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_070.jpeg
document_name: Olap Common
page_number: 070
page_id: Olap Common#page_070
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:19:12Z
fidelity: lossless
-->

# Essential OlapCommon

| Property          | Description                              | Type | Data Type |
|-------------------|------------------------------------------|------|-----------|
| VirtualKpiElements | Gets or sets the collection of VirtualKpiElement. | CLR  | Items    |

## 4.3.17.2 Adding Virtual KPI Element to the OlapReport

### OLAP Report Definition with VirtualKpiElement

```csharp
public OlapReport VirtualKPIReport()
{
    OlapReport olapReport = new OlapReport("Virtual KPI Report");
    olapReport.CurrentCubeName = "Adventure Works";

    MeasureElements measureElements = new MeasureElements();
    measureElements.Add(new MeasureElement { Name = "Internet Sales Amount" });

    olapReport.CategoricalElements.Add(measureElements);

    VirtualKpiElement virtualKPIElement = new VirtualKpiElement();
    virtualKPIElement.Name = "Sample KPI";
    virtualKPIElement.KpiValueExpression = ""; //Value expression
    virtualKPIElement.KpiGoalExpression = ""; //Goal expression
    virtualKPIElement.KpiStatusExpression = ""; //Status expression
    virtualKPIElement.KpiTrendExpression = ""; //Trend expression
    virtualKPIElement.StatusGraphic = ""; //Status graphic
    virtualKPIElement.TrendGraphic = ""; //Trend graphic
    olapReport.VirtualKpiElements.Add(virtualKPIElement);
    olapReport.CategoricalElements.Add(virtualKPIElement);

    DimensionElement internalDimension = new DimensionElement();
    internalDimension.Name = "Product";
    internalDimension.AddLevel("Product Categories", "Category");
    olapReport.SeriesElements.Add(internalDimension);

    return olapReport;
}
```

<!-- tags: [product, module, control, api, version?] keywords: [OlapReport, VirtualKPIElement, MeasureElements, DimensionElement, KpiValueExpression, KpiGoalExpression, KpiStatusExpression, KpiTrendExpression, StatusGraphic, TrendGraphic, ProductCategories, Category] -->
```

---

<!-- 페이지 51 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_074.jpeg
document_name: Olap Common
page_number: 074
page_id: Olap Common#page_074
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:19:25Z
fidelity: lossless
-->

# Essential OlapCommon

```md
When (
    [Measures].[Reseller Sales Amount]
    -
    (
        [Measures].[Reseller Sales Amount],
        ParallelPeriod
        (
            [Date].[Fiscal].[Fiscal Year],
            1,
            [Date].[Fiscal].CurrentMember
        )
    )
    /
    (
        [Measures].[Reseller Sales Amount],
        ParallelPeriod
        (
            [Date].[Fiscal].[Fiscal Year],
            1,
            [Date].[Fiscal].CurrentMember
        )
    ) > .02
Then 1
Else -1
End
```

## 4.4 QueryBuilderEngine

This class will generate the query from the MDXQuerySpecification. The query generation starts from invoking the `GenerateQueryEx()` static method of `QueryBuilderEngineVersion3`, the inner class of `QueryBuilderEngine` class.

<!-- tags: [OlapCommon, query generation, MDXQuerySpecification, QueryBuilderEngine,GenerateQueryEx, performance optimization] keywords: [Olap, query builder, MDX, cube, data analysis] -->
```

---

<!-- 페이지 52 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_078.jpeg
document_name: Olap Common
page_number: 078
page_id: Olap Common#page_078
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:19:35Z
fidelity: lossless
-->

## Essential OlapCommon

- **Item Source**
- **OlapReport**

### Steps to Use OlapCommon

1. **Provide an Item source. The source can be:**
   - `IEnumerable Collection`
   - `ITyped List`

2. **Once the Item source was bounded, give the OlapReport.**

3. **The given source will be formatted based on the given OlapReport and the result set will be passed to the controls.**

4. **The output will be displayed in the controls.**

## Summary
- This section outlines the process of configuring and utilizing the `OlapCommon` component in Syncfusion Winforms, detailing the steps required to provide data sources, format them using `OlapReport`, and display the results.

<!-- tags: [Essential OlapCommon, Syncfusion Winforms, data sources, reporting, OlapReport] keywords: [Item Source, IEnumerable Collection, ITyped List, OlapReport, data formatting, controls, output display] -->
```

---

<!-- 페이지 53 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_082.jpeg
document_name: Olap Common
page_number: 082
page_id: Olap Common#page_082
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:19:44Z
fidelity: lossless
-->

# Essential OlapCommon

## Overview
- Add WCF Service (from the installed templates) in to the Web project.
- Inherit the newly added WCF service with `IOLapDataProvider` and explicitly implement the `IOLapDataProvider`.
- The connection to the database is done with the help of WCF service.
- The service has to be created and instantiated as described below:
- The WCF Service has to implement the `IOLapDataProvider` interface that requires the `OlapDataProvider` which can be instantiated by passing the connection string.

## Content

### Creating OLAP WCF Service in Web Project

The code snippet below explains how to create OLAP WCF service in Web project:

```csharp
[AspNetCompatibilityRequirements(RequirementsMode = AspNetCompatibilityRequirementsMode.Allowed)]
[ServiceBehavior(IncludeExceptionDetailInFaults = true)]
public class OlapManager : IOLapDataProvider
{
#region Private variables
    private readonly OlapDataProvider _dataManager;
#endregion

#region Constructor
    /// <summary>
    /// Initializes a new instance of the <see cref="OlapManager"/>
    /// class.
    /// </summary>
    public OlapManager()
    {
        _dataManager = new OlapDataProvider("DataSource=localhost;Initial CatalogAdventure Works DW");
    }
#endregion

#region IOLapDataProvider Members

### IOLapDataProvider Members

#### ExecuteOlapReportWithLevelTypeAll Method

```csharp
    public CellSet ExecuteOlapReportWithLevelTypeAll(OlapReport report, bool showLevelTypeAll)
    {
        CellSet cellSet =
            _dataManager.ExecuteOlapReportWithLevelTypeAll(report, showLevelTypeAll);
        _dataManager.DataProvider.CloseConnection();
        return cellSet;
    }
```

#### Summary

```csharp
/// <summary>
/// Gets the MDX query.
/// </summary>
/// <param name="report">The report.</param>
/// <returns></returns>
```
```  
<!-- tags: [Essential OlapCommon, WCF Service, IOLapDataProvider, OlapDataProvider, OLAP WCF Service, Web project, C#] keywords: [OlapReport, CellSet, showLevelTypeAll, CloseConnection, MDX query, Adventure Works DW] -->
```

---

<!-- 페이지 54 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_086.jpeg
document_name: Olap Common
page_number: 086
page_id: Olap Common#page_086
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:19:58Z
fidelity: lossless
-->

# Essential OlapCommon

## Overview
- Provides methods to execute OLAP reports and MDX queries.
- Handles connection management for data providers.
- Supports retrieving cube information, schemas, and member collections.

## Content

### WinForms-specific Conventions
The following functions are part of the `OlapCommon` class and are used to interact with OLAP data.

#### Functions

##### GetMdxQuery
```vb
Public Function GetMdxQuery(ByVal report As Syncfusion.OlapSilverlight.Reports.OlapReport) As String
    Dim mdxReturned As String = Me._dataManager.GetMdxQuery(report)
    Me._dataManager.DataProvider.CloseConnection()
    Return mdxReturned
End Function
```

##### ExecuteOlapReport
```vb
Public Function ExecuteOlapReport(ByVal report As OlapReport) As CellSet
    Dim cellSet As CellSet = _dataManager.ExecuteOlapReport(report)
    _dataManager.DataProvider.CloseConnection()
    Return cellSet
End Function
```

##### ExecuteMdxQuery
```vb
Public Function ExecuteMdxQuery(ByVal mdxQuery As String) As CellSet
    Dim cellSet As CellSet = _dataManager.ExecuteMdxQuery(mdxQuery)
    _dataManager.DataProvider.CloseConnection()
    Return cellSet
End Function
```

##### GetCubes
```vb
Public Function GetCubes() As CubeInfoCollection
    Dim cubes As CubeInfoCollection = _dataManager.GetCubes()
    _dataManager.DataProvider.CloseConnection()
    Return cubes
End Function
```

##### GetCubeSchema
```vb
Public Function GetCubeSchema(ByVal cubeName As String) As CubeSchema
    Dim cubeSchema As CubeSchema = _dataManager.GetCubeSchema(cubeName)
    _dataManager.DataProvider.CloseConnection()
    Return cubeSchema
End Function
```

##### GetChildMembers
```vb
Public Function GetChildMembers(ByVal memberUniqueName As String, ByVal cubeName As String) As MemberCollection
    Dim childMembers As MemberCollection = _dataManager.GetChildMembers(memberUniqueName, cubeName)
    _dataManager.DataProvider.CloseConnection()
    Return childMembers
End Function
```

##### GetLevelMembers
```vb
Public Function GetLevelMembers(ByVal levelUniqueName As String, ByVal cubeName As String) As MemberCollection
    Dim levelMembers As MemberCollection = _dataManager.GetLevelMembers(levelUniqueName, cubeName)
    _dataManager.DataProvider.CloseConnection()
    Return levelMembers
End Function
```

##### Execute
```vb
Public Function Execute(ByVal mdxQuery As String) As Object
    Dim resultSet As var = Me._dataManager.Execute(mdxQuery)
    _dataManager.DataProvider.CloseConnection()
    Return resultSet
End Function
```

## API Reference

### Methods

#### GetMdxQuery
- **Parameters**: `report` (Syncfusion.OlapSilverlight.Reports.OlapReport)
- **Returns**: String (MDX query string)

#### ExecuteOlapReport
- **Parameters**: `report` (OlapReport)
- **Returns**: CellSet (Result set of the OLAP report)

#### ExecuteMdxQuery
- **Parameters**: `mdxQuery` (String)
- **Returns**: CellSet (Result set of the MDX query)

#### GetCubes
- **Returns**: CubeInfoCollection (Collection of available cubes)

#### GetCubeSchema
- **Parameters**: `cubeName` (String)
- **Returns**: CubeSchema (Schema of the specified cube)

#### GetChildMembers
- **Parameters**: `memberUniqueName` (String), `cubeName` (String)
- **Returns**: MemberCollection (Collection of child members)

#### GetLevelMembers
- **Parameters**: `levelUniqueName` (String), `cubeName` (String)
- **Returns**: MemberCollection (Collection of members at the specified level)

#### Execute
- **Parameters**: `mdxQuery` (String)
- **Returns**: Object (Result of the executed MDX query)

<!-- tags: [WinForms, OLAP, MDX, Cube, Schema, Member, DataProvider, Connection] keywords: [GetMdxQuery, ExecuteOlapReport, ExecuteMdxQuery, GetCubes, GetCubeSchema, GetChildMembers, GetLevelMembers, Execute] -->
```

---

<!-- 페이지 55 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_090.jpeg
document_name: Olap Common
page_number: 090
page_id: Olap Common#page_090
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:20:21Z
fidelity: lossless
-->

# Essential OlapCommon

```vb
Dim dimensionElementRow As DimensionElement = New DimensionElement()
'Specifying the Dimension Name
dimensionElementRow.Name = "Date"
dimensionElementRow.AddLevel("Fiscal", "Fiscal Year")

'Adding Column Members
olapReport1.CategoricalElements.Add(dimensionElementColumn)
'Adding Measure Element
olapReport1.CategoricalElements.Add(measureElementColumn)
'Adding Row Members
olapReport1.SeriesElements.Add(dimensionElementRow)
```

## 5.8.1 CurrentReport

Once the OlapReport is created by assigning the report to the **CurrentReport** property of the OlapDataManager, you can bind the OlapReport to the OlapDataManager.

The following code snippet explains the assigning of an OlapReport to CurrentReport property:

### C#
```csharp
OlapDataManager.CurrentReport = olapReport;
```

### VB
```vb
OlapDataManager.CurrentReport = olapReport
```

## 5.8.2 SetCurrentReport

The following code snippet explains setting an OlapReport to CurrentReport of an OlapDataManager using SetCurrentReport method:

### C#
```csharp
OlapDataManager.SetCurrentReport(olapReport);
```

### VB
```vb
OlapDataManager.SetCurrentReport(olapReport)
```

## 5.8.3 LoadOlapDataManager

The following code snippet explains loading an OlapReport to CurrentReport property of an OlapDataManager using LoadOlapDataManager method:

### C#
```csharp
```

<!-- tags: [Olap, OlapCommon, OlapReport, OlapDataManager, CurrentReport, SetCurrentReport, LoadOlapDataManager, WinForms] keywords: [OlapReport, OlapDataManager, CurrentReport, SetCurrentReport, LoadOlapDataManager] -->
```

---

<!-- 페이지 56 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_094.jpeg
document_name: Olap Common
page_number: 094
page_id: Olap Common#page_094
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:20:33Z
fidelity: lossless
-->

## Essential OlapCommon

### Code Example: C# and VB

```csharp
[C#]
OlapDataManager olapDataManager = new OlapDataManager("DataSource=localhost; Initial Catalog=Adventure Works DW");
string mdxQuery =
@"SELECT NON EMPTY ({{Hierarchize({DrilldownLevel({[Customer].[Customer Geography].[All Customers]}})) * 
{[MEASURES].[Internet Sales Amount]}) dimension properties 
member_type ON COLUMNS, NON EMPTY ({{Hierarchize(
{DrilldownLevel({[Date].[Fiscal].[All Periods]}}))}} ) 
dimension properties member_type ON ROWS 
FROM [Adventure Works]   CELL PROPERTIES
VALUE, FORMAT_STRING, FORMATTED_VALUE";
olapDataManager.ExecuteCellSet(mdxQuery);
```

```vb
[VB]
Dim olapDataManager As OlapDataManager = New OlapDataManager("DataSource=localhost; Initial Catalog=Adventure Works DW")
Dim mdxQuery As String = "SELECT NON EMPTY ({{Hierarchize({DrilldownLevel({[Customer].[Customer Geography].[All Customers]}})) * 
{[MEASURES].[Internet Sales Amount]}) dimension properties 
member_type ON COLUMNS, NON EMPTY ({{Hierarchize(
{DrilldownLevel({[Date].[Fiscal].[All Periods]}}))}} ) 
dimension properties member_type ON ROWS 
FROM [Adventure Works]   CELL PROPERTIES
VALUE, FORMAT_STRING, FORMATTED_VALUE"
olapDataManager.ExecuteCellSet(mdxQuery)
```

### Sequential Diagram

**Sequential Diagram**

The following sequential diagram is matching when user gives input as MDX query:

---

> **Note:** The diagram is not included in this markdown representation.

---

## API Reference

### WinForms-specific Information
The provided code examples demonstrate the use of the `OlapDataManager` class to execute MDX queries in a Windows Forms application. The `ExecuteCellSet` method is used to retrieve the results of the MDX query as a cell set.

## Code Examples (C# and VB)
The code examples provided above illustrate how to connect to a data source, construct an MDX query, and execute it using the `OlapDataManager`. The MDX query retrieves non-empty members of the specified dimensions and measures, formatting the values appropriately.

## Cross References
- See also: [MDX Query Basics](#mdx-query-basics)
- See also: [OlapDataManager Class Reference](#olapdatamanager-class-reference)

<!-- tags: [OlapDataManager, MDXQuery, WinForms, Syncfusion, C#, VB] keywords: [olap, mdx, query, data manager, windows forms, cell set, non-empty members, dimensions, measures, formatted values] -->
```

---

<!-- 페이지 57 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_098.jpeg
document_name: Olap Common
page_number: 098
page_id: Olap Common#page_098
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:20:49Z
fidelity: lossless
-->

# Essential OlapCommon

```csharp
olapDataManager.LoadReport(@"C:\SampleReport\RevenueAnalysis.xml");
```

```vb
olapDataManager.LoadReport("C:\SampleReport\RevenueAnalysis.xml")
```

## For Silverlight:

The saved report file can be used with `OlapDataManager` by serializing it to type `OlapReport` with `XmlSerializer`.

The following code snippet will illustrate the loading of a saved XML report file:

### C#

```csharp
private void LoadReport()
{
    OpenFileDialog dlg = new OpenFileDialog();
    dlg.Filter = "XML files (*.xml)|*.xml";
    bool? b = dlg.ShowDialog();

    if (b.HasValue && b.Value)
    {
        OlapReport report = null;

        using (FileStream stream = dlg.File.OpenRead())
        {
            System.Xml.Serialization.XmlSerializer serializer = new System.Xml.Serialization.XmlSerializer(typeof(OlapReportCollection));
            OlapReportCollection olapReportCollection = serializer.Deserialize(stream) as OlapReportCollection;
            report = olapReportCollection[0];
        }
        olapDataManager.SetCurrentReport(report);
    }
}
```

### VB

```vb
Private Sub LoadReport()
    Dim dlg As OpenFileDialog = New OpenFileDialog()
```

---

``` 
© 2013 Syncfusion. All rights reserved.
Page 98
```


---

<!-- 페이지 58 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_102.jpeg
document_name: Olap Common
page_number: 102
page_id: Olap Common#page_102
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:21:00Z
fidelity: lossless
-->

## Essential OlapCommon

```csharp
MeasureElements measureElementColumn = new MeasureElements();
measureElementColumn.Elements.Add(new MeasureElement { Name = "Internet Sales Amount" });

FilterElement filterElement = new FilterElement(AxisPosition.Categorical);
filterElement.Elements.Add(measureElementColumn);
filterElement.Elements.Add(dimensionElementColumn);
filterElement.FilterCase = FilterCase.GreaterThan;
filterElement.FilterValue.Add(new MeasureElement { Name = "Internet Sales Amount", Visible = true });
filterElement.FilterValue.Add(new FilterValue { Filter_Value = 2700000.0 });
filterElement.IsFilterCondition = true;
/// Adding Column Members
olapReport.CategoricalElements.Add(dimensionElementColumn);
olapReport.CategoricalElements.IsFilterOrSortOn = true;
/// Adding Measure Element
olapReport.FilterElements.Add(filterElement);
```

### [VB]

```vb
Dim dimensionElementColumn As DimensionElement = New DimensionElement()
' Specifying the Name for the Dimension Element
dimensionElementColumn.Name = "Customer"

Dim measureElementColumn As MeasureElements = New MeasureElements()
measureElementColumn.Elements.Add(New MeasureElement With {.Name = "Internet Sales Amount"})

Dim filterElement As FilterElement = New FilterElement(AxisPosition.Categorical)
filterElement.Elements.Add(measureElementColumn)
filterElement.Elements.Add(dimensionElementColumn)
filterElement.FilterCase = FilterCase.GreaterThan

filterElement.FilterValue.Add(New MeasureElement With {.Name = "Internet Sales Amount", .Visible = True})

filterElement.FilterValue.Add(New FilterValue With {.Filter_Value =
```

---  
© 2013 Syncfusion. All rights reserved.  
```  
<!-- tags: [Syncfusion Winforms, Olap Common, MeasureElements, FilterElement, DimensionElement, FilterCase, FilterValue, CSharp, VB, API Reference, Code Examples] keywords: [Olap Common, Essential Features, MeasureElements, FilterElement, DimensionElement, FilterCase, FilterValue, CSharp, VB, API, Code Examples, WinForms] -->
``` 
``` 


---

<!-- 페이지 59 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_106.jpeg
document_name: Olap Common
page_number: 106
page_id: Olap Common#page_106
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:21:13Z
fidelity: lossless
-->

# Essential OlapCommon

## Overview
- Connect WCF Service by an additional Binding Type in Silverlight application.
- OLAP Silverlight controls can be bound to BasicHttpBinding support.
- Incorrect specification of endpoint address will lead to Initialize Component Error.
- Include BasicHttpBinding configuration in Web.Config file for proper service binding.

## Content

### 5.21 Connect WCF Service by an additional Binding Type in Silverlight application

OLAP Silverlight controls can be bound to BasicHttpBinding support.

**Note:** Incorrect specification of endpoint address will lead to Initialize Component Error. The endpoint address should be set with respect to the type of bindings.

#### Use case Scenario

User can create Web service using the BasicHttpBinding feature and bind the service to OLAP Silverlight controls.

#### BasicHttpBinding

The following are steps to create a BasicHttpBinding:

Include the Basic Http Binding and Service endpoint address in the Web.Config file as given in the following code:

```xml
[XML]
<!-- <Bindings> -->
<bindings>
    <basicHttpBinding>
        <binding name="binaryHttpBinding" maxBufferSize="2147483647" maxReceivedMessageSize="2147483647">
            <readerQuotas maxDepth="2147483647" />
            <security mode="None" />
        </binding>
    </basicHttpBinding>
</bindings>

<!-- <Endpoint Address> -->
<services>
    <service behaviorConfiguration="Services.OlapManagerBehavior" name="Services.OlapManager">
        <endpoint address="basic" binding="basicHttpBinding" bindingConfiguration="binaryHttpBinding" contract="Syncfusion.OlapSilverlight.Manager.IOlapDataProvider" />
    </service>
</services>
```

### Page-level Navigation/TOC (if applicable)
- Connect WCF Service by an additional Binding Type in Silverlight application

## Cross References
- See also: BasicHttpBinding, OLAP Silverlight controls, Web.Config configuration

<!-- tags: [product, module, control, api, version?] keywords: [unclear] -->
```

---

<!-- 페이지 60 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_110.jpeg
document_name: Olap Common
page_number: 110
page_id: Olap Common#page_110
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:21:26Z
fidelity: lossless
-->

# Essential OlapCommon

## 5.24 Edit MDX Query before Its Execution

MDX Query can be edited before its execution to retrieve the CellSet through handling the BeforeMdxQueryExecute event of OlapDataManager. The following code example illustrates this.

### C#

```csharp
olapDataManager.BeforeMdxQueryExecute += new QueryExecuteEventHandler(olapDataManager_BeforeMdxQueryExecute);

void olapDataManager_BeforeMdxQueryExecute(object sender, QueryExecutingEventArgs e)
{
    e.MdxQuery = "Edit MDX query here";
}
```

### VB

```vb
Private olapDataManager.BeforeMdxQueryExecute += New QueryExecuteEventHandler(AddressOf olapDataManager_BeforeMdxQueryExecute)

Private Sub olapDataManager_BeforeMdxQueryExecute(ByVal sender As Object, ByVal e As QueryExecutingEventArgs)
    e.MdxQuery = "Edit MDX query here"
End Sub
```

## 5.25 Host BI Silverlight component in ASP.NET MVC Web Project

This section explains how to add the Silverlight components in an MVC project:

1. Open Visual Studio IDE.
2. Go to File → New → Project and create a new Silverlight application.

A dialog window opens as shown below:
```html
© 2013 Syncfusion. All rights reserved. 110 | Page
```
<!-- tags: [olapcommon, mdxquery, olapidatamanager, silverlight, asp.net mvc, tutorial, event handling, code examples, visual studio, mvc project setup] keywords: [mdxquery, olapidatamanager, silverlight, mvc, olapcommon, event, handler, tutorial] -->
```

---

<!-- 페이지 61 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_114.jpeg
document_name: Olap Common
page_number: 114
page_id: Olap Common#page_114
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:21:38Z
fidelity: lossless
-->

# Essential Olap Common

## Overview
- Demonstrates the process of integrating OlapGrid with a web project.
- Explains adding assemblies as references and configuring a WCF Service.
- Highlights the steps to create and configure a WCF Service named `OlapManager`.

## Content

### OlapGrid in Design
The image titled "Figure 17: OlapGrid in Designer Page" illustrates the Visual Studio designer with the OlapGrid tool being selected in the toolbox. The XAML code and project structure are visible, showing the integration of the OlapGrid component into the project.

#### Steps to Integrate OlapGrid

1. **Add Assemblies as References:**
   - Add the following two assemblies as references to the web project:
     - **Syncfusion.Olap.Base**
     - **Syncfusion.OlapSilverlight.BaseWrapper**

2. **Add WCF Service:**
   - Add a WCF Service to the web project by following these steps:
     - Right-click the **Project**.
     - Select **Add New Item**.
     - Choose **WCF Service**.
   - **Name the service as `OlapManager`**.
     - Delete the `IOLapManager.cs` file as the service has to be inherited with the `IOLapDataProvider`.

### Figure: OlapGrid in Designer Page

![OlapGrid in Designer Page](attachment:Figure_17_OlapGrid_in_Designer_Page.jpg)

### Setting Up the WCF Service

- **Name of the Service:** `OlapManager`
- **File to Delete:** `IOLapManager.cs`
- **Inheritance:** The service must inherit from `IOLapDataProvider`.

## Page-level Navigation/TOC (if applicable)

- **Step 1:** Add required assemblies.
- **Step 2:** Configure WCF Service.

## Cross References

See also:
- Documentation on OlapGrid component.
- WCF Service implementation guide.

## RAG Annotations

<!-- 
tags: [OlapGrid, WCF Service, OlapManager, Syncfusion Winforms, version 11.4.0.26]
keywords: [OlapGrid, Designer, Visual Studio, WCF, Service, Syncfusion, Integration, Reference, Assemblies, OlapManager, IOLapDataProvider]
-->
```

---

<!-- 페이지 62 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_118.jpeg
document_name: Olap Common
page_number: 118
page_id: Olap Common#page_118
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:21:52Z
fidelity: lossless
-->

# Essential OlapCommon

## Overview
- Describes the instantiation and usage of the `OlapDataProvider` in a WinForms application.
- Details executing `OlapReport` and `MDX Query` to retrieve CellSet data.
- Demonstrates connection management and closing the provider connection.

## Content

### WinForms-specific conventions
This section focuses on the instantiation and methods to execute reports and MDX queries using the `OlapDataProvider`.

```vb
Public Sub New()
    Dim connectionString As String = "DataSource=localhost;Initial Catalog=Adventure Works DW"
    ' Instantiating the OlapDataProvider with connection string
    dataManager = New OlapDataProvider(connectionString)
End Sub
```

#### Region "OlapDataProvider Members"

##### Executing the CellSet by passing OlapReport
```vb
''' <summary>
''' Executing the CellSet by passing OlapReport
''' </summary>
''' <param name="report">The report.</param>
''' <returns></returns>
Public Function ExecuteOlapReport(ByVal report As Syncfusion.OlapSilverlight.Reports.OlapReport) As Syncfusion.OlapSilverlight.Data.CellSet
    Dim cellSet As Syncfusion.OlapSilverlight.Data.CellSet = Me.dataManager.ExecuteOlapReport(report)
    ' Closing the provider connection
    Me.dataManager.DataProvider.CloseConnection()
    Return cellSet
End Function
```

##### Executing the CellSet by passing MDX Query
```vb
''' <summary>
''' Executing the CellSet by passing MDX Query
''' </summary>
''' <param name="mdxQuery">The MDX query.</param>
''' <returns> The CellSet </returns>
Public Function ExecuteMdxQuery(ByVal mdxQuery As String) As Syncfusion.OlapSilverlight.Data.CellSet
    Dim cellSet As Syncfusion.OlapSilverlight.Data.CellSet = Me.dataManager.ExecuteMdxQuery(mdxQuery)
    'Closing the provider connection.
    Me.dataManager.DataProvider.CloseConnection()
    Return cellSet
End Function
```

## API Reference

### Namespace: `Syncfusion.OlapSilverlight`

#### Class: `OlapDataProvider`

##### Methods
- **ExecuteOlapReport**:
  - **Parameters**:
    - `report` (Type: `OlapReport`): The report to execute.
  - **Returns**: `CellSet`
  - **Description**: Executes the given `OlapReport` and returns the CellSet data.

- **ExecuteMdxQuery**:
  - **Parameters**:
    - `mdxQuery` (Type: `String`): The MDX query to execute.
  - **Returns**: `CellSet`
  - **Description**: Executes the given MDX query and returns the CellSet data.

## Code Examples (multi-language supported)
The provided code examples illustrate how to:
- Instantiate the `OlapDataProvider` with a connection string.
- Execute an `OlapReport` or an `MDX Query` to retrieve data.
- Properly manage the connection and close it after execution.

## Page-level Navigation/TOC (if applicable)
- [title/heading not visible - replace with actual TOC content if applicable]

## Cross References
See also:
- [Cross-references to related sections or pages if present]

## RAG Annotations
<!-- tags: [Syncfusion Winforms, OlapDataProvider, OlapReport, MDX Query, CellSet] keywords: [connectionString, OlapDataProvider, OlapReport, ExecuteOlapReport, ExecuteMdxQuery, CellSet, CloseConnection] -->
```


---

<!-- 페이지 63 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_122.jpeg
document_name: Olap Common
page_number: 122
page_id: Olap Common#page_122
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:22:14Z
fidelity: lossless
-->

# Essential OlapCommon

```csharp
// Specifying the DataProvider for OlapDataManager.
m_OlapDataManager.DataProvider = this.DataProvider;
// Set current report for OlapDataManager.
m_OlapDataManager.SetCurrentReport(CreateOlapReport());
// Specifying the OlapDataManager for OlapGrid.
this.olapGrid1.OlapDataManager = m_OlapDataManager;
// Data Binding.
this.olapGrid1.DataBind();
}
```

### [VB]
```vb
Private Sub MainPage_Loaded(ByVal sender As Object, ByVal e As RoutedEvent Args)

    ' Initialize the service connection.
    Me.InitializeConnection()
    
    ' Instantiating the OlapDataManager.
    Dim m_OlapDataManager As OlapDataManager = New OlapDataManager()
    
    ' Specifying the DataProvider for OlapDataManager.
    m_OlapDataManager.DataProvider = Me.DataProvider
    
    ' Set current report for OlapDataManager.
    m_OlapDataManager.SetCurrentReport(CreateOlapReport())
    
    ' Specifying the OlapDataManager for OlapGrid.
    Me.olapGrid1.OlapDataManager = m_OlapDataManager
    
    ' Data Binding.
    Me.olapGrid1.DataBind()
End Sub
```

### Example Output - Internet Sales Amount

|  | Internet Sales Amount |  |
| --- | --- | --- |
|  | Australia | Canada | France | Germany | United Kingdom | United States | Total |
| FY 2002 | $2,568,701.39 | $573,100.97 | $414,245.32 | $513,353.17 | $550,507.33 | $2,452,176.07 | $7,072,084.24 |
| FY 2003 | $2,099,585.43 | $305,010.69 | $633,399.70 | $593,247.24 | $696,594.97 | $1,434,296.26 | $5,762,134.30 |
| FY 2004 | $4,383,479.54 | $1,088,879.50 | $1,592,880.75 | $1,784,107.09 | $2,140,388.50 | $5,483,882.67 | $16,473,618.05 |
| FY 2005 | $9,234.23 | $10,853.70 | $3,491.95 | $3,604.83 | $4,221.41 | $19,434.51 | $50,840.63 |
| Total | $9,061,000.58 | $1,977,844.86 | $2,644,017.71 | $2,894,312.34 | $3,391,712.21 | $9,389,789.51 | $29,358,677.22 |

> **Note:** Click [here for Sample Report](#) to view a sample report.

## References
- Sample Report: [here for Sample Report](#)

<!-- tags: [syncfusion, windowsforms, olapcommon, data provider, data manager, grid, sample report, version 11.4.0.26] keywords: [internet sales amount, australia, canada, france, germany, united kingdom, united states, fiscal years, total sales, data binding, data provider, olap report, olapgrid, winforms, syncfusion, programming examples, vb.net, c#] -->
```

---

<!-- 페이지 64 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_003.jpeg
document_name: Olap Common
page_number: 003
page_id: Olap Common#page_003
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:14:30Z
fidelity: lossless
-->

## Overview
- Lists various sections related to filtering, creating, and managing OLAP reports and data.
- Focuses on techniques for slicing, dicing, and filtering OLAP data.
- Highlights steps for processing OLAP data and using query specifications.

## Content

### 4.3 Filter and Report Operations
#### 4.3.10 Filtering slicer elements by range
- 34

#### 4.3.11 Creating the OlapReport
- 36

##### 4.3.11.1 Sample Reports for OLAP data
- **4.3.11.1.1 Simple Report**
  - 37
- **4.3.11.1.2 Report with slicing operation**
  - 38
- **4.3.11.1.3 Report with dicing operation**
  - 40
- **4.3.11.1.4 Ordered Report**
  - 43
- **4.3.11.1.5 Report with Filter**
  - 45
- **4.3.11.1.6 Report with subset**
  - 47
- **4.3.11.1.7 Drill down report**
  - 49
- **4.3.11.1.8 Report with Top count Filter**
  - 52
- **4.3.11.1.9 Report with Named set**
  - 54
- **4.3.11.1.10 Report with calculated member**
  - 56
- **4.3.11.1.11 Report with KPI Element**
  - 59
- **4.3.11.1.12 Report with member properties**
  - 61

##### 4.3.11.2 Sample Report for Non-OLAP data
- 63

#### 4.3.12 Binding the OlapReport to OlapDataManager
- 65

#### 4.3.13 Paging 65
- 65

#### 4.3.14 Drill Position
- 66

#### 4.3.15 Drill Replace
- 66

#### 4.3.16 MDX Query Parsing
- **4.3.16.1 MDX Query binding with drill up and drill down operations**
  - 67
- **4.3.16.2 Adding MDX Query binding with drill up and drill down operations to an Application**
  - 68

#### 4.3.17 Virtual KPI Element
- **4.3.17.1 Properties**
  - 69
- **4.3.17.2 Adding Virtual KPI Element to the OlapReport**
  - 70

### 4.4 QueryBuilderFactory
#### 4.4.1 MDXQuerySpecification
- 75

#### 4.4.2 Steps in Query Generation
- 75

### 4.5 OLAP Data Processing
#### 4.5.1 Steps in processing OLAP Data
- 76

#### 4.5.2 Steps in processing Non-OLAP data
- 77

## 5 How To
- 79

## References
- Referenced from Syncfusion Winforms User Guides.

<!-- tags: [syncfusion-sdk, winforms, olap, olapreport, querybuilding, filtering, data processing] keywords: [olapreport, mdxquery, kpi element, report operations, slicing, dicing, filtering, drill down, query specifications] -->
```

---

<!-- 페이지 65 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_007.jpeg
document_name: Olap Common
page_number: 007
page_id: Olap Common#page_007
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:14:51Z
fidelity: lossless
-->

# Online Analytical Processing (OLAP)

Online Analytical Processing (OLAP) is a service that performs a real-time, multi-dimensional analysis of complex data stored in a database. The OLAP typically consists of a server component that uses specialized algorithms, indexing tools to efficiently process data mining tasks, and an OLAP client that efficiently lets you visualize the OLAP data pertaining to your business needs.

Here is how Wikipedia defines OLAP.

## ADOMD.NET

The Syncfusion OLAP controls use the **ADOMD.NET**, which is a Microsoft .NET framework provider for retrieving data from OLAP servers in the .NET platform. While ADOMD.NET primarily retrieves OLAP data from SQL Server Analysis Services (Microsoft's OLAP Server), its adherence to industry standards like XML/A allows you to access any OLAP server (SAP, SAS, Hyperion, etc.) through it and hence provides you the ability to visualize using Syncfusion OLAP control, OLAP data from myriads of data sources including Microsoft's SSAS.

## ADOMD.NET assembly and setup files information

The following assembly is required to run Syncfusion's OLAP samples:

- Microsoft.AnalysisServices.AdomdClient.dll

Install the following setup files for the above assembly:

- SQLServer2005_ADOMD.msi and SQLServer2005_ASOLEDB9.msi
- Or
- SQLSERVER2008_ASADOMD10.msi and SQLSERVER2008_ASOLEDB10.msi

These setup files can be downloaded at [Microsoft download center](https://www.microsoft.com/download-center/).

**Note:** By default, the following setup files will be installed while installing Syncfusion's Essential Studio setup for BI edition:

- SQLSERVER2008_ASADOMD10.msi
- SQLSERVER2008_ASOLEDB10.msi

## API Reference (if applicable)
- Namespace, Class, Members (Methods/Properties/Events/Enums), Parameters table, Returns, Exceptions.

## Code Examples (multi-language supported)
Extract ALL code exactly using fenced blocks: ```csharp, ```vb, ```xml, ```xaml, ```js, ```css, ```ts, ```python, etc.

### WinForms-specific conventions
- Distinguish between control names, namespaces, and types; prefer C# samples; treat property grids, designer steps, and menu paths as regular text.

<!-- tags: [OLAP, ADOMD.NET, Syncfusion Winforms, Multi-dimensional data analysis] keywords: [OLAP, ADOMD.NET, OLAP server, data visualization, Syncfusion controls, SQL Server Analysis Services, BI tools] -->
```

---

<!-- 페이지 66 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_011.jpeg
document_name: Olap Common
page_number: 011
page_id: Olap Common#page_011
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:15:06Z
fidelity: lossless
-->

# Essential OlapCommon

## Overview
- Provides an overview of how the class library is organized under the Syncfusion.OlapSilverlight.BaseWrapper assembly.
- Describes the use of WCF Service in OLAP Silverlight controls for querying the database.
- Explains the role of the DataProvider property of OlapDataManager in service call operations.
- Guides on creating and connecting a WCF Service.

## Content

### 3.3.1 WCF Service

**Note:** This class library was organized under `Syncfusion.OlapSilverlight.BaseWrapper` assembly.

To query the database, OLAP Silverlight controls use WCF Service. The `DataProvider` property of `OlapDataManager` performs the service call operations. For more details on creating and connecting a WCF Service, refer to the section **Creating and connecting a WCF Service.**

## API Reference

- **Namespace:** Syncfusion.OlapSilverlight.BaseWrapper
- **Class:** OlapDataManager
  - Properties:
    - `DataProvider`: Handles service call operations for database queries.

## Code Examples

```csharp
// Example of setting up WCF Service connection
using Syncfusion.OlapSilverlight.BaseWrapper;

var olapDataManager = new OlapDataManager();
olapDataManager.DataProvider = new WCFServiceDataProvider();
```

## Page-level Navigation/TOC (if applicable)

- [3.3.1 WCF Service]
  - Overview
  - Creating and connecting a WCF Service

## Cross References

See also:
- Syncfusion.OlapSilverlight.BaseWrapper assembly
- WCFServiceDataProvider

## RAG Annotations

<!-- tags: [syncfusion, winforms, olapcontrols, wcf, dataprovider] keywords: [syncfusion, olap, silverlight, basewrapper, wcf, service, database, query, dataprovider, wcfserVICEDataprovider] -->
```

---

<!-- 페이지 67 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_015.jpeg
document_name: Olap Common
page_number: 015
page_id: Olap Common#page_015
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:15:19Z
fidelity: lossless
-->

# Essential Olap Common

## Overview
- Explains how to establish connections to the SSAS server and offline cubes using OlapDataManager.
- Demonstrates the use of C# and VB.NET code snippets for connection procedures.

## Content

### Establishing Connection with the SSAS server
By default, the `OlapDataManager` uses the MSOLAP native provider to establish a connection with the SSAS server.

#### C#
```csharp
OlapDataManager olapDataManager = new OlapDataManager("DataSource=localhost;
    Initial Catalog=Adventure Works DW");
```

#### [VB]
```vb
OlapDataManager olapDataManager = New OlapDataManager("DataSource=localhost;
    Initial Catalog=Adventure Works DW")
```

**Or**

### Establishing Connection with the SSAS server through Data Provider
The following code snippet describes establishing connection with the server:

#### C#
```csharp
AdomdDataProvider dataProvider = new AdomdDataProvider("DataSource=localhost;
    Initial Catalog=Adventure Works DW");
OlapDataManager olapDataManager = new OlapDataManager(dataProvider);
```

#### [VB]
```vb
Dim dataProvider As AdomdDataProvider = New AdomdDataProvider("DataSource=localhost;
    Initial Catalog=Adventure Works DW")
Dim olapDataManager As OlapDataManager = New OlapDataManager(dataProvider)
```

### Establishing connection with the offline cube
The following code snippet describes establishing connection with the offline cube:

#### C#
```csharp
OlapDataManager olapDataManager = new OlapDataManager(@"Data Source = 
    C:\Common\Data\OfflineCube\Adventure Works Ext.cub; Provider =
    MSOLAP;");
```

#### [VB]
```vb
OlapDataManager olapDataManager = New OlapDataManager("Data Source = 
    C:\\Common\\Data\\OfflineCube\\Adventure Works Ext.cub; Provider =
    MSOLAP;")
```

<!-- tags: [syncfusion winforms, olap common, olap data manager, ssas server connection, offline cube connection, c#, vb.net] keywords: [OlapDataManager, MSOLAP native provider, AdomdDataProvider, SSAS server, offline cube, connection examples] -->
```

---

<!-- 페이지 68 -->

<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_019.jpeg
document_name: Olap Common
page_number: 019
page_id: Olap Common#page_019
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:15:33Z
fidelity: lossless
-->

# Essential Olap Common

## Overview

- Overview of OlapDataManager and its key functionalities.
- Detailed description of methods for managing and manipulating Olap Reports and data collections.
- Explanation of how to create pivot engines and generate MDX queries.

## Content

### Table 5: Methods

| Method Name              | Description                                                                                                                                              | Parameters            | Return Type         | Reference Link       |
|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------|----------------------|----------------------|
| AddReport                | Used to add a new **OlapReport** to the report collection of **OlapDataManager**.                                                                        | **OlapReport**        | Void                |                      |
| CloneOlapDataManager    | Create a clone from the current state of **OlapDataManager** and return the new copy of **OlapDataManager**. The **IDataProvider** will be the same for both managers. | -                      | **OlapDataManager** |                      |
| ExecuteCellSet          | This is an overloaded method that can be invoked by calling or by passing the **MDXQuerySpecification** or by passing the MDX query as string. This method will invoke the data processing and will return the processed **CellSet**, which will be further formatted. | -                      | **CellSet**         | **ExecuteCellSet**   |
| ExecuteOlapTable        | Used to create pivot engine from the **CellSet**.                                                                                                        | -                      | **PivotEngine**     |                      |
| GetMDXQuery             | This method will generate the MDX query from the **MDXQuerySpecification** and return it as a string.                                                     | -                      | string              |                      |

## API Reference

### Methods

- **AddReport**  
  - **Description**: Adds a new **OlapReport** to the report collection of **OlapDataManager**.
  - **Parameters**: 
    - **OlapReport**: The report to be added.
  - **Return Type**: Void.

- **CloneOlapDataManager**  
  - **Description**: Creates a clone from the current state of **OlapDataManager** and returns the new copy of **OlapDataManager**. The **IDataProvider** remains the same for both managers.
  - **Parameters**: None.
  - **Return Type**: **OlapDataManager**.

- **ExecuteCellSet**  
  - **Description**: An overloaded method that can be invoked by calling or by passing the **MDXQuerySpecification** or by passing the MDX query as string. This method invokes the data processing and returns the processed **CellSet** which will be further formatted.
  - **Parameters**: None.
  - **Return Type**: **CellSet**.
  - **Reference Link**: **ExecuteCellSet**

- **ExecuteOlapTable**  
  - **Description**: Used to create a pivot engine from the **CellSet**.
  - **Parameters**: None.
  - **Return Type**: **PivotEngine**.

- **GetMDXQuery**  
  - **Description**: Generates the MDX query from the **MDXQuerySpecification** and returns it as a string.
  - **Parameters**: None.
  - **Return Type**: string.

## Cross References

- See also: Other relevant sections for **OlapReports**, **MDX Query Specification**, and **PivotEngine** functionality.

<!-- tags: [Syncfusion Winforms, Olap Common, OlapDataManager, Methods, MDXQuerySpecification, CellSet, PivotEngine] keywords: [AddReport, CloneOlapDataManager, ExecuteCellSet, ExecuteOlapTable, GetMDXQuery, OlapReport, OlapDataManager] -->

---

<!-- 페이지 69 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_023.jpeg
document_name: Olap Common
page_number: 023
page_id: Olap Common#page_023
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:15:52Z
fidelity: lossless
--> 

# Essential OlapCommon

## Overview
- Sort Element
- Calculated Member
- Subset Element
- Summary Element

## Content

These elements are to get the cube element information from the user. You can create an instance of this element and add the required information about the element to pick that specific element from the data base for processing.

These elements come under the following four elements group, which are based on the axis position and filtering constraints.

- **Categorical Elements** – contains the elements that has to come under categorical axis
- **Series Elements** – contains elements that has to come under series axis
- **Slicer Elements** – contains elements that have to come under slicer elements.
- **Filter Elements** – contains elements that are subjected to filter.

All the elements are internally maintained as Item.

### Architecture of Items

![Figure 4: Architecture of Items](https://i.imgur.com/8xYz1.png)

## 4.3.1 Properties and Methods

The OlapReport properties and its descriptions are tabulated:

```markdown
### OlapReport Properties
- Property Name | Description
- --- | ---
- [Property 1] | [Description 1]
- [Property 2] | [Description 2]
- [Property 3] | [Description 3]
```

<!-- tags: [essential olapcommon, elements, categorical elements, series elements, slicer elements, filter elements, item architecture, olapreport properties, winforms] keywords: [sort element, calculated member, subset element, summary element, axis position, filtering constraints, item maintenance, architecture of items, olap report properties] -->
```

---

<!-- 페이지 70 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_027.jpeg
document_name: Olap Common
page_number: 027
page_id: Olap Common#page_027
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:16:04Z
fidelity: lossless
-->

## Essential OlapCommon

### Creating Sliced Dimension

#### [VB]

```vb
Dim dimensionElementRow As DimensionElement = New DimensionElement()
' Specifying the Name for Row Dimension Element
dimensionElementRow.Name = "Date"
' Specifying the Hierarchy and Level Element Name
dimensionElementRow.AddLevel("Fiscal", "Fiscal Year")
```

#### [C#]

```csharp
DimensionElement dimensionElementSlicer = new DimensionElement();
// Specifying the dimension Name
dimensionElementSlicer.Name = "Product";
// Adding the Level Name along with the Hierarchy Name
dimensionElementSlicer.AddLevel("Product Categories", "Category");
// Adding the Member Element
dimensionElementSlicer.Hierarchy.LevelElements["Category"].Add("Bikes");
dimensionElementSlicer.Hierarchy.LevelElements["Category"].IncludeAvailableMembers = true;
```

<!-- tags: [Olap, Dimension, Slicer, Hierarchy, Level, Element, Product, Category, Row, DimensionElement] keywords: [dimension, slicer, hierarchy, level, element, product, category, row, DimensionElement, OlapCommon] -->
```

---

<!-- 페이지 71 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_031.jpeg
document_name: Olap Common
page_number: 031
page_id: Olap Common#page_031
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:16:14Z
fidelity: lossless
-->

# Essential OlapCommon

Calculated Member to be defined in OlapReport requires the following definitions:

- **Name** – Name of the calculated member
- **Expression** – Expression to form the calculated member
- **Measure/Dimension Element** – You should add a measure or dimension element from which the calculated member should be created.

The following steps will explain how to create and add a calculated member in an OlapReport:

1. **Create the dimension measure or dimension element** from which the calculated member has to be created.
2. **Create the calculated member** by giving the name and expression.
3. **Add the element created in Step 1** to the calculated member.
4. **Once the calculated member is defined**, add that member to the calculated member collection in an OlapReport.
5. **Add the newly created calculated members** in the categorical or series axis of an OlapReport.

The following code snippet will describe the creation and addition of a calculated member in OlapReport:

## Calculated Measure

### C#

```csharp
MeasureElement measureElement = new MeasureElement();
measureElement.Name = "Order Quantity";

CalculatedMember calculatedMeasure = new CalculatedMember();
calculatedMeasure.Name = "Order on Discount";
calculatedMeasure.Expression = "[Measures].[Order Quantity] + ([Measures].[Order Quantity] * 0.10)";
calculatedMeasure.AddElement(measureElement);
olapReport.CalculatedMembers.Add(calculatedMeasure);
```

### VB

```vb
Private measureElement As MeasureElement = New MeasureElement()
measureElement.Name = " Order Quantity "

Dim calculatedMeasure As CalculatedMember = New CalculatedMember()
calculatedMeasure.Name = " Order on Discount "
calculatedMeasure.Expression = "[Measures].[Order Quantity] + ([Measures].[Order Quantity] * 0.10)"
calculatedMeasure.AddElement(measureElement)
olapReport.CalculatedMembers.Add(calculatedMeasure)
```

## Page-level Navigation/TOC (if applicable)
- If the body contains a local Table of Contents for this page, keep it as a bullet/numbered list with links/text as shown.

## Cross References
- See also: bullet list of explicit links/texts present on the page.

## RAG Annotations
- Made up of tags and keywords like {OlapReport, CalculatedMember, OLAP, Expression, MeasureElement, DimensionElement, WinForms, Syncfusion}.
```

---

<!-- 페이지 72 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_035.jpeg
document_name: Olap Common
page_number: 035
page_id: Olap Common#page_035
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:16:29Z
fidelity: lossless
-->

### Overview
- Describes how to specify dimension, hierarchy, and level names for filtering.
- Explains methods to add a range for filter elements in slicer fields.
- Includes examples in C# and VB for implementing range filters.

### Content

#### Filter Specifications

| DimensionName | Specify the dimension name | None | String | NA |
|---------------|---------------------------|------|--------|----|
| HierarchyName | Specify the hierarchy name | None | String | NA |
| LevelName     | Specify the level name    | None | String | NA |
| StartValue    | Specify the unique name or name of the member element* | None | String | NA |
| EndValue      | Specify the unique name or name of the member element* | None | String | NA |

* **Note**: Name of the member element can be specified only when the name is formed with dimension name, hierarchy name, and level name.

#### Adding a Range for Filter Elements in Slicer Field

There are two methods to add range for the filter elements in a slicer field.

1. **First Method**: Specify the unique name for start and end value.
   Example in C#:
   ```csharp
   olapReport.SlicerRangeFilters.Add(new SlicerRangeFiltersInfo("[TimeFlat].[201010100031]", "[TimeFlat].[201010100037]"));
   ```

   Example in VB:
   ```vb
   olapReport.SlicerRangeFilters.Add(New SlicerRangeFiltersInfo("[TimeFlat].[201010100031]", "[TimeFlat].[201010100037]"))
   ```

2. **Second Method**: Specify the member name along with dimension name, hierarchy name, and level name. Entering the unique name for start and end value is not mandatory.
   Example in C#:
   ```csharp
   olapReport.SlicerRangeFilters.Add(new SlicerRangeFiltersInfo { DimensionName = "TimeFlat", HierarchyName = "TimeFlat", LevelName = "TimeId", StartValue = "201010100031", EndValue = "201010100037" });
   ```

#### Conclusion

This section covers the essential aspects of specifying filter elements in an OLAP report, including the use of dimension, hierarchy, and level names, as well as adding ranges to filter elements in slicer fields. The provided code examples help illustrate the implementation in C# and VB.

<!-- tags: [Syncfusion, Winforms, OLAP, Slicer Filters, Dimension, Hierarchy, Level, Range] keywords: [DimensionName, HierarchyName, LevelName, StartValue, EndValue, SlicerRangeFilters, SlicerRangeFiltersInfo] -->
```

---

<!-- 페이지 73 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_039.jpeg
document_name: Olap Common
page_number: 039
page_id: Olap Common#page_039
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:16:45Z
fidelity: lossless
-->

## Overview
- Demonstrates how to configure categorical elements, series elements, slicer elements, and measure elements for a report in an OLAP environment using C# and VB.NET.

## Content

### Example Code

#### C#
The following C# code demonstrates how to configure categorical elements, series elements, slicer elements, and measure elements for an OLAP report:

```csharp
olapReport.CategoricalElements.Add(dimensionElementColumn);
olapReport.SeriesElements.Add(dimensionElementRow);
olapReport.SlicerElements.Add(dimensionElementSlicer);
olapReport.SeriesElements.Add(measureElementRow);
```

#### VB.NET
The following VB.NET code demonstrates the same configuration for an OLAP report:

```vb
Dim olapReport As OlapReport = New OlapReport()

olapReport.Name = "Customer Report"
olapReport.CurrentCubeName = "Adventure Works"

Dim dimensionElementColumn As DimensionElement = New DimensionElement()

' Specifying the dimension Name
dimensionElementColumn.Name = "Customer"

' Adding the Level Name along with the Hierarchy Name
dimensionElementColumn.AddLevel("Customer Geography", "Country")

Dim dimensionElementRow As DimensionElement = New DimensionElement()

' Specifying the dimension Name
dimensionElementRow.Name = "Date"

' Adding the Level Name along with the Hierarchy Name
dimensionElementRow.AddLevel("Fiscal", "Fiscal Year")

Dim dimensionElementSlicer As DimensionElement = New DimensionElement()
dimensionElementSlicer.Name = "Sales Channel"
dimensionElementSlicer.AddLevel("Sales Channel", "Sales Channel")

Dim measureElementRow As MeasureElements = New MeasureElements()
measureElementRow.Elements.Add(New MeasureElement() { Name = "Internet Sales Amount" });
```

## API Reference

### OlapReport
- **Namespace**: Syncfusion.Olap
- **Description**: Represents an OLAP report with configurable elements.

#### Properties
- **CategoricalElements**: Collection of categorical elements.
- **SeriesElements**: Collection of series elements.
- **SlicerElements**: Collection of slicer elements.

#### Methods
- **Add(dimensionElement)**: Adds a dimension element to the collection.

### DimensionElement
- **Namespace**: Syncfusion.Olap
- **Description**: Represents a dimension element.

#### Properties
- **Name**: Specifies the name of the dimension.
- **Levels**: Collection of level names associated with the hierarchy.

#### Methods
- **AddLevel(hierarchyName, levelName)**: Adds a level to the dimension element.

### MeasureElement
- **Namespace**: Syncfusion.Olap
- **Description**: Represents a measure element.

#### Properties
- **Name**: The name of the measure.

## Code Examples

### C#
```csharp
// Example configuration for an OLAP report
OlapReport olapReport = new OlapReport();

olapReport.Name = "Customer Report";
olapReport.CurrentCubeName = "Adventure Works";

DimensionElement dimensionElementColumn = new DimensionElement();
dimensionElementColumn.Name = "Customer";
dimensionElementColumn.AddLevel("Customer Geography", "Country");

DimensionElement dimensionElementRow = new DimensionElement();
dimensionElementRow.Name = "Date";
dimensionElementRow.AddLevel("Fiscal", "Fiscal Year");

DimensionElement dimensionElementSlicer = new DimensionElement();
dimensionElementSlicer.Name = "Sales Channel";
dimensionElementSlicer.AddLevel("Sales Channel", "Sales Channel");

MeasureElements measureElementRow = new MeasureElements();
measureElementRow.Elements.Add(new MeasureElement() { Name = "Internet Sales Amount" });

// Adding elements to the report
olapReport.CategoricalElements.Add(dimensionElementColumn);
olapReport.SeriesElements.Add(dimensionElementRow);
olapReport.SlicerElements.Add(dimensionElementSlicer);
olapReport.SeriesElements.Add(measureElementRow);
```

### VB.NET
```vb
Dim olapReport As OlapReport = New OlapReport()

olapReport.Name = "Customer Report"
olapReport.CurrentCubeName = "Adventure Works"

Dim dimensionElementColumn As DimensionElement = New DimensionElement()
dimensionElementColumn.Name = "Customer"
dimensionElementColumn.AddLevel("Customer Geography", "Country")

Dim dimensionElementRow As DimensionElement = New DimensionElement()
dimensionElementRow.Name = "Date"
dimensionElementRow.AddLevel("Fiscal", "Fiscal Year")

Dim dimensionElementSlicer As DimensionElement = New DimensionElement()
dimensionElementSlicer.Name = "Sales Channel"
dimensionElementSlicer.AddLevel("Sales Channel", "Sales Channel")

Dim measureElementRow As MeasureElements = New MeasureElements()
measureElementRow.Elements.Add(New MeasureElement() { Name = "Internet Sales Amount" })

' Adding elements to the report
olapReport.CategoricalElements.Add(dimensionElementColumn)
olapReport.SeriesElements.Add(dimensionElementRow)
olapReport.SlicerElements.Add(dimensionElementSlicer)
olapReport.SeriesElements.Add(measureElementRow)
```

### Example: Configuring Elements
The examples above demonstrate how to:
1. Create an `OlapReport` instance.
2. Specify the report name and current cube.
3. Configure categorical, series, and slicer dimensions.
4. Add measure elements for specific data analysis.

<!-- tags: OlapReport, DimensionElement, MeasureElement, C#, VB.NET, OLAP, Syncfusion Winforms, version: 11.4.0.26 -->
```

---

<!-- 페이지 74 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_043.jpeg
document_name: Olap Common
page_number: 043
page_id: Olap Common#page_043
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:17:14Z
fidelity: lossless
-->

# Essential OlapCommon

```csharp
excludedRowElement.Hierarchy.LevelElements("Fiscal Year").Add("FY 2004")
excludedRowElement.Hierarchy.LevelElements("Fiscal Year").Add("FY 2005")
excludedRowElement.Hierarchy.LevelElements("Fiscal Semester").Add("H2 FY 2003")
excludedRowElement.Hierarchy.LevelElements("Month").Add("August 2002")
excludedRowElement.Hierarchy.LevelElements("Month").Add("September 2002")
excludedRowElement.Hierarchy.LevelElements("Fiscal Quarter").Add("Q2 FY 2003")
excludedRowElement.Hierarchy.LevelElements("Fiscal Quarter").Add("Q2 FY 2003")
```

#### Adding Column Members
```csharp
olapReport.CategoricalElements.Add(dimensionElementColumn, excludedColumn)
```

#### Adding Measure Element
```csharp
olapReport.CategoricalElements.Add(measureElementColumn)
```

#### Adding Row Members
```csharp
olapReport.SeriesElements.Add(dimensionElementRow, excludedRowElement)
```

## 4.3.11.1.4 Ordered Report

```csharp
[C#]

OlapReport olapReport = new OlapReport();
olapReport.Name = "Customer Report";
olapReport.CurrentCubeName = "Adventure Works";
DimensionElement dimensionElementColumn = new DimensionElement();

// Specifying the Name for the Dimension Element
dimensionElementColumn.Name = "Customer";
// Specifying the Hierarchy Name
dimensionElementColumn.HierarchyName = "Customer Geography";
dimensionElementColumn.AddLevel("Customer Geography", "Country");

// Creating Measure Elements
MeasureElements measureElementColumn = new MeasureElements();
```

## Page-level Navigation/TOC (if applicable)
- This section provides examples of Ordered Reports
- Demonstrates how to specify dimensions, hierarchies, and measures

### Cross References
- Refer to Chapter 4 for more on OlapReport configurations
- See also: Related topics in the user guide

<!-- tags: [OlapReport, Ordered Report, Dimension, Hierarchy, Measure, Syncfusion Winforms, 11.4.0.26] keywords: [OlapCommon, Ordered Report, DimensionElement, Customer Geography, MeasureElements, C#, Syncfusion] -->
```

---

<!-- 페이지 75 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_047.jpeg
document_name: Olap Common
page_number: 047
page_id: Olap Common#page_047
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:17:29Z
fidelity: lossless
-->

# Essential OlapCommon

```vbnet
' Specifying the Dimension Name
dimensionElementRow.Name = "Date"
dimensionElementRow.AddLevel("Fiscal", "Fiscal Year")

Dim filterElement As FilterElement = New FilterElement(AxisPosition.Categorical)
filterElement.Elements.Add(measureElementColumn)
filterElement.Elements.Add(dimensionElementColumn)
filterElement.FilterCase = FilterCase.GreaterThan

filterElement.FilterValue.Add(New MeasureElement With {.Name = "Internet Sales Amount", .Visible = True})

filterElement.FilterValue.Add(New FilterValue With {.Filter_Value = 2700000.00})
filterElement.IsFilterCondition = True
olapReport.CategoricalElements.Add(New Item With {.ElementValue = dimensionElementColumn})
olapReport.CategoricalElements.IsFilterOrSortOn = True
olapReport.FilterElements.Add(New Item With {.ElementValue = filterElement})
```

## 4.3.11.1.6 Report with subset

### C#

```csharp
OlapReport olapReport = new OlapReport();
olapReport.Name = "Customer Report";
olapReport.CurrentCubeName = "Adventure Works";
DimensionElement dimensionElementColumn = new DimensionElement();
// Specifying the Name for the Dimension Element
dimensionElementColumn.Name = "Customer";
// Specifying the Hierarchy Name
dimensionElementColumn.HierarchyName = "Customer Geography";
dimensionElementColumn.AddLevel("Customer Geography", "Country");

MeasureElements measureElementColumn = new MeasureElements();
measureElementColumn.Elements.Add(new MeasureElement { Name = "Internet
```


*Note*: It appears there is an incomplete line at the end. This may need further clarification.

## Page-level Navigation/TOC (if applicable)
- Local Table of Contents: Chapter or section headings as specified in the page image.

<!-- tags: [Syncfusion, Winforms, OlapCommon, Report, Filter, C#] keywords: [dimension, hierarchy, filter, internet sales, customer, country, measure element] -->
``` 


---

<!-- 페이지 76 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_051.jpeg
document_name: Olap Common
page_number: 051
page_id: Olap Common#page_051
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:17:42Z
fidelity: lossless
-->

# Essential OlapCommon

```vb
Dim olapReport As OlapReport = New OlapReport()
olapReport.Name = "Customer Report"
olapReport.CurrentCubeName = "Adventure Works"

Dim dimensionElementColumn As DimensionElement = New DimensionElement()
'Specifying the Name for the Dimension Element
dimensionElementColumn.Name = "Customer"
dimensionElementColumn.AddLevel("Customer Geography", "Country")

'Creating Measure Element
Dim olapReport As OlapReport = New OlapReport()
olapReport.CurrentCubeName = "Adventure Works"
Dim dimensionElementColumn As DimensionElement = New DimensionElement()
'Specifying the Name for the Dimension Element
dimensionElementColumn.Name = "Customer"
'Specifying the Hierarchy Name
dimensionElementColumn.HierarchyName = "Customer Geography"

Dim olapReport As OlapReport = New OlapReport()
olapReport.CurrentCubeName = "Adventure Works"
Dim dimensionElementColumn As DimensionElement = New DimensionElement()
'Specifying the Name for the Dimension Element
dimensionElementColumn.Name = "Customer"
'Specifying the Hierarchy Name
dimensionElementColumn.HierarchyName = "Customer Geography"
dimensionElementColumn.AddLevel("Customer Geography", "Country")

Dim measureElementColumn As MeasureElements = New MeasureElements()
measureElementColumn.Elements.Add(New MeasureElement With {.Name = "Internet Sales Amount"})

Dim dimensionElementRow As DimensionElement = New DimensionElement()
'Specifying the Dimension Name
dimensionElementRow.Name = "Date"
dimensionElementRow.HierarchyName = "Fiscal"
```

## Page-level Navigation/TOC (if applicable)

- \[No TOC visible on this page\]

## Cross References

- Refer to related sections or pages in the documentation for additional details.

## RAG Annotations

<!-- tags: [OlapReport, DimensionElement, MeasureElements, Adventure Works, Customer Geography, Fiscal, Internet Sales Amount] keywords: [dimension, hierarchy, levels, measure elements, data reporting, olap] -->
```

---

<!-- 페이지 77 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_055.jpeg
document_name: Olap Common
page_number: 055
page_id: Olap Common#page_055
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:17:55Z
fidelity: lossless
-->

## Essential OlapCommon

### Overview
- This section demonstrates the use of dimension elements in an OLAP report. It includes examples in both C# and VB.
- The process involves specifying dimensions, hierarchies, measures, and named sets to create a comprehensive OLAP report.
- This example utilizes the "Adventure Works" cube and includes elements such as "Customer," "Customer Geography," "Core Product Group," and "Internet Sales Amount."

### WinForms-specific conventions
```csharp
olapReport.SeriesElements.Add(dimensionElementRow);
```

### Content

#### VB Code
```vb
Dim olapReport As OlapReport = New OlapReport()
olapReport.Name = "Customer Report"
olapReport.CurrentCubeName = "Adventure Works"

Dim dimensionElementColumn As DimensionElement = New DimensionElement()
' Specifying the dimension Name
dimensionElementColumn.Name = "Customer"
' Specifying the Hierarchy Name
dimensionElementColumn.HierarchyName = "Customer Geography"
dimensionElementColumn.AddLevel("Customer Geography", "Country")

Dim measureElementColumn As MeasureElements = New MeasureElements()
' Specifying the measure elements
measureElementColumn.Elements.Add(New MeasureElement With {.Name = "Internet Sales Amount"})

' Specifying the NamedSet Element
Dim dimensionElementRow As NamedSetElement = New NamedSetElement()
' Specifying the dimension name
dimensionElementRow.Name = "Core Product Group"

'''Adding the Column members
olapReport.CategoricalElements.Add(dimensionElementColumn)
'''Adding the Measure elements
olapReport.CategoricalElements.Add(measureElementColumn)
'''Adding the Row members
olapReport.SeriesElements.Add(dimensionElementRow)
```

### Page-level Navigation/TOC (if applicable)
- Refer to the "Olap Common" section for more details on dimension elements and OLAP report configurations.

### Cross References
- See also: "Adventure Works" cube documentation, "DimensionElement" class reference, "MeasureElements" class reference, "NamedSetElement" class reference.

### Tags and Keywords
<!-- tags: [OlapReport, DimensionElement, MeasureElements, NamedSetElement, Adventure Works, Customer Geography, Core Product Group, Internet Sales Amount] keywords: [OLAP, dimension elements, report configurations, WinForms, Syncfusion OLAP, Adventure Works cube, Customer geography, named sets] -->
```

---

<!-- 페이지 78 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_059.jpeg
document_name: Olap Common
page_number: 059
page_id: Olap Common#page_059
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:18:09Z
fidelity: lossless
-->

# Essential OlapCommon

```csharp
'''Adding Measure Element
olapReport.CategoricalElements.Add(measureElementColumn)
olapReport.CategoricalElements.Add(calculatedMeasure1)
olapReport.CategoricalElements.Add(calculatedMeasure2)

'''Adding Row Members
olapReport.SeriesElements.Add(dimensionElementRow)
```

## 4.3.11.1.11 Report with KPI Element

### [C#]

```csharp
OlapReport olapReport = new OlapReport();
olapReport.Name = "Products Sales Report";
olapReport.CurrentCubeName = "Adventure Works";

DimensionElement dimensionElementColumn = new DimensionElement();
// Specifying the name for Dimension Element for Column
dimensionElementColumn.Name = "Product";
dimensionElementColumn.AddLevel("Product Categories", "Category");
dimensionElementColumn.Hierarchy.LevelElements["Category"].Add(this.productName);
dimensionElementColumn.Hierarchy.LevelElements["Category"].IncludeAvail
ableMembers = true;

MeasureElements measureElementColumn = new MeasureElements();
// Specifying the name for Measure Element
measureElementColumn.Elements.Add(new MeasureElement { Name = "Gross Pr
ofit" });

DimensionElement dimensionElementRow = new DimensionElement();
// Specifying the Name for Row Dimension Element
dimensionElementRow.Name = "Date";
dimensionElementRow.AddLevel("Fiscal", "Fiscal Year");

KpiElements kpiElement = new KpiElements();
kpiElement.Elements.Add(new KpiElement { Name = "Revenue", ShowKPIStatu
s = true, ShowKPIGOal = false, ShowKPITrend = true, ShowKPIValue = true
});

// Adding Column Members
olapReport.CategoricalElements.Add(dimensionElementColumn);
olapReport.CategoricalElements.Add(kpiElement);
```
```

---

<!-- 페이지 79 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_063.jpeg
document_name: Olap Common
page_number: 063
page_id: Olap Common#page_063
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:18:22Z
fidelity: lossless
-->

## Essential OlapCommon

```vb
IncludeAvailableMembers = True

' Adding the Member properties to the Dimension Element
dimElementRow.MemberProperties.Add(New MemberProperty("Title", "[Employee].[Employees].[Title]"))
dimElementRow.MemberProperties.Add(New MemberProperty("Phone", "[Employee].[Employees].[Phone]"))
dimElementRow.MemberProperties.Add(New MemberProperty("Email Address", "[Employee].[Employees].[Email Address]"))

Dim dimElementColumn As DimensionElement = New DimensionElement()
' Specifying the Dimension Name
dimElementColumn.Name = "Product"
' Specifying the Hierarchy and level name for the Dimension Element
dimElementColumn.AddLevel("Product Categories", "Category")
dimElementColumn.MemberProperties.Add(New MemberProperty("Dealer Price", "[Product].[Product Categories].[Dealer Price]"))
dimElementColumn.MemberProperties.Add(New MemberProperty("Standard Cost", "[Product].[Product Categories].[Standard Cost]"))

' Adding Row Members
olapReport.SeriesElements.Add(dimElementRow)

'''Adding Column Members
olapReport.CategoricalElements.Add(measureElementColumn)
```

### 4.3.11.2 Sample Report for Non-OLAP data

The following code snippet illustrates the sample `OlapReport` for an `OlapDataManager`:

#### [C#]

```csharp
OlapReport olapReport = new OlapReport();
olapReport.Name = "Sales Report";

// Specifying the Row Dimension Element
DimensionElement dimElementRow = new DimensionElement();
```

## Boilerplate Footer
© 2013 Syncfusion. All rights reserved. | Page
```

<!-- tags: [OlapCommon, OlapReport, OlapDataManager, Syncfusion, Winforms, DimenionElement] keywords: [olap, report, dimension element, olap manager, sample, sales report, employer, employee, title, phone, email address, product categories, dealer price, standard cost] -->


---

<!-- 페이지 80 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_067.jpeg
document_name: Olap Common
page_number: 067
page_id: Olap Common#page_067
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:18:35Z
fidelity: lossless
-->

# Essential OlapCommon

## 4.3.16 MDX Query Parsing

### 4.3.16.1 MDX Query binding with drill up and drill down operations

This feature provides support for the drill up and drill down operations for BI components such as BI Grid, BI Chart, and BI Client in order to view the OLAP data through different levels using an MDX query instead of the OlapReport class. Previously, the drill up and drill down operations were supported by the OlapReport class only.

#### Use Case Scenarios

This feature is useful when the user wants to perform drill up or drill down operations with the OLAP data using an MDX query instead of the OlapReport class.

#### Properties

Table: Property Table

| Property                | Description                                                                                   | Type | Data Type | Reference links |
|-------------------------|-----------------------------------------------------------------------------------------------|------|-----------|----------------|
| AllowMdxToRepo         | Gets or sets a value indicating whether to parse the given MDX into the OlapReport class or not. The default value is true. | CLR   | Boolean   | N/A             |
| Parse                  |                                                                                               |      |           |                 |

#### Sample Links

- **OlapGrid [WPF]**  
  `<InstalledDrive>:\Users\<UserName>\AppData\Local\Syncfusion\EssentialStudio\<version>\WPF\OlapGrid.WPF\Samples\Defining Reports\MDX Query Demo`

- **OlapChart [WPF]**  
  `<InstalledDrive>:\Users\<UserName>\AppData\Local\Syncfusion\EssentialStudio\<version>\WPF\OlapChart.WPF\Samples\Defining Reports\MDX Query Demo`

- **OlapClient [WPF]**  
  `<InstalledDrive>:\Users\<UserName>\AppData\Local\Syncfusion\EssentialStudio\<Version>\WPF\OlapClient.WPF\Samples\Product Showcase\MDX Query Demo`

- **OlapGrid [Silverlight]**

<!-- tags: [product, syncfusion, winforms, mdx query, olapreport, drill up, drill down, bi grid, bi chart, bi client] keywords: [mdx query, olapreport, drill operations, olapgrid, olapchart, olapclient, syncfusion winforms, essential studio] -->
```

---

<!-- 페이지 81 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_071.jpeg
document_name: Olap Common
page_number: 071
page_id: Olap Common#page_071
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:18:49Z
fidelity: lossless
-->

# Essential OlapCommon

```vb
Public Function VirtualKPIReport() As OlapReport
    Dim olapReport As New OlapReport("Virtual KPI Report")
    
    olapReport.CurrentCubeName = "Adventure Works"
    
    Dim measureElements As New MeasureElements()
    measureElements.Add(New MeasureElement With {.Name = "Internet Sales Amount"})
    olapReport.CategoricalElements.Add(measureElements)
    
    Dim virtualKPIElement As New VirtualKpiElement()
    virtualKPIElement.Name = "Sample KPI"
    virtualKPIElement.KpiValueExpression = "'Value expression"
    virtualKPIElement.KpiGoalExpression = "'Goal expression"
    virtualKPIElement.KpiStatusExpression = "'Status expression"
    virtualKPIElement.KpiTrendExpression = "'Trend expression"
    virtualKPIElement.StatusGraphic = "'Status graphic"
    virtualKPIElement.TrendGraphic = "'Trend graphic"
    olapReport.VirtualKpiElements.Add(virtualKPIElement)
    olapReport.CategoricalElements.Add(virtualKPIElement)
    
    Dim internalDimension As New DimensionElement()
    internalDimension.Name = "Product"
    internalDimension.AddLevel("Product Categories", "Category")
    olapReport.SeriesElements.Add(internalDimension)
    
    Return olapReport
End Function
```

## Content

The above code snippet demonstrates the creation of a virtual KPI report using the `OlapReport` class in VB. The report is configured to use the "Adventure Works" cube and includes the following elements:

1. **Measure Elements**:
   - A `MeasureElement` named "Internet Sales Amount" is added to the `MeasureElements` collection, which is then added to the `CategoricalElements` of the `OlapReport`.

2. **Virtual KPI Element**:
   - A `VirtualKpiElement` is created and configured with:
     - `Name` set to "Sample KPI".
     - Expressions for `KpiValueExpression`, `KpiGoalExpression`, `KpiStatusExpression`, and `KpiTrendExpression` placeholder expressions.
     - Placeholder expressions for `StatusGraphic` and `TrendGraphic`.
   - The `VirtualKPIElement` is added to both the `VirtualKpiElements` and `CategoricalElements` collections of the `OlapReport`.

3. **Internal Dimension**:
   - A `DimensionElement` named "Product" is created with a level `"Product Categories"` labeled as `"Category"`.
   - The `DimensionElement` is added to the `SeriesElements` collection of the `OlapReport`.

The function returns the configured `OlapReport` object, ready for further processing or display.

## API Reference

### Namespace: `Syncfusion` (Implied)
- **Class**: `OlapReport`
- **Methods**:
  - `Add()`: Used to add elements to the report.
- **Properties**:
  - `CurrentCubeName`: Specifies the name of the current cube.
  - `CategoricalElements`: Collection of categorical elements.
  - `VirtualKpiElements`: Collection of virtual KPI elements.
  - `SeriesElements`: Collection of series elements.
- **Types**:
  - `MeasureElement`
  - `VirtualKpiElement`
  - `DimensionElement`

## Code Examples

The provided VB code snippet is a complete example of how to construct a `VirtualKPIReport` with all necessary elements, including:
- Measure elements.
- Virtual KPI elements.
- Dimension elements.

This structure can be used as a template for creating similar reports.

<!-- tags: [OlapReport, VirtualKPIReport, MeasureElements, VirtualKpiElement, DimensionElement, Syncfusion] keywords: [OlapReport, VirtualKPIReport, MeasureElements, KPI, VirtualKPI, DimensionElement, SeriesElements, CategoricalElements, .NET] -->
```

---

<!-- 페이지 82 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_075.jpeg
document_name: Olap Common
page_number: 075
page_id: Olap Common#page_075
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:19:13Z
fidelity: lossless
-->

# Essential OlapCommon

## 4.4.1 MDXQuerySpecification

### Overview
- MDXQuerySpecification is the foundational element for query creation in OlapCommon.
- Categorizes query elements into three main clauses: `With`, `Select`, and `Where`.
- Iterates through report elements and stores them according to the specified categorization.
  
### Content

#### MDXQuerySpecification
MDXQuerySpecification is the base for query creation. The MDXQuerySpecification will categorize the element into three clauses namely:
- `With`
- `Select`
- `Where`

The elements in the given report are iterated and stored according to the specification.
- The calculated member element in the given report will be added under the `With` clause.
- The categorical and series items in the given report's categorical elements and series element will come in the `Select` category.
- The `Slicer` and `Filter` items will come under the `Where` category.

Based on the current report, the `TogglePivot` value and the axis position of each item will be assigned before it is stored in the appropriate clauses.

#### Query Specification Diagram

![MDXQuerySpecification](https://i.imgur.com/placeholder_image_link.png)
**Figure 8: MDXQuerySpecification**

#### Query Generation
Once the query specification is created, the `GenerateQueryEx()` method of `QueryBuilderEngine` was called by passing the created `MDXQuerySpecification` to generate the query.

---

## 4.4.2 Steps in Query Generation

### Overview
- Describes the process of generating a query using the MDXQuerySpecification.

### Content

#### Steps to Generate a Query
To generate a query:
1. Get the query specification and iterate through the items in each category (`With`, `Select`, and `Where`) of specification and separately store the column elements, row elements, filter elements, and slice elements.
2. The filter, slicer, and sort elements are moved to the appropriate axis based on their axis property.
3. Once the initial level categorizing of elements is completed, it starts creating a query string by writing using `With` or `Select`.
4. Now it starts writing the query by checking each and every property.

---

### Page-level Navigation/TOC
- [MDXQuerySpecification](#4.4.1-mdxqueryspecification)
- [Steps in Query Generation](#4.4.2-steps-in-query-generation)

### Cross References
- See also: [Olap Common: QueryBuilderEngine](#)

<!-- tags: [olapcommon, mdxqueryspecification, querygeneration, syncfusion, windowsforms, sfpivot] keywords: [query creation, mdx, with clause, select clause, where clause, calculated member, category, series, filter, slicer, axis, query string, togglepivot, QueryBuilderEngine] -->
```

---

<!-- 페이지 83 -->

<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_079.jpeg
document_name: Olap Common
page_number: 079
page_id: Olap Common#page_079
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:19:29Z
fidelity: lossless
-->

# Essential OlapCommon

## 5 How To

### 5.1 Establish the connection for an SSAS Server

A valid string is required to establish connection for an OlapDataManager.

Here is the code snippet that demonstrates how to connect SSAS by using connection string:

**[C#]**

```csharp
OlapDataManager dataManager = new OlapDataManager("DataSource=localhost; Initial Catalog=Adventure Works DW");
```

**[VB]**

```vb
Dim dataManager As New OlapDataManager("DataSource=localhost; Initial Catalog=Adventure Works DW")
```

Or

**[C#]**

```csharp
Syncfusion.Olap.DataProvider.IDataProvider dataProvider = new Syncfusion.Olap.DataProvider.AdomdDataProvider("DataSource=localhost; Initial Catalog=Adventure Works DW");
OlapDataManager dataManager = new OlapDataManager(dataProvider);
```

**[VB]**

```vb
Dim dataProvider As Syncfusion.Olap.DataProvider.IDataProvider = New Syncfusion.Olap.DataProvider.AdomdDataProvider("DataSource=localhost; Initial Catalog=Adventure Works DW")
Dim dataManager As New OlapDataManager(dataProvider)
```

### 5.2 Establish the connection for a Cube file

A valid string is required to establish connection for an OlapDataManager.

Here is the code snippet that demonstrates how to connect cube file by using connection string:

**[C#]**

```csharp
OlapDataManager dataManager = new OlapDataManager("DataSource=AdventureWorks_Ext.cub; Provider=MSOLAP");
```

**[VB]**

```vb
Dim dataManager As New OlapDataManager("DataSource=AdventureWorks_Ext.cub; Provider=MSOLAP")
```

Or

**[C#]**

<!-- tags: [syncfusion, winforms, olap, datamanager, ssas, cube, connectionstring] keywords: [olapdatamanager, adomddataprovider, connectionstring, ssas, cube, dataprovider] -->

---

<!-- 페이지 84 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_083.jpeg
document_name: Olap Common
page_number: 083
page_id: Olap Common#page_083
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:19:42Z
fidelity: lossless
-->

## Essential OlapCommon

### Overview
- Provides methods to retrieve MDX queries, execute OLAP reports, and manage cube information.
- Helper functions to work with cube schemas and execute MDX queries.
- Includes documentation and comment blocks for clarity.

### Content

#### Methods

##### Retrieve MDX Query
**Method**: `GetMdxQuery(Syncfusion.OlapSilverlight.Reports.OlapReport report)`
- **Parameters**:
  - `report`: The report object.
- **Returns**: `string` representing the MDX query.
- **Description**: Retrieves the MDX query for the specified report and closes the provider connection.

##### Execute OLAP Report
**Method**: `ExecuteOlapReport(OlapReport report)`
- **Parameters**:
  - `report`: The report object.
- **Returns**: `CellSet` representing the executed cell set.
- **Description**: Executes the OLAP report, retrieves the cell set, and closes the provider connection.

##### Execute MDX Query
**Method**: `ExecuteMdxQuery(string mdxQuery)`
- **Parameters**:
  - `mdxQuery`: The MDX query to execute.
- **Returns**: `CellSet` representing the executed cell set.
- **Description**: Executes the MDX query, retrieves the cell set, and closes the provider connection.

##### Get Cubes
**Method**: `GetCubes()`
- **Returns**: `CubeInfoCollection` containing the cubes.
- **Description**: Retrieves the cubes and closes the provider connection.

##### Get Cube Schema
**Method**: `GetCubeSchema(string cubeName)`
- **Parameters**:
  - `cubeName`: Name of the cube.
- **Returns**: Cube schema information for the specified cube.
- **Description**: Retrieves the schema for the specified cube.

### API Reference

#### `GetMdxQuery`
```csharp
public string GetMdxQuery(Syncfusion.OlapSilverlight.Reports.OlapReport report)
{
    string mdxReturned = this._dataManager.GetMdxQuery(report);
    // Closing the Provider Connection
    this._dataManager.DataProvider.CloseConnection();
    return mdxReturned;
}
```

##### ExecuteOlapReport
```csharp
public CellSet ExecuteOlapReport(OlapReport report)
{
    CellSet cellSet = _dataManager.ExecuteOlapReport(report);
    _dataManager.DataProvider.CloseConnection();
    return cellSet;
}
```

##### ExecuteMdxQuery
```csharp
public CellSet ExecuteMdxQuery(string mdxQuery)
{
    CellSet cellSet = _dataManager.ExecuteMdxQuery(mdxQuery);
    _dataManager.DataProvider.CloseConnection();
    return cellSet;
}
```

##### GetCubes
```csharp
public CubeInfoCollection GetCubes()
{
    CubeInfoCollection cubes = _dataManager.GetCubes();
    _dataManager.DataProvider.CloseConnection();
    return cubes;
}
```

##### GetCubeSchema
```csharp
/// <summary>
/// /// Gets the cube schema.
/// <summary>
/// /// </summary>
/// /// <param name="cubeName">Name of the cube.</param>
```

## Code Examples

### Example: Retrieving MDX Query
```csharp
string mdxQuery = GetMdxQuery(report);
```

### Example: Executing OLAP Report
```csharp
CellSet cellSet = ExecuteOlapReport(report);
```

### Example: Executing MDX Query
```csharp
CellSet cellSet = ExecuteMdxQuery(mdxQuery);
```

### Example: Getting Cubes
```csharp
CubeInfoCollection cubes = GetCubes();
```

### Example: Getting Cube Schema
```csharp
GetCubeSchema(cubeName);
```

### See also:
- [OlapSilverlight.Reports.OlapReport](https://Syncfusion.Winforms.OlapSilverlight.Reports)
- [CellSet](https://Syncfusion.Winforms.Cells)
- [CubeInfoCollection](https://Syncfusion.Winforms.Cubes)
- [MDX Query Execution](https://Syncfusion.Winforms.MdxExecution)

<!-- tags: Syncfusion, Winforms, OlapSilverlight, Reports, OLAP, MDX, Queries, CubeInfoCollection, CellSet, ProviderConnection keywords: GetMdxQuery, ExecuteOlapReport, ExecuteMdxQuery, GetCubes, GetCubeSchema, CloseConnection, Olap Common -->
```

---

<!-- 페이지 85 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_087.jpeg
document_name: Olap Common
page_number: 087
page_id: Olap Common#page_087
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:20:08Z
fidelity: lossless
-->

# Essential OlapCommon

```vb
End Function
Public Function ExecuteOlapReportWithTotalCount(ByVal report As OlapReport) As Syncfusion.OlapSilverlight.Common.SerializableDictionary(Of String, Object)
    Dim dict As
Syncfusion.OlapSilverlight.Common.SerializableDictionary(Of String, Object) =
    Me._dataManager.ExecuteOlapReportWithTotalCount(report)
    Me._dataManager.DataProvider.CloseConnection()
    Return dict
End Function
#End Region
#End Class
```

3. Include the custom binding and the service endpoint address in the Web.Config file.

## Web.Config

```xml
<!-- Binding -->
<bindings>
    <customBinding>
        <binding name="binaryHttpBinding">
            <binaryMessageEncoding/>
            <httpTransport maxReceivedMessageSize="2147483647"/>
        </binding>
    </customBinding>
</bindings>

<!-- Endpoint Address -->
<services>
    <service name="SilverlightApplication1.Web.OlapManager">
        <endpoint address="binary" binding="customBinding" bindingConfiguration="binaryHttpBinding" contract="Syncfusion.OlapSilverlight.Management.IOlapDataProvider"/>
    </service>
</services>
```

### 5.7 Connect WCF Service in Silverlight application

The user can connect the above WCF service using Channel Factory by CustomBinding (Or BasicHttpBinding) and End Point Address values.

The below code snippet demonstrates how to connect the WCF service:

#### C#

```csharp
Binding customBinding = new CustomBinding(new BinaryMessageEncodingBindingElement(), new HttpTransportBindingElement { MaxReceivedMessageSize = 2147483647 });
EndpointAddress address = new EndpointAddress(new Uri(App.Current.Host.Source.ToString() + "../../Services/OlapManager.svc/binary"));
ChannelFactory<IOlapDataProvider> clientChannel = new ChannelFactory<IO
```

<!-- tags: [Syncfusion Winforms, WCF Service, Silverlight, CustomBinding, BasicHttpBinding, ChannelFactory, OlapDataProvider, OlapReport, SerializableDictionary] keywords: [WCF, Silverlight, CustomBinding, BinaryMessageEncoding, HttpTransportBinding, MaxReceivedMessageSize, EndPointAddress, ChannelFactory, IOlapDataProvider, OlapReport, SerializableDictionary, ServiceAddress, MaxFileSize] -->
```

---

<!-- 페이지 86 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_091.jpeg
document_name: Olap Common
page_number: 091
page_id: Olap Common#page_091
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:20:22Z
fidelity: lossless
-->

## Essential OlapCommon

```csharp
OlapDataManager.LoadOlapDataManager(olapReport);
```

```vb
OlapDataManager.LoadOlapDataManager(olapReport)
```

### 5.8.4 LoadReportDefinitionFile

You can bind the OlapReport as xml file to OlapDataManager using the LoadReportDefinitionFile method. This contains two steps as follows:

1.  Loading the report definition file and
2.  Loading a specific report in that file by giving its name

The following code snippet will illustrate the loading of the report definition file:

```csharp
olapDataManager.LoadReportDefinitionFile(@"C:\SampleReports\SalesAnalysis.xml");
olapDataManager.LoadReport("SalesOn2003");
```

```vb
olapDataManager.LoadReportDefinitionFile("C:\SampleReports\SalesAnalysis.xml")
olapDataManager.LoadReport("SalesOn2003")
```

### 5.8.5 LoadReportDefinitionFromStream

You can load the OlapReport as a stream to the OlapDataManager using LoadReportDefinitionFromStream method. This contains two steps as follows:

1.  Loading the report stream
2.  Loading the specific report in that stream by giving its name

The following code snippet will illustrate the loading of the report definition from a stream:

```csharp
olapDataManager.LoadReportDefinitionFromStream(reportStream);
olapDataManager.LoadReport("SalesOn2003");
```

```vb
olapDataManager.LoadReportDefinitionFromStream(reportStream)
olapDataManager.LoadReport("SalesOn2003")
```
```

---

<!-- 페이지 87 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_095.jpeg
document_name: Olap Common
page_number: 095
page_id: Olap Common#page_095
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:20:34Z
fidelity: lossless
-->

# Essential OlapCommon

## Overview
- Explains the binding of Non-OLAP data to OlapDataManager.
- Demonstrates the sequential diagram for Olap base operations.
- Provides code examples in C# and VB for binding Non-OLAP data.

## Content

### Figure 10: Olap base sequential diagram

![Olap base sequential diagram](https://image-source-url.com/image10.png)

**5.10 Bind the Non-OLAP data to OlapDataManager**

To bind the Non-OLAP data, you should bind an item source to the OlapDataManager's item source property and give the Non-OLAP data report to process the given item source. The item source can be an Enumerable collection or an ITyped List.

#### The following code will illustrate the binding of the Non-OLAP data. Here we have used a sample Enumerable collection “ProductSalesCollection” and a sample Olap report “salesReport”:

##### [C#]

```csharp
ProductSalesCollection productSales = new ProductSalesCollection();
olapDataManager.ItemSource = productSales;

olapDataManager.SetCurrentReport(salesReport);
```

##### [VB]

```vb
Dim productSales As ProductSalesCollection = New ProductSalesCollection()
olapDataManager.ItemSource = productSales

olapDataManager.SetCurrentReport(salesReport)
```

### Sequential Diagram
<!-- tags: [OlapDataManager, Non-OLAP data, binding, Olap report, C#, VB, Enumerable collection] keywords: [OlapDataManager, Non-OLAP data, binding, Olap report, code examples, Enumerable collection, ITyped List] -->
```

---

<!-- 페이지 88 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_099.jpeg
document_name: Olap Common
page_number: 099
page_id: Olap Common#page_099
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:20:45Z
fidelity: lossless
-->

# Essential OlapCommon

```vb
dlg.Filter = "XML files (*.xml)|*.xml"
Dim b As Nullable(Of Boolean) = dlg.ShowDialog()

If b.HasValue AndAlso b.Value Then
    Dim report As OlapReport = Nothing

    Using stream As FileStream = dlg.File.OpenRead()
        Dim serializer As System.Xml.Serialization.XmlSerializer = New System.Xml.Serialization.XmlSerializer(GetType(OlapReportCollection))
        Dim olapReportCollection As OlapReportCollection = TryCast(serializer.Deserialize(stream), OlapReportCollection)
        report = olapReportCollection(0)
    End Using
    olapDataManager.SetCurrentReport(report)
End If
End Sub
```

## 5.13 Rename and remove a report

Once the report collection is loaded with reports, you can rename or remove any reports in that collection by using the RenameReport and RemoveReport methods.

### 5.13.1 RenameReport

A report in the report collection of OlapDataManager can be renamed by invoking RenameReport method with arguments such as, index of the report and new name for the report or with old name and new name of the report. The following code snippet will illustrate this:

#### [C#]

```csharp
olapDataManager.RenameReport(2, "SalesAnalysisOn2003");
olapDataManager.RenameReport("RevenueAnalysis", "RevenueAnalysisOn2003");
```

#### [VB]

```vb
olapDataManager.RenameReport(2, "SalesAnalysisOn2003")
olapDataManager.RenameReport("RevenueAnalysis", "RevenueAnalysisOn2003")
```
```

---

<!-- 페이지 89 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_103.jpeg
document_name: Olap Common
page_number: 103
page_id: Olap Common#page_103
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:20:57Z
fidelity: lossless
-->

# Essential OlapCommon

```csharp
2700000.0})
filterElement.IsFilterCondition = True
''' Adding Column Members
olapReport.CategoricalElements.Add(dimensionElementColumn)
olapReport.CategoricalElements.IsFilterOrSortOn = True
'''Adding Measure Element
olapReport.FilterElements.Add(filterElement)
```

## 5.18 Show/hide the Expander buttons in OLAP controls

There is a property in OlapReport called ShowExpanders, which is used to show/hide the expander buttons in the OLAP controls. By using this property, we can disable or enable the drill down/up behavior of the OLAP control.

To show the Expanders:

### [C#]

```csharp
/// Displaying the Expander button in Controls
olapReport.ShowExpanders = true;
```

### [VB]

```vb
'''Displaying the Expander button in Controls
olapReport.ShowExpanders = True
```

To hide the Expanders:

### [C#]

```csharp
/// Displaying the Expander button in Controls
olapReport.ShowExpanders = false;
```

### [VB]

### 
```

<!-- tags: [Olap Report, OLAP controls, expander buttons, ShowExpanders property, drill down, drill up] keywords: [OlapReport, Expanders, OLAP, ShowExpanders, C#, VB] -->
```

---

<!-- 페이지 90 -->

```html
<!--                                                                                                     
source: image                                                                                         
domain: syncfusion-sdk                                                                                
task: pdf-ocr-to-markdown                                                                             
language: en (keep original; do not translate)                                                        
source_filename: page_107.jpeg                                                                        
document_name: Olap Common                                                                            
page_number: 107                                                                                      
page_id: Olap Common#page_107                                                                         
product: Syncfusion Winforms                                                                           
version: 11.4.0.26                                                                                    
timestamp: 2025-08-09T07:21:08Z                                                                        
fidelity: lossless                                                                                   
-->                                                                                                   
                                                                                                      
## Essential OlapCommon                                                                                

### Instantiate the WCF service using Basic Http Binding and End Point Address values:                                                                         
                                                                                                      
- Declare the `IOLapDataProvider` for Service instantiation as given in the following code:                                                                    
                                                                                                      
#### C#                                                                                             
                                                                                                       ```csharp                                                                              
                                                                                           // Declaring the IOLapDataProvider for service instantiation                                                                                          
                                                                                           IOLapDataProvider DataProvider = null;                                                                                            
                                                                                                       ```                                                                                 
                                                                                                      
#### VB                                                                                            
                                                                                                       ```vb                                                                                
                                                                                           ' Declaring the IOLapDataProvider for service instantiation                                                                                          
                                                                                           Dim DataProvider As IOLapDataProvider = Nothing                                                                                  
                                                                                                       ```                                                                                 
                                                                                                      
- Specify the `basicHttpBinding` and Instantiate the `DataProvider` from the `ChannelFactory` as given in the following code:                                     
                                                                                                       [C#]                                                                                                     
                                                                                                       ```csharp                                                                              
                                                                                           private void InitializeConnection()                                                                                            
                                                                                           {                                                                                          
                                                                                                     Binding basicHttpBinding = new BasicHttpBinding(BasicHttpSecurityMode.None)                                                                                            
                                                                                                     {                                                                                      
                                                                                                       MaxBufferSize = 2147483647, MaxReceivedMessageSize = 2147483647                                                                                                              
                                                                                                     };                                                                          
                                                                                                     var Uri = App.Current.Host.Source.ToString();                                                                    
                                                                                                     EndpointAddress address = new EndpointAddress(new Uri(Uri +                                                                                                              
                                                                                                "........Services/OlapManager.svc/basic"));                                                                          
                                                                                                     ChannelFactory<IOLapDataProvider> clientChannel = new ChannelFactory<IOLapDataProvider>(basicHttpBinding, address);                                                   
                                                                                                     DataProvider = clientChannel.CreateChannel();                                                                     
                                                                                           }                                                                                          
                                                                                                       ```                                                                                 
                                                                                                      
## Page-level Navigation/TOC (if applicable)                                                          
                                                                                                      
<!-- tags: [OlapCommon, WCF service, BasicHttpBinding, IOLapDataProvider] keywords: [Instantiating WCF service, EndPointAddress, Service instantiation, C#, VB, App.Current.Host.Source, Syncfusion, Syncfusion Winforms, ChannelFactory] -->
```


---

<!-- 페이지 91 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_111.jpeg
document_name: Olap Common
page_number: 111
page_id: Olap Common#page_111
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:21:22Z
fidelity: lossless
-->

# Essential OlapCommon

## Overview
- This section explains the steps to create a new Silverlight application and configure it to host in a Web project using the Solution Explorer window.

## Content

### Creating a New Silverlight Application

#### Step 1: Open the New Project Dialog
1. **Select Silverlight Application**: Open the New Project dialog window from your development environment.

![Figure 13: New Project Dialog Window](https://i.imgur.com/new_project_dialog.png)

#### Step 2: Configure the Silverlight Application
2. Select **Silverlight Application** from the Installed Templates under **Visual C#**.
3. Click **OK** to proceed.

#### Step 3: Configure the Hosting Web Project
4. The New Silverlight Application dialog opens to allow configuration of hosting options.
   - **Host the Silverlight application in a new Web site**: Check this option to host the Silverlight application within a Web project.
   - **New Web project name**: Enter the desired name for the new Web project (e.g., `SilverlightApplication1.Web`).
   - **New Web project type**: Choose the type of Web project (e.g., `ASP.NET Web Application Project`, `ASP.NET Web Site`, or `ASP.NET MVC Web Project`).
   - **Silverlight Version**: Select the appropriate Silverlight version (e.g., Silverlight 5).

   ![Figure 14: Web Project Selection Window](https://i.imgur.com/web_project_selection.png)

#### Step 4: Verify the Solution Explorer
5. The Solution Explorer window displays the created Silverlight application with the selected MVC project integrated.

## Appendix
- The Solution Explorer window shows the Silverlight application with the MVC project.

<!-- tags: [Syncfusion Winforms, Silverlight, MVC Web Project, Silverlight Application, Solution Explorer] keywords: [New Project Dialog, Visual C#, Silverlight Version, Hosting Silverlight, Web Application, ASP.NET, Silverlight 5, Solution Explorer] -->
```

---

<!-- 페이지 92 -->

<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_115.jpeg
document_name: Olap Common
page_number: 115
page_id: Olap Common#page_115
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:21:35Z
fidelity: lossless
-->

# Essential OlapCommon

## Overview
- Describes the process of inheriting a WCF service with `IOLapDataProvider`.
- Explains how to connect to a database using the WCF service.
- Provides a code snippet to implement the `IOLapDataProvider` interface.

## Content

### Adding a New WCF Service

**Figure 18: Add New Item Dialog (WCF Service)**  
![Add New Item Dialog (WCF Service)](image_link)

1. **Inherit the newly added WCF service with `IOLapDataProvider`**:  
   Ensure that the newly added WCF service is inherited with the `IOLapDataProvider` interface and explicitly implements it.

2. **Connecting to the database using the WCF service**:  
   The connection to the database is facilitated through the WCF service. The service must be created and instantiated as described in the following code snippet.

### Implementing the `IOLapDataProvider` Interface

The WCF Service must implement the `IOLapDataProvider` interface. To implement this interface, you require the `OlapDataProvider`, which can be instantiated by passing the connection string.

#### Code Snippet to Implement the `IOLapDataProvider` Interface

```csharp
public class OlapManager : IOLapDataProvider
{
    Syncfusion.OlapSilverlight.Manager.OlapDataProvider dataManager;

    /// <summary>
```

## API Reference (if applicable)
- Namespace and Class details for `IOLapDataProvider` and `OlapDataProvider`.

## Code Examples
- The provided code snippet demonstrates the implementation of the `IOLapDataProvider` interface.

## Page-level Navigation/TOC (if applicable)
- Refer to the OCR content for any local Table of Contents or section headings.

## Cross References
- Refer to related documentation for more information on `IOLapDataProvider` and `OlapDataProvider`.

## RAG Annotations
<!-- tags: [product: Syncfusion Winforms, module: Essential Olap, api: IOLapDataProvider, version: 11.4.0.26] keywords: [WCF Service, IOLapDataProvider, OlapDataProvider, database connection, implementation, code snippet] -->

---

<!-- 페이지 93 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_119.jpeg
document_name: Olap Common
page_number: 119
page_id: Olap Common#page_119
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:21:49Z
fidelity: lossless
-->

### Essential OlapCommon

The `Essential OlapCommon` namespace provides essential methods to interact with OLAP cubes and their schemas. Below are the function definitions that demonstrate how to retrieve various components of an OLAP cube:

```vb
    Public Function GetChildMembers(ByVal memberUniqueName As String, ByVal cubeName As String) As MemberCollection
        Throw New NotImplementedException()
    End Function

    Public Function GetCubeSchema(ByVal cubeName As String) As CubeSchema
        Throw New NotImplementedException()
    End Function

    Public Function GetCubes() As CubeInfoCollection
        Throw New NotImplementedException()
    End Function

    Public Function GetLevelMembers(ByVal levelUniqueName As String, ByVal cubeName As String) As MemberCollection
        Throw New NotImplementedException()
    End Function

#End Region
End Class
```

## Include Custom Binding in Web.Config

11. Include the custom binding and the service endpoint address in the Web.Config file under the ServiceModel section. The following is an example configuration snippet:

```xml
[Web.Config]
<!--Binding-->
<bindings>
    <customBinding>
        <binding name="binaryHttpBinding">
            <binaryMessageEncoding />
            <httpTransport maxReceivedMessageSize="2147483647" />
        </binding>
    </customBinding>
</bindings>
```

This configuration ensures that the service can handle the required bindings and endpoint configurations effectively.

## API Reference

### Methods

#### GetChildMembers
```vb
Public Function GetChildMembers(ByVal memberUniqueName As String, ByVal cubeName As String) As MemberCollection
```
- **Parameters**:
  - `memberUniqueName`: The unique name of the member.
  - `cubeName`: The name of the cube.

#### GetCubeSchema
```vb
Public Function GetCubeSchema(ByVal cubeName As String) As CubeSchema
```
- **Parameters**:
  - `cubeName`: The name of the cube.

#### GetCubes
```vb
Public Function GetCubes() As CubeInfoCollection
```

#### GetLevelMembers
```vb
Public Function GetLevelMembers(ByVal levelUniqueName As String, ByVal cubeName As String) As MemberCollection
```
- **Parameters**:
  - `levelUniqueName`: The unique name of the level.
  - `cubeName`: The name of the cube.

## Code Examples

### Web.Config Configuration Example
```xml
<bindings>
    <customBinding>
        <binding name="binaryHttpBinding">
            <binaryMessageEncoding />
            <httpTransport maxReceivedMessageSize="2147483647" />
        </binding>
    </customBinding>
</bindings>
```

### VB.NET Example
```vb
Public Function GetCubeSchema(cubeName As String) As CubeSchema
    Dim cubeSchema As CubeSchema
    ' Implementation logic here
    Return cubeSchema
End Function
```

## Conclusion

This section provides guidance on integrating essential OLAP functionalities and configuring custom bindings in a Web.Config file. The methods outlined above are fundamental for interacting with OLAP cubes and their schema information.

<!-- tags: [Syncfusion, WinForms, OlapCommon, Web.Config, binding, OLAP, cube] keywords: [GetChildMembers, GetCubeSchema, GetCubes, GetLevelMembers, customBinding, binaryHttpBinding, maxReceivedMessageSize] -->
```

---

<!-- 페이지 94 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_123.jpeg
document_name: Olap Common
page_number: 123
page_id: Olap Common#page_123
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:22:09Z
fidelity: lossless
-->

# Essential OlapCommon

## Overview
- Demonstrates the use of OlapGrid Control with OLAP Data.
- Describes how to integrate and manipulate OLAP data within the OlapGrid.
- Highlights features and functionalities specific to displaying OLAP data.

## Content

### Figure 19: OlapGrid Control with OLAP Data

This figure showcases the OlapGrid Control applied to display OLAP (On-Line Analytical Processing) data. The OlapGrid Control is capable of handling multidimensional data structures typically found in OLAP cubes, providing a user-friendly interface for data analysis.

#### Key Features
- **Multidimensional Data Support**: The OlapGrid can display data from OLAP cubes, slicing and dicing data as needed.
- **Interactive Exploration**: Users can interactively explore the data by drilling down into categories or dimensions.
- **Customization Options**: The grid provides options to customize views, such as hiding or showing dimensions, rearranging them, and applying filters.

#### Usage Example

The following is a sample setup for integrating the OlapGrid with OLAP data:

```csharp
using Syncfusion.Olap.Controllers;
using Syncfusion.Olap.Grid;

// Create OLAP data controller
OlapController controller = new OlapController();

// Load OLAP data (example: from an XMLA data source)
controller.LoadXmla("http://localhost/olap/mondrian", "AdventureWorks");

// Create OlapGrid and bind it to the controller
OlapGrid grid = new OlapGrid();
grid.Controller = controller;

// Initialize the grid with initial dimensions and measures
grid.ShowDimension("Product", "Category");
grid.ShowMeasure("Sales Amount", "Product");

// Display the grid
this.Controls.Add(grid);
grid.Dock = DockStyle.Fill;
```

### WinForms-specific Notes

- **OlapGrid Properties**:
  - `Controller`: This property allows you to specify the OLAP data controller to be used for binding the grid.
  - `ShowDimension`: This method is used to display dimensions within the grid.
  - `ShowMeasure`: This method adds measures to the grid for aggregation and display.

- **Event Handling**:
  - `CellClick`: This event is triggered when a cell is clicked, useful for handling user interactions such as drilling down or filtering.

### API Reference

#### Methods

- **ShowDimension**
  - Displays a specific dimension in the grid.
  - **Parameters**:
    - `string dimensionName`: The name of the dimension to display.
- **ShowMeasure**
  - Adds a specific measure to the grid for display.
  - **Parameters**:
    - `string measureName`: The name of the measure to display.

#### Exceptions

- `OlapGridException`: Thrown when there are errors related to OLAP data manipulation or binding.

## Code Examples

### C#

```csharp
using Syncfusion.Olap.Grid;
using Syncfusion.Olap.Controllers;

OlapGrid grid = new OlapGrid();
OlapController controller = new OlapController();
controller.LoadXmla("http://localhost/olap/mondrian", "AdventureWorks");
grid.Controller = controller;
grid.ShowDimension("Product", "Category");
grid.ShowMeasure("Sales Amount", "Product");
this.Controls.Add(grid);
grid.Dock = DockStyle.Fill;
```

### VB.NET

```vb
Imports Syncfusion.Olap.Grid
Imports Syncfusion.Olap.Controllers

Dim grid As New OlapGrid()
Dim controller As New OlapController()
controller.LoadXmla("http://localhost/olap/mondrian", "AdventureWorks")
grid.Controller = controller
grid.ShowDimension("Product", "Category")
grid.ShowMeasure("Sales Amount", "Product")
Me.Controls.Add(grid)
grid.Dock = DockStyle.Fill
```

## Page-level Navigation/TOC
- Overview
- Content
  - Figure 19: OlapGrid Control with OLAP Data
  - Key Features
  - Usage Example
  - WinForms-specific Notes
    - Methods
    - Event Handling
  - API Reference
    - Methods
    - Exceptions

## Cross References
- See also: `OlapController`, `OLAP`, `Drill-Down`, `DataGrid`, `MultidimensionalDataAnalysis`

<!-- tags: [OlapGrid, OLAP, OnLineAnalyticalProcessing, OLAPData, DataGrid, WinForms, Syncfusion] keywords: [OlapGrid, OLAP, OLAPData, Dimensions, Measures, DataGrid, Grid, DrillDown, MultidimensionalData, OnLineAnalyticalProcessing] -->
```


---

<!-- 페이지 95 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_004.jpeg
document_name: Olap Common
page_number: 004
page_id: Olap Common#page_004
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:14:30Z
fidelity: lossless
-->

# Essential OlapCommon

## Overview
- Step-by-step guide to connecting with SSAS Server and Cube files.
- Instructions on establishing role-based connections and interacting with Mondrian Server via XML.
- Details on configuring WCF services for Silverlight OLAP controls.
- Comprehensive process on managing OlapDataManagers and OlapReports.
- Techniques for handling MDX queries and non-OLAP data within Olap controls.
- Procedures for saving, renaming, and removing reports in XML format.
- Methods for filtering, drilling, and exporting Olap data.

## Content

### 5.1 Establish the connection for an SSAS Server
- Page 79

### 5.2 Establish the connection for a Cube file
- Page 79

### 5.3 Establish Role-based Connection
- Page 80

### 5.4 Connecting to Mondrian Server through XML
- Page 80

### 5.5 Connect ActivePivot Server through XML
- Page 81

### 5.6 Create a WCF Service for Silverlight OLAP control
- Page 81

### 5.7 Connect WCF Service in Silverlight application
- Page 87

### 5.8 Bind an OlapReport with OlapDataManager
- Page 88

#### 5.8.1 CurrentReport
- Page 90

#### 5.8.2 SetCurrentReport
- Page 90

#### 5.8.3 LoadOlapDataManager
- Page 90

#### 5.8.4 LoadReportDefinitionFile
- Page 91

#### 5.8.5 LoadReportDefinitionFromStream
- Page 91

### 5.9 Bind the MDX query to OlapDataManager
- Page 92

### 5.10 Bind the Non-OLAP data to OlapDataManager
- Page 95

### 5.11 Save the report as xml file
- Page 96

### 5.12 Load xml report file
- Page 97

### 5.13 Rename and remove a report
- Page 99
  - **5.13.1 RenameReport**
  - Page 99
  - **5.13.2 RemoveReport**
  - Page 100

### 5.14 Get the reports in the OlapDataManager as a stream
- Page 100

### 5.15 Communicate the OLAP control with the base
- Page 100

### 5.16 Add the elements to an Axis
- Page 101

### 5.17 Apply the Filter through filter element
- Page 101

### 5.18 Show/hide the Expander buttons in OLAP controls
- Page 103

### 5.19 Process OlapReport Internally
- Page 104

### 5.20 Handle Drill Down/Up Process
- Page 104

### 5.21 Connect WCF Service by an additional Binding Type in Silverlight application
- Page 106

### 5.22 Retrieve the MDX Query of a CurrentReport
- Page 108

### 5.23 Add UseWhereClauseForSlicing to an Application
- Page 109

### 5.24 Edit MDX Query before Its Execution
- Page 110

### 5.25 Host BI Silverlight component in ASP.NET MVC Web Project
- Page 110

## API Reference (if applicable)
- **Namespace:** Essential.OlapCommon
- **Classes:** OlapDataManager, OlapReport
- **Members:**
  - Methods: LoadOlapDataManager(), LoadReportDefinitionFile()
  - Properties: CurrentReport, NonOlapData

## Code Examples (multi-language supported)
```csharp
// Example: Establishing a connection with SSAS Server
using Syncfusion.Olap.Common;
var connectionString = "Provider=MSOLAP;Data Source=ServerName;Initial Catalog=CubeName";
var olapConnection = new OlapConnection(connectionString);
```

## Cross References
- See also: Section 6: Advanced OLAP Reporting Techniques
- See also: Section 7: Troubleshooting OLAP Connections

<!-- tags: [Olap, OLAP control, WCF service, Silverlight, MDX query, OlapDataManager, OlapReport, SSAS Server] keywords: [essential olapcommon, olap connection, olap filtering, olap drilling, olap reporting, silverlight integration, wcf integration] -->
```

---

<!-- 페이지 96 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_008.jpeg
document_name: Olap Common
page_number: 008
page_id: Olap Common#page_008
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:14:54Z
fidelity: lossless
-->

# 3 Syncfusion OLAP Architecture

Syncfusion OLAP architecture allows you to build a full life cycle reporting solution for your enterprise. Here are the important pieces of the architecture:

- **OLAP Access Layer** - Built on top of ADOMD.NET and provides a high-level object model to let you easily define reports.
- **OLAP Controls** - Chart, Grid, Gauge, Client for ASP.NET (excluding Gauge), WPF, Silverlight, ASP.NET MVC (Grid only).
- **OLAP Report Builder** – RAD (Rapid Application Development) tool lets you select the dimensions you are interested in visualizing and also lets you define the appearance for the Chart and Grid.

## Overview
- The Syncfusion OLAP components enable the creation of a full life cycle reporting solution for your enterprise.

## Content
The following screenshot shows how the Syncfusion OLAP components allow you to build a full life cycle reporting solution for your enterprise.

### Diagram of Syncfusion OLAP Components

```markdown
UI Controls
|
v
Synfusion AdomdDataProvider ↔ OLAP DataManager (ODM)
|
v
Adomd.Net Provider (Microsoft.AnalysisServices.AdmdClient)
|
v
XML Data Provider
|
v
SOAP
|
v
XML Data Provider
|
v
OLAP Servers  SQL Server Analysis Server
```

### Explanation of the Diagram
1. **UI Controls**:
   - The user interacts with UI controls to visualize and manipulate data.

2. **Synfusion AdomdDataProvider**:
   - This component communicates with the OLAP DataManager (ODM) to access and manage OLAP data.

3. **OLAP DataManager (ODM)**:
   - Manages the data model for OLAP operations.

4. **Adomd.Net Provider**:
   - Connects to the OLAP server using the Microsoft.AnalysisServices.AdmdClient.

5. **Query Builder**:
   - Allows users to construct and define queries for data retrieval.

6. **XML Data Provider**:
   - Acts as a middleware for data communication.

7. **SOAP**:
   - Provides a communication protocol for data exchange.

## API Reference
- Not explicitly detailed in the image, but refers to ADOMD.NET and related interfaces for OLAP operations.

## Code Examples
- No explicit code examples provided in the text.

## RAG Annotations
<!-- tags: [Olap, OLAP, Syncfusion, Winforms, reporting, ADOMD.NET, architecture, OLAP Controls, Report Builder] keywords: [Syncfusion OLAP, reporting, UI Controls, OLAP Access Layer, OLAP Controls, OLAP Report Builder, AdomdDataProvider, OLAP DataManager, Adomd.Net Provider, Query Builder, XML Data Provider, SOAP, Microsoft.AnalysisServices.AdmdClient, SQL Server Analysis Server] -->
```

---

<!-- 페이지 97 -->

<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_012.jpeg
document_name: Olap Common
page_number: 012
page_id: Olap Common#page_012
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:15:11Z
fidelity: lossless
-->

# OlapCommon

## Concepts

### 4.1 OlapDataProvider

The database connectivity-related works are all taken care of by this part of the base. Here we are using `Microsoft.AnalysisServices.AdomdClient` data provider. Establishing the connection, checking the state of the connection, and closing the connection are basic operations provided by the general data provider, but we need some information beyond this in order to provide the input for our controls.

This part of the base will get the connection information and establish a connection with the specified data source and retrieve the information from the database and store it in its classes. This part of the base will have the required logic to retrieve the information from the database and store it in the object of classes in the `Data` namespace.

All the information about the connected cube will intersect and be stored in the object of classes in the `Data` namespace, which are equivalent to the classes in the `AdomdClient`. This information is required to provide the input for OLAP controls.

#### Important class in DataProvider namespace:
- AdomdDataProvider

##### 4.1.1 AdomdDataProvider

The important properties and methods in the `AdomdDataProvider` class are tabulated below:

### Table 1: Properties

| Property Name         | Description                                  | Type               | Value it Accepts | Reference Link |
|-----------------------|----------------------------------------------|--------------------|------------------|----------------|
| CatalogName           | To get the connected database name          | string             | -                | -              |
| ConnectionString      | To set or get the connection string          | string             | -                | -              |
| CurrentCellSet        | To get the currently executed CellSet        | CellSet            | -                | -              |
| GetCubes              | To get the information about the cubes in the connected data source | CubeInfoCollection | -                | -              |

## Summary
- The `OlapDataProvider` handles database connectivity tasks using the `Microsoft.AnalysisServices.AdomdClient` data provider.
- It retrieves cube information and stores it in the `Data` namespace classes for use by OLAP controls.
- The `AdomdDataProvider` class contains the key properties and methods for managing this functionality.

---

<!-- 페이지 98 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_016.jpeg
document_name: Olap Common
page_number: 016
page_id: Olap Common#page_016
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:15:24Z
fidelity: lossless
-->

# Essential OlapCommon

---

## Overview

- Establishing a connection with the XMLA Server using web standards like HTTP, SOAP, and XML.
- Using MDX as the query language for accessing multi-dimensional data stores.
- Scenarios for efficient OLAP database access over the internet.
- Connection code examples for Mondrian and Active Pivot servers.

---

## Content

### Establishing connection with XMLA Server:

XML for Analysis (XMLA) is a standard that allows client applications to transfer multi-dimensional or OLAP data sources, which is available in the Mondrian Server. The back-and-forth communication is done using web standards – HTTP, SOAP, and XML. The query language used is MDX, which is most widely supported for reporting from multi-dimensional data stores.

#### Use Case Scenarios

XMLA provides the most efficient way to access an OLAP database over the Internet.

#### Connecting to Mondrian Server

The following code illustrates how to connect to the Mondrian server:

#### C#

```csharp
// Connecting to Mondrian Server
OlapDataManager DataManager = new OlapDataManager("Data Source = http://localhost:8080/mondrian/xmla; Initial Catalog = FoodMart;");
DataManager.DataProvider.ProviderName = Syncfusion.Olap.DataProvider.Providers.Mondrian;
```

#### VB

```vb
' Connecting to Mondrian Server
Dim DataManager As OlapDataManager = New OlapDataManager("Datasource = http://bi.syncfusion.com:8080/mondrian/xmla; Initial Catalog=FoodMart;")
DataManager.DataProvider.ProviderName = Syncfusion.Olap.DataProvider.Providers.Mondrian
```

[Click here](#) for more information about Mondrian XMLA configurations.

### Connecting to Active Pivot Server

The following code illustrates how to connect to Active Pivot server:

---

## Page-level Navigation/TOC

- Establishing connection with XMLA Server
- Use Case Scenarios
  - Connecting to Mondrian Server
  - Connecting to Active Pivot Server

## Cross References

- See also: Mondrian XMLA configurations

---

<!-- tags: [syncfusion-sdk, olap, xmla, mondrian server, active pivot server, olapdata, winforms, multi-dimensional data, mdx, xmla configurations] keywords: [xmla, olap, mdx, mondrian server, active pivot, data connection, winforms, syncfusion] -->
```

---

<!-- 페이지 99 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_020.jpeg
document_name: Olap Common
page_number: 020
page_id: Olap Common#page_020
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:15:39Z
fidelity: lossless
-->

# Essential OlapCommon

## Overview
- Provides details about methods within the `OlapCommon` namespace.
- Enables retrieval and manipulation of OLAP reports and data managers.
- Includes utility methods for handling report files, streams, and events.

## Content

### Method Details

Below is a table detailing the methods and their functionalities within the `OlapCommon` namespace:

| Method Name               | Description                                                                 | Parameters           | Return Type            | Reference Link               |
|---------------------------|-----------------------------------------------------------------------------|-----------------------|-------------------------|------------------------------|
|                           | return the query as a string.                                              |                       |                         |                              |
| GetReport                 | This method will return the OlapReport collection by giving the Xml report file name as an input. | string               | OlapReportCollection    |                              |
| GetReportAsStream         | This method will return the current report collection along with the current state of OlapDataManager as a Stream. |                       | Stream                  | GetReportAsStream           |
| LoadOlapDataManager       | Will accept the OlapReport as an argument and Load the OlapDataManager with the given OlapReport. | OlapReport            | Void                    | LoadOlapDataManager         |
| LoadReport                | Used to get the report name as an argument and pick the specified report from the report collection to load the OlapDataManager with that report. | string               | Void                    |                              |
| LoadReportDefinitionFile  | Used to get the XML report file as input and load the OlapDataManager with the report in that file. | string               | Void                    | LoadReportDefinitionFile    |
| LoadReportDefinitionFromStream | Used to get a stream as input and read the report from that stream and load the OlapDataManager with that report. | Stream               | Void                    | LoadReportDefinitionFromStream |
| NotifyElementModified     | Used to trigger the `ElementModified` event.                                   |                       | Void                    |                              |

## API Reference

### Methods

#### `GetReport`
- **Description**: Returns the `OlapReport` collection by providing the XML report file name as input.
- **Parameters**: 
  - `string`: The XML report file name.
- **Return Type**: `OlapReportCollection`
- **Reference Link**: [GetReport]

#### `GetReportAsStream`
- **Description**: Returns the current report collection along with the current state of the `OlapDataManager` as a `Stream`.
- **Parameters**: None.
- **Return Type**: `Stream`
- **Reference Link**: [GetReportAsStream]

#### `LoadOlapDataManager`
- **Description**: Accepts an `OlapReport` as an argument and loads the `OlapDataManager` with the given `OlapReport`.
- **Parameters**: 
  - `OlapReport`: The report to load into the `OlapDataManager`.
- **Return Type**: `Void`
- **Reference Link**: [LoadOlapDataManager]

#### `LoadReport`
- **Description**: Gets the report name as an argument and picks the specified report from the report collection to load the `OlapDataManager` with that report.
- **Parameters**: 
  - `string`: The report name.
- **Return Type**: `Void`
- **Reference Link**: N/A

#### `LoadReportDefinitionFile`
- **Description**: Gets the XML report file as input and loads the `OlapDataManager` with the report in that file.
- **Parameters**: 
  - `string`: The XML report file name.
- **Return Type**: `Void`
- **Reference Link**: [LoadReportDefinitionFile]

#### `LoadReportDefinitionFromStream`
- **Description**: Gets a stream as input, reads the report from that stream, and loads the `OlapDataManager` with that report.
- **Parameters**: 
  - `Stream`: The stream containing the report.
- **Return Type**: `Void`
- **Reference Link**: [LoadReportDefinitionFromStream]

#### `NotifyElementModified`
- **Description**: Triggers the `ElementModified` event.
- **Parameters**: None.
- **Return Type**: `Void`
- **Reference Link**: N/A

## Code Examples

### Example of `GetReport`

```csharp
using Syncfusion.Olap.OlapCommon;

// Example code snippet to demonstrate the usage of GetReport
string reportFileName = "SampleReport.xml";
OlapReportCollection reports = OlapCommon.GetReport(reportFileName);
```

### Example of `LoadOlapDataManager`

```csharp
using Syncfusion.Olap.OlapCommon;

// Example code snippet to demonstrate the usage of LoadOlapDataManager
OlapReport report = new OlapReport();
OlapCommon.LoadOlapDataManager(report);
```

## Cross References

- See also: [Syncfusion OLAP Report documentation](https://www.syncfusion.com/documentation/olap/report-creation)
- See also: [OlapDataManager documentation](https://www.syncfusion.com/documentation/olap/data-manager)

### Tags and Keywords
<!-- tags: olap, report, olapreportcollection, stream, datamanager, reportfile, xml, event triggers, winforms, syncfusion -->
```

---

<!-- 페이지 100 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_024.jpeg
document_name: Olap Common
page_number: 024
page_id: Olap Common#page_024
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:16:07Z
fidelity: lossless
-->

# Essential OlapCommon

## Overview
- Describes the properties and functionalities of OlapReport related to calculations, categorical elements, current cube name, filter elements, and report settings.
- Defines settings for display options such as showing or hiding empty column/row data, expanders, and slicer elements.

## Content

### Properties Table

The following table lists the properties of the `OlapReport` and their respective descriptions, types, accepted values, and reference links:

| Name                  | Description                                                                                           | Type     | Value it accepts | Reference Link           |
|-----------------------|-------------------------------------------------------------------------------------------------------|----------|------------------|--------------------------|
| CalculatedMembers     | Used to set and get the calculated members of the `OlapReport`.                                      | Items    | Items            | CalculatedMembers        |
| CategoricalElements   | Contains the element that are said to be in categorical axis. We can add an element and get the collection of elements that comes under the categorical axis.                    | Items    | Items            | -                        |
| CurrentCubeName      | Used to set or get the current cube name of the Report.                                               | string   | String           | -                        |
| FilterElements       | Contains elements that are subjected to Filter constraints and a filter expression along the measure on which the filter expression is built.                             | Items    | Items            | FilterElements           |
| Name                 | Used to set or get the report name.                                                                    | string   | String           | -                        |
| SeriesElements       | Contains elements that are said to be in series axis. We can add an element and get the collection of elements that comes under the categorical axis.                          | Items    | Items            | -                        |
| ShowEmptyColumnData  | Used to show/hide the empty column in the result set.                                                  | bool     | True/False       | -                        |
| ShowemptyRowData     | Used to show/hide the empty row in the result set.                                                     | bool     | True/False       | -                        |
| ShowExpanders        | Used to show/hide the expander buttons in the Olap controls.                                           | bool     | True/False       | ShowExpanders            |
| SliceElements        | Contains the element that are said to be in slicer axis. We can add an element and get the                                                                            | Items    | Items            | -                        |

## Page-level Navigation/TOC (if applicable)
- If the page contains a local Table of Contents, it should be listed here as a bullet or numbered list.

## Cross References
- See also: OlapReport, CalculatedMembers, FilterElements, Report Settings

## RAG Annotations
<!-- tags: [product, syncfusion-winforms, olapreport, olapcommon, reportsettings] keywords: [calculated members, categorical elements, current cube name, filter elements, report name, series elements, show empty column data, show empty row data, show expanders, slice elements] -->
```

---

<!-- 페이지 101 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_028.jpeg
document_name: Olap Common
page_number: 028
page_id: Olap Common#page_028
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:16:23Z
fidelity: lossless
-->

# Essential OlapCommon

```vb
Dim dimensionElementSlicer As DimensionElement = New DimensionElement()
' Specifying the dimension Name
dimensionElementSlicer.Name = "Product"
' Adding the Level Name along with the Hierarchy Name
dimensionElementSlicer.AddLevel("Product Categories", "Category")
' Adding the Member Element
dimensionElementSlicer.Hierarchy.LevelElements("Category").Add("Bikes")
dimensionElementSlicer.Hierarchy.LevelElements("Category").IncludeAvailableMembers = True
```

## 4.3.3 Measure Element

In a cube, a measure is a set of values that are based on a column in the cube's **fact table** and are usually numeric. In addition, measures are the central values of a cube that are analyzed. That is, measures are the numeric data of primary interest to end users browsing a cube. The measures you select depend on the types of information end users request. Some common measures are sales, cost, expenditures, and production count.

We can create a measure element just by specifying its name. The following code will illustrate the creation of a measure element:

### C#

```csharp
MeasureElements measureElementColumn = new MeasureElements();
//Specifying the Measure Elements
measureElementColumn.Elements.Add(new MeasureElement { Name = "Internet Sales Amount" });
```

### VB

```vb
Dim measureElementColumn As MeasureElements = New MeasureElements()
' Specifying the Measure Elements
measureElementColumn.Elements.Add(New MeasureElement With {.Name = "Internet Sales Amount"})
```

## API Reference

### Namespaces and Classes
- `MeasureElements`
- `MeasureElement`

### Properties
#### MeasureElement
- `Name` (Type: String)
  - Specifies the name of the measure element.

### Methods
#### MeasureElements
- `Add(MeasureElement element)`
  - Adds a new measure element to the collection.

### Example Usage

#### Creating a Measure Element
```csharp
MeasureElements measureElementColumn = new MeasureElements();
measureElementColumn.Elements.Add(new MeasureElement { Name = "Internet Sales Amount" });
```

```vb
Dim measureElementColumn As MeasureElements = New MeasureElements()
measureElementColumn.Elements.Add(New MeasureElement With {.Name = "Internet Sales Amount"})
```

<!-- tags: [OlapCommon, MeasureElement, DimensionElement, Cube, FactTable] keywords: [measure, fact table, numeric data, end users, sales, cost, expenditures, production count, measure element, dimension element, cube, fact table] -->
```

---

<!-- 페이지 102 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_032.jpeg
document_name: Olap Common
page_number: 032
page_id: Olap Common#page_032
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:16:38Z
fidelity: lossless
-->

# Essential OlapCommon

## Calculated Dimension

```csharp
[C#]
DimensionElement internalDimension = new DimensionElement();
internalDimension.Name = "Product";
internalDimension.AddLevel("Product Categories", "Category");
// Calculated Dimension
CalculatedMember calculateDimension = new CalculatedMember();
calculateDimension.Name = "Bikes & Components";
calculateDimension.Expression = "([Product].[Product Categories].[Category].[Bikes] + [Product].[Product Categories].[Category].[Components] )";
calculateDimension.AddElement(internalDimension);
olapReport.CalculatedMembers.Add(calculateDimension)
```

```vb
[VB]
Dim internalDimension As DimensionElement = New DimensionElement()
internalDimension.Name = "Product"
internalDimension.AddLevel("Product Categories", "Category")
' Calculated Dimension
Dim calculateDimension As CalculatedMember = New CalculatedMember()
calculateDimension.Expression = "Bikes & Components"
calculateDimension.Expression = "([Product].[Product Categories].[Category].[Bikes] + [Product].[Product Categories].[Category].[Components] )"
calculateDimension.AddElement(internalDimension)
olapReport.CalculatedMembers.Add(calculateDimension)
```

### 4.3.8 Subset Element

Subset Elements are used to filter the result set by their count. It will just filter the number records and number of fields in the result set.

The following codes will illustrate the creation of a Subset Element:

```csharp
[C#]
SubsetElement subSetElementColumn = new SubsetElement(5);
subSetElementColumn.Name = "Top 5 Elements";
```

## API Reference

## Code Examples

<!-- tags: [product, module, control, api, version?] keywords: [calculated dimension, subset element, OlapCommon, Syncfusion Winforms] -->
```

---

<!-- 페이지 103 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_036.jpeg
document_name: Olap Common
page_number: 036
page_id: Olap Common#page_036
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:16:50Z
fidelity: lossless
-->

### Essential OlapCommon

```vb
[VB]
olapReport.SlicerRangeFilters.Add(New SlicerRangeFiltersInfo With {.DimensionName = "TimeFlat", .HierarchyName = "TimeFlat", .LevelName = "TimeId", .StartValue = "201010100031", .EndValue = "201010100037"})
```

|  | Number of failed connections |  |
| --- | --- | --- |
|  | Austria | Brazil | England | Germany | Poland | United States | Total |
| #null | 2 | 0 | 1 | 1 |  |  | 4 |
| Linux |  | 0 | 1 |  |  | 1 | 2 |
| Mac Os | 1 | 1 | 1 | 1 |  |  | 4 |
| Solaris |  |  |  |  |  |  | 1 |
| Windows |  | 1 | 0 | 1 | 0 |  | 2 |
| Total | 3 | 2 | 3 | 3 | 1 | 1 | 14 |

**Figure 6: Before applying range for filtering**

|  | Number of failed connections |  |
| --- | --- | --- |
|  | Austria | Brazil | England | Germany | Poland | United States | Total |
| #null | 0 |  | 1 |  |  |  | 1 |
| Linux |  | 0 | 1 |  |  |  | 1 |
| Mac Os |  |  | 1 |  |  |  | 1 |
| Solaris |  |  |  |  |  |  | 1 |
| Windows |  | 0 |  |  | 0 |  | 0 |
| Total | 0 | 0 | 3 | 0 |  | 1 | 5 |

**Figure 7: After applying range for filtering**

#### 4.3.11 Creating the OlapReport

**To create a report:**

1. **Instantiate a new object for `OlapReport`.**
2. **Create the required elements like dimension element, measure elements.**
3. **Add the created element in the desired axis (Column or Categorical, Row or Series, Filter or Slicer) elements.**
4. **Then bind the created report to the `OlapDataManager` using the `SetCurrentReport()` method or assign the report to `OlapDataManager`'s current report property.**

##### 4.3.11.1 Sample Reports for OLAP data

This section gives you the code snippet to generate different types of report for `OlapDataManager`.
```

---

<!-- 페이지 104 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_040.jpeg
document_name: Olap Common
page_number: 040
page_id: Olap Common#page_040
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:17:07Z
fidelity: lossless
-->

# Essential OlapCommon

```csharp
measureElementRow.Elements.Add(New MeasureElement With {.Name = "Internet Sales Amount"})

olapReport.CategoricalElements.Add(dimensionElementColumn)
olapReport.SeriesElements.Add(dimensionElementRow)
olapReport.SlicerElements.Add(dimensionElementSlicer)
olapReport.SeriesElements.Add(measureElementRow)
```

## 4.3.11.1.3 Report with dicing operation

```csharp
[C#]

OlapReport olapReport = new OlapReport();
olapReport.Name = "Customer Report";
olapReport.CurrentCubeName = "Adventure Works";
DimensionElement dimensionElementColumn = new DimensionElement();
//Specifying the Name for the Dimension Element
dimensionElementColumn.Name = "Customer";
//Specifying the Hierarchy Name
dimensionElementColumn.HierarchyName = "Customer Geography";
dimensionElementColumn.AddLevel("Customer Geography", "Country");

MeasureElements measureElementColumn = new MeasureElements();
measureElementColumn.Elements.Add(new MeasureElement { Name = "Internet Sales Amount" });

DimensionElement dimensionElementRow = new DimensionElement();
//Specifying the Dimension Name
dimensionElementRow.Name = "Date";
dimensionElementRow.HierarchyName = "Fiscal";
dimensionElementRow.AddLevel("Fiscal", "Fiscal Year");

//Specifying Excluded column elements
DimensionElement excludedColumnElement = new DimensionElement();
excludedColumnElement.Name = "Customer";
excludedColumnElement.HierarchyName = "Customer Geography";
excludedColumnElement.AddLevel("Customer Geography", "Country");
excludedColumnElement.Hierarchy.LevelElements["Country"].Add("Canada");
excludedColumnElement.Hierarchy.LevelElements["Country"].Add("France");
excludedColumnElement.Hierarchy.LevelElements["Country"].Add("United Kingdom");
excludedColumnElement.Hierarchy.LevelElements["Country"].Add("United States");
```

## Page-level Navigation/TOC (if applicable)
- If the body contains a local Table of Contents for this page, keep it as a bullet/numbered list with links/text as shown. Do not create links that don’t exist.
- Ignore global site TOC or breadcrumbs unless the page explicitly describes them.

## Cross References
- Add See also: bullet list of explicit links/texts present on the page. Do not fabricate.

## RAG Annotations
- At the end, add an HTML comment with tags and keywords derived ONLY from visible content:
  <!-- tags: [olap, report, dice operation, customer report, date hierarchy, excluded elements] keywords: [C#, dimensionElement, measureElements, hierarchy, fiscal year, customer geography, excluded column, United States] -->

<!-- tags: [olap, report, dice operation, customer report, date hierarchy, excluded elements] keywords: [C#, dimensionElement, measureElements, hierarchy, fiscal year, customer geography, excluded column, United States] -->
```


---

<!-- 페이지 105 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_044.jpeg
document_name: Olap Common
page_number: 044
page_id: Olap Common#page_044
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:17:23Z
fidelity: lossless
-->

# Essential OlapCommon

## Overview
- Create and configure elements for OLAP reports using the Syncfusion WinForms library.
- Define columns, measures, dimensions, and sorting using `DimensionElement` and `MeasureElement`.
- Add row elements with hierarchical levels for categorizing data.

## Content

### Creating and Configuring OLAP Report Elements

Here, we are demonstrating how to configure various elements for creating an OLAP report.

```csharp
measureElementColumn.Elements.Add(new MeasureElement { Name = "Internet<br>Sales Amount" });
DimensionElement dimensionElementRow = new DimensionElement();

// Specifying the Dimension Name
dimensionElementRow.Name = "Date";
dimensionElementRow.AddLevel("Fiscal", "Fiscal Year");

SortElement sortElement = new SortElement(AxisPosition.Categorical, SortOrder.BDESC, true);
sortElement.Element.UniqueName = "[Measures].[Internet Sales Amount]";

// Adding Column Members
olapReport.CategoricalElements.Add(dimensionElementColumn);
// Adding Measure Element
olapReport.CategoricalElements.Add(measureElementColumn);
// Adding Sort Element
olapReport.CategoricalElements.Add(sortElement);
// Adding Row Members
olapReport.SeriesElements.Add(dimensionElementRow);
```

### Configuring Elements in VB.NET

The following VB.NET code snippet shows how to create and configure the same OLAP report elements:

```vb
Dim olapReport As OlapReport = New OlapReport()
olapReport.Name = "Customer Report"
olapReport.CurrentCubeName = "Adventure Works"

Dim dimensionElementColumn As DimensionElement = New DimensionElement()

' Specifying the Name for the Dimension Element
dimensionElementColumn.Name = "Customer"

' Specifying the Hierarchy Name
dimensionElementColumn.HierarchyName = "Customer Geography"
dimensionElementColumn.AddLevel("Customer Geography", "Country")

' Creating Measure Elements
Dim measureElementColumn As MeasureElements = New MeasureElements()
measureElementColumn.Elements.Add(New MeasureElement With {.Name = "Internet<br>Sales Amount"})

Dim dimensionElementRow As DimensionElement = New DimensionElement()
```

## API Reference

### Namespaces and Classes
- **OlapReport**
  - Methods and Properties:
    - `Name` (String): Gets or sets the name of the report.
    - `CurrentCubeName` (String): Specifies the cube name to use for the report.
    - `CategoricalElements` (Collection): Contains elements configured for the categorical axis.
    - `SeriesElements` (Collection): Contains elements configured for the series axis.

### Methods
- **AddLevel**(String name, String levelName): Adds a hierarchical level to the dimension element.
- **SortElement**(AxisPosition position, SortOrder order, Boolean includeChildren): Creates a sort element for sorting data.

### Parameters
- **MeasureElement**:
  - Name (String): Name of the measure to display in the report.

## Code Examples

### C# Example

```csharp
var measureElementColumn = new DimensionElement();
measureElementColumn.Elements.Add(new MeasureElement { Name = "Internet Sales Amount" });
var dimensionElementRow = new DimensionElement();
dimensionElementRow.Name = "Date";
dimensionElementRow.AddLevel("Fiscal", "Fiscal Year");

var sortElement = new SortElement(AxisPosition.Categorical, SortOrder.BDESC, true);
sortElement.Element.UniqueName = "[Measures].[Internet Sales Amount]";

olapReport.CategoricalElements.Add(dimensionElementColumn);
olapReport.CategoricalElements.Add(measureElementColumn);
olapReport.CategoricalElements.Add(sortElement);
olapReport.SeriesElements.Add(dimensionElementRow);
```

### VB.NET Example

```vb
Dim olapReport As OlapReport = New OlapReport()
olapReport.Name = "Customer Report"
olapReport.CurrentCubeName = "Adventure Works"

Dim dimensionElementColumn As DimensionElement = New DimensionElement()

dimensionElementColumn.Name = "Customer"
dimensionElementColumn.HierarchyName = "Customer Geography"
dimensionElementColumn.AddLevel("Customer Geography", "Country")

Dim measureElementColumn As MeasureElements = New MeasureElements()
measureElementColumn.Elements.Add(New MeasureElement With {.Name = "Internet Sales Amount"})

Dim dimensionElementRow As DimensionElement = New DimensionElement()
```

## RAG Annotations
<!-- tags: [syncfusion-sdk, winforms, olapreport, dimensionelement, measureelement, sortelement, version: 11.4.0.26] keywords: [olap report, dimension, measure, sorting, hierarchy, axes, categorization, data analysis, business intelligence, vb.net, c#, olap, cube] -->
```

---

<!-- 페이지 106 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_048.jpeg
document_name: Olap Common
page_number: 048
page_id: Olap Common#page_048
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:17:49Z
fidelity: lossless
-->

## Essential OlapCommon

### Code Example: C#

```csharp
"Sales Amount" });

DimensionElement dimensionElementRow = new DimensionElement();
//Specifying the Dimension Name
dimensionElementRow.Name = "Date";
dimensionElementRow.AddLevel("Fiscal", "Fiscal Year");

//Specifying the SubsetElement
//Specify the start index and end index to retrieve the records.
SubsetElement subSetElementColumn = new SubsetElement(5);
subSetElementColumn.Name = "Top 5 Elements";

SubsetElement subSetElementRow = new SubsetElement(3);
subSetElementRow.Name = "Top 3 Elements";

///Adding Column Members
olapReport.CategoricalElements.Add(dimensionElementColumn);
///Adding Measure Element
olapReport.CategoricalElements.Add(measureElementColumn);
olapReport.CategoricalElements.SubSetElement = subSetElementColumn;
///Adding Row Members
olapReport.SeriesElements.Add(dimensionElementRow);
olapReport.SeriesElements.SubSetElement = subSetElementRow;
```

### Code Example: VB

```vb
[VB]

Dim olapReport As OlapReport = New OlapReport()
olapReport.Name = "Customer Report"
olapReport.CurrentCubeName = "Adventure Works"

Dim dimensionElementColumn As DimensionElement = New DimensionElement()
'Specifying the Name for the Dimension Element
dimensionElementColumn.Name = "Customer"
dimensionElementColumn.AddLevel("Customer Geography", "Country")

'Creating Measure Element
Dim olapReport As OlapReport = New OlapReport()
olapReport.CurrentCubeName = "Adventure Works"
Dim dimensionElementColumn As DimensionElement = New DimensionElement()
'Specifying the Name for the Dimension Element
```

### Summary: Key Points
- **DimensionElement** and **SubsetElement** are used to define the structure of the OLAP report.
- **DimensionElement** is used to specify the dimensions (e.g., "Date," "Fiscal Year," "Customer," "Country").
- **SubsetElement** is used to define the subset of elements to be retrieved (e.g., "Top 5 Elements").
- **MeasureElement** is also defined to specify the measure for the report.
- Both C# and VB examples are provided to illustrate the creation of an OLAP report using the Essential OlapCommon library.

---

<!-- tags: [syncfusion, olapcommon, dimensionelement, subsetelement, measelement, olapreport, winforms] keywords: [dimension, measure, subset, olap] -->
```

---

<!-- 페이지 107 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_052.jpeg
document_name: Olap Common
page_number: 052
page_id: Olap Common#page_052
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:18:04Z
fidelity: lossless
-->

# Essential OlapCommon

```csharp
dimensionElementRow.AddLevel("Fiscal", "Fiscal Year")
dimensionElementRow.Hierarchy.LevelElements("Fiscal Year").Add("FY 2002")
dimensionElementRow.Hierarchy.LevelElements("Fiscal Year").MemberElements(0).ShowChildMembers = True
dimensionElementRow.Hierarchy.LevelElements("Fiscal Year").MemberElements(0).Add("H1 FY 2002")
dimensionElementRow.Hierarchy.LevelElements("Fiscal Year").MemberElements(0).ChildMemberElements(0).ShowChildMembers = True
dimensionElementRow.Hierarchy.LevelElements("Fiscal Year").MemberElements(0).ChildMemberElements(0).Add("Q1 FY 2002")
dimensionElementRow.Hierarchy.LevelElements("Fiscal Year").MemberElements(0).ChildMemberElements(0).ChildMemberElements(0).ShowChildMembers = True
dimensionElementRow.Hierarchy.LevelElements("Fiscal Year").MemberElements(0).ChildMemberElements(0).ChildMemberElements(0).ChildMemberElements(0).Add("July 2001")
dimensionElementRow.Hierarchy.LevelElements("Fiscal Year").MemberElements(0).ChildMemberElements(0).ChildMemberElements(0).ChildMemberElements(0).ShowChildMembers = True
```

## 4.3.11.1.8 Report with Top count Filter

### [C#]

```csharp
OlapReport olapReport = new OlapReport();
olapReport.Name = "Customer Report";
olapReport.CurrentCubeName = "Adventure Works";

DimensionElement dimensionElementColumn = new DimensionElement();
//Specifying the Name for the Dimension Element
dimensionElementColumn.Name = "Customer";
dimensionElementColumn.AddLevel("Customer Geography", "Country");

//Creating Measure Element
MeasureElements measureElementColumn = new MeasureElements();
measureElementColumn.Elements.Add(new MeasureElement { Name = "Internet Sales Amount" });

DimensionElement dimensionElementRow = new DimensionElement();
//Specifying the Dimension Name
dimensionElementRow.Name = "Date";
dimensionElementRow.AddLevel("Fiscal", "Fiscal Year");
```

<!-- tags: [Syncfusion Winforms, Olap Common, Report Filter] keywords: [OlapReport, DimensionElement, MeasureElements, Customer, Date, Fiscal Year, Internet Sales Amount] -->
```

---

<!-- 페이지 108 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_056.jpeg
document_name: Olap Common
page_number: 056
page_id: Olap Common#page_056
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:18:21Z
fidelity: lossless
-->

# Essential OlapCommon

## Content

### 4.3.11.1.10 Report with calculated member

```csharp
[C#]

olapReport.CurrentCubeName = "Adventure Works";

DimensionElement dimensionElementColumn = new DimensionElement();
// Specifying the Name for the Dimension Element
dimensionElementColumn.Name = "Customer";
dimensionElementColumn.HierarchyName = "Customer Geography";
dimensionElementColumn.AddLevel("Customer Geography", "Country");

DimensionElement internalDimension = new DimensionElement();
internalDimension.Name = "Product";
internalDimension.AddLevel("Product Categories", "Category");

/// Calculated Measure
CalculatedMember calculatedMeasure1 = new CalculatedMember();
calculatedMeasure1.Name = "Order on Discount";
calculatedMeasure1.Expression = "[Measures].[Order Quantity] + ([Measures].[Order Quantity] * 0.10)";
calculatedMeasure1.AddElement(new MeasureElement { Name = "Order Quantity" });

/// Calculated Measure
CalculatedMember calculatedMeasure2 = new CalculatedMember();
calculatedMeasure2.Name = "Sales Range";
calculatedMeasure2.AddElement(new MeasureElement { Name = "Sales Amount" });
calculatedMeasure2.Expression = "IIF([Measures].[Sales Amount]>200000, \"High\", \"Low\")";

// Calculated Dimension
CalculatedMember calculateDimension = new CalculatedMember();
calculateDimension.Name = "Bikes & Components";
calculateDimension.Expression = "([Product].[Product Categories].[Category].[Bikes] + [Product].[Product Categories].[Category].[Components] )";
calculateDimension.AddElement(internalDimension);

MeasureElements measureElementColumn = new MeasureElements();
measureElementColumn.Elements.Add(new MeasureElement { Name = "Sales Amount" });
measureElementColumn.Elements.Add(new MeasureElement { Name = "Order Quantity" });

DimensionElement dimensionElementRow = new DimensionElement();
// Specifying the Dimension Name
dimensionElementRow.Name = "Date";
dimensionElementRow.AddLevel("Fiscal", "Fiscal Year");
```

## API Reference

### Namespaces and Classes

- **Namespace**: 
- **Class**: DimensionElement
- **Class**: CalculatedMember
- **Class**: MeasureElement
- **Class**: MeasureElements

### Methods

- AddElement
- AddLevel
- Add

### Properties

- Name
- HierarchyName

### Events

- None

## Code Examples

### C# Example

The provided C# code demonstrates how to create and configure a report with calculated members in an Olap report. It includes setting up dimension elements, calculated members, and measure elements. This example showcases how to define and compute derived metrics such as "Order on Discount" and "Sales Range," and how to handle calculated dimensions.

### Explanation

- **Setting Up Dimension Elements**: The code initializes dimension elements for the cube, specifying hierarchies and levels such as "Customer Geography" with the level "Country," and "Product Categories" with the level "Category."

- **Calculated Measures**: The code defines two calculated measures:
  - **Order on Discount**: Calculates the total order quantity with a 10% discount applied.
  - **Sales Range**: Categorizes sales amounts as "High" or "Low" based on a threshold of 200,000.

- **Calculated Dimension**: The code creates a calculated dimension combining two categories ("Bikes" and "Components") under the "Product Categories" dimension.

- **Measure Elements**: The example includes measure elements like "Sales Amount" and "Order Quantity," which are essential for populating the report.

## Summary

This section demonstrates the use of calculated members in an Olap report within Syncfusion WinForms. By defining dimension elements, measures, and calculated dimensions, users can create dynamic and flexible reports tailored to specific requirements.

---

<!-- tags: [olap, olapreport, calculatedmember, dimensionelement, measureelement, measureelements, syncfusionwinforms, v11.4.0.26] keywords: [calculated members, olap report, dimension elements, measures, calculated dimensions, olap cube, syncfusion winforms] -->
```

---

<!-- 페이지 109 -->

<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_060.jpeg
document_name: Olap Common
page_number: 060
page_id: Olap Common#page_060
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:18:45Z
fidelity: lossless
-->

# Essential OlapCommon

```vb
// Adding Measure Elements
olapReport.CategoricalElements.Add(measureElementColumn);
// Adding Row Members
olapReport.SeriesElements.Add(dimensionElementRow);
```

### [VB]

```vb
Dim olapReport As OlapReport = New OlapReport()
olapReport.Name = "Products Sales Report"
olapReport.CurrentCubeName = "Adventure Works"

Dim dimensionElementColumn As DimensionElement = New DimensionElement()
' Specifying the name for Dimension Element for Column
dimensionElementColumn.Name = "Product"
dimensionElementColumn.AddLevel("Product Categories", "Category")
dimensionElementColumn.Hierarchy.LevelElements("Category").Add(Me.productName)
dimensionElementColumn.Hierarchy.LevelElements("Category").IncludeAvailableMembers = True

Dim measureElementColumn As MeasureElements = New MeasureElements()
' Specifying the name for Measure Element
measureElementColumn.Elements.Add(New MeasureElement With {.Name = "Gross Profit"})

Dim dimensionElementRow As DimensionElement = New DimensionElement()
' Specifying the Name for Row Dimension Element
dimensionElementRow.Name = "Date"
dimensionElementRow.AddLevel("Fiscal", "Fiscal Year")

Dim kpiElement As KpiElements = New KpiElements()
kpiElement.Elements.Add(New KpiElement With {.Name = "Revenue",
                                             .ShowKPIStatus = True,
                                             .ShowKPIGoal = False,
                                             .ShowKPI Trend = True,
                                             .ShowKPIValue = True})
```

## Page-level Navigation/TOC (if applicable)
- If the body contains a local Table of Contents for this page, keep it as a bullet/numbered list with links/text as shown. Do not create links that don’t exist.
- Ignore global site TOC or breadcrumbs unless the page explicitly describes them.

## Cross References
- Add See also: bullet list of explicit links/texts present on the page. Do not fabricate.

<!-- tags: [olapcommon, essentialolapcommon, syncfusion, winforms, olapreport, dimensionelement, measureelements, kpielements] keywords: [OlapReport, DimensionElement, MeasureElements, KpiElements, Products Sales Report, Adventure Works, Product, Gross Profit, Date, Fiscal, Revenue] -->

---

<!-- 페이지 110 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_064.jpeg
document_name: Olap Common
page_number: 064
page_id: Olap Common#page_064
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:18:59Z
fidelity: lossless
-->

### Overview
- Configures dimension elements and hierarchy levels using `HierarchyElement` and `LevelElement`.
- Demonstrates adding row and column dimension elements with their respective hierarchies.
- Includes summary elements with specific columns and formatting.

### Content

#### Defining Dimensions and Hierarchies in C#
```csharp
dimensionElementRow.Name = "Geography";
dimensionElementRow.Hierarchy = new HierarchyElement() { Name = "Product Hierarchy" };

dimensionElementRow.Hierarchy.LevelElements.Add(new LevelElement() { Name = "Product" });
dimensionElementRow.Hierarchy.LevelElements.Add(new LevelElement() { Name = "Date" });

// Specifying the Column Dimension Element
DimensionElement dimensionElementColumn = new DimensionElement();
dimensionElementColumn.Name = "Geography";
dimensionElementColumn.Hierarchy = new HierarchyElement() { Name = "Geography Hierarchy" };

dimensionElementColumn.Hierarchy.LevelElements.Add(
    new LevelElement() { Name = "Country" });
dimensionElementColumn.Hierarchy.LevelElements.Add(
    new LevelElement() { Name = "State" });

// Specifying the Summary Elements
SummaryElements summaries = new SummaryElements();
summaries.Add(new SummaryInfo { Column = "Quantity", Key = "Quantity", Type = SummaryType.Sum });
summaries.Add(new SummaryInfo { Column = "Amount", Key = "Amount", Type = SummaryType.Sum, FormatString = "{0:c}" });

// Adding the Row Elements
olapReport.SeriesElements.Add(new Item { ElementValue = summaries });
```

#### Defining Dimensions and Hierarchies in VB.NET
```vb
Dim olapReport As OlapReport = New OlapReport()
olapReport.Name = "Sales Report"

' Specifying the Row Dimension Element
Dim dimensionElementRow As DimensionElement = New DimensionElement()
dimensionElementRow.Name = "Geography"
dimensionElementRow.Hierarchy = New HierarchyElement() With {.Name = "Product Hierarchy"}

dimensionElementRow.Hierarchy.LevelElements.Add(
    New LevelElement() With {.Name = "Product"})
dimensionElementRow.Hierarchy.LevelElements.Add(
    New LevelElement() With {.Name = "Time"})
```

### API Reference
#### Types Used
- **DimensionElement**: Represents a dimension element with hierarchy and levels.
- **HierarchyElement**: Represents a hierarchy within a dimension.
- **LevelElement**: Represents a level within a hierarchy.
- **SummaryElements**: Collection of summary elements.
- **SummaryInfo**: Represents information about a summary column.

### Code Examples

#### C#
The provided C# example shows how to create a row and column dimension element, define hierarchies and levels, add summary elements, and integrate them into an `OlapReport`.

#### VB.NET
The VB.NET example illustrates the creation of a dimension element, a hierarchy, and levels using the `With` keyword for object initialization. It provides a clearer way to define properties and relationships within the hierarchy structure.

### Cross References
- Additional resources on configuring dimension elements and summary elements can be found in the `OlapReport` documentation.

<!-- tags: [syncfusion, winforms, olapreport, dimensionelement, hierarchyelement, levelelement] keywords: [dimension, hierarchy, levels, summary elements, olap report, csharp, vb.net] -->
```

---

<!-- 페이지 111 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_068.jpeg
document_name: Olap Common
page_number: 068
page_id: Olap Common#page_068
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:19:19Z
fidelity: lossless
-->

# Essential OlapCommon

## Overview

- Demonstrates the use of MDX queries in OlapGrid, OlapChart, and OlapClient in Silverlight applications.
- Explains how to enable and disable MDX to OLAP parsing in applications.

## Content

### Navigation Paths

#### OlapGrid [Silverlight]

- `<InstalledDrive>\Users\<UserName>\AppData\Local\Syncfusion\EssentialStudio\<Version>\BI\Silverlight\OlapGrid.Silverlight\ReportDefinition\GridMDXQueryDemo`

#### OlapChart [Silverlight]

- `<InstalledDrive>\Users\<UserName>\AppData\Local\Syncfusion\EssentialStudio\<Version>\BI\Silverlight\OlapChart.Silverlight\DefiningReports\ChartMDXQueryDemo`

#### OlapClient [Silverlight]

- `<InstalledDrive>\Users\<UserName>\AppData\Local\Syncfusion\EssentialStudio\<Version>\BI\Silverlight\OlapClient.Silverlight\ProductShowcase\MDXQueryDemo`

### 4.3.16.2 Adding MDX Query binding with drill up and drill down operations to an Application

#### Overview

The following code samples are used to enable and disable the MDX to OLAP parsing and processing of an MDX query into OLAP data.

#### Code Examples

**[C#]**

```csharp
// Enable MDX to OLAP parsing.
OlapDataManager olapDataManager = new OlapDataManager();
olapDataManager.MdxQuery = "MDX Query Here";
olapDataManager.ExecuteCellSet();

// Disable MDX to OLAP parsing.
OlapDataManager olapDataManager = new OlapDataManager();
olapDataManager.AllowMdxToOlapReportParse = false;
olapDataManager.MdxQuery = "MDX Query Here";
olapDataManager.ExecuteCellSet();
```

**[VB]**

```vb
' Enable MDX to OLAP parsing.
Dim olapDataManager As New OlapDataManager()
olapDataManager.MdxQuery = "MDX Query Here"
olapDataManager.ExecuteCellSet()

' Disable MDX to OLAP parsing.
Dim olapDataManager As New OlapDataManager()
olapDataManager.AllowMdxToOlapReportParse = False
```

## Page-level Navigation/TOC

- [OlapGrid [Silverlight]](#olapgrid-silverlight)
- [OlapChart [Silverlight]](#olapchart-silverlight)
- [OlapClient [Silverlight]](#olapclient-silverlight)
- [4.3.16.2 Adding MDX Query binding with drill up and drill down operations to an Application](#43162-adding-mdx-query-binding-with-drill-up-and-drill-down-operations-to-an-application)

## Cross References

- See also:
  - [Olap Grid Documentation](#olap-grid-documentation)
  - [Olap Chart Documentation](#olap-chart-documentation)
  - [Olap Client Documentation](#olap-client-documentation)

<!-- tags: [syncfusion, winforms, olap, mdx, silverlight] keywords: [MDX query, OLAP parsing, drill up, drill down, Enable, Disable, OlapGrid, OlapChart, OlapClient, Silverlight] -->
```


---

<!-- 페이지 112 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_072.jpeg
document_name: Olap Common
page_number: 072
page_id: Olap Common#page_072
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:19:40Z
fidelity: lossless
-->

## Essential OlapCommon

### Sample of Value, Goal, Status, and Trend expressions

#### Value Expression
```csharp
[Measures].[Reseller Sales Amount]
```

#### Goal Expression
```csharp
[Measures].[Sales Amount Quota]
```

#### Status Expression
```csharp
Case
    When [Measures].[Reseller Sales Amount] / [Measures].[Sales Amount Quota] > 1
        Then 1
    When [Measures].[Reseller Sales Amount] / [Measures].[Sales Amount Quota] <= 1
        And
            [Measures].[Reseller Sales Amount] / [Measures].[Sales Amount Quota] >= .85
            Then 0
    Else -1
End
```

#### Trend Expression
```csharp
Case
    When IsEmpty
        (
            ParallelPeriod
            (
                [Date].[Fiscal].[Fiscal Year],
```

---

© 2013 Syncfusion. All rights reserved.
```

---

<!-- 페이지 113 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_076.jpeg
document_name: Olap Common
page_number: 076
page_id: Olap Common#page_076
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:19:49Z
fidelity: lossless
-->

# Essential OlapCommon

By invoking the `BuildAxisElements()` method, the building query for the column axis elements and row axis elements are done.

### Helper Methods for BuildAxisElements()

The helper methods for the `BuildAxisElements()` are:
- **BuildAxisItems**
- **BuildDimensionElement**
  - If no level is specified, the `GetDefaultLevel()` method will be called else
- **BuildHierarchyElement()** will be called
- **BuildLevelElements**
  - If the level member count is greater than zero, the `BuildMemberElement()` will be called else the `GetDefaultLevel()` method will be called.

The `BuildAxisElements()` will build the query for the column element when we pass the column items and it will generate the query for the row elements when the row items is passed as an argument. The `BuildAxisElements()` method will return a Boolean value which represents whether the KPI element is existing in the given item list or not. Based on that return, the value of the KPI Element axis was fixed.

Up to this, the **Select** section of the query was built, and now the **From** section. The **From** section will start by invoking the `BuildFilterCondition()` method.

### Helper Method for BuildFilterCondition()

The Helper method for the `BuildFilterCondition()` is given below:
1. **BuildFilteredElements()** - This method iterates through the elements and appends the parent details and child member details in the query based on the axis either in a row or in a column.
2. Then it comes to the **Where** section, by invoking the `BuildSlicerElements()` method.
3. Then the `BuildSlicerItem` is invoked. This method will check whether the given item is Dimension or Measure or KPI or NamedSet or Level and based on this the appropriate query part will appended with the query.

Finally, the Cell properties will append with the created query and the query string will be returned to the `OlapDataManager`. By using the newly generated query, the `OlapDataManager` will invoke the `ExecuteCellSet` or `DataProvide`, which will return the `CellSet`.

This `CellSet` will be used to create the `PivotEngine`, which will give the input to the controls.

## 4.5 OLAP Data Processing

The `OlapDataManager` accepts the input from the user and processes the data based on the input supplied and generates the formatted output which Syncfusion OLAP controls can understand. The `OlapDataManager` can process two types of data namely:
- OLAP data (Cube)
- Non-OLAP data (Enumerable collection, ITyped List)

### 4.5.1 Steps in processing OLAP Data

To process the OLAP data:

---

<!-- tags: [OlapDataManager, OLAP, OLAP Data Processing, PivotEngine, BuildAxisElements, BuildFilterCondition, WinForms] keywords: [OlapCommon, Query Building, Data Processing, KPI, Cube, ITyped List, Select Section, From Section, Where Section, CellSet, Syncfusion] -->
```

---

<!-- 페이지 114 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_080.jpeg
document_name: Olap Common
page_number: 080
page_id: Olap Common#page_080
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:20:07Z
fidelity: lossless
-->

## Essential OlapCommon

```csharp
Syncfusion.Olap.DataProvider.IDataProvider dataProvider = new Syncfusion.Olap.DataProvider.AdomdDataProvider("DataSource=AdventureWorks_Ext.cub; Provider=MSOLAP");
OlapDataManager dataManager = new OlapDataManager(dataProvider);
```

```vb
Dim dataProvider As Syncfusion.Olap.DataProvider.IDataProvider = New Syncfusion.Olap.DataProvider.AdomdDataProvider("DataSource=AdventureWorks_Ext.cub; Provider=MSOLAP")
Dim dataManager As New OlapDataManager(dataProvider)
```

### 5.3 Establish Role-based Connection

You can apply Role-based filtering to OLAP components by specifying the appropriate role name designed for specific set of users in the SSAS Cube. You must specify the role name in the "Roles" attribute of the connection string. The following code example illustrates this.

```csharp
OlapDataManager olapDataManager = new OlapDataManager(@"DataSource=http://bi.syncfusion.com/olap/msmdpump.dll; Roles=Role1; Initial Catalog=Adventure Works DW 2008 SE;");
```

```vb
Dim olapDataManager As OlapDataManager = New OlapDataManager("DataSource=http://bi.syncfusion.com/olap/msmdpump.dll; Roles=Role1; Initial Catalog=Adventure Works DW 2008 SE;")
```

### 5.4 Connecting to Mondrian Server through XMLA

The following code illustrates how to connect to the Mondrian server:

```csharp
// Connecting to Mondrian Server

OlapDataManager DataManager = new OlapDataManager("Data Source = http://localhost:8080/mondrian/xmla; Initial Catalog = FoodMart;");
// Where localhost is the machine name which has installed Mondrian Services. For example http://bi.syncfusion.com:8080/mondrian/xmla
DataManager.DataProvider.ProviderName = Syncfusion.Olap.DataProvider.Providers.Mondrian;
```

## Page-level Navigation/TOC (if applicable)
- Overview
  - Olap Common
  - Establish Role-based Connection
  - Connecting to Mondrian Server through XMLA

## API Reference (if applicable)
- `Syncfusion.Olap.DataProvider.IDataProvider`
- `Syncfusion.Olap.DataProvider.AdomdDataProvider`
- `OlapDataManager`

### WinForms-specific conventions
- `Syncfusion.Olap.DataProvider.IDataProvider`
- `Syncfusion.Olap.DataProvider.AdomdDataProvider`
- `OlapDataManager`

## Code Examples (multi-language supported)
- C# Example for establishing a Role-based connection
  ```csharp
  OlapDataManager olapDataManager = new OlapDataManager(@"DataSource=http://bi.syncfusion.com/olap/msmdpump.dll; Roles=Role1; Initial Catalog=Adventure Works DW 2008 SE;");
  ```
- VB Example for establishing a Role-based connection
  ```vb
  Dim olapDataManager As OlapDataManager = New OlapDataManager("DataSource=http://bi.syncfusion.com/olap/msmdpump.dll; Roles=Role1; Initial Catalog=Adventure Works DW 2008 SE;")
  ```
- C# Example for connecting to Mondrian Server
  ```csharp
  OlapDataManager DataManager = new OlapDataManager("Data Source = http://localhost:8080/mondrian/xmla; Initial Catalog = FoodMart;");
  DataManager.DataProvider.ProviderName = Syncfusion.Olap.DataProvider.Providers.Mondrian;
  ```

## Cross References
- See also: [MSOLAP Provider](https://docs.syncfusion.com/windowsforms/olap/msolap-provider/)

<!-- tags: [product, module, control, api, version?] keywords: [Olap Common, Role-based Connection, Mondrian Server, XMLA, C#, VB, Syncfusion Winforms, 11.4.0.26] -->
```

---

<!-- 페이지 115 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_084.jpeg
document_name: Olap Common
page_number: 084
page_id: Olap Common#page_084
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:20:31Z
fidelity: lossless
-->

# Essential OlapCommon

```csharp
/// <returns></returns>
public CubeSchema GetCubeSchema(string cubeName)
{
    CubeSchema cubeSchema = _dataManager.GetCubeSchema(cubeName);
    _dataManager.DataProvider.CloseConnection();
    return cubeSchema;
}

/// <summary>
/// Gets the child members.
/// </summary>
/// <param name="memberUniqueName">Name of the member unique.</param>
/// <param name="cubeName">Name of the cube.</param>
/// <returns></returns>
public MemberCollection GetChildMembers(string memberUniqueName, string cubeName)
{
    MemberCollection childMembers = _dataManager.GetChildMembers(memberUniqueName, cubeName);
    _dataManager.DataProvider.CloseConnection();
    return childMembers;
}

/// <summary>
/// Gets the level members.
/// </summary>
/// <param name="levelUniqueName">Name of the level unique.</param>
/// <param name="cubeName">Name of the cube.</param>
/// <returns></returns>
public MemberCollection GetLevelMembers(string levelUniqueName, string cubeName)
{
    MemberCollection levelMembers = _dataManager.GetLevelMembers(levelUniqueName, cubeName);
    _dataManager.DataProvider.CloseConnection();
    return levelMembers;
}

/// <summary>
/// Executes the specified MDX query.
/// </summary>
/// <param name="mdxQuery">The MDX query.</param>
/// <returns></returns>
public object Execute(string mdxQuery)
{
    var resultSet = this._dataManager.Execute(mdxQuery);
    // Closing the Provider Connection
    _dataManager.DataProvider.CloseConnection();
}
```

## API Reference

### Methods

- `GetCubeSchema(string cubeName)`
  - **Returns**: `CubeSchema`
  - Retrieves the schema for a given cube.

- `GetChildMembers(string memberUniqueName, string cubeName)`
  - **Returns**: `MemberCollection`
  - Retrieves the child members for a specified member unique name within a cube.

- `GetLevelMembers(string levelUniqueName, string cubeName)`
  - **Returns**: `MemberCollection`
  - Retrieves the members for a specified level unique name within a cube.

- `Execute(string mdxQuery)`
  - **Returns**: `object`
  - Executes the specified MDX query and returns the result set.

### Parameters

- `cubeName`: The name of the cube to access.
- `memberUniqueName`: The unique name of the member to retrieve child members for.
- `levelUniqueName`: The unique name of the level to retrieve members for.
- `mdxQuery`: The MDX query to execute.

## Code Examples

### Example: Retrieving Cube Schema

```csharp
CubeSchema cubeSchema = OlapCommon.GetCubeSchema("SalesCube");
```

### Example: Retrieving Child Members

```csharp
MemberCollection childMembers = OlapCommon.GetChildMembers("Product.Category", "SalesCube");
```

### Example: Executing an MDX Query

```csharp
object resultSet = OlapCommon.Execute(
    "SELECT " +
    "    {[Measures].[Sales Amount]} ON COLUMNS, " +
    "    {[Product].[Category].Members} ON ROWS " +
    "FROM [SalesCube]"
);
```

<!-- tags: [product, OlapCommon, CubeSchema, MemberCollection, MDX Query, API Reference, Parameters, Methods, Code Examples] keywords: [cube schema, child members, level members, MDX execution, data retrieval, OOAP] -->
```

---

<!-- 페이지 116 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_088.jpeg
document_name: Olap Common
page_number: 088
page_id: Olap Common#page_088
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:20:52Z
fidelity: lossless
-->

## Essential OlapCommon

```csharp
IolapDataProvider>(customBinding, address);
IOLapDataProvider _dataProvider = clientChannel.CreateChannel();
//////Sets the data provider (WCF Service connection) in OlapDataManager
_olapDataManager.DataProvider = _dataProvider;
```

```vb
Dim customBinding As Binding = New CustomBinding(New BinaryMessageEncodingBindingElement(), New HttpTransportBindingElement() With { _
    Key .MaxReceivedMessageSize = 2147483647 _
})
Dim address As New EndpointAddress(New Uri(App.Current.Host.Source.ToString() & 
    ".../.../.../Services/OlapManager.svc/binary"))
Dim clientChannel As New ChannelFactory(Of IOLapDataProvider)(customBinding, address)
Dim _dataProvider As IOLapDataProvider = clientChannel.CreateChannel()

'''Sets the data provider (WCF Service connection) in OlapDataManager
_olapDataManager.DataProvider = _dataProvider
```

## 5.8 Bind an OlapReport with OlapDataManager

Once the connection is established, you can create and bind the OlapReport to the manger by using any one of the following property and methods:

### Property:

- 1. CurrentReport

### Methods:

- 1. SetCurrentReport
- 2. LoadOlapDataManager
- 3. LoadReportDefinitionFile
- 4. LoadReportDefinitionFromStream

### Methods for Silverlight:

- 1. SetCurrentReport
- 2. LoadReportFromStream

The following code snippet will illustrate the binding of OlapReport using these methods with a sample OlapReport:

### Sample OlapReport

```csharp
[C#]
```

<!-- tags: [OlapCommon, OlapReport, OlapDataManager, Winforms] keywords: [Olap Report, Data Manager, WCF Service, Binding, Syncfusion, C#, VB] -->
```

---

<!-- 페이지 117 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_092.jpeg
document_name: Olap Common
page_number: 092
page_id: Olap Common#page_092
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:21:05Z
fidelity: lossless
-->

# Essential Olap Common

## Sequential Diagram

The following sequential diagram shows the workflow of OlapBase when a user gives input as an OlapReport.

<div align="center">
 <img src="seq_diagram.png" alt="Olap Base sequential diagram" />
 <p>Figure 9: Olap Base sequential diagram</p>
</div>

## 5.9 Bind the MDX Query to OlapDataManager

### Overview
- MDX queries are one of the inputs accepted by the `OlapDataManager` to process the data in the connected data source.
- There are two ways to pass the MDX query to the `OlapDataManager`.

### WinForms-specific conventions
- **Property Binding**: Through the `MdxQuery` property.
- **Method Binding**: Through the `ExecuteCellSet()` method argument.

### Content

MDX queries are one of the inputs accepted by the `OlapDataManager` to process the data in the connected data source. To bind the MDX query to the `OlapDataManager`, you can use either of the following two methods:

1. **Through the `MdxQuery` property**  
   - Assign the MDX query string directly to the `MdxQuery` property of the `OlapDataManager`.

2. **Through the `ExecuteCellSet()` method argument**  
   - Pass the MDX query as an argument when invoking the `ExecuteCellSet()` method on the `OlapDataManager`.

## Page-level Navigation/TOC

- **Sequential Diagram**
- **5.9 Bind the MDX query to OlapDataManager**

### API Reference (if applicable)
- Relevant properties and methods can be referenced in the API documentation for more details.

### Code Examples (multi-language supported)
Here is an example of how to bind an MDX query using both methods:

```csharp
// Using MdxQuery property
OlapDataManager olapDataManager = new OlapDataManager();
olapDataManager.MdxQuery = "SELECT FROM [YourCube].[YourView]";

// Using ExecuteCellSet method
CellSet cellSet = olapDataManager.ExecuteCellSet("SELECT FROM [YourCube].[YourView]");
```

## Cross References
- [Refer to the OlapDataManager documentation for more detailed information.](#OlapDataManager-documentation)

## RAG Annotations
<!-- tags: Olap Common, OlapDataManager, MDX query, property binding, method binding keywords: MDX query, OlapDataManager, MdxQuery, ExecuteCellSet -->
```

---

<!-- 페이지 118 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_096.jpeg
document_name: Olap Common
page_number: 096
page_id: Olap Common#page_096
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:21:20Z
fidelity: lossless
-->

# Essential OlapCommon

The following sequential diagram shows the workflow of OlapBase when the input is a Non-OLAP data:

```plaintext
          User
            |
            v
        OlapDataManager
            |
            v
        DataProvider
            |
            v
        QuerySpecification
            |
            v
        QueryBuilder
            |
            v
        QueryBuilderHelper
            |
            v
        PivotEngine
```

**Figure 11: Olap base Sequential diagram**

## 5.11 Save the report as xml file

The user can save the current report set of OlapDataManager as an xml file for the future needs by using the SaveReport method.

The following code snippet will illustrate the saving of the current report set as an xml file:

### C#

```csharp
olapDataManager.SaveReport(@"C:\SampleReport\RevenueAnalysis.xml");
```

### VB

```vb
olapDataManager.SaveReport("C:\SampleReport\RevenueAnalysis.xml")
```

### For Silverlight:

You can save the current report of OlapDataManager as an xml file for their future use by serializing the report with `XmlSerializer`.

The following code snippet will illustrate the saving of the current report set as an xml file:

### C#

```csharp
private void SaveReport()
{
    SaveFileDialog dlg = new SaveFileDialog();
}
```

<footer>
© 2013 Syncfusion. All rights reserved.
106 | Page
</footer>
```

---

<!-- 페이지 119 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_100.jpeg
document_name: Olap Common
page_number: 100
page_id: Olap Common#page_100
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:21:31Z
fidelity: lossless
-->

# Essential OlapCommon

## Overview
- Understand how to manage reports in the OlapDataManager.
- Learn to use methods for removing and retrieving reports.
- Explore data communication between the OLAP control and the base.

## Content

### 5.13.2 RemoveReport

A report in the report collection of the OlapDataManager can be removed by invoking the RemoveReport method. This method will accept the report name as an argument and remove that report from the report collection of OlapDataManager.

The following code snippet will illustrate the removal of a report:

```csharp
olapDataManager.RemoveReport("SalesAnalysisOn2005");
```

```vb
olapDataManager.RemoveReport("SalesAnalysisOn2005")
```

### 5.14 Get the reports in the OlapDataManager as a stream

You can get the report collection in the OlapDataManager as a stream by using GetReportAsStream method. This method will return the current report collection of the OlapDataManager as a stream.

The following code snippet will explain obtaining the report as a stream:

```csharp
Stream reportStream = olapDataManager.GetReportAsStream();
```

```vb
Dim reportStream As Stream = olapDataManager.GetReportAsStream()
```

### 5.15 Communicate the OLAP control with the base

Each and every control has an OlapDataManager property. Through this property, the control sends and receives information to and from the base.

Below steps explains how to load data in an OLAP control:

1. Give the connection information and OlapReport to the OlapDataManager.
2. Assign this OlapDataManager to the control's OlapDataManager property.
3. By invoking the control's DataBind() method virtually when setting the value for the OlapDataManager property, the data processing will begin and the output is displayed in the Control.

---

## Page-level Navigation/TOC

- [5.13.2 RemoveReport]
- [5.14 Get the reports in the OlapDataManager as a stream]
- [5.15 Communicate the OLAP control with the base]

## Cross References

See also:
- OlapDataManager
- OlapReport
- DataBind()

<!-- tags: [Olap DataManager, Olap Report, RemoveReport, GetReportAsStream, DataBind] keywords: [Olap, WinForms, Report Management, Data Binding, Stream] -->
```

---

<!-- 페이지 120 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_104.jpeg
document_name: Olap Common
page_number: 104
page_id: Olap Common#page_104
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:21:45Z
fidelity: lossless
-->

## Overview

- Displays the Expander button in Controls.
- Explains internal processing of OlapReport within OlapDataManager.
- Describes methods for handling Drill Down/Up operations.

## Content

### 5.19 Process OlapReport Internally

Once the `OlapReport` is created and bound to the `OlapDataManager`, the data processing begins. By binding the report, the given report will be set as the current report of the `OlapDataManager` and it will invoke the two important methods that let the way to generate the **MDX query** and `CellSet`.

- **NotifyReportChanged**
  - After initialization, the data processing begins. When the `NotifyReportChanged` is invoked, it triggers the `ReportChaned` event, which will be handled by the control level.

- **NotifyElementModified**
  - The `NotifyElementModified` method begins the processing by invoking the `ExecuteCellSet()` method, which creates the `CellSet` and `PivotEngine` based on the `OlapReport`.

#### Explanation of `ExecuteCellSet()`
- The `ExecuteCellSet()` method checks whether the user has given the MDX query. If the query exists, it will invoke an overloaded method of the `ExecuteCellSet(string query)` which in turn calls the `ExecuteCellSet(string query, bool b1, bool b2)` of `DataProvider` class. The given query will be executed in the `DataProvider` class and the `CellSet` will be produced.
- If the query does not exist, the overloaded method of `ExecuteCellSet (MDXQuerySpecification querySpecification)` will get invoked. This method will invoke the `MDXQuerySpecification` creation and from there the query creation will be invoked and the query will be returned. The `ExecutCellSet()` method receives the query and passes it to the data provider’s `ExecuteCellset` method. The query will be executed there on the connected database and a `CellSet` will be returned. From the `CellSet`, the `PivotEngine` will be created, from which the controls can get their input.

### 5.20 Handle Drill Down/Up Process

Whenever we collapse or expand the controls like a grid or chart, the level member items will change and the query will be regenerated to create the new `CellSet`.

The important methods that identify the drill-down members are:

- **ToggleExpandableState()**
- **UpdateDrillDowlItems()**
- **DrillUpDown()**

## Code Examples

```csharp
/// Displaying the Expander button in Controls
olapReport.ShowExpanders = false;
```

## Page-level Navigation/TOC (if applicable)

- 5.19 Process OlapReport Internally
  - NotifyReportChanged
  - NotifyElementModified
- 5.20 Handle Drill Down/Up Process

<!-- tags: [olapreport, drilldown, syncfusion, olapmanager, pivotengine] keywords: [notifyreportchanged, notifyelementmodified, excutecellset, mdxquery, drilldown, drillup, cellset, pivotengine, dataprovider] -->
```

---

<!-- 페이지 121 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_108.jpeg
document_name: Olap Common
page_number: 108
page_id: Olap Common#page_108
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:22:03Z
fidelity: lossless
-->

## Essential OlapCommon

### Initialize Connection in VB

```vb
Private Sub InitializeConnection()
    Dim basicHttpBinding As System.ServiceModel.Channels.Binding = New BasicHttpBinding(BasicHttpSecurityMode.None With {.MaxReceivedMessageSize = 2147483647})
    'Address for Basic HTTP binding in corresponding Web configuration file
    Dim address As EndpointAddress = New EndpointAddress(New Uri(App.Current.Host.Source & "../../OlapManager.svc/basic"))
    Dim clientChannel As ChannelFactory(Of IOlapDataProvider) = New ChannelFactory(Of IOlapDataProvider)(basicHttpBinding, address)
    DataProvider = clientChannel.CreateChannel()
End Sub
```

### Retrieve the MDX Query of a CurrentReport

The MDX query of a current report is used to display data in Grid/Chart control and it can be retrieved by calling the `GetMdxQuery()` method.

The following code explains how to retrieve MDX Query from the OlapDataManager:

#### In C#

```csharp
olapDataManager.GetMDXQuery();
```

#### In VB

```vb
olapDataManager.GetMDXQuery()
```

#### In Silverlight

```csharp
[C#]
string currentMdxQuery = null;
//// Invoke the service call to retrieve the MDX query from the Server based on current report.
_olapDataManager.GetMdxQuery(_olapDataManager.CurrentReport);
_olapDataManager.MdxQueryObtained += () => {
    //// MDX Query retrieved.
    currentMdxQuery = _olapDataManager.CurrentReport.CurrentMdxQuery;
};
```

## Code Examples

### Initializing Connection in C#

```csharp
[C#]
Private Sub InitializeConnection()
    Dim basicHttpBinding As System.ServiceModel.ServiceModel.HttpBinding = New BasicHttpBinding (BasicHttpSecurityMode.None With (.MaxReceivedMessageSize = 2147483647))
    ' Address for Basic HTTP binding in corresponding Web configuration file
    Dim address As EndpointAddress = New EndpointAddress (New Uri(". /APP. Current. Source & " "" / / / / OIapManager.svc/basic"))
    Dim clientChannel As ChannelFactory(Of IOlapDataProvider) = New ChannelFactory(Of IOlapDataProvider) (basicHttpBinding, address)
    DataProvider = clientChannel.CreateChannel()
End Sub
```

### Retrieving MDX Query from OlapDataManager

#### Sample Code

```csharp
[C#]
string currentMdxQuery = null;
//// Invoke the service call to retrieve the MDX query from the Server based on current report.
_olapDataManager.GetMdxQuery(_olapDataManager.CurrentReport);
_olapDataManager.MdxQueryObtained += () => {
    //// MDX Query retrieved.
    currentMdxQuery = _olapDataManager.CurrentReport.CurrentMdxQuery;
};
```

<!-- tags: [Olap Common, WinForms, MDX Query, OlapDataManager, Silverlight, Syncfusion Winforms] keywords: [MDX Query, OlapDataManager, GetMdxQuery, InitializeConnection, ChannelFactory, DataProvider, Silverlight, WCF] -->
```

---

<!-- 페이지 122 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_112.jpeg
document_name: Olap Common
page_number: 112
page_id: Olap Common#page_112
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:22:21Z
fidelity: lossless
-->

# Essential OlapCommon

## Overview
- This page provides a detailed view of the Solution Explorer with a Silverlight and MVC project structure in an Microsoft Visual Studio project solution.
- Guides users through opening the `Main.xaml` file located within the Silverlight project in the Solution Explorer.

## Content

### WinForms-specific conventions

#### Solution Explorer with Silverlight and MVC Projects

![](Solution%20Explorer%20with%20Silverlight%20and%20MVC%20Projects.png)

**Figure 15: Solution Explorer with Silverlight and MVC Projects**

The Solution Explorer window displays the structure of a solution named `SilverlightApplication1`, containing two projects:

- **SilverlightApplication1**:
  - Properties
  - References
  - App.xaml
  - MainPage.xaml
  
- **SilverlightApplication1.Web**:
  - Properties
  - References
  - App_Data
  - ClientBin
  - Content
  - Controllers
  - Models
  - Scripts
  - Views
  - Global.asax
  - Silverlight.js
  - SilverlightApplication1TestPage.aspx
  - SilverlightApplication1TestPage.html
  - Web.config

This visual representation helps developers understand the organization of files and folders within a mixed Silverlight and MVC project.

### Steps to Open `Main.xaml`

4. Double-click to open the `Main.xaml`, which is found under the Silverlight project in Solution Explorer as shown below:

### Code Examples

The image does not contain any explicit code examples in this section. However, if you are looking to work on UI design or XAML manipulation, `Main.xaml` would likely contain XAML markup for layout and UI elements. For example:

```xaml
<UserControl x:Class="SilverlightApplication1.MainPage"
             xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
             xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
             mc:Ignorable="d"
             d:DesignHeight="300" d:DesignWidth="400">
    <Grid x:Name="LayoutRoot" Background="White">
        <TextBlock Text="Hello, Silverlight!" FontSize="24" HorizontalAlignment="Center" VerticalAlignment="Center" />
    </Grid>
</UserControl>
```

This is a basic example of what a `Main.xaml` file might contain in a Silverlight project.

## Page-level Navigation/TOC (if applicable)

- [Figure 15: Solution Explorer with Silverlight and MVC Projects]
- Steps to Open `Main.xaml`
- Code Examples

## Cross References

See also:
- Related documentation or sections that may discuss Silverlight or MVC project integration, or WinForms control interaction.

## RAG Annotations

<!-- tags: [product, Silverlight, MVC, Solution Explorer, WinForms] keywords: [SilverlightApplication1, SilverlightApplication1.Web, MainPage.xaml, Global.asax, XAML, Solution Explorer, Silverlight, MVC] -->
```

---

<!-- 페이지 123 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_116.jpeg
document_name: Olap Common
page_number: 116
page_id: Olap Common#page_116
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:22:39Z
fidelity: lossless
-->

# Essential `OlapCommon`

## Overview
- This class provides methods to execute OLAP reports and MDX queries for retrieving data from a data source.
- It includes handling connection management and executing queries or reports to obtain `CellSet` results.

## Content

### `OlapManager` Constructor

```csharp
/// <summary>
/// Initializes a new instance of the <see cref="OlapManager"/> class.
/// </summary>
public OlapManager()
{
    string connectionString = "DataSource=localhost;Initial Catalog=Adventure Works DW";

    // Instantiating the OlapDataProvider with connection string.
    dataManager = new OlapDataProvider(connectionString);
}
```

### `ExecuteOlapReport` Method

```csharp
/// <summary>
/// Executes the CellSet by passing an OlapReport.
/// </summary>
/// <param name="report">The report.</param>
/// <returns>The CellSet</returns>
public Syncfusion.OlapSilverlight.Data.CellSet ExecuteOlapReport(Syncfusion.OlapSilverlight.Reports.OlapReport report)
{
    Syncfusion.OlapSilverlight.Data.CellSet cellSet = this.dataManager.ExecuteOlapReport(report);

    // Closing the provider connection.
    this.dataManager.DataProvider.CloseConnection();

    return cellSet;
}
```

### `ExecuteMdxQuery` Method

```csharp
/// <summary>
/// Executes the CellSet by passing an MDX Query.
/// </summary>
/// <param name="mdxQuery">The MDX query.</param>
/// <returns>The CellSet</returns>
public Syncfusion.OlapSilverlight.Data.CellSet ExecuteMdxQuery(string mdxQuery)
{
    Syncfusion.OlapSilverlight.Data.CellSet cellSet = this.dataManager.ExecuteMdxQuery(mdxQuery);
}
```

## API Reference

### `OlapManager`
- **Methods:**
  - `ExecuteOlapReport(Syncfusion.OlapSilverlight.Reports.OlapReport report)`: Executes a report and returns a `CellSet`.
  - `ExecuteMdxQuery(string mdxQuery)`: Executes an MDX query and returns a `CellSet`.

### Parameters
- `report`: The `OlapReport` object used for executing the report.
- `mdxQuery`: The MDX query as a string.

### Returns
- `CellSet`: A structured collection of data representing the result of the report or query.

## Code Examples

### Example: Executing an OLAP Report
```csharp
OlapManager manager = new OlapManager();
OlapReport report = new OlapReport();
// Configure report parameters here...
CellSet result = manager.ExecuteOlapReport(report);
// Process the result...
```

### Example: Executing an MDX Query
```csharp
OlapManager manager = new OlapManager();
string mdxQuery = "SELECT ..."; // Define your MDX query here
CellSet result = manager.ExecuteMdxQuery(mdxQuery);
// Process the result...
```

## Cross References
- Refer to the `OlapDataProvider` and `OlapReport` classes for more information on how they work with `OlapManager`.

<!-- tags: [product, module, control, api, version?] keywords: [Olap, MDX, Query, CellSet, OlapReport, Data, WinForms] -->
```

---

<!-- 페이지 124 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_120.jpeg
document_name: Olap Common
page_number: 120
page_id: Olap Common#page_120
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:22:57Z
fidelity: lossless
-->

# Essential OlapCommon

```xml
</bindings>
<!--Endpoint Address-->
<services>
  <service name="SilverlightApplication1.Web.OlapManager" >
    <endpoint address="binary" binding="customBinding" bindingConfiguration="binaryHttpBinding" contract="Syncfusion.OlapSilverlight.Manager.IOlapDataProvider" />
  </service>
</services>
```

## Setting Up the Service

12. Add the `System.ServiceModel` assembly as a reference for the Silverlight project.

13. Add the following namespace in MainPage.xaml.cs:

- System.ServiceModel
- System.ServiceModel.Channels
- Syncfusion.OlapSilverlight.Reports
- Syncfusion.Silverlight.Grid
- Syncfusion.OlapSilverlight.Manager
- Syncfusion.OlapSilverlight.Engine

14. Instantiate the service from MainPage.xaml.cs which is in the Silverlight Project.

15. Declare the `IOlapDataProvider` for service instantiation.

### Code Example

#### C#

```csharp
// Declaring the IOlapDataProvider for service instantiation.
IOlapDataProvider DataProvider = null;
```

#### VB

```vb
'Declaring the IOlapDataProvider for service instantiation.
Dim DataProvider As IOlapDataProvider = Nothing
```

16. Specify the custom binding and instantiate the `DataProvider` from the `ChannelFactory`.

### Code Example

#### C#

```csharp
private void InitializeConnection()
{
    System.ServiceModel.Channels.Binding customBinding = new CustomBi
    ...
}
```

## Copyright Notice

© 2013 Syncfusion. All rights reserved.
```

---

<!-- 페이지 125 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_124.jpeg
document_name: Olap Common
page_number: 124
page_id: Olap Common#page_124
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:23:08Z
fidelity: lossless
-->

# Index

## Overview
- This section provides an index covering various topics related to Business Intelligence (BI), Online Analytical Processing (OLAP), and the Syncfusion OLAP Architecture.
- Includes detailed entries on concepts such as MDX Query Parsing, Drilling through reports, and creating OLap Reports.
- References tools like AdomdDataProvider, OlapDataManager, and OlapReport for working with OLAP data.

## Content

### 1 Business Intelligence (BI)

- **1.1 What is BI?** (5)
- **1.2 Why to use BI?** (5)
- **1.3 What's new in BI?** (5)
- **1.3.1 Multi-dimensional Data** (5)

### 2 Online Analytical Processing (OLAP)

- **2.1 ADOMD.NET** (7)
- **2.2 ADOMD.NET assembly and setup files** (7)
- information (7)

### 3 Syncfusion OLAP Architecture

- **3.1 OLAP Base** (9)
- **3.2 OLAP Silverlight Base** (10)
- **3.3 OLAP Silverlight Base Wrapper** (10)
- **3.3.1 WCF Service** (11)

### 4 Concepts

- **4.1 OlapDataProvider** (12)
  - **4.1.1 AdomdDataProvider** (12)
- **4.2 OlapDataManager** (14)
  - **4.2.1 Properties and Methods** (17)
  - **4.2.2 UseWhereClauseForSlicing** (21)
  - **4.2.3 Drill Through** (22)
- **4.3 OlapReport** (22)
  - **4.3.1 Properties and Methods** (23)
  - **4.3.10 Filtering slicer elements by range** (34)
  - **4.3.11 Creating the OlapReport** (36)
    - **4.3.11.1 Sample Reports for OLAP data** (36)
      - **4.3.11.1.1 Simple Report** (37)
      - **4.3.11.1.2 Report with slicing operation** (38)
      - **4.3.11.1.3 Report with dicing operation** (40)
      - **4.3.11.1.4 Ordered Report** (43)
      - **4.3.11.1.5 Report with Filter** (45)
      - **4.3.11.1.6 Report with subset** (47)
      - **4.3.11.1.7 Drill down report** (49)
      - **4.3.11.1.8 Report with Top count Filter** (52)
      - **4.3.11.1.9 Report with Named set** (54)
      - **4.3.11.1.10 Report with calculated member** (56)
      - **4.3.11.1.11 Report with KPI Element** (59)
      - **4.3.11.1.12 Report with member properties** (61)
  - **4.3.11.2 Sample Report for Non-OLAP data** (63)
  - **4.3.12 Binding the OlapReport to OlapDataManager** (65)

### 4.4 QueryBuilderEngine

- **4.4.1 MDXQuerySpecification** (75)
- **4.4.2 Steps in Query Generation** (75)

## API Reference

### AdomdDataProvider

### OlapDataManager

- Properties and Methods

### OlapReport

- Properties and Methods

## Code Examples

### Example: Creating an OLAP Report

```csharp
OlapReport olapReport = new OlapReport();
OlapDataManager olapDataManager = new OlapDataManager();
AdomdDataProvider adomdDataProvider = new AdomdDataProvider();
olapReport.OlapDataManager = olapDataManager;
```

## Cross References

- **See also:** AdomdDataProvider, OlapDataManager, OlapReport, MDX Query Parsing, Drilling through reports.

<!-- tags: [syncfusion, winforms, olap, olapreport, olapdatamanager, adomddataprovider, medxquery] keywords: [bi, olap, adomd, syncfusion, olapreport, mddlquery, olapdata, architecture] -->
```