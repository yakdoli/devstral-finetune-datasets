```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_239.jpeg
document_name: tools
page_number: 239
page_id: tools#page_239
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:56:13Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### 3.4.4.1 General

This section covers the following topics:

#### 3.4.4.1.1 How to activate a particular docked control?

You can call the ActivateControl method inside NewDockStateEndLoad event to achieve this.

| Methods        | Description                                                                                                                                                                                                 |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ActivateControl | Activates the docked control which is passed as a parameter to this method. This method will be effective only when the control is tabbed to other control or controls. This method can be called from a handler for DockingManager.NewDockStateEndLoad Event. The parameter is, <br> <br> Ctrl - Indicates the docking window. |

**[C#]**

```csharp
//The NewDockStateEndLoad event occurs immediately after a new dock state has been loaded.
private void dockingManager1_NewDockStateEndLoad(object sender, System.EventArgs e)
{
    this.dockingManager1.ActivateControl(this.listBox1);
    Console.WriteLine("Listbox is activated");
}
```

**[VB.NET]**

```vbnet
'The NewDockStateEndLoad event occurs immediately after a new dock state has been loaded.
Private Sub dockingManager1_NewDockStateEndLoad(ByVal sender As Object, ByVal e As System.EventArgs)
    Me.dockingManager1.ActivateControl(Me.listBox1)
    Console.WriteLine("Listbox is activated")
End Sub
```

<!-- tags: [Syncfusion, Winforms, Essential Tools, Docked Controls, NewDockStateEndLoad, ActivateControl] keywords: [C#, VB.NET, dock state, tabbed controls, event handler, Listbox, ActiveControl] -->
```