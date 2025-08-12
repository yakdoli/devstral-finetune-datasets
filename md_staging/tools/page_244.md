```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_244.jpeg
document_name: tools
page_number: 244
page_id: tools#page_244
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:00:49Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates the use of docking functionality in WinForms applications.
- Implements docking and floating controls using the `DockingManager`.
- Displays docking relationships between controls.

```csharp
Rectangle(250, 250, 220, 260));
    this.dockingManager1.FloatControl(this.myUserControl21, new
Rectangle(350, 350, 220, 260));

    this.dockingManager1.DockControl(this.myUserControl31, this,
DockStyle.Right, 200);
    this.dockingManager1.DockControl(this.myUserControl11,
        this.myUserControl21, DockStyle.Bottom, 200);
}
```

## Content

### GetDockingRelationship Function

The `GetDockingRelationship` method retrieves and displays the docking relationship between the docked control and its target control.

```csharp
private void GetDockingRelationship(Control dockedControl)
{
    Control targetControl;
    string statusMessage = string.Empty;

    if (dockedControl.Parent is DockHost)
    {
        DockHost dockhost = dockedControl.Parent as DockHost;
        DockHostController dhc = dockhost.InternalController as
DockHostController;
        DockControllerBase baseController = dhc.DICurrent.dController;

        if (baseController != null)
        {
            if (baseController is SizingController || baseController is
DockHostController)
            {
                if (count != dockedctrls.Count - 1)
                {
                    targetControl =
                baseController.HostControl.Controls[0];
                    statusMessage = dockedControl.Name + " is docked to "
                        + targetControl.Name + ".";
                    statusMessage += "DockingStyle " +
this.dockingManager1.GetDockStyle(dockedControl);
                }
                else if (count == dockedctrls.Count - 1)
                {
                    targetControl = baseController.HostControl;
                    statusMessage = dockedControl.Name + " is docked to "
                        + targetControl.Name + ".";
                    statusMessage += "DockingStyle " +
this.dockingManager1.GetDockStyle(dockedControl);
                }
            }
            else if (baseController is DockTabController)
            {
```

## API Reference

### Method

- **Name**: `GetDockingRelationship`
- **Parameters**:
  - `Control dockedControl`: The control whose docking relationship needs to be determined.
- **Returns**: Void (displays the relationship in a status message).

### Properties
- **DockManager**: Used to manage the docking functionality of controls.
- **DockStyle**: Specifies how the control is docked (e.g., `Right`, `Bottom`).

## Code Examples

Example Usage:

```csharp
// Docking a control to the right of the container
this.dockingManager1.DockControl(myControl, dockHost, DockStyle.Right, 200);

// Retrieving the docking relationship
GetDockingRelationship(myDockedControl);
```

## Cross References

See also:
- [DockManager Documentation](#)
- [DockStyle Enumeration](#)

<!-- tags: [Docking, WinForms, ControlDocking, DockManager] keywords: [docking, control, dockStyle, dockedctrls, DockManager, DockHost] -->
```