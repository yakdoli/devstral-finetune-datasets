```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_673.jpeg
document_name: tools
page_number: 673
page_id: tools#page_673
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:26:54Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- A detailed explanation of the `GradientPanelExt` control with customized properties.
- Focus on customizing the foreground color and rounded corners of the panel.
- Includes programming examples in C# and VB.NET.

## Content

### 3.5.6.3.3.4 Border Settings

#### Corner Radius

The `GradientPanelExt` comes as a rounded rectangle by default. The rounded corners can be removed or their radius can be modified using the `CornerRadius` property.

#### GradientPanelExt Property: CornerRadius

| GradientPanelExt Property | Description |
|---------------------------|-------------|
| CornerRadius              | Used to set or get the radius truncation for the control's corners. |

#### Code Examples

**[C#]**
```csharp
gradientPanelExt1.CornerRadius = 14;
```

**[VB.NET]**
```vb
Private gradientPanelExt1.CornerRadius = 14
```

### Figure

**Figure 415**: GradientPanelExt with Customized Foreground

![GradientPanelExt with Customized Foreground](image_displayed_here)

## API Reference

### GradientPanelExt

#### Properties

- **CornerRadius**
  - **Type**: `Int`
  - **Description**: Allows setting or getting the radius truncation for the control's corners.
  - **Default Value**: Depends on control default setting.
  - **Required**: No

## RAG Annotations

<!-- tags: [Windows Forms, GradientPanelExt, Corner Radius, Custom Foreground, C#, VB.NET] keywords: [GradientPanelExt, CornerRadius, Customized Foreground, Border Settings, Rounded Corners, WinForms] -->
```