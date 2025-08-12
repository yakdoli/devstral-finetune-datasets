```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_158.jpeg
document_name: XlsIO
page_number: 158
page_id: XlsIO#page_158
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:57:53Z
fidelity: lossless
-->

## Overview
- Demonstrates setting icon sets and color scale conditional formatting for specific ranges in an Excel worksheet.

## Content

### Setting Icon Sets

The following code snippet shows how to apply icon sets for a range of cells in an Excel worksheet.

```csharp
//Sets Icon sets for another range
conditionalFormats = worksheet.Range["E7:E46"].ConditionalFormats;
conditionalFormat = conditionalFormats.AddCondition();
conditionalFormat.FormatType = ExcelCFTYPE.ICONSET;
iconSet = conditionalFormat.ICONSET;
iconSet.ICONSET = ExcelICONSETTYPE.ThreeSymbols;
iconSet.ICONCriteria[0].Type = CONDITIONVALUETYPE.LOWESTVALUE;
iconSet.ICONCriteria[0].Value = "0";
iconSet.ICONCriteria[1].Type = CONDITIONVALUETYPE.HIGHESTVALUE;
iconSet.ICONCriteria[1].Value = "0";
iconSet.ShowIconOnly = true;
```

### Setting Color Scale Conditional Formatting

The following code snippet shows how to apply a color scale conditional format for a different range of cells.

```csharp
//Sets Color scale conditional format type
conditionalFormats = worksheet.Range["D7:D46"].ConditionalFormats;
conditionalFormat = conditionalFormats.AddCondition();
conditionalFormat.FormatType = ExcelCFTYPE.ColorScale;
IColorScale colorScale = conditionalFormat.ColorScale;

//Sets 3 - color scale.
colorScale.SetConditionCount(3);

colorScale.Criteria[0].FormatColorRGB = Color.FromArgb(230, 197, 218);
colorScale.Criteria[0].Type = CONDITIONVALUETYPE.LOWESTVALUE;
colorScale.Criteria[0].Value = "0";

colorScale.Criteria[1].FormatColorRGB = Color.FromArgb(244, 210, 178);
colorScale.Criteria[1].Type = CONDITIONVALUETYPE.Percentile;
colorScale.Criteria[1].Value = "50";

colorScale.Criteria[2].FormatColorRGB = Color.FromArgb(245, 247, 171);
colorScale.Criteria[2].Type = CONDITIONVALUETYPE.HIGHESTVALUE;
colorScale.Criteria[2].Value = "0";
```

## API Reference

### Members

- **ExcelCFTYPE**
  - ENUMERATION OF CONDITONAL FORMATS TYPES
    - `ExcelCFTYPE.ICONSET`
    - `ExcelCFTYPE.ColorScale`

- **ICONSET**
  - **Properties**
    - `ICONSET`: Type of icon set.
    - `ICONCriteria`: Array of icon criteria.
    - `ShowIconOnly`: Boolean indicating whether only the icon should be shown.

- **ColorScale**
  - **Properties**
    - `Criteria`: Array of color scale criteria.
    - `SetConditionCount`: Method to set the number of conditions in the color scale.

### ConditionVALUETYPE

- ENUMERATION OF VALUE TYPES FOR CRITERIA
  - `LOWESTVALUE`
  - `PERCENTILE`
  - `HIGHESTVALUE`

## Tags and Keywords

<!-- tags: Excel, ConditionalFormatting, IconSet, ColorScale, Worksheet, Range, SyncfusionWinforms SDK keywords: xlsio, conditional formatting, icon set, color scale, excel, cells, worksheet operations, winforms -->
```