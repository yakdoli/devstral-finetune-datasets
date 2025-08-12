```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_651.jpeg
document_name: tools
page_number: 651
page_id: tools#page_651
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:26:57Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- The GradientPanel control allows customization of its appearance, including setting dashed borders and specifying border colors.
- Automates scrolling functionality by managing scroll bars, margins, and minimum scroll size.
- Automatically adjusts its size based on the contents, controlled by AutoSize and AutoSizeMode properties.

## Content

### GradientPanel Appearance

#### Scroll Settings

When the contents inside the gradient panel exceed the visible area, scroll bars appear. The AutoScroll property must be set to true for this functionality. The margin width for the control during auto scroll is set using the AutoScrollMargin property. The minimum logical size for the auto scroll region is specified with the AutoScrollMinSize property.

```csharp
this.gradientPanel1.AutoScroll = true;
this.gradientPanel1.AutoScrollMargin = new System.Drawing.Size(5, 5);
this.gradientPanel1.AutoScrollMinSize = new System.Drawing.Size(20, 20);
```

```vbnet
Me.gradientPanel1.AutoScroll = True
Me.gradientPanel1.AutoScrollMargin = New System.Drawing.Size(5, 5)
Me.gradientPanel1.AutoScrollMinSize = New System.Drawing.Size(20, 20)
```

### Size properties

The GradientPanel can automatically size itself based on the contents available in the control by enabling the AutoSize property. The mode of resizing can be specified through the AutoSizeMode property. Two options are provided for the AutoSizeMode:

- **GrowOnly**: The control grows as much as necessary to fit its contents but does not shrink smaller than the size specified in the Size property of the control.
- **GrowAndShrink**: The control grows and shrinks to fit its contents, which may result in a size smaller than specified in the Size property.

```csharp
```

### See Also

- GradientPanel Appearance
- 3.5.6.2.4.3 Scroll Settings

---

<!-- tags: [Syncfusion Winforms, GradientPanel, AutoScroll, AutoSizeMode, AutoSize, Windows Forms] keywords: [AutoScrollMargin, AutoScrollMinSize, GradientPanel, AutoSizeMode, AutoScroll, Windows Forms, ScrollBars] -->
``` 
