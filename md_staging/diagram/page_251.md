```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_251.jpeg
document_name: diagram
page_number: 251
page_id: diagram#page_251
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:22:53Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

The diagram has built-in UI dialogs to add, edit, and remove the dynamic properties.

## Overview
- Provides built-in UI dialogs for managing dynamic properties.
- Allows storage of additional data to nodes or connectors.
- Utilizes the PropertyBag property to handle dynamic property data.

## Use Case Scenario
It is used to store additional data to the nodes or connectors as needed.

### Properties

| Property     | Description                                               | Data Type           |
|--------------|-----------------------------------------------------------|---------------------|
| PropertyBag  | Gets or sets the dynamic property data dictionary.        | Dictionary<string, object> |

### Code Examples

#### Adding Additional Data Using PropertyBag (C#)
```csharp
node.PropertyBag.Add("Name", employ.EmployeeName);
node.PropertyBag.Add("ID", employ.EmployeeID);
node.PropertyBag.Add("Designation", employ.Designation);
```

#### Adding Additional Data Using PropertyBag (VB)
```vb
node.PropertyBag.Add("Name", employ.EmployeeName)
node.PropertyBag.Add("ID", employ.EmployeeID)
node.PropertyBag.Add("Designation", employ.Designation)
```

<!-- tags: [product, diagram, windows forms, propertybag, dynamic properties, syncfusion] keywords: [dynamic properties, propertybag, windows forms diagram, add data, edit data, remove data, built-in UI dialogs] -->
```