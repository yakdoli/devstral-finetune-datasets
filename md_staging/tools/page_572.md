```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_572.jpeg
document_name: tools
page_number: 572
page_id: tools#page_572
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:21:31Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates how to add dropdown items to a `ComboBoxAdv` control using both the designer and code.
- Explains the process of configuring the `Items` collection in the designer and adding items programmatically.

## Content

### Figure 352: Adding DropDown Items to ComboBoxAdv Control

The figure illustrates the process of adding dropdown items to a `ComboBoxAdv` control. The top image shows the `Properties` window for the `ComboBoxAdv1` control, highlighting the `(Items)` collection. Below is the `String Collection Editor` where the items are specified as strings. The items listed are:

- Currency
- DateTimePicker
- ComboBoxAdv
- AutoComplete
- ListBox
- ContextMenu
- CurrencyEdit

#### Adding Items Programmatically

In addition to using the designer, items can also be added programmatically. Below are the code snippets for both C# and VB.NET.

```csharp
[C#]

this.comboBoxAdv1.Items.AddRange(new object [] { "Currency", 
"DateTimePicker", "ComboBoxAdv", "AutoComplete", 
"ListBox","ContextMenu","CurrencyEdit" });
```

```vbnet
[VB.NET]

Me.comboBoxAdv1.Items.AddRange( New Object () { "Currency", 
"DateTimePicker", "ComboBoxAdv", "AutoComplete", "ListBox", 
"ContextMenu", _ 
"CurrencyEdit" })
```

## API Reference

- **Namespace**: Syncfusion.Windows.Forms
- **Class**: ComboBoxAdv
- **Method**: AddRange(ICollection value)

### Parameters
| Name       | Type         | Description                                                                      |
|------------|--------------|----------------------------------------------------------------------------------|
| value      | ICollection   | The collection of items to add to the `ComboBoxAdv` control.                    |

### Returns
- None

### Exceptions
- ArgumentNullException: Thrown if the `value` is null.

## Code Examples

### Example 1: Adding Dropdown Items Using the Designer
Use the设计师的`String Collection Editor` GUI界面 to add items to the `ComboBoxAdv` 控制面板的下拉菜单。

### Example 2: Adding Dropdown Items Programmatically

#### C# Example
```csharp
this.comboBoxAdv1.Items.AddRange(new object [] { 
    "Currency", 
    "DateTimePicker", 
    "ComboBoxAdv", 
    "AutoComplete", 
    "ListBox", 
    "ContextMenu", 
    "CurrencyEdit" });
```

#### VB.NET Example
```vbnet
Me.comboBoxAdv1.Items.AddRange( New Object () { 
    "Currency", 
    "DateTimePicker", 
    "ComboBoxAdv", 
    "AutoComplete", 
    "ListBox", 
    "ContextMenu", 
    "CurrencyEdit" })
```

### Getting Started with ComboBoxAdv

For more detailed information on configuring and using the `ComboBoxAdv` control, refer to the [ComboBoxAdv documentation](https://docs.syncfusion.com/windowsforms/comboboxadv/overview).

## See also:
- String Collection Editor
- Properties Window
- Designer

<!-- tags: [ComboBoxAdv, Syncfusion Windows Forms, Designer, String Collection Editor, AddRange] keywords: [dropdown items, programmatically, designer, GUI, C#, VB.NET] -->
```
