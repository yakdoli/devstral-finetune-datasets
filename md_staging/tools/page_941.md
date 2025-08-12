```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_941.jpeg
document_name: tools
page_number: 941
page_id: tools#page_941
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:43:38Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- The `PropertyChanged` event is triggered when specific properties of the `LabeledControl`, `Gap`, or `Position` change.
- The `GradientLabel` class provides enhanced features for creating visually appealing labels in Windows Forms.

## Content

### 3.5.10.1.4.1 PropertyChanged Event

This event is fired when the `LabeledControl`, `Gap`, or `Position` properties of this class change.

The event handler receives an argument of type `SyncfusionPropertyChangedEventArgs` containing data related to this event.

```csharp
[C#]

private void autoLabel1_PropertyChanged(object sender,
    Syncfusion.ComponentModel.SyncfusionPropertyChangedEventArgs e)
{
    Console.WriteLine("PropertyChanged event is raised");
}
```

```vbnet
[VB.NET]

Private Sub autoLabel1_PropertyChanged(ByVal sender As Object, ByVal e As Syncfusion.ComponentModel.SyncfusionPropertyChangedEventArgs)
    Console.WriteLine("PropertyChanged event is raised")
End Sub
```

### 3.5.10.2 GradientLabel

The `GradientLabel` class provides a way to create fancy and appealing labels in your forms.

The `GradientLabel` class is fully compatible with the Windows Forms label that it derives from and gets most of its uniqueness from the `BrushInfo` class that is used for the `GradientLabel.BackgroundColor` property.

The `GradientLabel.Border3DStyle` is another property that can specify the look and feel of the `GradientLabel`.

![Example of GradientLabel Control](https://i.imgur.com/example.png)
Figure 604: GradientLabel Control

## API Reference

- **Namespace:** Syncfusion.Windows.Forms.Tools
- **Class:** GradientLabel
- **Properties:**
  - `BackgroundColor`: Defines the gradient background of the label.
  - `Border3DStyle`: Specifies the 3D appearance style of the label.

## Code Examples

### C#

```csharp
using Syncfusion.Windows.Forms.Tools;

GradientLabel label = new GradientLabel();
label.BackgroundColor = new GradientInfo(Color.Blue, Color.White, GradientStyle.LinearVertical);
label.Border3DStyle = Border3DStyle.Flat;
```

### VB.NET

```vbnet
Imports Syncfusion.Windows.Forms.Tools

Dim label As GradientLabel = New GradientLabel()
label.BackgroundColor = New GradientInfo(Color.Blue, Color.White, GradientStyle.LinearVertical)
label.Border3DStyle = Border3DStyle.Flat
```

## Page-level Navigation/TOC (if applicable)

- [3.5.10.1.4.1 PropertyChanged Event](#3.5.10.1.4.1-propertychanged-event)
- [3.5.10.2 GradientLabel](#3.5.10.2-gradientlabel)

## Cross References

See also:
- [Syncfusion WinForms Documentation](https://cdn.syncfusion.com/documentation/windowsforms/)
- [Syncfusion PropertyChange Events](https://help.syncfusion.com/windowsforms/common-feature/propertychanged-event)

<!-- tags: [syncfusion, windowsforms, propertychangepropertyargs, gradientlabel, gradientinfo, border3dstyle, namespace, class, members, gradientcontrol, winforms, control, api, version: 11.4.0.26] keywords: [propertychanged event, gradientlabel, gradientinfo, border3dstyle, labeledcontrol, gap, position, event handler, syncfusionpropertychangedeventargs, windows forms label, 3d appearance] -->
```