```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_269.jpeg
document_name: edit
page_number: 269
page_id: edit#page_269
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:10:44Z
fidelity: lossless
-->

## 4.14.23 SingleLineChanged Event

### Overview
- Discusses the `SingleLineChanged` event, which is fired when the `SingleLineMode` property changes.
- Explains the `SingleLineMode` property and its role in enabling the single line mode.

### Content

#### Overview of SingleLineChanged Event
This event is fired when the value of the `SingleLineMode` property is changed. The `SingleLineMode` property specifies whether the single line mode is enabled.

##### Event Handler
The event handler receives an argument of type `EventArgs`.

##### C# Code Example
```csharp
// Handle the SingleLineChanged event.
this.editControl1.SingleLineChanged += new EventHandler(editControl1_SingleLineChanged);

// Set the SingleLineMode property to True.
this.editControl1.SingleLineMode = true;

private void editControl1_SingleLineChanged(object sender, EventArgs e)
{
    // The below statement can be seen in the output window at runtime.
    Console.WriteLine(" SingleLineChanged event is raised ");
}
```

##### VB.NET Code Example
```vb
' Handle the SingleLineChanged event.
AddHandler Me.editControl1.SingleLineChanged, AddressOf editControl1_SingleLineChanged

' Set the SingleLineMode property to True.
Me.editControl1.SingleLineMode = True

Private Sub editControl1_SingleLineChanged(ByVal sender As Object, ByVal e As EventArgs)
    ' The below statement can be seen in the output window at runtime.
    Console.WriteLine(" SingleLineChanged event is raised ")
End Sub
```

### 4.14.24 Text Events

#### Overview of Text Events
This section discusses the following text events:

- **TextChanged**

<!-- tags: SingleLineChanged Event, Text Events, SingleLineMode, WinForms, Syncfusion, C#, VB.NET, EventHandler, Event Args, TextChanged -->
```