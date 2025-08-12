<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_240.jpeg
document_name: tools
page_number: 240
page_id: tools#page_240
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:54:45Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### 3.4.4.1.2 How to change the dock tab alignment?

This can be controlled by setting the DockTabAlignment property which is discussed in Tabbed Docking topic.

### 3.4.4.1.3 How to detect the docking style assigned to a control?

You can detect the Docking style that is assigned to the control, at run time, using GetDockingStyle method.

| Method            | Description                                                                                                                                                                                                                                                                                                                                                         |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GetDockingStyle   | Returns the current docking style of the control. <br> The return value for this method would be docking style value, that specifies the dock type / position. The docked control for which the dock style is to be identified should be passed as a parameter to this method. The parameter is, <br> Ctrl - Indicates the docked control for which the DockStyle needs to be retrieved. |

#### [C#]

```csharp
//Getting the docking style
private void button1_Click(object sender, EventArgs e)
{
    this.dockingManager1.GetDockStyle(this.panel1);
    Console.Write("Dock style :" + this.dockingManager1.GetDockStyle(this.panel1));
}
```

#### [VB.NET]

```vb
'Getting the docking style
Private Sub button1_Click(ByVal sender As Object, ByVal e As System.EventArgs)
    Me.dockingManager1.GetDockStyle(this.panel1)
    Console.Write("Dock style :" + this.dockingManager1.GetDockStyle(this.panel1))
End Sub
```

### 3.4.4.1.4 How to Enable the Tabbed Style Dockable Window using TabbedMDI manager?

<!-- tags: [syncfusion, winforms, tools, tabbed docking, essential tools, dock tab alignment, docking style, tabbed style, dockable window] keywords: [DockTabAlignment, GetDockingStyle, TabbedMDI] -->