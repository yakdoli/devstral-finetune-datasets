```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_385.jpeg
document_name: XlsIO
page_number: 385
page_id: XlsIO#page_385
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:15:02Z
fidelity: lossless
-->

# Essential XlsIO

Here is the sample for dynamically applied conditional format to data, during runtime.

![](images/sample_image.png)

Figure 104: Dynamically applied conditional format to data (during runtime)

The following code sample illustrates how to create or apply conditional format to the Marker.

### Code Example

```csharp
[//]: # ([C#])
ITemplateMarkersProcessor marker = 
workbook.CreateTemplateMarkersProcessor();
IConditionalFormats conditions = 
marker.CreateConditionalFormats(sheet["D3"]);
IConditionalFormat condition = conditions.AddCondition();
condition.FormatType = ExcelCFormatType.IconSet;
condition.IconSet.IconSet = ExcelIconSetType.ThreeFlags;
```

```vb
[//]: # ([VB])
```

## Page-level Navigation/TOC (if applicable)

## Cross References

See also: [Dynamic Conditional Formatting]

<!-- tags: [Essential XlsIO, Conditional Formatting, Dynamic Formatting, Runtime, Marker] keywords: [dynamic formatting, runtime conditional formatting, marker processing, ExcelCFormatType, ExcelIconSetType, Syncfusion Winforms] -->
```