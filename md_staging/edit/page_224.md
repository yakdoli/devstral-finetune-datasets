```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_224.jpeg
document_name: edit
page_number: 224
page_id: edit#page_224
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:06:58Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

This event occurs in `FindNext()` when search reaches the starting point of the search before the message box displays.

## Overview
- The event handler receives an argument of **`FindCompleteEventArgs`**.
- This argument class sets the text for the message box.
- Users can localize this text.

## Content

### Code Examples

#### [C#]

```csharp
// Handle the FindComplete event.
this.FindComplete += new EventHandler<FindCompleteEventArgs>(FindDialogExt_FindComplete);

// Set the value for message box for when search reaches the starting point of search
void FindDialogExt_FindComplete(object sender, frmFindDialog.FindCompleteEventArgs e)
{
    // Arabic text as message (localize)
    if (messageString != string.Empty)
        e.Message = "إنتهى";
    else
        e.Message = "Find reached the starting point of the search.";
}
```

#### [VB.NET]

```vb
' Handle the FindComplete event.
Private Me.editControl.FindComplete += New EventHandler(Of
    FindCompleteEventArgs)(AddressOf FindDialogExt_FindComplete)

' Set the value for message box for when search reaches the starting point of search
Private Sub FindDialogExt_FindComplete(ByVal sender As Object, ByVal e As
    frmFindDialog.FindCompleteEventArgs)
    ' Arabic text as message (localize)
    If messageString <> String.Empty Then
        e.Message = "إنتهى"
    Else
        e.Message = "Find reached the starting point of the search."
    End If
End Sub
```

## Page-level Navigation/TOC
- **Overview**
  - Description of the event occurring in `FindNext()`
  - Explanation of the event handler and its argument
  - Localizing the text for the message box
- **Content**
  - **Code Examples**
    - **C#**
    - **VB.NET**

## Cross References
- Related concepts and references within the documentation can be explored for further information.

<!-- tags: [Syncfusion Winforms, FindCompleteEventArgs, Localization, Event Handler, Message Box, Code Examples] keywords: [FindNext, C#, VB.NET, Localization, Event Handling, MessageBox, WinForms, Essential Edit] -->
```