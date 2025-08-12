```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_725.jpeg
document_name: tools
page_number: 725
page_id: tools#page_725
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:29:37Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview

- Explains how to style the `DomainUpDownExt` control in Windows Forms using properties like `BorderStyle`, `Border3DStyle`, `BorderSides`, `BorderColor`, and `BackColor`.
- Demonstrates both C# and VB.NET code examples for customizing the appearance of the control.
- Describes the events related to the `DomainUpDownExt` control.

## Content

### Styling the DomainUpDownExt Control

**C#**
```csharp
this.domainUpDownExt1.BorderStyle =
    System.Windows.Forms.BorderStyle.FixedSingle;
this.domainUpDownExt1.Border3DStyle =
    System.Windows.Forms.Border3DStyle.Bump;
this.domainUpDownExt1.BorderSides =
    System.Windows.Forms.Border3DSide.Right;
this.domainUpDownExt1.BorderColor =
    System.Drawing.Color.DodgerBlue;
this.domainUpDownExt1.BackColor =
    System.Drawing.Color.AntiqueWhite;
```

**VB.NET**
```vbnet
Me.domainUpDownExt1.BorderStyle =
    System.Windows.Forms.BorderStyle.FixedSingle
Me.domainUpDownExt1.Border3DStyle =
    System.Windows.Forms.Border3DStyle.Bump
Me.domainUpDownExt1.BorderSides =
    System.Windows.Forms.Border3DSide.Right
Me.domainUpDownExt1.BorderColor =
    System.Drawing.Color.DodgerBlue
Me.domainUpDownExt1.BackColor =
    System.Drawing.Color.AntiqueWhite
```

#### Figures

- **Figure 456: DomainUpDownExt Control with Border Settings**
  ![Figure 456: DomainUpDownExt Control with Border Settings](image_url)
  - The picture shows the styled `DomainUpDownExt` control with a "Bump" 3D border style and a "DodgerBlue" border color.

- **Figure 457: BackColor = "AntiqueWhite"**
  ![Figure 457: BackColor = "AntiqueWhite"](image_url)
  - The picture shows the background color of the `DomainUpDownExt` control set to "AntiqueWhite".

### 3.5.8.2.4 DomainUpDownExt Events

This section describes the events of the `DomainUpDownExt` control.

#### DomainUpDownExt Events

| DomainUpDownExt Events | Description |
|------------------------|-------------|
|                        |             |

<!-- tags: [windowsforms, domainupdownext, border, style, event Handling] keywords: [DomainUpDownExt, BorderStyle, Border3DStyle, BorderSides, BorderColor, BackColor] -->
```