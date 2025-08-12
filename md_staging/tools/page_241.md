```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_241.jpeg
document_name: tools
page_number: 241
page_id: tools#page_241
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:56:43Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

The Tabbed MDI Package provides a new Tabbed MDI layout mode (as an alternative to the default Cascade and Tiled modes), popularized by VS .NET.

## Overview
- The Tabbed MDI Package offers a tabbed MDI layout for Windows Forms applications.
- It enables a dockable window to be integrated into the Tabbed MDI manager during application startup.

### Key Steps
1. Add 4 panels and the DockingManager to your application.
2. Declare the TabbedMDIManager.

### Code Declarations

#### C#
```csharp
private Syncfusion.Windows.Forms.Tools.TabbedMDIManager tm;
```

#### VB.NET
```vb
Private tm As Syncfusion.Windows.Forms.Tools.TabbedMDIManager
```

## Setting Up the Tabbed MDI Layout

### Steps to Configure
1. **Enable Docking for Panels**:
   - Use the `SetEnableDocking` method for each panel.
   - This method sets the panels to be dockable.

   ```csharp
   this.dockingManager1.SetEnableDocking(this.panel1, true);
   this.dockingManager1.SetEnableDocking(this.panel2, true);
   this.dockingManager1.SetEnableDocking(this.panel3, true);
   this.dockingManager1.SetEnableDocking(this.panel4, true);
   ```

2. **Set Dock Labels**:
   - Assign labels to each dockable panel for identification.

   ```csharp
   this.dockingManager1.SetDockLabel(this.panel1, "Panel 1");
   this.dockingManager1.SetDockLabel(this.panel2, "Panel 2");
   this.dockingManager1.SetDockLabel(this.panel3, "Panel 3");
   this.dockingManager1.SetDockLabel(this.panel4, "Panel 4");
   ```

3. **Convert Dockable Windows to MDI Child Windows**:
   - Use the `SetAsMDIChild` method to enable the dockable windows as MDI children.

   ```csharp
   this.dockingManager1.SetAsMDIChild(this.panel1, true);
   this.dockingManager1.SetAsMDIChild(this.panel2, true);
   this.dockingManager1.SetAsMDIChild(this.panel3, true);
   ```

4. **Attach the MDI Container to the TabbedMDI Manager**:
   - Final step to integrate the MDI container with the TabbedMDI manager.

   ```csharp
   this.tm = new TabbedMDIManager();
   ```

### Notes
- Ensure the form's `IsMDIContainer` property is set to `true`.
- The `SetAsMDIChild` method must be called before `AttachToMdiContainer` to achieve the desired VS.NET editor-like tabbed window appearance.

## Summary
The Tabbed MDI Package enhances the user experience by providing a tabbed MDI interface in Windows Forms applications, similar to the layout found in VS.NET. By following the steps outlined, developers can easily integrate this feature into their applications.

## See also:
- [Tabbed MDI Package Documentation](https://syncfusion.com/help/)
- [DockingManager Class Reference](https://syncfusion.com/documentation/windowsforms/dockingmanager/)

<!-- tags: [windowsforms, tabbed-mdi, dockingmanager, syncfusion-tools, mdicontainer] keywords: [tabbed, MDI, dockable, window, layout, VS.NET, editor, interface, windows forms, synchronization, forms] -->
```