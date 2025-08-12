```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_137.jpeg
document_name: tools
page_number: 137
page_id: tools#page_137
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:45:53Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

![](image.png "Figure 54: DockedControl set to Float")

## DisallowFloating

By enabling the `DisallowFloating` property, a control can be dragged and redocked to the host form, but cannot be floated.

### DockManager Property Description

| DockManager Property    | Description                                                                                   |
|--------------------------|-----------------------------------------------------------------------------------------------|
| DisallowFloating         | Property which sets value indicating whether the docked controls are allowed to float or not. |

### Code Examples

[C#]

```csharp
this.dockingManager1.DisallowFloating = true;
```

[VB.NET]

```vb
Me.dockingManager1.DisallowFloating = True
```

---

<!-- tags: [product, module, control, api, version?] keywords: [DockingStyle, DisallowFloating, control, drag, redock, float, host form, DockManager, Syncfusion Winforms, property, documentation] -->
```