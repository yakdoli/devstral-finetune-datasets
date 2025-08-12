```html
<!--  
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_156.jpeg
document_name: tools
page_number: 156
page_id: tools#page_156
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:57:31Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

Docking manager can display a super tooltip by enabling the **DockingManager.EnableSuperTooltip** property. For this, a **SuperTooltip** control should be dragged and dropped onto the form, and it should be selected in the **DockingManager.SuperTooltip** property.

## Properties of DockingManager

| DockingManager Property            | Description                                                                 |
|-------------------------------------|-----------------------------------------------------------------------------|
| EnableSuperTooltip                  | Gets/Sets whether to enable SuperToolTip using the dock caption buttons. |
| SuperToolTip                        | Indicates the SuperToolTip associated with the docking manager.            |

## Adding SuperTooltip Programmatically

A SuperTooltip can be added to the docking manager programmatically using the following code snippet.

```csharp
this.dockingManager1.EnableSuperToolTip = true;
this.dockingManager1.SuperToolTip = this.superToolTip1;
```

```vbnet
Me.dockingManager1.EnableSuperToolTip = True
Me.dockingManager1.SuperToolTip = Me.superToolTip1
```

### Figure: SuperToolTip added to the Docking Manager

![SuperToolTip added to the Docking Manager](https://via.placeholder.com/150 "SuperToolTip added to the Docking Manager")

**Figure 71: SuperToolTip added to the Docking Manager**

Text for the super tooltip and other customizing options can be specified for a particular button by using the **CaptionButton Collection Editor**.

## Page-level Navigation/TOC (if applicable)

- **Essential Tools for Windows Forms**
  - **Adding SuperTooltip Programmatically**
  - **CaptionButton Collection Editor**

## Cross References

See also:
- DockingManager.EnableSuperTooltip
- DockingManager.SuperTooltip
- CaptionButton Collection Editor
<!-- tags: [DockingManager, SuperTooltip, CaptionButton, CollectionEditor, WinForms, Syncfusion] keywords: [EnableSuperTooltip, SuperToolTip, CaptionButton, AddSuperTooltip, Programmatic, DesignTime, Runtime] -->
```
