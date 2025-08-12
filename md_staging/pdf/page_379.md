```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_379.jpeg
document_name: pdf
page_number: 379
page_id: pdf#page_379
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:49:12Z
fidelity: lossless
-->

## 5.4.4 Register the Syncfusion Gecko Wrapper manually?

**Purpose:** Register the `Syncfusion.GeckoWrapper.dll` for use with the XulRunner-SDK 2.0.

To register the Gecko wrapper manually:

1. Copy the `Syncfusion.GeckoWrapper.dll` to the `Bin` folder of `XulRunner-SDK 2.0`.
2. Register the `Syncfusion.GeckoWrapper.dll` using the following command in the command prompt:
   ```
   regsvr32 Syncfusion.GeckoWrapper.dll
   ```

## 5.4.5 How can we make IE9 to render metafile?

**Purpose:** Convert webpages to searchable metafile format using IE9 by modifying a registry setting.

Webpages can be converted to searchable metafile format using IE9 if the following registry value is set to `(DWORD) 00000001`:

- `HKEY_LOCAL_MACHINE (or HKEY_CURRENT_USER)\SOFTWARE\Microsoft\Internet Explorer\MAIN\FeatureControl\FEATURE_IVIEWOBJECTDRAW_DMLT9_WITH_GDI`

**Note:** This registry setting will not be effective for webpages displayed in IE9 Standards mode.

## 5.5 PDF Grid

### 5.5.1 How to position the background image as a tile?

#### Overview
- Explains how to set the background image to a tiled pattern in the PDF Grid.
- Involves setting the `ImagePosition` property to `PdfGridImagePosition.Tile`.

#### Content
We can position the background image as a tile within the PDF Grid, by setting the property `"ImagePosition"` to `PdfGridImagePosition.Tile`.

```csharp
grid.Rows(1).Cells(3).ImagePosition = 
PdfGridImagePosition.Tile
```

For more information on positioning background images, refer to the section **Background Image Positioning** in `PdfGrid Cell`.

---

<!-- tags: [pdf, grid, background image, tile, Syncfusion] keywords: [Syncfusion, WinForms, PDF Grid, GeckoWrapper, IE9, metafile, ImagePosition, Tile] -->
```