```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_294.jpeg
document_name: diagram
page_number: 294
page_id: diagram#page_294
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:26:38Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- This section explains how to manage history and descriptions in Windows Forms using Essential Diagram controls.
- Demonstrates using the `HistoryManager` for getting undo and redo descriptions.
- Explains how to import Visio stencils into symbol palettes using the VisioStencilConverter class.

## Content

### History Management
```csharp
// Gets a redo description from the redo list.
nDescReturned =
    diagram1.Model.HistoryManager.GetRedoDescriptions(nDescWanted, out strDescriptions);
```

```vbnet
[VB.NET]

Dim strDescriptions() As String
Dim nDescWanted As Integer = 1
' Gets an undo description from the undo list.
Dim nDescReturned As Integer =
    diagram1.Model.HistoryManager.GetUndoDescriptions(nDescWanted, strDescriptions)
' Gets a redo description from the redo list.
nDescReturned =
    diagram1.Model.HistoryManager.GetRedoDescriptions(nDescWanted, strDescriptions)
```

### Importing Visio Stencils

#### 5.38 How to Import Visio Stencil?
You can import Visio stencils (.vss and .vsx) into symbol palettes. Essential Diagram uses the Visio stencil converter to convert the stencils as the symbol palette. You have to add `Syncfusion.Diagram.Utility.Windows.dll` as a reference in your application to use this converter.

The following code example illustrates how to convert Visio stencils into symbol palettes.

```csharp
[C#]
SymbolPalette paletteToReturn = null;
string strFileName = "Basic Flowchart Shapes.vss";
// Create an instance of VisioStencilConverter
VisioStencilConverter converter = new VisioStencilConverter(strFileName);
converter.ShowProgressDialog = true;
// Convert the stencil as SymbolPalette
paletteToReturn = converter.Convert();
paletteGroupBarl.AddPalette(paletteToReturn);
```

```vbnet
[VB.NET]
```

## API Reference

### Namespaces and Classes
- `Syncfusion.Diagram.HistoryManager`
- `Syncfusion.Diagram.Utility.Windows.VisioStencilConverter`

### Methods
- `GetUndoDescriptions(nDescWanted, strDescriptions)`
- `GetRedoDescriptions(nDescWanted, out strDescriptions)`
- `Convert()`

### Parameters
- `nDescWanted`: The index of the description you want to retrieve.
- `strDescriptions`: An array to hold the undo/redo descriptions.
- `strFileName`: The file name of the Visio stencil to be converted.

## Code Examples

### C# Example
```csharp
SymbolPalette paletteToReturn = null;
string strFileName = "Basic Flowchart Shapes.vss";
 VisioStencilConverter converter = new VisioStencilConverter(strFileName);
converter.ShowProgressDialog = true;
paletteToReturn = converter.Convert();
paletteGroupBarl.AddPalette(paletteToReturn);
```

## RAG Annotations
<!-- tags: [syncfusion, windowsforms, diagram, visio, visiostencils, import, undo, redo, historymanager] keywords: [ Ceddig, diagram1, HistoryManager, GetRedoDescriptions, GetUndoDescriptions, SymbolPalette, VisioStencilConverter, AddPalette, FlowchartShapes.vss, WindowsForms] -->
``` 
