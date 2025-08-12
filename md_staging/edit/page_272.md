```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_272.jpeg
document_name: edit
page_number: 272
page_id: edit#page_272
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:10:08Z
fidelity: lossless
-->

## Content

### Overview
- The `LineChanged` event is triggered when any line is modified in the `Edit` control.
- Demonstrates handling the `LineChanged` event in C# and VB.NET.

### 4.14.24.3.1 Line Changed
The `LineChanged` event will be fired when any line is modified in the `Edit` control.

#### [C#]

```csharp
// Handle the LineChanged event.
this.editControl.LineChanged += new Syncfusion.Windows.Forms.Edit.TextChangingEventHandler(editControl1_LineChanged);

void editControl1_LineChanged(object sender, Syncfusion.Windows.Forms.Edit.TextChangingEventArgs e)
{
    // The following statement can be seen in the output window at run time.
    Console.WriteLine("Line Changed");
}
```

#### [VB.NET]

```vb.net
' Handle the LineChanged event.
AddHandler Me.editControl.LineChanged, AddressOf Me.editControl1_LineChanged

Private Sub editControl1_LineChanged(ByVal , As objectsender, ByVal e As Syncfusion.Windows.Forms.Edit.TextChangingEventArgs)
    ' The following statement can be seen in the output window at runtime.
    Console.WriteLine("Line Changed")
End Sub
```

## API Reference

### Events
- **LineChanged**:
  - **Type**: `TextChangingEventHandler`
  - **Description**: Triggered when any line is modified in the `Edit` control.
  - **Parameters**:
    - `sender`: The source of the event.
    - `e`: Event data containing details of the text change.

## Code Examples

### C# Example
```csharp
this.editControl.LineChanged += new Syncfusion.Windows.Forms.Edit.TextChangingEventHandler(editControl1_LineChanged);

void editControl1_LineChanged(object sender, Syncfusion.Windows.Forms.Edit.TextChangingEventArgs e)
{
    Console.WriteLine("Line Changed");
}
```

### VB.NET Example
```vb.net
AddHandler Me.editControl.LineChanged, AddressOf Me.editControl1_LineChanged

Private Sub editControl1_LineChanged(ByVal , As objectsender, ByVal e As Syncfusion.Windows.Forms.Edit.TextChangingEventArgs)
    Console.WriteLine("Line Changed")
End Sub
```

<!-- tags: [Syncfusion, Winforms, LineChanged, Edit control, event handling, C#, VB.NET] keywords: [LineChanged event, text modification, Syncfusion.Windows.Forms.Edit, event handler, text control, runtime output] -->
```