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