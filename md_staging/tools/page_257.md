```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_257.jpeg
document_name: tools
page_number: 257
page_id: tools#page_257
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:01:22Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

<figure>
  <img src="Access Docked controls Collection" alt="Access Docked controls Collection" />
  <figcaption>Figure 107: List Box disabled from Docking</figcaption>
</figure>

### 3.4.4.3.2 How to determine whether any two controls are in the same tabbed group?

This can be done by calling the `IsSameTabbedGroup` method.

```csharp
this.dockingManager.IsSameTabbedGroup(this.listBox1, this.listBox2);
```

```vbnet
Me.dockingManager.IsSameTabbedGroup(Me.listBox1, Me.listBox2)
```

### 3.4.4.3.3 How to get the docking group details?

#### To get the docking group

There is no concept of 'group' in Docking Manager, and a tabbed group is just an intermediate state. However, if necessary, this can be determined by first ascertaining that the control is in a tabbed docking group, getting hold of the `DockTabController`, getting its `DockTab`, and then iterating the `DockTabPages`. The `dhcClient` member of each `DockTabPage` will reference the `DockHostController` that is associated with it. Once the controller is available, you can get to the control through the `DockHostController.HostControl` property and use the control's `Controls[0]` indexer to get the actual dockable control.

Follow the given steps to get the docking group.

---

© 2013 Syncfusion. All rights reserved. 257 | Page
```