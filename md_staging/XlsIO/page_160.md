```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_160.jpeg
document_name: XlsIO
page_number: 160
page_id: XlsIO#page_160
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:59:45Z
fidelity: lossless
-->

## Conditional Formatting with Icon Sets and Color Scales

### Setting Up Icon Sets

`iconSet.ShowIconOnly = True`

```csharp
'Sets Icon sets for another range
formats = sheet.Range("E7:E46").ConditionalFormats
format = formats.AddCondition()
format.FormatType = ExcelCFType.IconSet
iconSet = format.IconSet
iconSet.IconSet = ExcelIconSetType.ThreeSymbols
iconSet.IconCriteria(0).Type = ConditionValueType.LowestValue
iconSet.IconCriteria(0).Value = "0"
iconSet.IconCriteria(1).Type = ConditionValueType.HighestValue
iconSet.IconCriteria(1).Value = "0"
iconSet.ShowIconOnly = True
```

### Configuring Color Scale Conditional Formatting

```csharp
'Sets Color Scale conditional format type
formats = sheet.Range("D7:D46").ConditionalFormats
format = formats.AddCondition()
format.FormatType = ExcelCFType.ColorScale
Dim colorScale As IColorScale = format.ColorScale

'Sets 3 - color scale.
colorScale.SetConditionCount(3)

colorScale.Criteria(0).FormatColorRGB = System.Drawing.Color.FromArgb(230, 197, 218)
colorScale.Criteria(0).Type = ConditionValueType.LowestValue
colorScale.Criteria(0).Value = "0"

colorScale.Criteria(1).FormatColorRGB = System.Drawing.Color.FromArgb(244, 210, 178)
colorScale.Criteria(1).Type = ConditionValueType.Percentile
colorScale.Criteria(1).Value = "50"

colorScale.Criteria(2).FormatColorRGB = System.Drawing.Color.FromArgb(245, 247, 171)
```

<!-- tags: [xlsio, conditional formatting, icon sets, color scales] keywords: [iconset, excelcftype, colorscale, conditionvaluetype] -->
```