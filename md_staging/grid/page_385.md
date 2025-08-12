```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_385.jpeg
document_name: grid
page_number: 385
page_id: grid#page_385
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:13:45Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates how to customize the title of the NamedRange Collection Editor dialog box.
- Uses event handling to dynamically set the dialog box title based on specific criteria.
- Includes code example for setting the title to "CashFlow Inputs" for the ShowNamedRange dialog.

## Content

### Customizing the NamedRange Collection Editor Title

The following code snippet illustrates how to change the title of the NamedRange Collection Editor dialog box:

```vb
Private GridFormulaNamedRangesEditHelper.ShowingNamedRangesDialog += _
    New ControlEventHandler(AddressOf helper_ShowingNamedRangesDialog)

' Event handler to change the title of NamedRange Collection Editor dialog box.
Private Sub helper_ShowingNamedRangesDialog(ByVal sender As Object, ByVal e As ControlEventArgs)
    Dim f As Form = TryCast(e.Control, Form)
    If f IsNot Nothing Then

        ' Set the title for the dialog box.
        f.Text = "CashFlow Inputs"
    End If
End Sub
```

#### Explanation:
1. **Event Subscription**: The `ShowingNamedRangesDialog` event is subscribed to using a `ControlEventHandler`.
2. **Event Handler Logic**:
   - The `helper_ShowingNamedRangesDialog` subroutine is executed when the dialog is shown.
   - It casts the control to a `Form` and checks if it is not `Nothing`.
   - If valid, it sets the dialog title to "CashFlow Inputs".

### Visual Representation

#### Figure: Custom Title for NamedRange Collection Editor

![Custom Title set for the NamedRange Collection Editor](https://i.imgur.com/7k3vWJg.png)

#### Caption:
**Figure 139: Custom Title set for the NamedRange Collection Editor**

### Summary
The custom title for the `ShowNamedRange` dialog is successfully set to "CashFlow Inputs" using the provided event handler and code logic. This approach allows dynamic customization of the dialog box title based on application needs.

## RAG Annotations
<!-- tags: [Syncfusion, WinForms, Grid, NamedRange, CollectionEditor, CustomTitle, EventHandling] keywords: [Essential Grid, CashFlow Inputs, Dialog Title, NamedRange Collection Editor, F# events, Form customization, Dynamic Title] -->
```