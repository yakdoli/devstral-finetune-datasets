```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_217.jpeg
document_name: edit
page_number: 217
page_id: edit#page_217
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:07:56Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- Demonstrates the Gradient Background feature in the Essential Edit control.
- Shows how to set background color for specified ranges of text.
- Explains setting background colors for lines or selected blocks of text.

## Content

### Gradient Background Demo

#### Figure 68: Edit Control with Gradient Background

A sample that demonstrates the Gradient Background feature is available in the below sample installation path.

```
..\My Documents\Syncfusion\EssentialStudio\Version Number\Windows\Edit.Windows\Samples\2.0\Appearance\GradientBackgroundDemo
```

### Setting BackgroundColor for Specified Range of Text

The SetBackgroundColor method is used to set the background color for a specified range of text.

#### Code Example

```csharp
[C#]

this.editControl1.SetBackgroundColor(new Point(1, 1), new Point(9, 9), Color.AliceBlue);
```

```vb.NET
[VB.NET]

Me.editControl1.SetBackgroundColor(New Point(1, 1), New Point(9, 9), Color.AliceBlue)
```

### Setting Background Color for Individual Lines or Selected Blocks of Text

Edit Control allows setting custom background color for individual lines as well as for selected block of text.

---
© 2013 Syncfusion. All rights reserved.
```