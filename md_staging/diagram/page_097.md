```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_097.jpeg
document_name: diagram
page_number: 097
page_id: diagram#page_097
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:15:01Z
fidelity: lossless
-->

## Essential Diagram for Windows Forms

```csharp
RegexOptions.RightToLeft;
Match match = Regex.Match(strFileName, ".vss|.vsx|.vsd|.vdx", options);
if (match.Success)
{
    VisioStencilConverter converter = new VisioStencilConverter(strFileName, this);
    converter.ShowProgressDialog = true;
    curSymbolPalette = converter.Convert();
    if (curSymbolPalette != null)
        PaletteGroupBar1.AddPalette(curSymbolPalette);
}
else
{
    try
    {
        iStream = new FileStream(strFileName, FileMode.Open, FileAccess.Read);

        // Deserialize the Binary format
        IFormatter formatter = new BinaryFormatter();
        AppDomain.CurrentDomain.AssemblyResolve += new ResolveEventHandler(DiagramBaseAssembly.AssemblyResolver);
        curSymbolPalette = (SymbolPalette)formatter.Deserialize(iStream);
        PaletteGroupBar1.AddPalette(curSymbolPalette);
    }
    catch (Exception se)
    {
        MessageBox.Show(this, se.Message);
    }
    finally
    {
        iStream.Close();
    }
}
}
```

### Saving the active Palette

You can save the current active palette of PaletteGroupBar window by means of serializing the palette (.edp) file. The `PaletteGroupBar.CurrentSymbolPalette` property returns the currently selected symbol palette.

Follow the steps given below for saving current symbol palette

---

``` 
© 2013 Syncfusion. All rights reserved. 
```
``` 
Page 97 |
``` 
``` 
Page 
```
``` 
``` 
© 2013 Syncfusion. All rights reserved. 
```
Page 97 | 11
```

<!-- tags: [Syncfusion, Windows Forms, Diagram, EssentialDiagram, Palette, SymbolPalette, VisioStencilConverter, AssemblyResolver, Deserialization, serialization, edp file, Windows Forms, Control, Properties, Methods, Events, WinForms, Package, Version] keywords: [Essential Diagram, Windows Forms, PaletteGroupBar, CurrentSymbolPalette, Deserialize, Serialize, vss, vsx, vsd, vdx, Stream, Exception handling, PaletteGroupBar, ShowProgressDialog, SymbolPalette, BinaryFormatter, AssemblyResolver, Deserialization, Serialization, Active Palette, WinForms, Control, Properties, Methods, Events, Windows Forms, Package, Version] -->
``` 
