```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_947.jpeg
document_name: tools
page_number: 947
page_id: tools#page_947
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:45:05Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Explains how to set border sides for GradientLabel using the BorderSides property.
- Describes replacing default border styles with Border3DStyle.
- Details 3D border styles (Raised, Sunken, Flat, etc.) and the 'Adjust' setting for no border.
- Discusses the foreground settings of the GradientLabel control.

## Content

We can set the border sides for the GradientLabel using the **BorderSides** property. If **BorderSides** is set to 'Left', only the left border of GradientLabel will be shown.

The GradientLabel replaces the default border style provided for Label classes with the **Border3DStyle** type in this property. This property uses the **Border3DStyle** enumeration.

In 3D mode, the border styles can be Raised, Sunken, Flat and so on. Setting the value to 'Adjust' shows no border.

### Code Examples

#### C#

```csharp
this.gradientLabel1.BorderSides = System.Windows.Forms.Border3DSide.Top;
this.gradientLabel1.BorderStyle = System.Windows.Forms.Border3DStyle.Flat;
this.gradientLabel1.BorderColor = Color.Red;
```

#### VB.NET

```vbnet
Me.gradientLabel1.BorderSides = System.Windows.Forms.Border3DSide.Top
Me.gradientLabel1.BorderStyle = System.Windows.Forms.Border3DStyle.Flat
Me.gradientLabel1.BorderColor = Color.Red
```

**Figure 608: Border Settings of GradientLabel**

![Figure 608: Border Settings of GradientLabel](https://i.imgur.com/887UzUG.png)

### 3.5.10.2.3.2 Foreground Settings

This section illustrates the foreground settings of the GradientLabel control.

#### DrawActiveWhenDisabled

Disabled text can be drawn active using the below given property.

| GradientLabel Property      | Description                   |
|-----------------------------|-------------------------------|
| DrawActiveWhenDisabled      | Property for enabling disabled text to appear active. |

## API Reference (if applicable)

None specified in the given content.

## Code Examples (multi-language supported)

Already provided in the content section.

## Cross References

None specified in the given content.

## Page-level Navigation/TOC (if applicable)

None specified in the given content.

### RAG Annotations

<!-- tags: [gradientlabel, bordersides, border3dstyle, 3dborderstyles, drawactivewhendisabled, foregroundsettings, syncfusion winforms, version: 11.4.0.26] keywords: [gradientlabel, border sides, border3dstyle, raised, sunken, flat, adjust, disabled text, active, foreground settings] -->
```