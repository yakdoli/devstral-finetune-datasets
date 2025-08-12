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