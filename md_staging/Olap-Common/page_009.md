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