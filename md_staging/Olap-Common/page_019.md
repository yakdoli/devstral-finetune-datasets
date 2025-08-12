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