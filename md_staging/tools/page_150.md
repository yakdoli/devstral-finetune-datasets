```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_150.jpeg
document_name: tools
page_number: 150
page_id: tools#page_150
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:55:24Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

```csharp
Dim captionButton5 As Syncfusion.Windows.Forms.Tools.CaptionButton = New Syncfusion.Windows.Forms.Tools.CaptionButton()
toolTipInfo = new Syncfusion.Windows.Forms.Tools.ToolTipInfo()
captionButton.ImageIndex = 4
captionButton.Name = "Custom Button"
captionButton.Type = Syncfusion.Windows.Forms.Tools.CaptionButtonType.Custom;
captionButton.SuperToolTipInfo = toolTipInfo
captionButton.TransparentImageColor = System.Drawing.Color.Transparent
Me.dockingManager1.CaptionButtons.Add(captionButton)
```

A sample which demonstrates the addition of Custom Caption Buttons is available in the below sample installation path.

```
..My Documents\Syncfusion\EssentialStudio\<Version Number>\Windows\Tools.Windows\Samples\2.0\Docking Package\Custom Caption
```

### Custom Button for Caption Bar in Floating Form

This feature enables you to add custom buttons to the caption bar when an item is in a floating state.

You can now add custom buttons to the caption bar when an item is in a floating state. It is not required to dock the item to use the custom buttons.

**Table 11: Properties Table**

| Property                     | Description                                      | Type      | Data Type | Reference links |
|------------------------------|--------------------------------------------------|-----------|------------|-----------------|
| ShowCustomButtonsInFloating | Specifies whether caption button will be enabled while floating. | -         | Boolean    | NA              |

### Enabling Custom Button for Caption Bar while Floating

To enable custom button for caption bar while floating, set the `ShowCustomButtonsInFloating` property to `true`. By default this is set to `false`.

```csharp
this.dockingManager1.ShowCustomButtonsInFloating = true;
```

<!-- tags: [Syncfusion Winforms, CaptionButton, ToolTipInfo, floating state, Custom Caption Buttons] keywords: [Custom Button, Caption Bar, Docking Package, ShowCustomButtonsInFloating] -->
```