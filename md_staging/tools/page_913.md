```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_913.jpeg
document_name: tools
page_number: 913
page_id: tools#page_913
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:42:01Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Content

### `TextAlignChanged` Event

- **C#:**
  ```csharp
  private void textBoxExt1_TextAlignChanged(object sender, EventArgs e)
  {
      Console.WriteLine(" TextAlignChanged event is raised ");
  }
  ```

- **VB.NET:**
  ```vb
  Private Sub textBoxExt1_TextAlignChanged(ByVal sender As Object, ByVal e As EventArgs)
      Console.WriteLine(" TextAlignChanged event is raised ")
  End Sub
  ```

### `ThemesEnabledChanged` Event

- **Description:**
  This event occurs when the `ThemesEnabled` property is changed. The `ThemesEnabled` property specifies whether or not to use XP Themes when the `BorderStyle` property is set to `'Fixed3D'`.

- **Event Handler:**
  The event handler receives an argument of type `EventArgs` containing data related to this event.

- **C#:**
  ```csharp
  private void textBoxExt1_ThemesEnabledChanged(object sender, EventArgs e)
  {
      Console.WriteLine(" ThemesEnabledChanged event is raised ");
  }
  ```

- **VB.NET:**
  ```vb
  Private Sub textBoxExt1_ThemesEnabledChanged(ByVal sender As Object, ByVal e As EventArgs)
      Console.WriteLine(" ThemesEnabledChanged event is raised ")
  End Sub
  ```

### Revamping of Editors Controls

- **Overview:**
  The controls `DoubleTextBox`, `IntegerTextBox`, `PercentTextBox`, and `CurrencyTextBox` have been revamped. Details of the revamping and the changes in the behavior and properties are described here.

## API Reference

- **Event Handlers:**
  - `TextAlignChanged`
  - `ThemesEnabledChanged`

## Code Examples

### C# Example
```csharp
// Example of handling TextAlignChanged event
private void textBoxExt1_TextAlignChanged(object sender, EventArgs e)
{
    Console.WriteLine(" TextAlignChanged event is raised ");
}
```

### VB.NET Example
```vb
' Example of handling ThemesEnabledChanged event
Private Sub textBoxExt1_ThemesEnabledChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine(" ThemesEnabledChanged event is raised ")
End Sub
```

## Cross References

- For more information on the revamped controls, refer to the specific sections on `DoubleTextBox`, `IntegerTextBox`, `PercentTextBox`, and `CurrencyTextBox`.

<!-- tags: [syncfusion, winforms, event, textalignchanged, themesenabledchanged, editors controls, revamping, textbox] keywords: [themesenabled, textalignchanged, event handler, fixed3d, doubletextbox, integertextbox, percenttextbox, currencytextbox] -->
```