```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_414.jpeg
document_name: tools
page_number: 414
page_id: tools#page_414
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:12:27Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview

- 1. **Border3DStyle**: Configures the 3D border style for the MonthCalendarAdv control when **BorderStyle=Fixed3D**.
- 2. **BorderSides**: Defines which sides of a control can have a border.
- 3. **BorderColor**: Specifies the 2D border color for controls with **BorderStyle="FixedSingle"**.

## Content

| Property            | Description                                                                                                                                                                                                                                                                                                                                                                               |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Border3DStyle**   | Sets the 3D border style for the MonthCalendarAdv control, when the **BorderStyle=Fixed3D**. The styles include: <br> <br> **Raised**, <br> **RaisedOuter**, <br> **RaisedInner**, <br> **Sunken (default)**, <br> **SunkenOuter**, <br> **SunkenInner**, <br> **Etched**, <br> **Bump**, <br> **Adjust**, <br> **Flat**. |
| **BorderSides**     | Specifies the sides of the control which can have a border. The options for sides are: <br> **Left**, <br> **Top**, <br> **Right**, <br> **Bottom**, <br> **Middle**, <br> **All (default)**.                                                                                                                                         |
| **BorderColor**     | Specifies the 2D border color when **BorderStyle="FixedSingle"**.                                                                                                                                                                                                                                                           |

## Code Examples

```csharp
// Setting 3D border style
this.monthCalendarAdv1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
// Setting "SunkenInner" 3D border style
this.monthCalendarAdv1.Border3DStyle = System.Windows.Forms.Border3DStyle.SunkenInner;
```

## RAG Annotations
<!-- tags: [WinForms, MonthCalendarAdv, Border3DStyle, BorderSides, BorderColor, BorderStyle] keywords: [3D border style, 2D border color, border options, MonthCalendarAdv, Style Settings] -->
```