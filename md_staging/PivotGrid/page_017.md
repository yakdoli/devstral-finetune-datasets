```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_017.jpeg
document_name: PivotGrid
page_number: 017
page_id: PivotGrid#page_017
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:53:23Z
fidelity: lossless
-->

# Essential PivotGrid WindowsForms

## Concepts and Features

### 4.1 PivotItem

PivotItem is an item in a PivotTable field. It provides the information needed to define a pivot item for either a row or column. It consists of the following fields.

#### Table 5: Properties Table for PivotItem

| Property Name | Description | Type | Value it Accepts | Reference link |
|---------------|-------------|------|------------------|----------------|
| Comparer      | Gets or sets the IComparer object used for sorting. If this value is null, then sorting will be performed under the assumption that this field is IComparable. | IComparer | - | - |
| FieldHeader   | Gets or sets the title you want to see in the header for this pivot item. | string | - | - |
| FieldMappingName | Gets or sets the property's mapping name. | string | - | - |
| Format | Gets or sets the format item for the specified field. | string | - | - |
| TotalHeader | Gets or sets the string you want to append to the pivot item's summary cells. | string | - | - |

#### 4.1.1 Defining PivotItem in Code-Behind

The PivotItem can be defined in code-behind. The following code example illustrates this.

```csharp
<!-- code example would go here -->
```
<!-- tags: [winforms, pivotgrid, pivotitem, code-behind, syncfusion, windowsforms, pivottable, fieldheader, fieldmappingname, format, totalheader] keywords: [pivotitem, code-behind, pivotgrid, pivottable, fieldmappingname, format, totalheader, fieldheader] -->
```