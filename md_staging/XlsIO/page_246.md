```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_246.jpeg
document_name: XlsIO
page_number: 246
page_id: XlsIO#page_246
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:03:56Z
fidelity: lossless
-->

# Section Header (if provided, inferred from visible text)

## Overview
- Instructions on editing group data and location for Sparklines.
- Customization options for Line Weight in line sparkline types.
- Discussion on handling hidden and empty cell settings for Sparklines.

## Content

### Sparkline Group Styling
```csharp
sparklineGroup.FirstPointColor = Color.Green;
sparklineGroup.LastPointColor = Color.DarkOrange;
sparklineGroup.HighPointColor = Color.DarkBlue;
sparklineGroup.LowPointColor = Color.DarkViolet;
sparklineGroup.MarkersColor = Color.Black;
```

### Edit Group Data and Location
MS Excel provides an option to edit the location and group data of an existing Sparklines, by which you can assign a new location or group data for an existing sparklines. XlsIO provides an equivalent API to perform this functionality.

```csharp
[C#]
sparklines.RefreshRanges(dataRange, referenceRange);
```

### Line Weight
MS Excel 2010 provides an exclusive option to customize the Line Weight of the Line Sparkline type. XlsIO provides an API to perform this functionality.

```csharp
[C#]
sparklineGroup.LineWeight = 1.0;
```

#### Known Limitations:
The Line weight can be applied only for the line sparkline type.

### Hidden and Empty Cell Settings
Normally, in a sparkline group data there is a possibility of an empty cell or an hidden cell. MS Excel 2010 provides a dialog box to manage these settings.

![Hidden and Empty cells Settings](https://<image_url>/hidden_and_empty_cells_settings.png)
**Figure 83: Hidden and Empty cells Settings**

## API Reference (if applicable)
- `sparklines.RefreshRanges(dataRange, referenceRange);`: Updates the data range and reference range for an existing sparkline group.
- `sparklineGroup.LineWeight`: Sets the line weight for the Line Sparkline type.
- `sparklineGroup.FirstPointColor`: Specifies the color for the first point in the sparkline.
- `sparklineGroup.LastPointColor`: Specifies the color for the last point in the sparkline.
- `sparklineGroup.HighPointColor`: Specifies the color for the high point in the sparkline.
- `sparklineGroup.LowPointColor`: Specifies the color for the low point in the sparkline.
- `sparklineGroup.MarkersColor`: Specifies the color for the markers in the sparkline.

## Code Examples
```csharp
// Example of setting sparkline group colors
sparklineGroup.FirstPointColor = Color.Green;
sparklineGroup.LastPointColor = Color.DarkOrange;
sparklineGroup.HighPointColor = Color.DarkBlue;
sparklineGroup.LowPointColor = Color.DarkViolet;
sparklineGroup.MarkersColor = Color.Black;

// Example of refreshing sparkline ranges
sparklines.RefreshRanges(dataRange, referenceRange);

// Example of setting line weight
sparklineGroup.LineWeight = 1.0;
```

## Cross References
See also:
- Documentation on working with sparklines in Excel
- References to other XlsIO functionalities for managing and customizing sparklines

## RAG Annotations
<!-- tags: [XlsIO, Sparklines, HiddenCells, LineWeight, ExcelFunctionality] keywords: [sparklineGroup, FirstPointColor, LineWeight, hidden cells, refresh ranges] -->
```
