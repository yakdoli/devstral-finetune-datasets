```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_248.jpeg
document_name: tools
page_number: 248
page_id: tools#page_248
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:01:07Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

```vbnet
Object, ByVal e As EventArgs)
    count = 0
    Dim ienum As IEnumerator = Me.dockingManager1.Controls
    dockedctrls = New ArrayList()

    While ienum.MoveNext()
        dockedctrls.Add(ienum.Current)
    End While

    For Each dockedControl As Control In dockedctrls
        GetDockingRelationship(dockedControl)
        count = count + 1
    Next
End Sub
```

## How to get or set the dock ability for a control?

The current dock ability for the controls can be retrieved or set using the below methods.

| Methods         | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| GetDockAbility   | Retrieves the dock ability of the control. The parameter is, <br> Ctrl - Indicates the docked control for which DockAbility has to be obtained. |
| SetDockAbility   | Sets the dock ability of the control. <br> Ctrl - Indicates the docked control for which DockAbility need to be set. |

### C#

```csharp
// Getting the Dock Ability
this.dockingManager1.GetDockAbility(this.panel2);

// Setting the Dock Ability
this.dockingManager1.SetDockAbility(this.panel2, "Bottom, Horizontal");
```

### VB.NET

```vbnet
' Getting the Dock Ability
this.dockingManager1.GetDockAbility(this.panel2)

' Setting the Dock Ability
this.dockingManager1.SetDockAbility(this.panel2, "Bottom, Horizontal")
```

<!-- tags: [Syncfusion, Winforms, DockManager, DockingControls, ControlDockability] keywords: [DockAbility, DockedControls, GetDockAbility, SetDockAbility, dockedctrls] -->
```