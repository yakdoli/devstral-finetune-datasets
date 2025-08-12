```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_177.jpeg
document_name: diagram
page_number: 177
page_id: diagram#page_177
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:19:51Z
fidelity: lossless
-->

### Essential Diagram for Windows Forms

#### Overview
- This page explains how to handle the visibility of layers and configure rulers in a Syncfusion WinForms Diagram control.
- Layers can be used to control the visibility of all objects on a specific layer.
- Rulers can be enabled and customized programmatically using properties such as `ShowRulers` and `RulersHeight`.

## Content

### The visibility of the layer can be handled to control the visibility of all the objects on that layer.

#### C#
```csharp
Layer layer0 = new Layer();
this.diagram1.Model.Layers.Add(layer0);
layer0.Enabled = true;
layer0.Visible = true;
layer1.Visible = true;
```

#### VB
```vb
Dim layer0 As New Layer()
Me.diagram1.Model.Layers.Add(layer0)
layer0.Enabled = True
layer0.Visible = True
layer1.Visible = True
```

### 4.6.5 Rulers

Rulers can be enabled by setting the `ShowRulers` property for the diagram control. The rulers will automatically inherit the `MeasurementUnit` set for the diagram model and get converted accordingly.

The height of the ruler can be set through the `RulersHeight` property.

| Property         | Description                                         |
|------------------|-----------------------------------------------------|
| ShowRulers       | Specifies whether to display the ruler for the diagram control. |
| RulersHeight     | Specifies the height of the ruler.                   |

Programmatically the ruler properties can be set as follows.

#### C#
```csharp
this.diagram1.ShowRulers = true;
this.diagram1.RulersHeight = 25;
```

## API Reference
- **Namespace**: Syncfusion.Windows.Forms.Diagram
- **Properties**:
  - `ShowRulers`: A boolean property to enable or disable the ruler display.
  - `RulersHeight`: An integer property to set the height of the ruler.

## Code Examples

See the code examples provided in the section for enabling and configuring rulers in a Syncfusion WinForms Diagram control.

```markdown
### Ruler Configuration

```csharp
this.diagram1.ShowRulers = true;
this.diagram1.RulersHeight = 25;
```

```vb
Me.diagram1.ShowRulers = True
Me.diagram1.RulersHeight = 25
```
```

### Links
- [Diagram Control Properties](#diagram-control-properties)
- [Layer Management](#layer-management)

<!-- tags: [diagram, Windows Forms, Syncfusion, WinForms, Ruler, Layer, ShowRulers, RulersHeight, API, Control, Properties] keywords: [diagram control, ruler, layer visibility, Syncfusion Windows Forms, Diagram Layer, property settings] -->
```