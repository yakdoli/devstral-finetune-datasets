```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_588.jpeg
document_name: tools
page_number: 588
page_id: tools#page_588
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:22:38Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Provides examples of C# and VB.NET code for handling events and displaying predefined percent values in a ComboBoxAdv control.
- Explains the DropDown event and its use-case.
- Guides users through frequently asked questions related to programmatically interacting with ComboBoxAdv.

## Content

### Event Handling in ComboBoxAdv

#### Code Samples

**C#**
```csharp
private void PercentComboBoxAdv1_SelectedValueChanged(object sender, System.EventArgs e)
{
    // Displays the corresponding selected value.
    this.PercentComboBoxAdv1.TextBox.PercentValue = Double.Parse(this.PercentComboBoxAdv1.SelectedItem.ToString());
}
```

**VB.NET**
```vb
Private Sub PercentComboBoxAdv1_SelectedValueChanged(ByVal sender As Object, ByVal e As System.EventArgs)
    ' Displays the corresponding selected value.
    Me.PercentComboBoxAdv1.TextBox.PercentValue = Double.Parse(Me.PercentComboBoxAdv1.SelectedItem.ToString())
End Sub
```

#### Figure: ComboBoxAdv with Predefined Percent Value

![ComboBoxAdv with Predefined Percent Value](https://placehold.it/300x200)

**Figure 362: ComboBoxAdv with Predefined Percent Value**

### DropDown Event

This event is handled before the dropdown is shown.

An use-case for this event is discussed in the following topic: [How to programmatically select the record in the dropdown that matches the text typed in?]()

### Frequently Asked Questions

This section illustrates the solutions for various task-based queries about the control.

#### How to Programmatically Select the Record in the Dropdown That Matches the Text Typed In

This query addresses how to programmatically select a record in the dropdown that corresponds to the text entered.

### Summary

This section provides detailed information on handling events and programmatically interacting with the ComboBoxAdv control in Windows Forms applications.

## Page-level Navigation/TOC (if applicable)
- Event Handling in ComboBoxAdv
  - C# Code Sample
  - VB.NET Code Sample
  - Figure: ComboBoxAdv with Predefined Percent Value
- DropDown Event
- Frequently Asked Questions
  - How to Programmatically Select the Record in the Dropdown That Matches the Text Typed In

## Cross References
- Related topics:
  - How to programmatically select the record in the dropdown that matches the text typed in?

<!-- tags: [Syncfusion, WinForms, ComboBoxAdv, EventHandling, ProgrammaticallySelect] keywords: [ComboBoxAdv, PercentComboBoxAdv, DropDownEvent, SelectedValueChanged, FrequentlyAskedQuestions, ProgrammaticallySelect] -->
```