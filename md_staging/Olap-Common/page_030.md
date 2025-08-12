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