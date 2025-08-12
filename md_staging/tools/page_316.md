```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_316.jpeg
document_name: tools
page_number: 316
page_id: tools#page_316
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:05:06Z
fidelity: lossless
-->

## Overview

- This page discusses essential tools for Windows Forms and provides guidance on working with the autocomplete feature. It includes details on displaying the autocomplete popup programmatically, removing default selections from the autocomplete dropdown, and deleting items in the list at runtime.

## Content

### 3.5.1.1.5.2 How to Programmatically display the autocomplete popup when a text box is enabled with autocomplete feature?

You can show the autocomplete popup programmatically using the following code.

#### C#

```csharp
this.AutoComplete1.AutoCompletePopup.ParentControl = this.textBox1;
this.AutoComplete1.AutoCompletePopup.ShowPopup(Point.Empty);
```

#### VB.NET

```vb
Me.AutoComplete1.AutoCompletePopup.ParentControl = Me.textBox1
Me.AutoComplete1.AutoCompletePopup.ShowPopup(Point.Empty)
```

### 3.5.1.1.5.3 How to remove default selection from autocomplete drop-down?

To remove the default selection in autocomplete drop-down, set `SelectedIndex` property to `-1` inside the `DropDownDisplayed` event of the autocomplete control as follows.

#### C#

```csharp
private void autoComplete1_DropDownDisplayed(object sender, EventArgs e)
{
    this.AutoComplete1.SelectedIndex = -1;
}
```

#### VB.NET

```vb
Private Sub autoComplete1_DropDownDisplayed(ByVal sender As Object, ByVal e As EventArgs)
    Me.AutoComplete1.SelectedIndex = -1
End Sub
```

### 3.5.1.1.5.4 How to delete the items in the list at run time?

You can delete items in the list at run time by pressing the Delete Key, by enabling the `AllowListDelete` property.

#### C#

```csharp
```

## API Reference (if applicable)

This section contains information on specific APIs related to the autocomplete and list deletion features.

## Code Examples (multi-language supported)

The code examples provided demonstrate how to programmatically manage the autocomplete feature and delete items from a list at runtime.

## Page-level Navigation/TOC (if applicable)

This page contains sub-sections detailing specific aspects of working with autocomplete in Windows Forms.

## Cross References

See also: Additional relevant sections or pages that might provide complementary information on Windows Forms, autocomplete, or related features.

<!-- tags: [winforms, autocomplete, list deletion, drop-down selection, programming, event handling] keywords: [autocomplete, list, deletion, drop-down, selection, programmatic display, selectedindex, dropdowndisplayed, allowlistdelete, csharp, vb.net] -->
```