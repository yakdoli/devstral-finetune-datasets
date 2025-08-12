```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_128.jpeg
document_name: tools
page_number: 128
page_id: tools#page_128
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:39:15Z
fidelity: lossless
-->

## WinForms Docking Controls

### Overview
- This page demonstrates the steps to enable docking functionality for controls in a Windows Forms application using Syncfusion tools.
- Details on setting the visual style and enabling docking for controls are provided.
- Examples include configuring docking styles such as "tabbed."

### Content

#### Setting the Visual Style of Docked Controls

The visual style of the docked controls can be set to enhance the appearance.

**C#**
```csharp
// Set the visual Style of the docked controls
this.dockingManager.VisualStudio = Syncfusion.Windows.Forms.VisualStudio.Office2003;
```

**VB.NET**
```vb
' Set the visual Style of the docked controls
Me.dockingManager.VisualStudio = Syncfusion.Windows.Forms.VisualStudio.Office2003
```

#### Enabling Docking for Controls

To enable the controls to be docked, call the `SetEnableDocking` method.

**C#**
```csharp
this.dockingManager.SetEnableDocking(this.listBox1, true);
this.dockingManager.SetEnableDocking(this.listBox2, true);
```

**VB.NET**
```vb
Me.dockingManager.SetEnableDocking(Me.listBox1, True)
Me.dockingManager.SetEnableDocking(Me.listBox2, True)
```

#### Specifying Docking Styles

Docking styles for the controls can be specified in the `DockControl` method. Here, the docking style is set to "tabbed."

**C#**
```csharp
// Tab the docked controls
this.dockingManager.DockControl(this.listBox1,
                               this.listBox2,
                               Syncfusion.Windows.Forms.Tools.DockStyle.Tabbed,
                               200,
                               true);
```

**VB.NET**
```vb
' Tab the docked controls
Me.dockingManager.DockControl(Me.listBox1,
                              Me.listBox2,
                              Syncfusion.Windows.Forms.Tools.DockStyle.Tabbed,
                              200,
                              True)
```

#### Resulting Form

The resulting form will look like the below image.

## Conclusion

This section provides a comprehensive guide on configuring docking for controls in a Windows Forms application, ensuring a consistent and user-friendly experience.

<!-- tags: [Syncfusion, Windows Forms, Docking Controls, Visual Studio, Office2003, Tabbed Docking] keywords: [docking, controls, visual style, tabbed, Windows Forms, Syncfusion] -->
```