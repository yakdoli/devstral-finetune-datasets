```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_129.jpeg
document_name: tools
page_number: 129
page_id: tools#page_129
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:40:32Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

![Figure: Tabbed Dockable Listbox Controls](image.png)
*Figure 48: Tabbed Dockable Listbox Controls*

### 3.4.3 Concepts and Features

This section covers the following topics which discusses the concepts and features of docking.

#### 3.4.3.1 Docking Styles

This section will discuss the below four docking styles.

- Docking - Lets you dock the control on any of the four sides of the container control.
- Tabbed Docking - Lets you tab two or more controls.
- Floating - Floats the dockable control.
- AutoHiding - Auto hides the dockable controls and displays as autohidden tabs.

##### 3.4.3.1.1 Docking

Docked control can be docked to any of the four sides of the container control, i.e., to Left, Right, Top, and Bottom. DockingManager lets you specify the type of docking and the bounds of the docked control using the `DockControl` method. This method also sets `Tabbed style` for the controls.

```csharp
// Tab the docked controls
this.dockingManager.DockControl(this.listBox1,
this.listBox2, Syncfusion.Windows.Forms.Tools.DockingStyle.Left, 200, true
);
```

```vb.net
[VB.NET]
```

---

---
© 2013 Syncfusion. All rights reserved. 129 | Page
```