```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_386.jpeg
document_name: XlsIO
page_number: 386
page_id: XlsIO#page_386
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:12:28Z
fidelity: lossless
-->

## Essential XlsIO

### Code Example

```csharp
marker = workbook.CreateTemplateMarkersProcessor()
Dim conditions As IConditionalFormats = marker.CreateConditionalFormats(sheet("D3"))
Dim condition As IConditionalFormat = conditions.AddCondition()
condition.FormatType = ExcelCType.IconSet
condition.IconSet.IconSet = ExcelIconSetType.ThreeFlags
```

### Additional References

For More Information Refer:
- AutoFilters
- Validating Data
- Template Markers
- Grouping and Ungrouping

### 4.5.6 Outlines

Microsoft Excel has grouping and outlining features, which allows you to group large quantities of data. You can group/ungroup a range of rows and columns. To do this, go to the **Data** menu, point to **Group and Outline**, and select **Group/UnGroup** in Excel.
```html

<!-- tags: [Essential XlsIO, WinForms, Conditional Formatting, Templates, Grouping, Outlining] keywords: [AutoFilters, Validating Data, Template Markers, Group and Outline, Group/UnGroup] -->
```