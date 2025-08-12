```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_182.jpeg
document_name: tools
page_number: 182
page_id: tools#page_182
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:16:29Z
fidelity: lossless
-->

## Freezing Controls

The `FreezeResizing` property decides whether to freeze the specified control.

### Code Examples

**[C#]**

```csharp
this.dockingManager1.FreezeResizing = true;
this.dockingManager1.SetFreezeResize(this.panel1, true);
```

**[VB.NET]**

```vb
Me.dockingManager1.FreezeResizing = True
Me.dockingManager1.SetFreezeResize(Me.panel1, True)
```

### Sample Path

A sample which uses `FreezeResizing` property is available in the below sample installation path:

```
..My Documents\Synccfusion\EssentialStudio\Version Number\Windows\Tools.Windows\Samples\2.0.Docking Package\SDDemo
```

## 3.4.3.7 Advanced Features

### Overview
- Details the advanced features available in this section.

### DockingClientPanel

- A premise of any docking windows implementation is the existence of a client window the bounds of which vary at run-time as windows get docked or undocked.
- This paradigm is particularly suitable for MDI type forms where the MDIClient window resizes or relocates in synchronization with changes in the docking windows layout.
- Child controls located within the MDIClient window are assured of a static spatial relationship with the parent container.
- Non-MDI forms lack such client windows, and non-dockable, statically positioned controls risk being clipped by docked windows nearby.
- The Essential Tools `DockingClientPanel` control overcomes this limitation by providing an auto-resized client surface for non-dockable controls.

## See Also

- [Getting Started](Getting Started)
```