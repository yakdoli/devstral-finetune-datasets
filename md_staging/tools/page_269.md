```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_269.jpeg
document_name: tools
page_number: 269
page_id: tools#page_269
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:02:07Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## 3.4.4.8.1 How to serialize or deserialize the docking state for a docked control on loading the application?

### Overview
- Describes the process to serialize or deserialize the docking state of a docked control in a Windows Forms application.
- Explains how to access the DockHost and retrieve the current serialization information using `GetSerCurrentDI()` method.
- Provides examples in both C# and VB.NET for obtaining the docking position and area of a control.

## Content

To serialize or deserialize the docking state, follow the below steps.

### Before Closing the Docked/Floating Control
Before closing the docked / floating control, access the control's parent and cast this to type `Syncfusion.Windows.Forms.Tools.DockHost`.

#### Example: Accessing the DockHost
```csharp
// C#
Syncfusion.Windows.Forms.Tools.DockHost dhost = ctrl.Parent as Syncfusion.Windows.Forms.Tools.DockHost;
```

```vb
' VB.NET
Dim dhost As Syncfusion.Windows.Forms.Tools.DockHost = Me.listView1.Parent as Syncfusion.Windows.Forms.Tools.DockHost
```

### Accessing the DockHost's InternalController
- Access the `DockHost`'s `InternalController` and get its current serialization information through the `GetSerCurrentDI()` method.

#### Example: Accessing the InternalController
```csharp
// C#
Syncfusion.Windows.Forms.Tools.DockHostController dhc = dhost.InternalController as Syncfusion.Windows.Forms.Tools.DockHostController;
```

```vb
' VB.NET
Dim dhc As Syncfusion.Windows.Forms.Tools.DockHostController = dhost.InternalController as Syncfusion.Windows.Forms.Tools.DockHostController
```

#### Explanation
This returns an object of type `Syncfusion.Windows.Forms.Tools.DockInfo`. The `DockInfo.DockingStyle` member gives the dock position of the control with respect to the host form, and the `DockInfo.rcDockArea` provides the dock area.

#### Example: Retrieving Dock Information
```csharp
// C#
Syncfusion.Windows.Forms.Tools.DockInfo di = dhc.GetSerCurrentDI();
```

```vb
' VB.NET
Dim di As Syncfusion.Windows.Forms.Tools.DockInfo =
```

### Summary
By following these steps, you can effectively manage the serialization and deserialization of docking states for controls in a Windows Forms application, ensuring consistent user experience and functionality across application sessions.

## References
- See also: other sections on docking and floating controls in the documentation for additional details.

<!-- tags: [syncfusion, windows forms, docking controls, serialization, deserialization, dockhost, internalcontroller, dockingstyle, dockinfo] keywords: [syncfusion, windows forms, docking controls, serialize, deserialize, dockhost, internalcontroller, dockingstyle, dockinfo] -->
```