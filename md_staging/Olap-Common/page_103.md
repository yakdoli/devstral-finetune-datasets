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