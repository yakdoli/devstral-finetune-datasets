```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_293.jpeg
document_name: diagram
page_number: 293
page_id: diagram#page_293
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:26:43Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

```csharp
SymbolPalette palette = new SymbolPalette("Palette");
// Add some nodes to the palette.
palette.AppendChild(new Ellipse(0, 0, 100, 100));
palette.AppendChild(new RoundRect(new RectangleF(0, 0, 100, 50, MeasureUnits.Pixel));
palette.AppendChild(new LineConnector(PointF.Empty, new PointF(0, 100)));
// Add the palette to PaletteGroupBar.
paletteGroupBar1.AddPalette(palette);
```

### [VB.NET]

```vbnet
' Create an instance of SymbolPalette.
Dim palette As SymbolPalette = New SymbolPalette("Palette")
' Add some nodes to the palette.
palette.AppendChild(New Ellipse(0, 0, 100, 100))
palette.AppendChild(New RoundRect(New RectangleF(0, 0, 100, 50), MeasureUnits.Pixel))
palette.AppendChild(New LineConnector(PointF.Empty, New PointF(0, 100)))
' Add the palette to PaletteGroupBar.
paletteGroupBar1.AddPalette(palette)
```

## 5.37 How to Get the Undo/Redo Description?

The `HistoryManager` class has an option to get undo or redo description. You can use the `GetUndoDescriptions` or `RedoDescriptions` method to get the desired depth of descriptions available in the history of undo or redo list, respectively. The following code example illustrates this.

### [C#]

```csharp
string[] strDescriptions;
int nDescWanted = 1;
// Gets an undo description from the undo list.
int nDescReturned =
    diagram1.Model.HistoryManager.GetUndoDescriptions(nDescWanted, out strDescriptions);
```

<!-- tags: [product, module, control, api, version?] keywords: [getting started, symbolpalette, undoredo, historymanager, descpalette, palettexample] -->
```