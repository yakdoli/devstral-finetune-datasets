```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_242.jpeg
document_name: tools
page_number: 242
page_id: tools#page_242
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:58:40Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Enabling Docking and TabbedMDI in Windows Forms

The following code demonstrates how to enable docking and integrate a TabbedMDI container with an MDI form in both C# and VB.NET. The examples show how to attach panels to the docking manager, set their dock labels, and configure them as MDI children. The TabbedMDI manager is then attached to the MDI form, and the visual style is set to Office2003.

#### C#

```csharp
this.tm.TabControlAdded += new
TabbedMDITabControlEvents.Handler(this-tm_TabControlAdded);

// Assign the MDI form into the TabbedManager MDI container.
this.tb.AttachToMdiContainer(this);
this.dockingManager1.VisualStyle =
Syncfusion.Windows.Forms.VisualStyle.Office2003;
```

#### VB.NET

```vb.net
' Enables docking for panel.
Me.dockingManager1.SetEnableDocking(Me_panel1, True)
Me.dockingManager1.SetEnableDocking(Me_panel2, True)
Me.dockingManager1.SetEnableDocking(Me_panel3, True)
Me.dockingManager1.SetEnableDocking(Me_panel4, True)
' Sets dock label.
Me.dockingManager1.SetDockLabel(Me_panel1, "Panel 1")
Me.dockingManager1.SetDockLabel(Me_panel2, "Panel 2")
Me.dockingManager1.SetDockLabel(Me_panel3, "Panel 3")

' Changes docking window to MDI child window.
Me.dockingManager1.SetAsMDIChild(Me_panel1, True)
Me.dockingManager1.SetAsMDIChild(Me_panel2, True)
Me.dockingManager1.SetAsMDIChild(Me_panel3, True)
Me.dockingManager1.SetAsMDIChild(Me_panel4, True)
' Attach MDI container to TabbedMDI manager.
Me.tm = New TabbedMDIManager()
AddHandler tm.TabControlAdded, AddressOf tm_TabControlAdded
' Assign the MDI form into the TabbedManager MDI container.
Me.tb.AttachToMdiContainer(Me)
Me.dockingManager1.VisualStyle =
Syncfusion.Windows.Forms.VisualStyle.Office2003
```

### Customizing Tab Style

You can also change the appearance of the tabs by applying the `TabStyle` in the `TabControlAdded` event.

#### C#

```csharp
// Enable the rendering for the Tabbed MDI manager tabs.
private void tm_TabControlAdded(object sender,
TabbedMDITabControlEvents.Handler args)
{
    args.TabControl.TabStyle = typeof(TabRendererWhidbey);
}
```

## API Reference

### Methods

- **SetEnableDocking**: Enables docking for a specified panel.
- **SetDockLabel**: Sets the dock label for a panel.
- **SetAsMDIChild**: Configures a panel as an MDI child window.
- **AttachToMdiContainer**: Attaches the MDI form to the TabbedMDI manager.

### Properties

- **VisualStyle**: Sets the visual style of the docking manager.

## Related Topics

- Customizing docking windows
- Configuring TabbedMDI样式

```Markdown
<!-- tags: [product, module, control, api, version?] keywords: [Docking, TabbedMDI, MDIChildren, Panel, TabStyle, TabControlAdded, VisualStyle, Office2003] -->
```