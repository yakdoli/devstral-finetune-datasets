```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_975.jpeg
document_name: tools
page_number: 975
page_id: tools#page_975
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:46:43Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Explains how to use the `CheckedChangedEventArgs` class to determine the source of a change event.
- Demonstrates code snippets in both C# and VB.NET to check the source type of an event.
- Provides a FAQs section to help users understand how to databind a `CheckBoxAdv` control to a SQL database.

## Content

### Event Handler with CheckedChangedEventArgs

The event handler receives an argument of type `CheckedChangedEventArgs` containing data related to this event. The member, `Source` of this argument, allows you to check the `SourceType`. Refer to the below code snippet.

#### C#

```csharp
private void checkBoxAdv1_CheckedChanged(object sender, Syncfusion.Windows.Forms.Tools.CheckedChangedEventArgs e)
{
    if (e.Source == CheckedChangedEventArgs.SourceType.Mouse)
    {
        Console.WriteLine("Using Mouse");
    }
    else if (e.Source == CheckedChangedEventArgs.SourceType.Keyboard)
    {
        Console.WriteLine("Using Keyboard");
    }
    else if (e.Source == CheckedChangedEventArgs.SourceType.Programmatic)
    {
        Console.WriteLine("Using Code");
    }
}
```

#### VB.NET

```vb
Private Sub checkBoxAdv1_CheckedChanged(ByVal sender As Object, ByVal e As Syncfusion.Windows.Forms.Tools.CheckedChangedEventArgs)
    If e.Source = CheckedChangedEventArgs.SourceType.Mouse Then
        Console.WriteLine("Using Mouse")
    ElseIf e.Source = CheckedChangedEventArgs.SourceType.Keyboard Then
        Console.WriteLine("Using Keyboard")
    ElseIf e.Source = CheckedChangedEventArgs.SourceType.Programmatic Then
        Console.WriteLine("Using Code")
    End If
End Sub
```

### 3.5.11.1.5 Frequently Asked Questions

This section will help you become more familiar in using the CheckBoxAdv control.

#### 3.5.11.1.5.1 How to databind a CheckBoxAdv to an SQL database if the corresponding datatable field is a bit field

The CheckBoxAdv's `IntValue` property can be used to databind bit values as illustrated below.

## API Reference

### Properties
- IntValue: Used to databind bit values to the CheckBoxAdv control.

## Code Examples

#### C# Example

```csharp
// Example showing how to databind a CheckBoxAdv to an SQL database
private void BindCheckBoxAdv()
{
    checkBoxAdv1.DataSource = myDataTable;
    checkBoxAdv1.DataBindings.Add("IntValue", myDataTable, "bitField");
}
```

#### VB.NET Example

```vb
' Example showing how to databind a CheckBoxAdv to an SQL database
Private Sub BindCheckBoxAdv()
    checkBoxAdv1.DataSource = myDataTable
    checkBoxAdv1.DataBindings.Add("IntValue", myDataTable, "bitField")
End Sub
```

### Cross References

See also:
- [Syncfusion WinForms Documentation](https://www.syncfusion.com/products/windowsforms/documentation)
- [CheckBoxAdv Control](https://help.syncfusion.com/windowsforms/checkboxadv)

### RAG Annotations
<!-- tags: [product, windowsforms, checkboxadv, checkedchangedeventargs, integration, databinding] keywords: [CheckboxAdv, IntValue, databinding, SQL database, Windows Forms, Syncfusion] -->
```