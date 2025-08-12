```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_177.jpeg
document_name: edit
page_number: 177
page_id: edit#page_177
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:05:40Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

```csharp
// Get list of the lexems that are inside the current stack.
IList list = editControl1.GetLexemsInsideCurrentStack(false);
if (list == null) return;

int iBoldedIndex = 0;
foreach (ILexem lexem in list)
{
    if (lexem.Text == ",")
        iBoldedIndex++;
}

if (iBoldedIndex >= e.List.SelectedItem.BoldedItems.Count)
    e.List.SelectedItem.BoldedItems.SelectedItem = null;
else
{
    // Gets or sets selected item.
    e.List.SelectedItem.BoldedItems.SelectedItem =
        e.List.SelectedItem.BoldedItems[iBoldedIndex];
}
```

### [VB.NET]

```vb
Private Sub editControl1_ContextPromptUpdate(ByVal sender As Object, ByVal e As Syncfusion.Windows.Forms.Edit.ContextPromptUpdateEventArgs) Handles EditControl1.ContextPromptUpdate

    ' Select the items that should be bold.
    If Not (e.List.SelectedItem Is Nothing) Then

        ' Get list of the lexems that are inside the current stack.
        Dim list As IList = editControl1.GetLexemsInsideCurrentStack(False)
        If list Is Nothing Then
            Return
        End If

        Dim iBoldedIndex As Integer = 0
        Dim lexem As ILexem
        For Each lexem In list
            If lexem.Text = "," Then
                iBoldedIndex += 1
            End If
        Next lexem

        If iBoldedIndex >= e.List.SelectedItem.BoldedItems.Count Then
            e.List.SelectedItem.BoldedItems.SelectedItem = Nothing
        Else
        End If
    End If
End Sub
```

## API Reference

### Methods

- `GetLexemsInsideCurrentStack()`: Retrieves the list of lexems within the current stack.

## Code Examples

The following examples demonstrate how to interact with the `EditControl` and manage bolded items for lexems.

### C#

```csharp
// Example of updating bolded items based on current stack
int iBoldedIndex = 0;
foreach (ILexem lexem in list)
{
    if (lexem.Text == ",")
        iBoldedIndex++;
}
if (iBoldedIndex >= e.List.SelectedItem.BoldedItems.Count)
{
    e.List.SelectedItem.BoldedItems.SelectedItem = null;
}
else
{
    e.List.SelectedItem.BoldedItems.SelectedItem =
        e.List.SelectedItem.BoldedItems[iBoldedIndex];
}
```

### VB.NET

```vb
' Example of updating bolded items based on current stack
Dim iBoldedIndex As Integer = 0
For Each lexem In list
    If lexem.Text = "," Then
        iBoldedIndex += 1
    End If
Next lexem
If iBoldedIndex >= e.List.SelectedItem.BoldedItems.Count Then
    e.List.SelectedItem.BoldedItems.SelectedItem = Nothing
Else
    e.List.SelectedItem.BoldedItems.SelectedItem =
        e.List.SelectedItem.BoldedItems(iBoldedIndex)
End If
```

## Pagination

This page is from the document *edit*.

## Copyright Notice

© 2013 Syncfusion. All rights reserved.

<!-- tags: [Essential Edit, Windows Forms, Syncfusion, Lexem, Bolded Items, Code Examples, C#, VB.NET, Stack] keywords: [Syncfusion Windows Forms, Lexems, Bolded Items, Context Prompt Update, EditControl, List Management, Text Manipulation, Example Code] -->
```