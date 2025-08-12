```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_159.jpeg
document_name: XlsIO
page_number: 159
page_id: XlsIO#page_159
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:58:22Z
fidelity: lossless
-->

# Essential XlsIO

The following VB.NET code snippet demonstrates how to add conditional formatting with a data bar and an icon set for the same cell in a range. Specifically, it shows how to set data bar and icon set attributes, define constraints, and configure color settings.

```vb
'Add condition for the range
Dim formats As IConditionalFormats = sheet.Range("C7:C46").ConditionalFormats
Dim format As IConditionalFormat = formats.AddCondition()

'Set Data bar and icon set for the same cell
'Set the format type
format.FormatType = ExcelCFTypes.DataBar
Dim dataBar As IDataBar = format.DataBar

'Set the constraint
dataBar.MinPoint.Type = ConditionValueType.LowestValue
dataBar.MinPoint.Value = "0"
dataBar.MaxPoint.Type = ConditionValueType.HighestValue
dataBar.MaxPoint.Value = "0"

'Set color for Bar
dataBar.BarColor = System.Drawing.Color.FromArgb(156, 208, 243)

'Hide the value in data bar
dataBar.ShowValue = False

'Add another condition in the same range
format = formats.AddCondition()

'Set Icon format type
format.FormatType = ExcelCFTypes.IconSet
Dim iconSet As IIconSet = format.IconSet
iconSet.IconSet = ExcelIconSetType.FourRating
iconSet.IconCriteria(0).Type = ConditionValueType.LowestValue
iconSet.IconCriteria(0).Value = "0"
iconSet.IconCriteria(1).Type = ConditionValueType.HighestValue
iconSet.IconCriteria(1).Value = "0"
```

## API Reference
- **Namespace**: Excel
- **Class**: `IConditionalFormats`
  - **Methods**
    - `AddCondition()`: Adds a new conditional format to the range.
  - **Properties**
    - `ConditionalFormat`: A representation of the conditional formatting rules for the specified range.
    - `DataBar`: Accessor for setting data bar formatting properties.
    - `FormatType`: Enumerates different formatting types such as data bars and icon sets.
    - `IDataBar`: Represents properties for data bar conditional formatting.
    - `IIconSet`: Represents properties for icon set conditional formatting.
    - **Properties within `IDataBar`**
      - `MinPoint`: Represents the minimum point of a data bar.
      - `MaxPoint`: Represents the maximum point of a data bar.
      - `ShowValue`: Determines whether to show the value within the data bar.
      - `BarColor`: Sets the color of the data bar.
    - **Properties within `IIconSet`**
      - `IconSet`: Enumerates the type of icon set.
      - `IconCriteria`: Represents conditions for individual icons in the set.

## Code Examples
The provided VB.NET code snippet effectively illustrates how to configure data bar and icon set conditional formatting for a specific range of cells. This example highlights the integration of both formatting types within the same range, demonstrating flexibility and control over visual representation in Excel documents.

## Cross References
- Refer to the Excel API documentation for detailed information on `IConditionalFormats`, `IDataBar`, and `IIconSet` classes for additional formatting options.

<!-- tags: [Syncfusion, XlsIO, conditional formatting, VB.NET, data bar, icon set, range formatting] keywords: [conditional formatting, data bar, icon set, range, Excel, VB.NET, IConditionalFormats, IDataBar, IIconSet] -->
```
