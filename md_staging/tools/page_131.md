```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_131.jpeg
document_name: tools
page_number: 131
page_id: tools#page_131
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:43:09Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Explains how to set docking styles at runtime.
- Discusses the use of Dock Arrows and the DragProviderStyle property.
- Introduces tabbed docking of controls inside a container.

## Content

### Docking Style Selected at Run Time

![](image.png)  
**Figure 50: Docking Style selected at Run Time**

#### Note:
At run time, docking style can also be set with the help of **Dock Arrows** provided by the **DragProviderStyle property**.

#### 3.4.3.1.2 Tabbed Docking

This section will discuss how the docked controls inside a container can be tabbed.

**At Design Time**

The docked controls can be tabbed in the designer, by just dragging and dropping into one another. DockingManager helps you in doing this using different **DragProviderStyle**.

---

### API Reference

#### Properties
- **Dock Arrows**
- **DragProviderStyle**

#### Methods
- `DockTo`
- `TabControls`

---

### Code Examples

```csharp
// Example of setting Dock Arrows at run time
using System.Windows.Forms;

DockManager.DockProviderStyle = DragProviderStyle.UseDockArrows;
```

---

## Cross References

See also:
- Docking styles and properties in the Windows Forms documentation.
- DockManager API reference.

<!-- tags: [Docking, Windows Forms, Dock Manager, DragProviderStyle, Tabbed Docking] keywords: [Dock Arrows, DragProviderStyle, tabbed controls, Windows Forms, DockingManager, tabbed docking, controls inside a container] -->
```