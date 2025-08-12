```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_251.jpeg
document_name: tools
page_number: 251
page_id: tools#page_251
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:01:38Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Obtaining Docking Information in Code

The following code snippets demonstrate how to access the docking properties of a control using `Syncfusion.Windows.Forms.Tools.DockHost` and `Syncfusion.Windows.Forms.Tools.DockHostController`.

#### C# Example

```csharp
Syncfusion.Windows.Forms.Tools.DockHost dhost = this.listView1.Parent as Syncfusion.Windows.Forms.Tools.DockHost;
Syncfusion.Windows.Forms.Tools.DockHostController hdc = dhost.InternalController as Syncfusion.Windows.Forms.Tools.DockHostController;

// The DockInfo object will give all the information about docked control.
Syncfusion.Windows.Forms.Tools.DockInfo di = hdc.GetSerCurrentDI();
MessageBox.Show(di.rcDockArea.ToString());
```

#### VB.NET Example

```vb
' listView1 is the dockable control. We could get it's dock properties by accessing DockHost and DockHostController.
Dim dhost As Syncfusion.Windows.Forms.Tools.DockHost = CType(IIf(Me.listView1.Parent Is Syncfusion.Windows.Forms.Tools.DockHost, Me.listView1.Parent, Nothing), Syncfusion.Windows.Forms.Tools.DockHost)
Dim hdc As Syncfusion.Windows.Forms.Tools.DockHostController = CType(IIf(TypeOf dhost.InternalController Is Syncfusion.Windows.Forms.Tools.DockHostController, dhost.InternalController, Nothing), Syncfusion.Windows.Forms.Tools.DockHostController)

' The DockInfo object will give all the information about docked control.
Dim di As Syncfusion.Windows.Forms.Tools.DockInfo = hdc.GetSerCurrentDI()
MessageBox.Show(di.rcDockArea.ToString())
```

### Steps to Access Docking Information

- **Just before you close a docked / floating control**, access the control's parent and cast this to type `Syncfusion.Windows.Forms.Tools.DockHost`.
- **Now access the DockHost's InternalController** and get its current serialization info using the `GetSerCurlInfo()` method. This will fetch an object of type `Syncfusion.Windows.Forms.Tools.DockInfo`. The `DockInfo.DockingStyle` member gives the dock position of the particular control with respect to the host form, and the `DockInfo.rcDockArea` member returns the control bounds.
- **If the control is floating**, then `DockingStyle` will be equal to `Syncfusion.Windows.Forms.Tools.DockingStyle.Fill`. You can serialize this information against the control's name and later upon loading, appropriately use either the `DockingManager.DockControl()` / `FloatControl()` method, based on the serialized `DockingStyle` / `rcbounds` values, to set the control's dock state.

### How to Identify the Docking Window Which is Currently Being Closed

#### 3.4.4.1.9 How to identify the docking window which is currently being closed?

This can be done through the `DockVisibilityChanged` Event.

## Cross References

- See also: [DockingManager.DockControl()]
- See also: [DockingManager.FloatControl()]
- See also: [DockInfo.DockingStyle]
- See also: [DockInfo.rcDockArea]

<!-- tags: [syncfusion, winforms, tools, dock, dockhost, dockhostcontroller, dockinfo, event, serialization, docked controls, floating controls, dockvisibilitychanged, guide] keywords: [getting-docking-information, control-docking-state, serialization, dockstyle, rcdockarea, dockvisibility, dockmanagemet, floatcontrol] -->
```