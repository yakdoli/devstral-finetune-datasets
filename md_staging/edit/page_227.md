```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_227.jpeg
document_name: edit
page_number: 227
page_id: edit#page_227
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:07:39Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- Provides options for the status bar sizing grip: **Smart**, **Visible**, and **Hidden**.
- Demonstrates configuring the visibility of the status bar sizing grip in both C# and VB.NET.
- Explains visibility settings for individual Status Bar Panels.

## Content

### Status Bar Sizing Grip Configuration

#### Code Examples

**C#**
```csharp
// Set the visibility of the statusbar sizing grip.
this.editControl1.StatusBarSettings.GripVisibility =
    Syncfusion.Windows.Forms.Edit.Enums.SizingGripVisibility.Visible;
```

**VB.NET**
```vbnet
' Set the visibility of the statusbar sizing grip.
Me.editControl1.StatusBarSettings.GripVisibility =
    Syncfusion.Windows.Forms.Edit.Enums.SizingGripVisibility.Visible
```

#### Sizing Gripper in the Status Bar

<figure>
  <img src="image_of_statusbar_gripper.png" alt="Sizing Gripper in the Status Bar" />
  <figcaption>Figure 74: Sizing Gripper in the Status Bar</figcaption>
</figure>

### Visibility Settings

The StatusBar feature in Edit Control can be turned on by setting the `StatusBarSettings.Visible` property to `True`. By default, this property is set to `False`. The individual Status Bar Panels can be optionally shown / hidden by using the `Visible` property corresponding to the respective panel.

#### Code Examples

**C#**
```csharp
// Set the visibility of the status bar sizing grip.
this.editControl1.StatusBarSettings.GripVisibility =
    Syncfusion.Windows.Forms.Edit.Enums.SizingGripVisibility.Visible;

// Shows the built-in statusbar.
this.editControl1.StatusBarSettings.Visible = true;

// Enable the TextPanel in the StatusBar.
this.editControl1.StatusBarSettings.TextPanel.Visible = true;
```

**VB.NET**
```vbnet
Me.editControl1.StatusBarSettings.GripVisibility =
    Syncfusion.Windows.Forms.Edit.Enums.SizingGripVisibility.Visible
```

## Page-level Navigation/TOC (if applicable)
- [unclear]

## Cross References
- See also: [unclear]

## RAG Annotations
<!-- tags: [product, module, control, api, version?] keywords: [essential edit, windows forms, status bar, visibility settings, sizing grip, edit control] -->
```