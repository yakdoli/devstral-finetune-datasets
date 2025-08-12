```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_207.jpeg
document_name: edit
page_number: 207
page_id: edit#page_207
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:06:23Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- Explains how to set the border style for controls.
- Details properties for customizing graphics in the Edit Control.

## Content

### Border Style Example

#### C#
```csharp
this.editControl1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
```

#### VB.NET
```vb
Me.editControl1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
```

### 4.9.1.5 Graphics Customization Settings

The following properties can be used to set the composition quality, interpolation mode, and smoothing mode for images added to the Edit Control. The rendering hint can also be set for text added to the Edit Control.

| Edit Control Property                | Description                                                                 |
|---------------------------------------|-----------------------------------------------------------------------------|
| GraphicsCompositingQuality            | Specifies image composition quality. The options provided are as follows: |
|                                       | - Invalid                                                                  |
|                                       | - Default                                                                  |
|                                       | - HighSpeed                                                                |
|                                       | - HighQuality                                                              |
|                                       | - GammaCorrected                                                           |
|                                       | - AssumeLinear                                                             |
| GraphicsInterpolationMode             | Specifies the interpolation mode. The options provided are as follows:    |
|                                       | - Invalid                                                                  |
|                                       | - Default                                                                  |
|                                       | - Low                                                                      |
|                                       | - High                                                                     |
|                                       | - Bilinear                                                                 |
|                                       | - Bicubic                                                                  |
|                                       | - NearestNeighbor                                                          |
|                                       | - HighQualityBilinear                                                      |
|                                       | - HighQualityBicubic                                                       |
| GraphicsSmoothingMode                 | Specifies the smoothing mode. The options provided are as follows:        |
|                                       | - Invalid                                                                  |
|                                       | - Default                                                                  |

## Page-level Navigation/TOC (if applicable)
- [More advanced graphics settings](#more-advanced-graphics-settings)
- [Example usage with images](#example-usage-with-images)

## Cross References
- See also: [Image rendering hints](#image-rendering-hints)

## Code Examples (multi-language supported)
```csharp
using System;
using System.Windows.Forms;

class Program
{
    static void Main()
    {
        var form = new Form();
        var editControl = new Syncfusion.EditControl();
        form.Controls.Add(editControl);

        // Set GraphicsCompositingQuality
        editControl.GraphicsCompositingQuality = System.Drawing.Drawing2D.CompositingQuality.HighQuality;

        form.ShowDialog();
    }
}
```

### Note: 
This example demonstrates how to set the `GraphicsCompositingQuality` property to enhance image rendering in the `Syncfusion.EditControl`.

## RAG Annotations
<!-- tags: windowsforms, editcontrol, graphicsquality, controls, properties, interpolationkeywords: graphicscompositingquality, graphicsinterpolationmode, graphicssmoothingmode, imagecomposition, interpolationmodes -->
```