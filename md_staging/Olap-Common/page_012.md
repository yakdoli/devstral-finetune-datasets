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