```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_686.jpeg
document_name: tools
page_number: 686
page_id: tools#page_686
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:28:43Z
fidelity: lossless
 -->

# Essential Tools for Windows Forms

## Overview

This section discusses the appearance settings for the Splitter control in Windows Forms, focusing on how runtime appearance can be customized using specific properties.

## Runtime Appearance

The properties to control the appearance of the thumbnail arrows, and grip, while mouse hovering at runtime, are as follows.

### SplitContainerAdv Properties

| SplitContainerAdv Properties                 | Description                                                                 |
|----------------------------------------------|-----------------------------------------------------------------------------|
| HotBackgroundColor                           | Sets the background color of the Thumbnail while under mouse cursor.      |
| HotExpandFill                                | Sets the color for the arrows while under mouse cursor.                     |
| HotExpandLine                                | Sets the outline color for the arrows while under mouse cursor.            |
| HotGripDark                                  | Sets color for the grip while under mouse cursor.                          |
| HotGridLight                                 | Sets the shadow around the grip while under mouse cursor.                  |

### Code Example

```csharp
this.splitContainerAdv2.HotBackgroundColor = new 
Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.GradientStyle.Horizontal
```

<!-- tags: [syncfusion, winforms, splitcontaineradv, properties, runtimeappearance, splitcontaineradv2] keywords: [splitcontaineradv, hotbackgroundcolor, hotexpandfill, hotexpandline, hotgripdark, hotgridlight] -->
```