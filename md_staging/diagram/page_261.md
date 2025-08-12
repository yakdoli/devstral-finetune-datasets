```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_261.jpeg
document_name: diagram
page_number: 261
page_id: diagram#page_261
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:24:48Z
fidelity: lossless
-->

## Essential Diagram for Windows Forms

### 5.8 How To Copy / Paste Nodes In Essential Diagram

The following code snippet illustrates how you can copy / paste nodes (symbol, shape, or link) in Essential Diagram.

#### C#

```csharp
//Copy Code
this.diagram1.Controller.Copy();

//Paste Code
//If the data in the clipboard is of the type ClipboardNodeCollection,
//paste it onto the Diagram.
IDataObject clipboardData = Clipboard.GetDataObject();
if (clipboardData.GetDataPresent(typeof(ClipboardNodeCollection)))
{
    this.diagram1.Controller.Paste();
}
```

#### VB.NET

```vb.net
'Copy Code
Me.diagram1.Controller.Copy()

'Paste Code
'If the data in the clipboard is of the type ClipboardNodeCollection,
'paste it onto the Diagram.
Dim clipboardData As IDataObject = Clipboard.GetDataObject()
If clipboardData.GetDataPresent(Type.GetType("ClipboardNodeCollection"))
Then
    Me.diagram1.Controller.Paste()
End If
```

### 5.9 How To Create a Connection Programatically
```html
<!-- tags: [Essential Diagram, WinForms, Copy Paste Nodes, ClipboardNodeCollection, Controller, Paste] keywords: [C#, VB.NET, Diagram, Nodes, Connections, Clipboard, DataObject, GetDataPresent, GetType] -->
```