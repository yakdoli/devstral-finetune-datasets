```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_094.jpeg
document_name: diagram
page_number: 094
page_id: diagram#page_094
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:14:20Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Palette
| Palette | Indicates the loaded palette is in palette view. |
| --- | --- |

## Methods
| Method | Description |
| --- | --- |
| LoadPalette | Loads given Symbol Palette to the PaletteGroupView. |

## Events for PaletteGroupBar and GroupView
The important events of the PaletteGroupBar and GroupView with their descriptions are given in the below table.

| Event | Description |
| --- | --- |
| Click | Occurs when component is clicked. |
| DoubleClick | Occurs when the component is double-clicked. |
| GroupViewItemHighlighted | Event fired when an item in the GroupView control is highlighted. |
| GroupViewItemSelected | Event fired when an item in the GroupView control is selected. |
| GroupViewItemReordered | Event fired after the GroupView control items have been reordered by a drag-and-drop operation. |
| GroupViewItemRenamed | Event fired after an in-place rename operation. |
| ShowContextMenu Event | Event fired when the right mouse button is clicked over the control. |

## Programming the Properties
Programmatically, the properties can be set as follows.

### C#
```csharp
paletteGroupBar1.AllowDrop = true;
paletteGroupBar1.Controls.Add(paletteGroupView1);
paletteGroupBar1.Controls.Add(paletteGroupView2);
paletteGroupBar1.Dock = System.Windows.Forms.DockStyle.Left;
paletteGroupBar1.EditMode = false;
paletteGroupBar1.GroupBarItems.AddRange(new
Syncfusion.Windows.Forms.Tools.GroupBarItem[]
    { groupBarItem1, groupBarItem2 });
```

## Footer
© 2013 Syncfusion. All rights reserved. Page 94
```

<!-- tags: [syncfusion winforms, palette, palettegroupbar, groupview, event handling] keywords: [palettegroupbar, groupview, events, properties, programming, syncfusion, windows forms, allowdrop, editmode, dockstyle] -->
```