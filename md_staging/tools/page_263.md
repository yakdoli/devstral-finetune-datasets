```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_263.jpeg
document_name: tools
page_number: 263
page_id: tools#page_263
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:02:28Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Content

### 3.4.4.5.2 How to display context menu of a docked control at a specified point?

This can be done using ShowMenu method.

| **Method**    | **Description**                                                                                                         |
|---------------|-------------------------------------------------------------------------------------------------------------------------|
| ShowMenu      | Show's the docking caption context menu at the specified point (Pt). The parameters are, <br> <br> Ctrl - Indicates the control for which dock / floating state is been queried. <br> Pt - Indicates the location of the menu to be displayed. |

#### C#

```csharp
private void button1_Click(object sender, EventArgs e)
{
    this.dockingManager1.ShowMenu(this.listBox1, new Point(100, 100));
}
```

#### VB.NET

```vb
Private Sub button1_Click(ByVal sender As Object, ByVal e As System.EventArgs)
    Me.dockingManager1.ShowMenu(Me.listBox1, New Point(100, 100))
End Sub
```

### 3.4.4.6 Floating

This section covers the below topics.

#### 3.4.4.6.1 How to find out whether a docked control is floating or not?

This can be achieved by calling IsFloating method.

This method returns a value indicating whether the control is in docked or floating state. If the control is in floating state, the value returned will be true, and if it is docked, value returned will be false.

## Page-level Navigation/TOC (if applicable)
- **3.4.4.5.2 How to display context menu of a docked control at a specified point?**
- **3.4.4.6 Floating**
  - **3.4.4.6.1 How to find out whether a docked control is floating or not?**

<!-- tags: [syncfusion-windows-forms, showmenu, floating-state, docked-control, context-menu] keywords: [syncfusion, winforms, tools, context menu, docked control, floating state, workshop] -->
```