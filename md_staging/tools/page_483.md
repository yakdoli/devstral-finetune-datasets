```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_483.jpeg
document_name: tools
page_number: 483
page_id: tools#page_483
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:16:01Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Describes how to configure the DateTimePickerAdv control to use an enhanced menu.
- Details the options available in the Syncfusion XP Menu as context menu for the DateTimePickerAdv.
- Explains the use of the ClipboardFormat and CopyFieldsOnly properties to control the behavior during copy and paste operations.

## Content

### DateTimePickerAdv Enhancements

To enable the enhanced menu for the DateTimePickerAdv control, set the `UseEnhancedMenu` property to `True`.

```csharp
Me.DateTimePickerAdv1.UseEnhancedMenu = True
```

#### Syncfusion XP Menu as Context Menu

The enhanced menu provides a set of options for manipulating dates and times within the DateTimePickerAdv control. The figure below illustrates the Syncfusion XP Menu as a context menu.

![Syncfusion XP Menu as Context Menu](https://i.imgur.com/1234567.png)
*Figure 280: Syncfusion XP Menu as Context Menu*

### Menu Options

The menu options are:

- **Cut** - Cuts the displayed date and by default displays the string "No Date is selected".
- **Copy** - Copies the displayed date and stores it in the clipboard.
- **Paste** - Pastes the copied date.
- **No Date/Time** - Selects no date and displays the string "No Date is selected".

### ClipboardFormat Property

We can set the text value format that is copied to the clipboard using the `ClipboardFormat` property. This property allows specifying the format of the value of the DateTimePickerAdv control that is copied. The available formats are:

- **Long (default)** - Displays the date and time in the long format.
- **Short** - Displays the date in a shorter format.
- **Time** - Copies only the time component.
- **Custom** - Allows customization of the format.

### CopyFieldsOnly Property

This property indicates whether only the selected field (date or time) will be copied or the entire text field will be copied.

#### DateTimePickerAdv Properties

| DateTimePickerAdv Properties       | Description                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| `ClipboardFormat`                   | While doing copy / paste operation, we can specify the format of the value of the DateTimePickerAdv control that is copied, by using the `ClipBoardFormat` property. The formats are: <br>- Long (default) <br>- Short <br>- Time <br>- Custom |
| `CopyFieldsOnly`                   | Indicates whether only the selected field will be copied or the whole text field will be copied.                                         |

### Code Example

```csharp
[C#]
```

### Summary

The DateTimePickerAdv control in Syncfusion Winforms offers enhanced functionality through the use of a context menu. This menu provides options for copying, pasting, and manipulating dates and times, with formatting customization available through the `ClipboardFormat` property, and field selection control using the `CopyFieldsOnly` property.

## API Reference

### Properties

- **ClipboardFormat** - Specifies the format of the value that is copied to the clipboard during copy operations.
  - **Type**: string
  - **Default**: `"Long"`

- **CopyFieldsOnly** - Indicates whether only the selected field (date or time) will be copied or the entire text field will be copied.
  - **Type**: bool
  - **Default**: `false`

## Code Examples

### Setting ClipboardFormat
```csharp
// Set the clipboard format to "Short"
dateTimePickerAdv1.ClipboardFormat = "Short";
```

### Using CopyFieldsOnly
```csharp
// Set to copy only the selected field
dateTimePickerAdv1.CopyFieldsOnly = true;
```

### Enabling Enhanced Menu
```csharp
// Enable the enhanced menu for the DateTimePickerAdv
dateTimePickerAdv1.UseEnhancedMenu = true;
```

## Conclusion

By leveraging the enhanced menu and properties of the DateTimePickerAdv control, developers can provide a more user-friendly experience for handling dates and times in their Windows Forms applications. The ability to customize clipboard formats and control field selection adds flexibility to date and time manipulation scenarios.

<!-- tags: [product, tools, DateTimePickerAdv, clipboard, menu, format, Control, Windows Forms] keywords: [context menu, enhanced menu, clipboardFormat, copyFieldsOnly, enhanced functionality, user-friendly experience, date and time manipulation] -->
```