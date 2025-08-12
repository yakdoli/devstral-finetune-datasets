```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_671.jpeg
document_name: tools
page_number: 671
page_id: tools#page_671
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:28:19Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- The document discusses the use of the `GradientPanelExt` control with a focus on setting background colors and images.
- Users can programmatically configure the `GradientPanelExt` control's layout and appearance using C# and VB.NET code snippets.

## Image Settings

A background image can be set for the gradient panel using the `BackgroundImage` property. Users can set the layout for the background image using the `BackgroundImageLayout` property. These properties can be set programmatically using the following code snippets.

### C#
```csharp
gradientPanelExt1.BackgroundImage = 
    ((System.Drawing.Image)(resources.GetObject("gradientPanelExt1.BackgroundImage")));
gradientPanelExt1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
```

### VB.NET
```vb
Private Me.gradientPanelExt1.BackgroundImage = 
    CType(resources.GetObject("gradientPanelExt1.BackgroundImage"), System.Drawing.Image)
Private Me.gradientPanelExt1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
```

### Figure: GradientPanelExt with BackgroundColor Set
![GradientPanelExt with BackgroundColor Set](image.jpg)

## API Reference

### Methods
- `SetGradientPanelExtBackgroundImage`: Sets the background image for the `GradientPanelExt` control.
- `SetGradientPanelExtBackgroundImageLayout`: Sets the layout of the background image for the `GradientPanelExt` control.

## Code Examples

### Example: Setting Background Image for GradientPanelExt
```csharp
// C#
gradientPanelExt1.BackgroundImage = 
    ((System.Drawing.Image)(resources.GetObject("gradientPanelExt1.BackgroundImage")));
gradientPanelExt1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
```

### Example: Setting Background Image Layout for GradientPanelExt
```vb
' VB.NET
Private Me.gradientPanelExt1.BackgroundImage = 
    CType(resources.GetObject("gradientPanelExt1.BackgroundImage"), System.Drawing.Image)
Private Me.gradientPanelExt1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
```

## Cross References

See also:
- [GradientPanelExt Documentation](#GradientPanelExt)
- [BackgroundImage Property Reference](#BackgroundImage)
- [BackgroundImageLayout Property Reference](#BackgroundImageLayout)

## RAG Annotations
<!-- tags: [product, module, control, api, version?] keywords: [k1, k2, ...] -->
<!-- tags: syncfusion, windowsforms, gradientpanelext, backgroundimage, backgroundimagelayout, gradientpanel, properties, methods, codeexamples, csharp, vb.net, version:11.4.0.26 -->
```