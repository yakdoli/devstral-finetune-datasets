```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_256.jpeg
document_name: edit
page_number: 256
page_id: edit#page_256
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:08:58Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

```csharp
{
    // The below statement can be seen in the output window at runtime.
    Console.WriteLine(" InsertModeChanged event is raised ");
}
```

**[VB.NET]**

```vbnet
' Handle the InsertModeChanged event.
AddHandler Me.editControl1.InsertModeChanged, AddressOf editControl1_InsertModeChanged

' Set the value of the InsertMode property.
Me.editControl1.InsertMode = False

Private Sub editControl1_InsertModeChanged(ByVal sender As Object, ByVal e As EventArgs)
    ' The below statement can be seen in the output window at runtime.
    Console.WriteLine(" InsertModeChanged event is raised ")
End Sub
```

## 4.14.12 LanguageChanged Event

This event occurs when the current parser language is changed.

The event handler receives an argument of type **EventArgs**.

**[C#]**

```csharp
private void editControl1_LanguageChanged(object sender, EventArgs e)
{
    Console.WriteLine(" LanguageChanged event is raised ");
}
```

**[VB.NET]**

```vbnet
Private Sub editControl1_LanguageChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine(" LanguageChanged event is raised ")
End Sub
```

## API Reference

**Namespace:** [Details not provided in the snippet].

**Class:** [Details not provided in the snippet].

**Event:** LanguageChanged

### Parameters

- **sender:** Type: object  
  The source of the event.

- **e:** Type: EventArgs  
  The event data.

### Returns

None.

### Exceptions

Not applicable in the context of the snippet.

## Code Examples

**C# Example:**

```csharp
private void editControl1_LanguageChanged(object sender, EventArgs e)
{
    Console.WriteLine(" LanguageChanged event is raised ");
}
```

**VB.NET Example:**

```vbnet
Private Sub editControl1_LanguageChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine(" LanguageChanged event is raised ")
End Sub
```

<!-- tags: [product, module, control, api, version?] keywords: [k1, k2, ...] -->
```