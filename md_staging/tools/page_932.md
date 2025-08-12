```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_932.jpeg
document_name: tools
page_number: 932
page_id: tools#page_932
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:43:18Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Adding events to Windows Forms controls.
- Overriding methods to handle specific events.
- Overview of advanced Label controls in Windows Forms.

## Content

### Adding Event

```vb
' Adding event.
Public Event FontSelected As System.EventHandler
```

### Handling Event in Code

2. Override the `OnSelectedIndexChanged` method and fire the event there.

#### C# Implementation

```csharp
protected override void OnSelectedIndexChanged(EventArgs e)
{
    // FontSelected event fires here.
    if(FontSelected!=null) FontSelected(this,e);
    base.OnSelectedIndexChanged (e);
}
```

#### VB.NET Implementation

```vb
Protected Overrides Sub OnSelectedIndexChanged(ByVal e As EventArgs)
    ' FontSelected event fires here.
    RaiseEvent FontSelected(Me, e)
    MyBase.OnSelectedIndexChanged(e)
End Sub
```

### Label Controls

#### 3.5.10 Label Controls

The following are the advanced versions of Windows Label controls.

##### 3.5.10.1 AutoLabel

The AutoLabel control is a label-derived control that lets you pair a label with any other control. Once paired, the AutoLabel will be automatically repositioned as the labeled control's position changes.

![AutoLabel Control](attachment:image1)

### Figure 595: AutoLabel Control

The FlowLayoutPanel layout manager will always treat the AutoLabel-labeled control pair as a unit. You can use AutoLabels and FlowLayouts together to implement complex and powerful form layouts.

### See Also

#### Copyright Notice
© 2013 Syncfusion. All rights reserved.

## Code Examples

```csharp
// Example of using AutoLabel
AutoLabel autoLabel1 = new AutoLabel();
// Pair with another control
// Implementation logic for AutoLabel repositioning
```

```vb
' Example of using AutoLabel
Dim autoLabel1 As New AutoLabel()
' Pair with another control
' Implementation logic for AutoLabel repositioning
```

### Page-level Navigation/TOC (if applicable)
- 3.5.10 Label Controls
  - 3.5.10.1 AutoLabel

### Cross References
- Related controls and features in Windows Forms documentation.

<!-- tags: [windowsforms, labelcontrols, autolabel, customcontrols, eventhandling] keywords: [windows forms, essential tools, autoLabel, label controls, event management, control positioning, complex form layouts] -->
```