```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_149.jpeg
document_name: tools
page_number: 149
page_id: tools#page_149
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:54:23Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Explains how to add and customize caption buttons in the CaptionButton Collection Editor.
- Demonstrates both design-time and runtime methods for managing caption buttons.

## Content

### CaptionButton Customization

In the CaptionButton Collection Editor, click "Add" to add a new caption button. To customize the caption button, modify the properties provided to the right of the members in the editor.

#### Designer View
<figure>
  <img src="captionbutton_editor.png" alt="CaptionButton Collection Editor" />
  <figcaption>Figure 65: CaptionButton Collection Editor</figcaption>
</figure>

This can be done programmatically using the below code snippets.

### Code Examples

#### C#

```csharp
Syncfusion.Windows.Forms.Tools.CaptionButton captionButton = new 
Syncfusion.Windows.Forms.Tools.CaptionButton();
toolTipInfo = new Syncfusion.Windows.Forms.Tools.ToolTipInfo();
captionButton.ImageIndex = 4;
captionButton.Name = "Custom Button";
captionButton.Type = Syncfusion.Windows.Forms.Tools.CaptionButtonType.Custom;
captionButton.SuperToolTipInfo = toolTipInfo;
captionButton.TransparentImageColor = System.Drawing.Color.Transparent;
this.dockingManager1.CaptionButtons.Add(captionButton);
```

#### VB.NET

```vb
Dim captionButton As New Syncfusion.Windows.Forms.Tools.CaptionButton()
Dim toolTipInfo As New Syncfusion.Windows.Forms.Tools.ToolTipInfo()
captionButton.ImageIndex = 4
captionButton.Name = "Custom Button"
captionButton.Type = Syncfusion.Windows.Forms.Tools.CaptionButtonType.Custom
captionButton.SuperToolTipInfo = toolTipInfo
captionButton.TransparentImageColor = System.Drawing.Color.Transparent
Me.dockingManager1.CaptionButtons.Add(captionButton)
```

## Page-level Navigation/TOC (if applicable)

- [Unclear]

<!-- tags: [syncfusion, winforms, captionbutton, designertool, customization, programming] keywords: [captionbutton, collectioneditor, designer, codeexample, csharp, vb.net] -->
``` 
