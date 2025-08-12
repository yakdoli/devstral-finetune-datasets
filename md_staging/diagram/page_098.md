```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_098.jpeg
document_name: diagram
page_number: 098
page_id: diagram#page_098
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:14:33Z
fidelity: lossless
-->

## Essential Diagram for Windows Forms

### Overview
- Steps for adding a SaveFileDialog control, setting its Filter, and handling the button click event.
- Integration of the SaveFileDialog control to save palettes in the `.edp` format.

### Content

#### Steps to Add and Configure SaveFileDialog
1. Add a SaveFileDialog control into the form.
2. Set the Filter property of SaveFileDialog as `Essential Diagram Palettes (*.edp)|All files (*. *)`.
3. Add the following lines of code to your button click event.

```csharp
[C#]

if (savePaletteDialog.ShowDialog(this) == DialogResult.OK)
{
    SymbolPalette symbolPalette =
        PaletteGroupBar1.CurrentSymbolPalette;
    string strSavePath = savePaletteDialog.FileName;

    if (symbolPalette != null)
    {
        FileStream fStream = new FileStream(strSavePath,
            FileMode.OpenOrCreate, FileAccess.Write);
        BinaryFormatter formatter = new BinaryFormatter();
        formatter.Serialize(fStream, symbolPalette);
        fStream.Close();
    }
}
```

#### Diagram of Palette GroupBar and Palette GroupView
- **Figure 58:** The image illustrates the layout and components of the Palette GroupBar and Palette Group View, depicted as follows:

    - **Palette Group Bar:** Located at the bottom, showing the categories available in the palette.
    - **Palette Group View:** Displays the contents of the currently selected category from the Palette Group Bar.

### Cross References
- Refer to the section discussing the PaletteGroupBar and PaletteGroupView controls for more details.

<!-- tags: [Syncfusion Winforms, Diagram, PaletteGroupBar, PaletteGroupView] keywords: [SaveFileDialog, Filter, SymbolPalette, serialize, Palette Group Bar, Palette Group View] -->
```
