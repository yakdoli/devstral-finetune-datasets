```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_782.jpeg
document_name: tools
page_number: 782
page_id: tools#page_782
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:34:26Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- The page discusses properties and methods related to customizing the appearance and behavior of the PercentTextBox control in Windows Forms.
- It covers the ReadOnlyBackColor property, ResetBackColor and ResetReadOnlyBackColor methods, as well as the Foreground color settings for different scenarios.

## Content

### ReadOnlyBackColor property
#### Figure: "ReadOnlyBackColor" property Set
**Note:** The ReadOnly property must be set to `True` for the above setting to take effect.

The methods associated with the above properties are given below.

| Methods                      | Description                                        |
|------------------------------|----------------------------------------------------|
| ResetBackColor               | Resets the BackColor property to its default value. |
| ResetReadOnlyBackColor       | Resets the ReadOnlyBackColor property to its default value. |

### 3.5.8.5.3.5.2 Foreground Settings
The Foreground settings of the PercentTextBox control are discussed below.

#### Foreground Color
The foreground color of the control can be set using the properties given below.

| PercentTextBox Properties | Description                                                      |
|---------------------------|------------------------------------------------------------------|
| PositiveColor             | Gets / sets the forecolor when the current value is positive.  |
| NegativeColor             | Gets / sets the forecolor when the current value is negative. The default value is set to 'Red'. |
| ZeroColor                 | Gets / sets the forecolor when the current value is zero.      |

#### Code Examples

```csharp
this.percentTextBox1.PositiveColor = System.Drawing.Color.ForestGreen;
this.percentTextBox1.NegativeColor = System.Drawing.Color.Orange;
this.percentTextBox1.ZeroColor = System.Drawing.Color.Orchid;
```

```vb.net
' Unfinished VB.NET sample - continue if more is required.
```

## API Reference
- **Properties**
  - `PositiveColor`: Gets / sets the forecolor when the current value is positive.
  - `NegativeColor`: Gets / sets the forecolor when the current value is negative. The default value is set to 'Red'.
  - `ZeroColor`: Gets / sets the forecolor when the current value is zero.

- **Methods**
  - `ResetBackColor`: Resets the BackColor property to its default value.
  - `ResetReadOnlyBackColor`: Resets the ReadOnlyBackColor property to its default value.

## Code Examples (multi-language supported)
The sample code demonstrates how to configure the foreground colors for different value scenarios using C# and VB.NET.

<!-- tags: [winforms, percenttextbox, propertys, methods, foreground color, read only backcolor] keywords: [PercentTextBox, ReadOnlyBackColor, PositiveColor, NegativeColor, ZeroColor, ResetBackColor, ResetReadOnlyBackColor] -->
``` 
``` 

