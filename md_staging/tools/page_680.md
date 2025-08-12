```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_680.jpeg
document_name: tools
page_number: 680
page_id: tools#page_680
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:28:02Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates how to create and configure `SplitContainerAdv` controls in VB.NET and C#.
- Explains the customization of the control's appearance and behavior.

## Content

### Code Examples

```vb
[VB.NET]
Me.splitContainerAdv1 = New Syncfusion.Windows.Forms.Tools.SplitContainerAdv()
Me.Controls.Add(Me.splitContainerAdv1)
```

```csharp
this.splitContainerAdv1.BackColor = System.Drawing.Color.AliceBlue;
this.splitContainerAdv1.Location = new System.Drawing.Point(64, 48);
this.splitContainerAdv1.Size = new System.Drawing.Size(224, 136);
this.splitContainerAdv1.SplitterDistance = 47;
```

```vb
[VB.NET]
Me.splitContainerAdv1.BackColor = System.Drawing.Color.AliceBlue
Me.splitContainerAdv1.Location = New System.Drawing.Point(64, 48)
Me.splitContainerAdv1.Size = New System.Drawing.Size(224, 136)
Me.splitContainerAdv1.SplitterDistance = 47
```

### Running the Application
- **Run the application**: You will see the `SplitContainerAdv` with two panels in it as shown below.

![Figure 422: SplitContainerAdv Created Programmatically](attachment://image.png)

**Figure 422: SplitContainerAdv Created Programmatically**

### 3.5.6.4.3 Concepts and Features

This section will guide you in getting started with the `SplitContainerAdv` control. It explains all the concepts and features of the control in detail.

#### 3.5.6.4.3.1 SplitContainerAdv
- Provides a detailed explanation of the `SplitContainerAdv` control in VB.NET and C#.

## Page-level Navigation/TOC (if applicable)
- This section provides an introduction to the `SplitContainerAdv` control and its key features.

## Cross References
- See additional controls in the related sections of the documentation.

<!-- tags: [Syncfusion Winforms, SplitContainerAdv, control configuration] keywords: [Windows Forms, SplitContainerAdv, VB.NET, C#, programmatic creation, customization, features] -->
```