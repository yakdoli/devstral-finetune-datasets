```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_172.jpeg
document_name: grid
page_number: 172
page_id: grid#page_172
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:00:32Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates how to configure slider properties for a grid control.
- Includes C# and VB.NET code examples for setting slider properties.
- Discusses configuring slider behavior such as maximum, minimum, tick frequency, large change, and small change.

## Content

### Slider Properties Configuration

#### C# Code Example
```csharp
// Set Slider Properties.
sp.Maximum = 40;
sp.Minimum = 0;
sp.TickFrequency = 8;
sp.LargeChange = 16;
sp.SmallChange = 4;
```

#### VB.NET Code Example
```vb
' Set up a Slider control.
Dim style As GridStyleInfo = gridControl1(row, 3)
Dim sp As SliderStyleProperties = New SliderStyleProperties(style)
style.CellType = "Slider"

' Set Slider Properties.
sp.Maximum = 40
sp.Minimum = 0
sp.TickFrequency = 8
sp.LargeChange = 16
sp.SmallChange = 4
```

#### Slider Cells Visualization
![Slider Cells](https://example.com/image-url)

**Figure 91: Slider Cells**

### Static Behavior

#### Section Heading
4.1.4.1.16 Static

## API Reference

None specified in the provided text.

## Code Examples

#### C# Code Example
```csharp
// Set Slider Properties.
sp.Maximum = 40;
sp.Minimum = 0;
sp.TickFrequency = 8;
sp.LargeChange = 16;
sp.SmallChange = 4;
```

#### VB.NET Code Example
```vb
' Set up a Slider control.
Dim style As GridStyleInfo = gridControl1(row, 3)
Dim sp As SliderStyleProperties = New SliderStyleProperties(style)
style.CellType = "Slider"

' Set Slider Properties.
sp.Maximum = 40
sp.Minimum = 0
sp.TickFrequency = 8
sp.LargeChange = 16
sp.SmallChange = 4
```

## RAG Annotations
<!-- tags: [syncfusion, winforms, grid, slider, properties] keywords: [slider properties, grid control, cell type, maximum, minimum, tick frequency, large change, small change, c#, vb.net, essential grid, windows forms] -->
``` 
