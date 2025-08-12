```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_247.jpeg
document_name: XlsIO
page_number: 247
page_id: XlsIO#page_247
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:04:49Z
fidelity: lossless
-->

# Essential XlsIO

XlsIO provides a simple API to implement the above functionality. This is illustrated in the following code.

```csharp
sparklineGroup.DisplayEmptyCellsAs = SparklineEmptyCells.Gaps;
sparklineGroup.DisplayHiddenRC = true;
```

## Display Axis

MS Excel 2010 provides an option to display the axis for the sparklines types. This is illustrated in the following code.

```csharp
sparklineGroup.DisplayAxis = true;
```

### Plot Right to Left

The plotting of Sparklines is done from left to right by default. There is an option available in the Sparkline tools to customize the plotting nature from right to left. XlsIO provides a simple API to perform this functionality.

```csharp
sparklineGroup.PlotRightToLeft = true;
```

### Clear

XlsIO provides an API to clear the selected Sparklines within the sparkline groups and also the selected sparklinegroup within the excel spreadsheet. This is illustrated in the following code.

```csharp
// Clears the sparkline group from the sheet.
sheet.SparklineGroups.Remove(sparklineGroup);
// Clears the Sparkline from the sparklines.
sparklines.Remove(sparkline);
```

## API Reference
- Properties: DisplayEmptyCellsAs, DisplayHiddenRC, DisplayAxis, PlotRightToLeft
- Methods: Remove

<!-- tags: [XlsIO, Essential XlsIO, Sparklines, MS Excel, display axis, plot right to left, clear sparklines] keywords: [sparklineGroup, DisplayEmptyCellsAs, DisplayHiddenRC, DisplayAxis, PlotRightToLeft, Remove] -->
```