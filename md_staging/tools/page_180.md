```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_180.jpeg
document_name: tools
page_number: 180
page_id: tools#page_180
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:14:02Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

![DockAbility Set within a control to Right, Top and Tabbed](#)

*Figure 94: DockAbility Set within a control to Right, Top and Tabbed*

## See Also
- [Docking](Docking)

## 3.4.3.6.2 DockToFill, Freeze Resizing

The DockToFill property allows users to implement a very unique docking layout where a non-MDIContainer form or ContainerControl's entire client region is occupied by the dockable controls.

### DockingManager Property
| DockingManager Property | Description |
|--------------------------|-------------|
| DockToFill               | Sets the boolean value indicating whether the docked control occupies the form's full client region. |

### Code Example: [C#]

```csharp
this.dockingManager1.DockToFill = true;
```

### RAG Annotations

<!-- tags: [DockToFill, DockToFill Property, dockable controls, ContainerControl, DockToFill Example, C# Example] keywords: [DockToFill, DockToFill Property, dockable controls, ContainerControl, DockToFill Example, C# Example] -->
```