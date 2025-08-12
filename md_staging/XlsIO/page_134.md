```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_134.jpeg
document_name: XlsIO
page_number: 134
page_id: XlsIO#page_134
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:56:13Z
fidelity: lossless
-->

## Overview

- Demonstrates setting and retrieving color palette settings in Excel sheets using the XlsIO library.
- Focuses on iterating through the color palette and setting styles and text in a spreadsheet.
- Includes examples in both C# and VB.NET.

## Content

### Working with Color Palette in Excel

The following examples show how to interact with the color palette in Excel using the XlsIO library.

#### C#

```csharp
int pos = 0;
for (int j = 1; j < 100; j++)
{
    for (int i = 1; i <= 3; i++)
    {
        ExcelKnownColors knownEnm = (ExcelKnownColors)pos;
        sheet.Range[j, i].CellStyle.ColorIndex = knownEnm;
        sheet.Range[j, i].Text = palette[pos].Name + ", " +
            string.Format("R{0}:G{1}:B{2}:A{3}", palette[pos].R,
            palette[pos].G, palette[pos].B, palette[pos].A);
        pos++;
        
        if (pos >= palette.Length) break;
    }
    if (pos >= palette.Length) break;
}
```

#### VB.NET

```vb
' Creating color palette.
Dim known As String() = System.Enum.GetNames(GetType(KnownColor))
Dim palette As Color() = workbook.Palette

Dim i As Integer = CInt(ExcelKnownColors.Custom0)

Do While i < palette.Length
    Dim value As KnownColor = CType(System.Enum.Parse(GetType(KnownColor), known(i)), KnownColor)
    workbook.SetPaletteColor(i, Color.FromKnownColor(value))
    i += 1
Loop

palette = workbook.Palette
Dim pos As Integer = 0
For j As Integer = 1 To 99
    For i = 1 To 3
        Dim knownEnm As ExcelKnownColors = CType(pos, ExcelKnownColors)
        sheet.Range(j, i).CellStyle.ColorIndex = knownEnm
        sheet.Range(j, i).Text = palette(pos).Name & ", " &
        String.Format("R{0}:G{1}:B{2}:A{3}", palette(pos).R, palette(pos).G, palette(pos).B, palette(pos).A)
        pos += 1
        
        If pos >= palette.Length Then
            ' Break out of inner loop if necessary.
            Exit For
        End If
    Next
    If pos >= palette.Length Then
        ' Break out of outer loop if necessary.
        Exit For
    End If
Next
```

### Explanation

- **C# Example**:
  - Initializes a `pos` variable to track the current color in the palette.
  - Iterates through rows and columns (limited to three columns per row) using nested `for` loops.
  - Sets the `ColorIndex` of each cell to the corresponding Excel color and displays its name and RGB properties.
  - Breaks out of the loops when all colors in the palette have been processed.

- **VB.NET Example**:
  - Creates a `palette` using the workbook's available colors.
  - Uses a `Do While` loop to populate the `palette` with predefined colors.
  - Iterates through rows and columns, setting the `ColorIndex` of each cell and displaying the color details.
  - Uses `Exit For` to handle the case when all palette colors have been processed.

### Key Points
- Both examples effectively demonstrate how to populate an Excel sheet with color styles and display color information.
- The use of `KnownColors` and `ColorIndex` helps in associating named colors with Excel cells.
- The structured approach ensures that all available colors in the predefined palette are utilized efficiently.

## API Reference

### Methods Used
- `System.Enum.GetNames`: Retrieves the names of the constants in an enumeration.
- `System.Enum.Parse`: Converts the string representation of a enumeration to an actual enumeration value.
- `Color.FromKnownColor`: Creates a Color structure from a KnownColor.
- `sheet.Range[ , ].CellStyle.ColorIndex`: Sets the color index for a specific cell style.
- `sheet.Range[ , ].Text`: Sets the text for a specific cell.

### Properties
- `Palette.Length`: Indicates the number of colors in the palette.

## Code Examples

The examples above provide comprehensive code snippets in both C# and VB.NET for interacting with the color palette in Excel using the XlsIO library. These examples effectively demonstrate setting cell styles, retrieving color information, and iterating through the palette.

## Page-level Navigation/TOC (if applicable)

This section provides examples of setting and retrieving color palette details in Excel using XlsIO. Further exploration can be found in related documentation.

### See also:
- [XlsIO Overview](#xlsio-overview)
- [Working with Cell Styles](#working-with-cell-styles)
- [Handling Excel Colors in XlsIO](#handling-excel-colors-in-xlsio)

<!-- tags: [XlsIO, WinForms, color palette, Excel, sheet, cell styles] keywords: [color, palette, ExcelKnownColors, KnownColor, Palette, ColorIndex, text] -->
```
