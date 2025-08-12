```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_219.jpeg
document_name: grid
page_number: 219
page_id: grid#page_219
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:03:38Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

A Slider control embedded in a grid cell is termed as a Slider Cell. Slider control can be embedded in the grid cells by using Slider cell type. The class **SliderStyleProperties** provides custom properties specific to the Slider control. All the properties support the style inheritance mechanism.

### Embedding the Slider Control

The Slider control can be embedded by using the following set of codes:

#### Using C#

```csharp
gridControl1.CellModels.Add("Slider", new SliderCellModel(gridControl1.Model));
GridStyleInfo style;
style = gridControl1[4, 5];
SliderStyleProperties sp = new SliderStyleProperties(style);
style.CellType = "Slider";
sp.Maximum = 40;
sp.Minimum = 0;
sp.TickFrequency = 8;
sp.LargeChange = 16;
sp.SmallChange = 4;
sp.Orientation = Orientation.Vertical;
```

#### Using VB.NET

```vb.net
gridControl1.CellModels.Add("Slider", New SliderCellModel(gridControl1.Model))
Dim style As GridStyleInfo
style = gridControl1(4, 5)
Dim sp As SliderStyleProperties = New SliderStyleProperties(style)
style.CellType = "Slider"
sp.Maximum = 40
sp.Minimum = 0
sp.TickFrequency = 8
sp.LargeChange = 16
sp.SmallChange = 4
sp.Orientation = Orientation.Vertical
```

---

<!-- tags: [product, grid, slider control, slider cell, slider style properties, winforms] keywords: [slidercontrol, grid cell embedding, custom properties, style inheritance, csharp, vb.net, orientation] -->
```