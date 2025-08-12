```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_243.jpeg
document_name: edit
page_number: 243
page_id: edit#page_243
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:08:29Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

```csharp
End Sub
```

## 4.14.4 ConfigurationChanged Event

This event is fired on changing the configuration of the Edit Control. Configuration can be set for the Edit Control using the `ApplyConfiguration` method.

The event handler receives an argument of type `EventArgs`.

### C#

```csharp
this.editControl.ConfigurationChanged += new
EventHandler(editControl_ConfigurationChanged);
this.editControl.ApplyConfiguration("XML");

private void editControl_ConfigurationChanged(object sender, EventArgs e)
{
    this.editControl.ApplyConfiguration("XML");
}
```

### VB.NET

```vb
AddHandler Me.editControl.ConfigurationChanged, AddressOf
editControl_ConfigurationChanged
Me.editControl.ApplyConfiguration("XML")

Private Sub editControl_ConfigurationChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine(" ConfigurationChanged event is raised ")
End Sub
```

## 4.14.5 Collapse Events

This section discusses the below given collapse events.

### 4.14.5.1 CollapsedAll Event

``` 
© 2013 Syncfusion. All rights reserved.  
```
``` 
Page 243  
```
