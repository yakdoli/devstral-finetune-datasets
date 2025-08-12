```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_096.jpeg
document_name: diagram
page_number: 096
page_id: diagram#page_096
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:12:44Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

```csharp
groupBarItem1.Client = paletteGroupView1
groupBarItem1.Text = "Basic Shapes"
groupBarItem2.Client = paletteGroupView2
groupBarItem2.Text = "ElectricalSymbols"

paletteGroupView1.ButtonView = True
paletteGroupView1.Location = New System.Drawing.Point(2, 24)
paletteGroupView1.Name = "paletteGroupView1"
paletteGroupView1.Size = New System.Drawing.Size(71, 0)
paletteGroupView1.TabIndex = 0

paletteGroupView1.Text = "paletteGroupView1"

paletteGroupView1.LoadPalette("..\..\..\..\..\Common\Data\Diagram\BasicShapes.edp")
paletteGroupView2.LoadPalette("..\..\..\..\..\Common\Data\Diagram\ElectricalSymbols.edp")
```

## Dynamically add Symbol Palette into PaletteGroupBar

You can add Symbol Palettes into PaletteGroupBar by means of deserializing the palette (*.edp) file dynamically. The PaletteGroupBar control supports `PaletteGroupBar1.AddPalette()` method in order to add a palette into the PaletteGroupBar.

Follow the steps given below for adding symbol palette into PaletteGroupBar:

1. Add OpenFileDialog control into form.
2. Set the `Filter` property of OpenFileDialog as,
   ```
   Essential Diagram Palettes|*.edp|Visio Stencils|*.vss; *.vsx|Visio Drawings(Shapes only)|*.vsd; *.vdx|All files|*.*
   ```
3. Add the following lines of code to your button click event.

### WinForms-specific Conventions
- Control names and namespaces are used exactly, such as `paletteGroupView1`, `groupBarItem1`, and `openPaletteDialog`.
- The code demonstrates interactive file selection and palette addition using the OpenFileDialog.

### Notes
- Ensure that the file paths are correct and accessible for the `LoadPalette` method.
- The example uses `C#` syntax for clarity and compatibility with Syncfusion Winforms.

## Code Examples

```csharp
if (openPaletteDialog.ShowDialog(this) == DialogResult.OK)
{
    SymbolPalette curSymbolPalette;
    FileStream iStream;
    string strFileName = openPaletteDialog.FileName;
    RegexOptions options = RegexOptions.IgnoreCase |
}
```

<!-- tags: [diagram, winforms, palette, palettegroupbar, essentialdiagram, syncfusion] keywords: [symbol palette, openFileDialog, control, palettegroupview, palettegroupbar, deserialization, edp file, visio stencils, OpenFileDialog] -->
```