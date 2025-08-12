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