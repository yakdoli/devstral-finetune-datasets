```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_536.jpeg
document_name: grid
page_number: 536
page_id: grid#page_536
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:22:31Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```csharp
zoomWindow.Location = pt
style.Font.Size = size
End If
Else
Me.zoomWindow.Visible = False
MessageBox.Show("Not a record cell")
End If
End Sub
```

Now when you click any cell, it displays a picture box over the cell showing the cell content in a magnified manner.

**Note:** For more details on this feature, refer the following browser sample:

`<Install Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Windows\Samples\2.0\Zoom and Scrolling\Zoom Grid Demo`

## 4.1.4.32 Tile Image In Grid Cell

**Essential GridControl** supports Tile Image feature in Grid cell.

Set `BackgroundImageMode` property to `GridBackgroundImageMode.TileImage` to add title image in grid cell.

The following code illustrates how to add **Tile Image** feature in Grid cell.

### C#

```csharp
this.gridControl1[2, 2].BackgroundImageMode = GridBackgroundImageMode.TileImage;
```

### VB

```vb
Me.gridControl1(2, 2).BackgroundImageMode = GridBackgroundImageMode.TileImage
```

When the code runs, the following image displays.

---

© 2013 Syncfusion. All rights reserved.
```