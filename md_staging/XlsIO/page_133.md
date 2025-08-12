```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_133.jpeg
document_name: XlsIO
page_number: 133
page_id: XlsIO#page_133
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:57:24Z
fidelity: lossless
-->

### Color Pallet

Excel supports colors for fonts and background fills through what is called the **Color Pallet**. The Pallet is an array or series of 56 RGB colors. The value of each of those 56 colors may be any of the 16 million available colors, but the Pallet, and thus the number of distinct colors in a workbook, is limited to 56 colors. The RGB values in the Pallet are accessed by the **ColorIndex** property. The ColorIndex is an offset or index in the Pallet, and thus has a value between 1 and 56. In the default, unmodified Pallet, the 3rd element in the Pallet is the RGB value 255 (&HFF), which is red.

When you format a cell's background to red, for example, you are actually assigning to the **ColorIndex** property of the Interior a value of 3. Excel reads the 3 in the ColorIndex property, and goes to the 3rd element of the Pallet to get the actual RGB color. If you modify the Pallet, say by changing the 3rd element from red (255 = &HFF) to blue (16,711,680 = &HFF0000), all items that were once red are changed to blue. This is because the value of the 3rd element in the Pallet has been changed from red to blue, while the ColorIndex property remains equal to 3.

You can change the values in the default pallet by modifying the **Colors** array of the workbook. You can also get the colors in the palette by using the **Palette** property.

### Colors in XlsIO

XlsIO provides support for adding new colors to the color palette that are not available in the standard MS Excel color palette, by using the **SetPaletteColor** method. If you have modified as workbook's Pallet, you can reset the pallet back to the default values, by using the **ResetPalette** method.

The following code example illustrates how to set the color palette.

```csharp
// Creating color palette.
string[] known = Enum.GetNames(
    typeof(KnownColor)
);
Color[] palette = workbook.Palette;

for (int i = (int)ExcelKnownColors.Custom0; i < palette.Length; i++)
{
    KnownColor value = (KnownColor)Enum.Parse(
      typeof(KnownColor),
      known[i]
    );
    workbook.SetPaletteColor(
      i, Color.FromKnownColor(value)
    );
}

palette = workbook.Palette;
```

<!-- tags: [XlsIO, Color Palette, ColorIndex, SetPaletteColor, ResetPalette] keywords: [color, excel, color index, palette, workbook, red, blue, backgroundColor, knownColor, miscellaneous colors] -->
```