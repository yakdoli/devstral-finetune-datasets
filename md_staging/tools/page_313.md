```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_313.jpeg
document_name: tools
page_number: 313
page_id: tools#page_313
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:04:49Z
fidelity: lossless
-->

## Overview
- Explanation of AutoCompleteItemBrowsed event and its usage.
- Illustration of displaying selected AutoComplete URL in a separate TextBox using C# and VB.NET code examples.
- Introduction to MatchItem Event and its application in overriding default matching in target edit control.

## Content

### AutoCompleteItemBrowsed Event

The following table lists the members associated with the AutoCompleteItemBrowsed event and their descriptions:

| Members           | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| Handled           | Specifies whether SelectedValue should be applied to the target control. This can be used only with AutoCompleteItemSelected. |
| ItemArray         | Returns the AutoComplete item as an object array.                          |
| MatchColumnIndex  | Returns the index of the item that was used for matching.                 |

When the user selects an item from the list of possible matches when the AutoComplete is set to AutoSuggest, we can display the selected URL in a separate TextBox. The following code illustrates this:

#### [C#]

```csharp
private void autoComplete1_AutoCompleteItemBrowsed(object sender, Syncfusion.Windows.Forms.Tools.AutoCompleteItemEventArgs args)
{
    string itemText = args.ItemArray[0].ToString();
    string eventlogmessage = String.Format("Event: {0} Item: {1}\r\n", "AutoCompleteItemSelected", itemText);
    textBox1.Text = textBox1.Text + eventlogmessage;
}
```

#### [VB.NET]

```vb
Private Sub autoComplete1_AutoCompleteItemBrowsed(ByVal sender As Object, ByVal args As Syncfusion.Windows.Forms.Tools.AutoCompleteItemEventArgs)
    Dim itemText As String = args.ItemArray(0).ToString()
    Dim eventlogmessage As String = [String].Format("Event: {0} Item: {1}" & Chr(13) & "" & Chr(10) & "", "AutoCompleteItemSelected", itemText)
    textBox1.Text = textBox1.Text + eventlogmessage
End Sub
```

### 3.5.1.1.4.4 MatchItem Event

We can override the default matching of the current content of the target edit control using this event. The event handler receives an argument of type AutoCompleteMatchItemEventArgs. The following are the properties associated with the AutoCompleteMatchItemEventArgs argument:

| Members          | Description                                        |
|------------------|----------------------------------------------------|

<!-- tags: [Syncfusion Winforms, AutoComplete, AutoCompleteItemEventArgs, MatchItem Event] keywords: [AutoCompleteItemBrowsed, C#, VB.NET, textBox, AutoCompleteItemSelected, eventlogmessage, MatchColumnIndex, AutoCompleteMatchItemEventArgs] -->
```