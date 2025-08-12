```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_273.jpeg
document_name: edit
page_number: 273
page_id: edit#page_273
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:10:57Z
fidelity: lossless
-->

## LineInserted Event

### Overview
- The `LineInserted` event is triggered when a new line is inserted in the `Edit` control.
- Handles the event with specific code examples for both C# and VB.NET.

### Content

#### LineInserted Event Handling

##### C#

```csharp
// Handle the LineInserted event.
this.editControl1.LineInserted += new 
Syncfusion.Windows.Forms.Edit.LineInsertedEventHandler(editControl1_LineInserted);

void editControl1_LineInserted(object sender, Syncfusion.Windows.Forms.Edit.LinesEventArgs e)
{
    // The following statement can be seen in the output window at run time.
    Console.WriteLine("Line Inserted");
}
```

##### VB.NET

```vb
' Handle the LineInserted event.
AddHandler Me.editControl1.LineInserted, AddressOf Me.editControl1_LineInserted

Private Sub editControl1_LineInserted(ByVal , As objectsender, ByVal e As Syncfusion.Windows.Forms.Edit.LinesEventArgs)
    ' The following statement can be seen in the output window at run time.
    Console.WriteLine("Line Inserted")
End Sub
```

### API Reference

- **Event**: `LineInserted`
  - **Namespace**: `Syncfusion.Windows.Forms.Edit`
  - **Interface**: `IEditControl`
  - **Signature**:
    ```csharp
    public event LineInsertedEventHandler LineInserted;
    ```
    ```vb
    Public Event LineInserted(sender As Object, e As LinesEventArgs)
    ```
  - **Parameters**:
    - `sender`: Type `object`, the object that raises the event.
    - `e`: Type `LinesEventArgs`, the event data.

### Code Examples

#### C#

```csharp
this.editControl1.LineInserted += (sender, e) => 
{
    Console.WriteLine("Line Inserted");
};
```

#### VB.NET

```vb
AddHandler Me.editControl1.LineInserted,
    Sub(sender As Object, e As LinesEventArgs)
        Console.WriteLine("Line Inserted")
    End Sub
```

### Page-level Navigation/TOC
- [4.14.24.3.2 LineInserted](#lineinserted-event)

### Cross References
- See also: `LinesEventArgs`, `EditControl`, `EventHandler`

<!-- tags: [Syncfusion Winforms, LineInserted Event, C#, VB.NET, Edit Control] keywords: [LineInserted, Event Handler, Edit, Syncfusion, Windows Forms, .NET] -->
```