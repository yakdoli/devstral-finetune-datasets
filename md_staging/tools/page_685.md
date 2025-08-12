```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_685.jpeg
document_name: tools
page_number: 685
page_id: tools#page_685
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:27:34Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- This section covers the usage of `SplitContainerAdv` control properties for customizing the appearance of the `ThumbnailArrow` and spaces the components' splitters.

## Content

### 3.5.6.4.3.1.2.1 Thumbnail Arrow and Grip Settings

SplitContainerAdv control supports various appearance settings for the ThumbnailArrow in the control, which are discussed in detail below. The properties which control the appearance of the splitter components are as follows.

| SplitContainerAdv Properties      | Description                          |
|-----------------------------------|----------------------------------------|
| ExpandFill                        | Sets the color for the arrows.        |
| ExpandLine                        | Sets the outline color for the arrows. |
| GripDark                          | Sets color for the grip.              |
| GridLight                         | Sets the shadow around the grip.      |

#### [C#]
```csharp
this.splitContainerAdv2.ExpandFill = new Syncfusion.Drawing.BrushInfo(System.Drawing.Color.AliceBlue);
this.splitContainerAdv2.ExpandLine = System.Drawing.Color.Red;
this.splitContainerAdv2.GripDark = new Syncfusion.Drawing.BrushInfo(System.Drawing.Color.Wheat);
this.splitContainerAdv2.GripLight = new Syncfusion.Drawing.BrushInfo(System.Drawing.Color.Crimson);
```

#### [VB.NET]
```vb
Me.splitContainerAdv2.ExpandFill = New Syncfusion.Drawing.BrushInfo(System.Drawing.Color.AliceBlue)
Me.splitContainerAdv2.ExpandLine = System.Drawing.Color.Red
Me.splitContainerAdv2.GripDark = New Syncfusion.Drawing.BrushInfo(System.Drawing.Color.Wheat)
Me.splitContainerAdv2.GripLight = New Syncfusion.Drawing.BrushInfo(System.Drawing.Color.Crimson)
```

<!-- tags: [product, module, control, api, version?] keywords: [SplitContainerAdv, ThumbnailArrow, Grip, ExpandFill, ExpandLine, GripDark, GridLight, C#, VB.NET, Windows Forms, 11.4.0.26] -->
```