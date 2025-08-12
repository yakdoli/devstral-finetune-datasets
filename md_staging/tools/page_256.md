```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_256.jpeg
document_name: tools
page_number: 256
page_id: tools#page_256
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:01:40Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Extracting and Managing Controls

#### WinForms Code Examples

- **C# Example**
```csharp
// Getting the Controls into an ArrayList.
IEnumerator ienum = this.dockingManager.Controls;
ArrayList dockedctrls = new ArrayList();
while (ienum.MoveNext())
    dockedctrls.Add(ienum.Current);
// Iterating through the collection to perform the required operation.
foreach (Control ctrl in dockedctrls)
{
    // Disabling the docking and disposing control.
    this.dockingManager.SetEnableDocking(ctrl, false);
    ctrl.Dispose();
}
```

- **VB.NET Example**
```vb
' Getting the Controls into an ArrayList.
Dim ienum As IEnumerator = Me.dockingManager.Controls
Dim dockedctrls As ArrayList = New ArrayList()
Do While ienum.MoveNext()
    dockedctrls.Add(ienum.Current)
Loop
' Iterating through the collection to perform the required operation.
For Each ctrl As Control In dockedctrls
    ' Disabling the docking and disposing control.
    Me.dockingManager.SetEnableDocking(ctrl, False)
    ctrl.Dispose()
Next ctrl
```

<!-- tags: [Windows Forms, ArrayList, Controls, Docking, Disposing] keywords: [DockingManager, Controls, EnableDocking, Dispose, ArrayList, C#, VB.NET] -->
```