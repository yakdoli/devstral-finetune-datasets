```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_240.jpeg
document_name: edit
page_number: 240
page_id: edit#page_240
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:08:01Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- This section explains the **CodeSnippetEvent** handling in Windows Forms. It includes handling the activation and deactivation events of code snippets.
- Covers the **CodeSnippetActivating** and **CodeSnippetDeactivating** events, discussing their arguments and handling techniques in C# and VB.NET.

## Content

### 4.14.3.2 CodeSnippetDeactivating Event

This event occurs when the code snippet is to be deactivated.

#### Event Handler Details
The event handler receives an argument of type **CodeSnippetsEventArgs**. The following **CodeSnippetsEventArgs** member provides information specific to this event.

#### Table: CodeSnippetsEventArgs Member Information

| Member            | Description                     |
|-------------------|----------------------------------|
| **CodeSnippet**   | Code snippet that is currently activated. |

#### C# Example

```csharp
[C#]

private void editControl1_CodeSnippetDeactivating(object sender,
Syncfusion.Windows.Forms.Edit.CodeSnippetsEventArgs e)
{
    // The below line will be displayed in the output window at runtime.
    Console.WriteLine(" CodeSnippetDeactivating event is raised ");
}
```

#### VB.NET Example

```vb
[VB.NET]

Private Sub editControl1_CodeSnippetDeactivating(ByVal sender As Object,
ByVal e As Syncfusion.Windows.Forms.Edit.CodeSnippetsEventArgs)
    ' The below line will be displayed in the output window at runtime.
    Console.WriteLine(" CodeSnippetDeactivating event is raised ")
End Sub
```

### CodeSnippetActivating Event Example

#### VB.NET Code

```vb
[VB.NET]

Private Sub editControl1_CodeSnippetActivating(ByVal sender As Object, ByVal e As Syncfusion.Windows.Forms.Edit.CancellableCodeSnippetsEventArgs)
    ' The below line will be displayed in the output window at runtime.
    Console.WriteLine(" CodeSnippetActivating event is raised ")
End Sub
```

## API Reference

- **Namespace:** Syncfusion.Windows.Forms.Edit
- **Event:** CodeSnippetDeactivatingEventArgs
  - **Argument Type:** CodeSnippetsEventArgs
    - **Member:** CodeSnippet
      - Description: Code snippet that is currently activated.

## Code Examples

- **C# Example for CodeSnippetDeactivating Event**
  ```csharp
  // Code example omitted for brevity.
  ```
- **VB.NET Example for CodeSnippetDeactivating Event**
  ```vb
  ' Example code omitted for brevity.
  ```

## Cross References
- **See also:**
  - [Code Snippet Handling in Windows Forms](#anchor)

<!-- tags: [syncfusion, windowsforms, code snippets, events, codeSnippetDeactivating, codeSnippetActivating] keywords: [code snippet, deactivation, activation, event handling, windows forms, C#, VB.NET] -->
```