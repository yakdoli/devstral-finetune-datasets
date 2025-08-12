```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_157.jpeg
document_name: XlsIO
page_number: 157
page_id: XlsIO#page_157
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:59:08Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Demonstrates how to set Data bar and Icon sets for the same cell in Excel using conditional formatting.

## Content

### Setting Data Bar and Icon Set for the Same Cell

#### Code Example

```csharp
// Set Data bar and icon set for the same cell
// Set the conditionalFormat type
conditionalFormat.FormatType = ExcelCFTType.DataBar;
IDataBar dataBar = conditionalFormat.DataBar;

// Set the constraint
dataBar.MinPoint.Type = ConditionValueType.LowestValue;
dataBar.MinPoint.Value = "0";
dataBar.MaxPoint.Type = ConditionValueType.HighestValue;
dataBar.MaxPoint.Value = "0";

// Set color for Bar
dataBar.BarColor = Color.FromArgb(156, 208, 243);

// Hide the value in data bar
dataBar.ShowValue = false;

dataBar.MaxPoint = new ConditionValue(ConditionValueType.HighestValue, "0");
dataBar.BarColor = Color.Red;
dataBar.ShowValue = false;

// Add another condition in the same range
conditionalFormat = conditionalFormats.AddCondition();

// Set Icon conditionalFormat type
conditionalFormat.FormatType = ExcelCFTType.IconSet;
IIconSet iconSet = conditionalFormat.IconSet;
iconSet.IconSet = ExcelIconSetType.FourRating;
iconSet.IconCriteria[0].Type = ConditionValueType.LowestValue;
iconSet.IconCriteria[0].Value = "0";
iconSet.IconCriteria[1].Type = ConditionValueType.HighestValue;
iconSet.IconCriteria[1].Value = "0";
iconSet.ShowIconOnly = true;
```

## API Reference

- **Types**
  - `ExcelCFTType`
  - `IDataBar`
  - `ConditionValueType`
  - `ConditionValue`
  - `IIconSet`
  - `ExcelIconSetType`

## Code Examples

The provided code demonstrates how to configure conditional formatting in Excel to display data bars and icons for the same cell. It shows how to set constraints, colors, and visibility properties for the data bar, as well as how to configure an icon set for the same range.

## Cross References

See also: 
- Conditional Formatting in Excel
- Data Bar and Icon Set Features

<!-- tags: [XlsIO, conditional formatting, data bar, icon set, ExcelCFTType, IIconSet, ExcelIconSetType] keywords: [conditional formatting, data bar, icon set, lowest value, highest value, show value, color, range, Excel] -->
```