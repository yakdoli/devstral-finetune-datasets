```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_135.jpeg
document_name: XlsIO
page_number: 135
page_id: XlsIO#page_135
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:57:01Z
fidelity: lossless
-->

## Color and Pattern Operations

### Getting or Setting the Nearest RGB Color

XlsIO provides the ability to retrieve or set the closest RGB color in the palette using the `SetColorOrGetNearest` method. This method returns the `ColorIndex` value of the color in the Palette that is closest to a given RGBLong color value. The computation of the closest color is performed by treating each RGB color as a point in a 3-dimensional space, with the axes representing the Red, Green, and Blue components. The "closest" color is determined geometrically by calculating the Pythagorean distance (without the square root) between the RGBLong color and each Color in the palette. The `ColorIndex` that minimizes this distance is returned. The distance `Dist` between two colors is calculated as follows:

\[
\text{Dist} = (R1 - R2)^2 + (G1 - G2)^2 + (B1 - B2)^2
\]

Where `R1`, `G1`, and `B1` are the components of RGBLong, and `R2`, `G2`, and `B2` are the components of the Color.

### Applying Patterns to Cells

Excel offers various pattern styles for highlighting cells, which can be applied using the `Pattern` tab in the `Format Cells` dialog box. XlsIO also provides APIs to specify these background pattern styles for a cell. The following C# code example demonstrates how to set the pattern type and color for specific cells:

```csharp
// Setting the Pattern Types.
sheet.Range["A2"].CellStyle.FillPattern = ExcelPattern.Angle;
sheet.Range["A4"].CellStyle.FillPattern = ExcelPattern.DarkDownwardDiagonal;

// Setting the Pattern Color.
sheet.Range["A2"].CellStyle.FillBackground = ExcelKnownColors.Aqua;
sheet.Range["A4"].CellStyle.FillBackground = ExcelKnownColors.Pale_blue;
```

## Summary

1. **Color Matching**: XlsIO allows retrieving or setting the nearest RGB color with a `SetColorOrGetNearest` method, using a geometrical distance calculation.
2. **Pattern Application**: Excel pattern styles can be specified for cells using APIs provided by XlsIO.
3. **Example Code**: Demonstrates setting pattern types and colors programmatically.
---

<!-- tags: [xlsio, color-matching, patterns, cells, visuallysts] keywords: [xlsio, setcolororgetnearest, excelpattern, fillpattern, fillbackground] -->
```