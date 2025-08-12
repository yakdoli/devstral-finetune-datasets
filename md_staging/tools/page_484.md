<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_484.jpeg
document_name: tools
page_number: 484
page_id: tools#page_484
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:15:45Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview

- Describes the settings for copy fields, clipboard formats, and navigating between fields in the `DateTimePickerAdv` control.
- Demonstrates property settings for enabling tab navigation and field separation.

## Content

### DateTimePickerAdv Copy Fields and Clipboard Format

#### Code Example: C#
```csharp
this.dateTimePickerAdv1.CopyFieldsOnly = true;
this.dateTimePickerAdv1.ClipboardFormat =
    System.Windows.Forms.DateTimePickerFormat.Short;
```

#### Code Example: VB.NET
```vb
Me.dateTimePickerAdv1.CopyFieldsOnly = True
Me.dateTimePickerAdv1.ClipboardFormat =
    System.Windows.Forms.DateTimePickerFormat.Short
```

### Navigating between fields

#### Description
At runtime, users can easily navigate between values in the `text field` like date, month, year, and time using the TAB key. The following property settings are necessary for tabbing between the fields.

#### Properties and Descriptions

| DateTimePickerAdv Properties | Description |
|-------------------------------|-------------|
| TabStop                     | Indicates whether the user can use the Tab key to focus the DateTimePickerAdv control.                                   |
| TabForwarding                | Indicates if the control will move its focus to the next field when the tab key is pressed.                           |
| TabIndex                     | Indicates the index in the TAB order that this control will occupy.                                                 |
| TabLeave                     | Indicates whether the focus should be moved away from the control when there are no fields to tab through.           |

#### Code Example: C#
```csharp
this.dateTimePickerAdv1.TabForwarding = true;
this.dateTimePickerAdv1.TabIndex = 1;
this.dateTimePickerAdv1.TabLeave = true;
this.dateTimePickerAdv1.TabStop = true;
```

#### Code Example: VB.NET
```vb
Me.dateTimePickerAdv1.TabForwarding = True
Me.dateTimePickerAdv1.TabIndex = 1
Me.dateTimePickerAdv1.TabLeave = True
Me.dateTimePickerAdv1.TabStop = True
```

## See Also

- **Text Field, Null value Settings**

- **3.5.3.2.3.5.3 Navigating between fields**

## API Reference

### Properties

- **CopyFieldsOnly**: Indicates whether only the fields (like date, month, year, time) should be copied.
- **ClipboardFormat**: Specifies the format used for copying and pasting dates.
- **TabStop**: Indicates whether the control can receive focus via the Tab key.
- **TabForwarding**: Indicates if the focus should move to the next field when the Tab key is pressed.
- **TabIndex**: Specifies the tab order index for the control.
- **TabLeave**: Indicates whether the focus should leave the control when there are no fields to tab through.

## Code Examples

- **Setting CopyFieldsOnly and ClipboardFormat**:
  ```csharp
  this.dateTimePickerAdv1.CopyFieldsOnly = true;
  this.dateTimePickerAdv1.ClipboardFormat =
      System.Windows.Forms.DateTimePickerFormat.Short;
  ```

  ```vb
  Me.dateTimePickerAdv1.CopyFieldsOnly = True
  Me.dateTimePickerAdv1.ClipboardFormat =
      System.Windows.Forms.DateTimePickerFormat.Short
  ```

- **Enabling Tab Navigation**:
  ```csharp
  this.dateTimePickerAdv1.TabForwarding = true;
  this.dateTimePickerAdv1.TabIndex = 1;
  this.dateTimePickerAdv1.TabLeave = true;
  this.dateTimePickerAdv1.TabStop = true;
  ```

  ```vb
  Me.dateTimePickerAdv1.TabForwarding = True
  Me.dateTimePickerAdv1.TabIndex = 1
  Me.dateTimePickerAdv1.TabLeave = True
  Me.dateTimePickerAdv1.TabStop = True
  ```

<!-- tags: [Syncfusion Winforms, DateTimePickerAdv, Properties, Navigation, Tab Order, ClipboardFormat, CopyFieldsOnly, TabStop, TabForwarding, TabIndex, TabLeave] keywords: [Windows Forms, DateTimePicker, Tab Navigation, Tab Order, Control Focus, Copy Fields, Clipboard Format, Null Value, DateTime Picker, Advanced DateTime Picker, DateTimePickerAdv] -->