```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_268.jpeg
document_name: edit
page_number: 268
page_id: edit#page_268
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:09:47Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- This section discusses the `ScrollEventArgs` and `SelectionChanged` events in the context of WinForms, providing code examples in C# and VB.NET.
- It explains the properties of the `ScrollEventArgs` class and includes examples for handling the Vertical Scroll event.
- Additionally, it covers the `SelectionChanged` event with examples for handling text selection changes.

## Content

### ScrollEventArgs Properties

| Property       | Description                                                                                     |
|----------------|-------------------------------------------------------------------------------------------------|
| NewValue       | Gets / sets the new System.Windows.Forms.ScrollBar.Value for the scrollbar.                     |
| OldValue       | Gets / sets the old System.Windows.Forms.ScrollBar.Value for the scrollbar.                     |
| ScrollOrientation | Gets the scrollbar orientation that raised the scroll event.               |
| Type           | Gets the type of scroll event that occurred.                                                   |

### Handling Vertical Scroll Event

#### Example in C#

```csharp
private void editControl1_VerticalScroll(object sender, ScrollEventArgs e)
{
    Console.WriteLine("VerticalScroll event is raised ");
}
```

#### Example in VB.NET

```vb
Private Sub editControl1_VerticalScroll(ByVal sender As Object, ByVal e As ScrollEventArgs)
    Console.WriteLine("VerticalScroll event is raised ")
End Sub
```

### SelectionChanged Event

#### Overview

This event is raised when text selection has been changed.

- The event handler receives an argument of type `EventArgs`.

#### Example in C#

```csharp
private void editControl1_SelectionChanged(object sender, EventArgs e)
{
    MessageBox.Show("SelectionChanged event is raised ");
}
```

#### Example in VB.NET

```vb
Private Sub editControl1_SelectionChanged(ByVal sender As Object, ByVal e As EventArgs)
    MessageBox.Show("SelectionChanged event is raised ")
End Sub
```

## API Reference

- **`ScrollEventArgs` Class:**
  - **Properties:**
    - `NewValue`: Gets or sets the new scroll bar value.
    - `OldValue`: Gets or sets the old scroll bar value.
    - `ScrollOrientation`: Gets the orientation of the scrollbar.
    - `Type`: Gets the scroll event type.

- **`EventArgs` Class:**
  - Basic event arguments class used for the `SelectionChanged` event.

## Code Examples

- **Handling Scroll Events:**
  - **C#:**
    ```csharp
    private void editControl1_VerticalScroll(object sender, ScrollEventArgs e)
    {
        Console.WriteLine("VerticalScroll event is raised ");
    }
    ```

  - **VB.NET:**
    ```vb
    Private Sub editControl1_VerticalScroll(ByVal sender As Object, ByVal e As ScrollEventArgs)
        Console.WriteLine("VerticalScroll event is raised ")
    End Sub
    ```

- **Handling Selection Changed Event:**
  - **C#:**
    ```csharp
    private void editControl1_SelectionChanged(object sender, EventArgs e)
    {
        MessageBox.Show("SelectionChanged event is raised ");
    }
    ```

  - **VB.NET:**
    ```vb
    Private Sub editControl1_SelectionChanged(ByVal sender As Object, ByVal e As EventArgs)
        MessageBox.Show("SelectionChanged event is raised ")
    End Sub
    ```

<!-- tags: [product, module, control, api, version?] keywords: [winforms, selectionchanged event, scroll events, scrollargs, eventargs, csharp, vb.net, examples] -->
```