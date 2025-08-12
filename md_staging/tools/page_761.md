```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_761.jpeg
document_name: tools
page_number: 761
page_id: tools#page_761
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:32:06Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

The event handler receives an argument of type `EventArgs` containing data related to this event.

### Event Handler Example

#### C#

```csharp
private void integerTextBox1_IntegerValueChanged(object sender, EventArgs e)
{
    Console.WriteLine(" IntegerValueChanged event is raised ");
}
```

#### VB.NET

```vb
Private Sub integerTextBox1_IntegerValueChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine(" IntegerValueChanged event is raised ")
End Sub
```

## Special Event: SetNullThis

**3.5.8.4.4.5 SetNullThis**

This event occurs when the NULL state is to be set based on a value.

The event handler receives an argument of type `SetNullEventArgs` containing data related to this event. The following `SetNullEventArgs` members provide information specific to this event.

### Members of SetNullEventArgs

| Members    | Description                                                                 |
|------------|-----------------------------------------------------------------------------|
| Cancel     | Gets / sets a value indicating whether the event should be canceled.      |
| NullValue  | Returns the NULL value.                                                    |

### Event Handler Example for SetNull

#### C#

```csharp
private void integerTextBox1_SetNull(object sender, Syncfusion.Windows.Forms.Tools.SetNullEventArgs e)
{
    Console.WriteLine(" SetNull event is raised ");
}
```

#### VB.NET

```vb
Private Sub integerTextBox1_SetNull(ByVal sender As Object, ByVal e As Syncfusion.Windows.Forms.Tools.SetNullEventArgs)
    Console.WriteLine(" SetNull event is raised ")
End Sub
```

## Copyright

© 2013 Syncfusion. All rights reserved. | Page 761
```