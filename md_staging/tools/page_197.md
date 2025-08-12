```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_197.jpeg
document_name: tools
page_number: 197
page_id: tools#page_197
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:26:18Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates how to work with docking behaviors for MDI (Multiple Document Interface) child forms in WinForms using Syncfusion controls.
- Shows examples in both C# and VB.NET for managing docking and MDI forms.

### Layout
- **Stores a set of four integers** that represents the location and size of a rectangle.

## Content

### C#
```csharp
private void button1_Click(object sender, System.EventArgs e)
{
    // Sets the panel1 as child form for the MDI form
    this.dockingManager1.SetAsMDIChild(this.panel1, true);
}

private void button2_Click(object sender, System.EventArgs e)
{
    // Sets the MDI child form to the normal Docking window.
    this.dockingManager1.SetAsMDIChild(this.panel1, false);
}

// Overloaded
private void button1_Click(object sender, System.EventArgs e)
{
    // Sets the panel1 as child form for the MDI form
    this.dockingManager1.SetAsMDIChild(listBox1, true, new Rectangle(200, 400, 500, 300));
}

private void button2_Click(object sender, System.EventArgs e)
{
    // Sets the MDI child form to the normal Docking window.
    this.dockingManager1.SetAsMDIChild(listBox1, true, new Rectangle(200, 400, 500, 300));
}
```

### VB.NET
```vb
Private Sub button1_Click(ByVal sender As Object, ByVal e As System.EventArgs) Handles button1.Click
    ' Sets the panel1 as child form for the MDI form
    Me.dockingManager1.SetAsMDIChild(Me.panel1, True)
End Sub

Private Sub button2_Click(ByVal sender As Object, ByVal e As System.EventArgs) Handles button2.Click
    ' Sets the MDI child form to the normal Docking window.
    Me.dockingManager1.SetAsMDIChild(Me.panel1, False)
End Sub
```

## API Reference (if applicable)
- `SetAsMDIChild`: Exposes the functionality to set a child form as an MDI child or revert it to the normal Docking window.
  - **Parameters**:
    - `control`: The control or child form to be set as MDI child or altered for docking.
    - `asMDIChild`: Boolean flag to determine whether the control should be treated as an MDI child.
    - `region`: Optional `Rectangle` to specify location and size.

## Code Examples
The above examples demonstrate how to use the `SetAsMDIChild` method in both C# and VB.NET to control the docking behavior of MDI child forms.

## Cross References
- For further details on MDI windows and docking, refer to the documentation on Syncfusion's official website.
- Additional resources can be found in the Syncfusion WinForms documentation.

<!-- tags: [Syncfusion WinForms, MDI, Docking, Window Layout, Multiple Document Interface] keywords: [SetAsMDIChild, MDI, Docking, Layout, Rectangle, C#, VB.NET] -->
```
