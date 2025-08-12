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