```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_999.jpeg
document_name: tools
page_number: 999
page_id: tools#page_999
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:48:08Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

End Sub

## 3.5.11.2.4.2 GroupCheckChanged Event

This event is fired when the Checked property of the RadioButtonAdv in the group changes.

The event handler receives an argument of type EventArgs containing data related to this event.

### Code Example

```csharp
[C#]
private void radioButtonAdv1_GroupCheckChanged(object sender, EventArgs e)
{
    Console.WriteLine(" GroupCheckChanged event is raised");
}
```

```vb
[VB.NET]
Private Sub radioButtonAdv1_GroupCheckChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine(" GroupCheckChanged event is raised")
End Sub
```

## 3.5.12 SpellChecker

### Overview

- Spell checking is a key feature in text processing applications.
- The Essential Tools package includes a SpellChecker control with custom dictionary support.

### Description

SpellChecker is a component that comes with built-in support to handle spell checking and suggestion replacements for RichTextBox and TextBox controls. SpellChecker can even be associated with non-TextBoxBase control via an interface.

### IT Scenarios

- SpellChecker would help in text processing application and data entry forms.

## 3.5.12.1 Samples and Location

### Where to Find Samples?

---

<!-- tags: [Syncfusion Winforms, SpellChecker, RadioButtonAdv, EventArgs, Event Handling, Custom Dictionary, RichTextBox, TextBox, Text Processing] keywords: [SpellChecker, GroupCheckChanged, Custom Dictionary, Text Processing, RadioButton, Advanced, Event Handler, Sample Locations] -->
```