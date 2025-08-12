```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_238.jpeg
document_name: tools
page_number: 238
page_id: tools#page_238
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:54:47Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Content

### Table: Member Details

| Member          | Description                                |
|-----------------|--------------------------------------------|
| PersistenceID   | Lets you specify a unique ID.             |

### C# Example

```csharp
//Lets you specify a unique ID used to distinguish the persistence 
//information of different 
//instances of the Form type.
protected void DockingManager_ProvidePersistenceID(object sender, Syncfusion.Windows.Forms.ProvidePersistenceIDEventArgs e)
{
    Console.WriteLine("Provide Persistence ID Event has been raised");
    Syncfusion.Windows.Forms.Tools.DockingManager dm = sender as DockingManager;
    Console.WriteLine("Host control name = " + dm.HostControl.Name.ToString());
    //The docking state stores in a place named as that Host control name.
    e.PersistenceID = dm.HostControl.Name.ToString();
}
```

### VB.NET Example

```vb
'Lets you specify a unique ID used to distinguish the persistence 
'information of different 
'instances of the Form type.
Protected Sub DockingManager_ProvidePersistenceID(ByVal sender As Object, ByVal e As Syncfusion.Windows.Forms.ProvidePersistenceIDEventArgs)
    Console.WriteLine("Provide Persistence ID Event has been raised")
    Dim dm As Syncfusion.Windows.Forms.Tools.DockingManager = CType(ConversionHelpers.AsWorkaround(sender, GetType(DockingManager)), DockingManager)
    Console.WriteLine("Host control name = " & dm.HostControl.Name.ToString)
    'The docking state stores in a place named as that Host control name.
    e.PersistenceID = dm.HostControl.Name.ToString
End Sub
```

### 3.4.4 Frequently Asked Questions

This section will help you become more familiar in using the Docking Windows Package.

## Footer

© 2013 Syncfusion. All rights reserved.
**Page 238**
<!-- tags: [product, Winforms, Docking Windows Package, toolset, control, winform] keywords: [Docking Windows Package, frequently asked questions, unique ID, persistenceID, form type, host control, persistence information, DockingManager] -->
```