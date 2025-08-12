```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_712.jpeg
document_name: grid
page_number: 712
page_id: grid#page_712
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:35:40Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

| **gridGroupingControl1.GroupDropPanel** | Lets the user to control the drop panel behavior. |
| --- | --- |
| **gridGroupingControl1.Splitter** | Provides the splitter related properties. |

## Example

In this example, the grouping grid is built with hierarchical dataset created at runtime. The formatting of the Group Drop Area can be controlled by handling the PrepareViewStyleInfo event for each of the grids in the Group Drop Panel.

1. **Formatting of the Splitter and GroupDropPanel**

```csharp
// Splitter Color.
this.gridGroupingControl1.Splitter.BackColor = Color.Red;

// Panel Color.
this.gridGroupingControl1.GroupDropPanel.BackColor = Color.YellowGreen;
```

```vb.net
' Splitter Color.
Private Me.gridGroupingControl1.Splitter.BackColor = Color.Red

' Panel Color.
Private Me.gridGroupingControl1.GroupDropPanel.BackColor = Color.YellowGreen
```

2. **The PrepareViewStyleInfo event for each of the grids can be hooked by looping through the controls in the panel.**

```csharp
foreach (Control ctl in this.gridGroupingControl1.GroupDropPanel.Controls)
{
    GridGroupDropArea groupDropArea = ctl as GridGroupDropArea;

    switch (groupDropArea.Model.Table.TableDescriptor.Name)
    {
        case "ParentTable":
            groupDropArea.Model.ColCount = 80;
    }
}
```

## API Reference (if applicable)
- **Namespace**: GridGroupingControl
- **Members**:
  - **GroupDropPanel**: Lets the user to control the drop panel behavior.
  - **Splitter**: Provides the splitter related properties.

## Code Examples (multi-language supported)
- **C#**
  ```csharp
  this.gridGroupingControl1.Splitter.BackColor = Color.Red;
  this.gridGroupingControl1.GroupDropPanel.BackColor = Color.YellowGreen;
  ```
- **VB.NET**
  ```vb.net
  Private Me.gridGroupingControl1.Splitter.BackColor = Color.Red
  Private Me.gridGroupingControl1.GroupDropPanel.BackColor = Color.YellowGreen
  ```

<!-- tags: [Syncfusion, Winforms, Grid, GroupDropPanel, Splitter, PrepareViewStyleInfo] keywords: [grid grouping, hierarchical dataset, runtime visualization, drop panel behavior, splitter formatting, event handling] -->
```