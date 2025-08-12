```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_203.jpeg
document_name: grid
page_number: 203
page_id: grid#page_203
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:02:31Z
fidelity: lossless
-->

## Overview
- Demonstrates the usage of GridCellModelBase in creating customized cell controls for editing DataTables.
- Highlights the serialization capabilities of GridCellModelBase and its role in handling persistent data.
- Explains how to override the CreateRenderer method to create a GridCellRendererBase object for handling user interactions in a new cell type.

## Content

|                         | Description |
|-------------------------|-------------|
| Slider Control in a cell.            | Placeholder for specific details.       |
| RepeaterUserControl      | Shows how you can use a derived cell control in a grid to create a repeater control used to edit DataTables.       |

### See Also

#### 4.1.4.3.1 GridCellModelBase

The main function of the GridCellModelBase derived class is to serialize your control. It can hold any persistent state independent data that your control uses. The state-dependent data should be part of the GridStyleInfo object for the cell, but any other persistent property (for example, the initial height of a drop-down) will be in this GridCellModelBase derived class.

The other major function of this class is to create a cellrenderer object of the correct type. In fact, the only required override in a GridCellModelBase derived class is the CreateRenderer method. In that override, you can create and return a GridCellRendererBase derived object that would handle the user interactions in your new cell type.

In general, you probably will not be able to derive directly from the base class, but instead from an existing Essential Grid derived class such as the GridStaticCellModel. The following code example illustrates this.

```csharp
// Define a custom Cell Model by inheriting GridStaticCellModel.
public class LinkLabelCellModel : GridStaticCellModel
{
    protected LinkLabelCellModel(SerializationInfo info,
                                 StreamingContext context): base(info, context)
    {
    }

    public LinkLabelCellModel(GridModel grid): base(grid)
    {
        AllowFloating = false;
    }

    // Override CreateRenderer Method to create a CellRenderer object.
    public override GridCellRendererBase CreateRenderer(GridControlBase
```

### API Reference
- **Namespace**: Syncfusion.Windows.Forms.Grid
- **Class**: GridCellModelBase
- **Methods**: CreateRenderer

#### Parameters
| Name                | Type                                            | Description                                                                          | Default | Required |
|---------------------|-------------------------------------------------|--------------------------------------------------------------------------------------|---------|----------|
| GridModel grid      | GridModel                                       | The grid model associated with the cell.                                             | N/A     | Yes      |
| SerializationInfo   | object                                          | Contains any persistent state-independent data for the cell model.                   | N/A     | No       |
| StreamingContext    | object                                          | Specifies the source and destination of the serialized stream.                       | N/A     | No       |

#### Returns
- **GridCellRendererBase**: The cell renderer object that handles user interactions for the cell.

### Code Examples
- The example above demonstrates how to create a custom cell model by inheriting from GridStaticCellModel and overriding the needed methods.

## Page-level Navigation/TOC (if applicable)
- **4.1.4.3.1 GridCellModelBase**
  - Overview of GridCellModelBase
  - Serialization capabilities
  - User interaction management via CellRenderers
  - Sample code for creating a custom cell model

## Cross References
- **See also**: Relevant topics or classes such as RepeaterUserControl, GridStyleInfo, GridCellRendererBase, and GridStaticCellModel.

<!-- tags: [Syncfusion Winforms, Grid, GridCellModelBase, GridCellRendererBase, DataTables, Serialization, User Interactions] keywords: [GridCellModelBase, GridStyleInfo, GridCellRendererBase, GridStaticCellModel, RepeaterUserControl, DataTable, Custom Cell Model, Serialization, User Interaction] -->
```