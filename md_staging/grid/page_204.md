<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_204.jpeg
document_name: grid
page_number: 204
page_id: grid#page_204
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:02:38Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```csharp
control)
{
    return new LinkLabelCellRenderer(control, this);
}
}
```

```vb.net
' Define a custom Cell Model by inheriting GridStaticCellModel.
Public Class LinkLabelCellModel
    Inherits GridStaticCellModel

    Protected Sub New(ByVal info As SerializationInfo, ByVal context As StreamingContext)
        MyBase.New(info, context)
    End Sub

    Public Sub New(ByVal grid As GridModel)
        MyBase.New(grid)
        AllowFloating = False
    End Sub

    ' Override CreateRenderer Method to create a CellRenderer object.
    Public Overloads Overrides Function CreateRenderer(ByVal control As GridControlBase) As GridCellRendererBase
        Return New LinkLabelCellRenderer(Control, Me)
    End Function
End Class
```

## 4.1.4.3.2 GridCellRendererBase

The class derived from the GridCellRendererBase handles the drawing of the cell and the user interaction aspect of the cell architecture. It takes care of things like the handling of the mouse and keyboard messages. Some of the virtual members you might override are listed in the following table.

| Virtual Method         | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| OnInitialize(int rowIndex, int colIndex) | Override this method if you need to do any initialization for the current cell. One primary use of this method is to move state information from the GridStyleInfo object to the cell control. |

## Page-level Navigation/TOC (if applicable)
- **[Edit] This section should be populated if the provided image contains a local Table of Contents or similar navigation elements.**

## Cross References
- **[Edit] This section should be populated if the provided image contains cross-references to other sections, modules, or related content.**

<!-- tags: Essential Grid for Windows Forms, GridCellRendererBase, LinkLabelCellRenderer, LinkLabelCellModel, GridStyleInfo, GridModel, GridControlBase keywords: GridCellRendererBase, OnInitialize, LinkLabelCellRenderer, LinkLabelCellModel -->