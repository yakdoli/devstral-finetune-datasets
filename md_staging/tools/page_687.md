```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_687.jpeg
document_name: tools
page_number: 687
page_id: tools#page_687
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:29:23Z
fidelity: lossless
-->

## Overview
- Discusses the appearance settings of `SplitContainerAdv` control in Syncfusion Winforms.
- Demonstrates how to configure various appearance properties such as background, expand lines, and grip colors using C# and VB.NET code examples.
- Focuses on controlling the interactive appearance during runtime, specifically when the mouse hovers over the control.

## Content

### Appearance Settings on Mouse Hovering at Runtime

#### C#

```csharp
this.splitContainerAdv2.HotBackgroundColor = new
  Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.GradientStyle.Horizontal,
    System.Drawing.Color.SandyBrown, System.Drawing.Color.AntiqueWhite);
this.splitContainerAdv2.HotExpandFill = new
  Syncfusion.Drawing.BrushInfo(System.Drawing.Color.Red);
this.splitContainerAdv2.HotExpandLine = System.Drawing.Color.DeepPink;
this.splitContainerAdv2.HotGripDark = new
  Syncfusion.Drawing.BrushInfo(System.Drawing.Color.MistyRose);
this.splitContainerAdv2.HotGripLight = new
  Syncfusion.Drawing.BrushInfo(System.Drawing.Color.Purple);
```

#### [VB.NET]

```vbnet
Me.splitContainerAdv2.HotBackgroundColor = New
  Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.GradientStyle.Horizontal,
    System.Drawing.Color.SandyBrown, System.Drawing.Color.AntiqueWhite)
Me.splitContainerAdv2.HotExpandFill = New
  Syncfusion.Drawing.BrushInfo(System.Drawing.Color.Red)
Me.splitContainerAdv2.HotExpandLine = System.Drawing.Color.DeepPink
Me.splitContainerAdv2.HotGripDark = New
  Syncfusion.Drawing.BrushInfo(System.Drawing.Color.MistyRose)
Me.splitContainerAdv2.HotGripLight = New
  Syncfusion.Drawing.BrushInfo(System.Drawing.Color.Purple)
```

**Figure 427: Appearance Settings on Mouse Hovering at Run Time**

#### 3.5.6.4.3.1.3 Appearance Settings

This section discusses the properties which controls the appearance of the `SplitContainerAdv` control.

#### Background Settings

The below table describes the background settings.

## Background Settings
The below table describes the background settings.

<!-- tags: [syncfusion, winforms, splitcontaineradv, appearance, runtime, hot settings] keywords: [splitcontaineradv, appearance settings, runtime, mouse hovering, background, gradient, expand line, grip colors, brushinfo] -->
```