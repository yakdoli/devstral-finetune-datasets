```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_261.jpeg
document_name: tools
page_number: 261
page_id: tools#page_261
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:01:34Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### IsMDIMode Method

The `IsMDIMode` method allows you to detect whether the specified control is in MDI child mode or not. The return value will be `true` if the control is in MDI mode, otherwise it will be `false`.

#### Code Examples

##### C#

```csharp
this.dockingManager1.IsMDIMode(this.listBox2);
```

##### VB.NET

```vb
Me.dockingManager1.IsMDIMode(Me.listBox2)
```

### See Also

- **MDI Child Transition**

### 3.4.4.4.3 How to use UserControls as TabbedMDIManager’s children?

Normally, tabbed-MDI is used in MDI applications where the child forms are the children that get tabbed. However, you can also use tabbed-MDI with UserControls as children and that are also dockable. The sample attached here shows how the UserControls can be used as tabbed-MDI children in association with the DockingManager.

#### Note

**Set the IsMdiContainer property of the form to true. Otherwise, this will not work.**

#### Code Examples

##### C#

```csharp
this.tabbedMDIManager = new TabbedMDIManager();
this.tabbedMDIManager.AttachToMdiContainer(this);

// Dock the User Controls
this.dockingManager1.SetEnableDocking(this.userControl1, true);
this.dockingManager1.SetEnableDocking(this.userControl2, true);
this.dockingManager1.SetEnableDocking(this.userControl3, true);

// Set the user controls to MDI mode
this.dockingManager1.SetAsMDIChild(this.userControl1, true);
this.dockingManager1.SetAsMDIChild(this.userControl21, true);
this.dockingManager1.SetAsMDIChild(this.userControl31, true);
```

##### VB.NET

```vb
Me.tabbedMDIManager = New TabbedMDIManager()
```

## API Reference

### Methods

- **IsMDIMode**: Checks if the specified control is in MDI mode.
- **SetEnableDocking**: Enables docking for a specified control.
- **SetAsMDIChild**: Sets a control as an MDI child.

### Parameters

- **control**: The control to check or modify.
- **enable**: A boolean indicating whether to enable docking.

### Returns

- **IsMDIMode**: A boolean indicating whether the control is in MDI mode.

### Exceptions

- **InvalidOperationException**: Thrown if the control cannot be set as an MDI child.

### See also

- **DockingManager**
- **TabbedMDIManager**

<!-- tags: [windows forms, tabbed-mdi, user controls, mdi mode, synchronization, api, controls] keywords: [IsMDIMode, SetEnableDocking, SetAsMDIChild, MDIChildTransition, tabbedMDI, dockable, user controls, dockingmanager, tabbedMDIManager] -->
```
