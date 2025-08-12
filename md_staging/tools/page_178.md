```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_178.jpeg
document_name: tools
page_number: 178
page_id: tools#page_178
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:13:50Z
fidelity: lossless
-->

## Visibility of the Arrows

The docking arrows visibility, while dropping a control inside the form or into another docked control, can be set using the below properties.

### DockControl Property

| DockedControl Property          | Description                                                                                  |
|----------------------------------|----------------------------------------------------------------------------------------------|
| **DockAbility**                 | Indicates where the user can dock in this control using drag providers.                      |
| **OuterDockAbility**            | Indicates where the user can dock the controls in a form using the drag providers.           |

### Property Grid

Figure 92: Property Grid indicating DockAbility and OuterDockAbility

![Property Grid](https://res.cloudinary.com/practicaldev/image/fetch/s--E6b4cHvJ--/c_limit%2Cf_auto%2Cfl_strip%2Cw_1200/https://www.syncfusion.com/documentation/windows-forms/essential-tools/images/property-grid.png)

## API Reference

- **Syncfusion.Windows.Forms.Tools.DockControl**
  - **DockAbility**
    - **Type**: Enumerated values (Top, Right, Tabbed)
    - **Description**: Indicates the positions where the user can dock in the control using drag providers.
    - **Default**: Top, Right, Tabbed
  - **OuterDockAbility**
    - **Type**: Enumerated values (Left, Top, Tabbed)
    - **Description**: Indicates the positions where the user can dock the controls in a form using the drag providers.
    - **Default**: Left, Top, Tabbed

## Code Examples

```csharp
using Syncfusion.Windows.Forms.Tools;

// Example of setting DockAbility and OuterDockAbility
DockControl dockControl = new DockControl();
dockControl.DockAbility = DockStyle.Top | DockStyle.Right | DockStyle.Tabbed;
dockControl.OuterDockAbility = DockStyle.Left | DockStyle.Top | DockStyle.Tabbed;
```

## Related Concepts

- **Docking**: The ability to attach controls to edges of the form or other controls.
- **Drag-and-Drop**: Interactive feature allowing users to move controls within the form.
- **DockStyle Enum**: Defines the possible docking positions for controls.

<!-- tags: [Docking, Arrows, Controls, DockControl, Windows Forms, Essential Tools] keywords: [DockAbility, OuterDockAbility, Property Grid, drag providers, form, controls] -->
```