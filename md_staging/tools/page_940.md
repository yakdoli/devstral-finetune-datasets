```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_940.jpeg
document_name: tools
page_number: 940
page_id: tools#page_940
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:43:44Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- AutoLabel control with a ColorUIControl positioned to "Top"
- Size settings of the AutoLabel control explained
- AutoSize property to enable automatic resizing
- AutoLabel Event section detailing the PropertyChanged event
- C# and VB.NET examples provided for AutoSize property

## Content

### AutoLabel Control

#### Size

This section illustrates the size settings of the AutoLabel control.

The AutoLabel control can be resized using the below given property.

**Figure 603: AutoLabel of the ColorUIControl positioned to "Top"**

![AutoLabel of the ColorUIControl positioned to "Top"](https://github.com/syncfusion/windowsforms-sdk/assets/16747174/f88429eb-ea88-4cce-92c6-e42af86b5931)

**3.5.10.1.3.4 Size**

This section illustrates the size settings of the AutoLabel control.

The AutoLabel control can be resized using the below given property.

| AutoLabel Property | Description |
|---------------------|-------------|
| AutoSize           | Enables automatic resizing based on font size. |

**Note:** This is valid only for label controls that do not wrap text.

### Code Examples

**C#**

```csharp
this.autoLabel1.AutoSize = true;
```

**VB.NET**

```vb
Me.autoLabel1.AutoSize = True
```

### AutoLabel Event

**3.5.10.1.4 AutoLabel Event**

A detailed explanation about the PropertyChanged event is given in the following section.

| AutoLabel Event   | Description |
|-------------------|-------------|
| PropertyChanged    | This event is fired when the LabeledControl, Gap or Position properties change. |

## Cross References

See also: AutoLabel of the ColorUIControl, AutoSize property, PropertyChanged event

<!-- tags: [Windows Forms, AutoLabel, ColorUIControl, AutoSize, PropertyChanged, WinForms, Syncfusion] keywords: [AutoLabel, ColorUIControl, AutoSize, PropertyChanged, Windows Forms, Size settings, VB.NET, C#, Syncfusion, property event, label controls, font size, AutoLabel Event] -->
```