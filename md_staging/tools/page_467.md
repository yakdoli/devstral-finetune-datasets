```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_467.jpeg
document_name: tools
page_number: 467
page_id: tools#page_467
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:14:58Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview

- Demonstrates how to configure the `DateTimePickerAdv` control in a Windows Forms application.
- Explains setting various formats for the text field including "Long," "Short," "Time," and custom formats.
- Describes how to specify spacing between components in the text field using the `Spacing` property.

## Content

### DateTimePickerAdv Text Field Formats

The `DateTimePickerAdv` control in Windows Forms allows customization of the text field formats. Below are examples in C# and VB.NET to illustrate setting different formats:

#### C#

```csharp
System.Windows.Forms.DateTimePickerFormat.Custom;
this.dateTimePickerAdv5.CustomFormat = "dd - MM - yyyy";
```

#### VB.NET

```vb
' Sets "Long" format for the text field
Me.dateTimePickerAdv5.Format = System.Windows.Forms.DateTimePickerFormat.Long

' Sets "Short" format for the text field
Me.dateTimePickerAdv5.Format = System.Windows.Forms.DateTimePickerFormat.Short

' Sets "Time" format for the text field
Me.dateTimePickerAdv5.Format = System.Windows.Forms.DateTimePickerFormat.Time

' Sets custom format for the text field
Me.dateTimePickerAdv5.Format = System.Windows.Forms.DateTimePickerFormat.Custom
Me.dateTimePickerAdv5.CustomFormat = "dd - MM - yyyy"
```

### Figure: TextField Formats for DateTimePickerAdv

![Figure 266: TextField Formats for DateTimePickerAdv](https://i.imgur.com/example_image.png)

#### Spacing in TextField

We can specify spacing for the text field in the control (e.g., between month, year, and date) using the `Spacing` property. The default value is `0`.

#### Code Example

```csharp
this.dateTimePickerAdv1.Spacing = 5;
```

## API Reference

### `Spacing` Property

- **Type**: `int`
- **Description**: Specifies the spacing (in pixels) between components in the text field.
- **Default Value**: `0`
- **Usage**: Set the spacing to control the appearance and readability of the date/time input.

## Code Examples

### C#

```csharp
this.dateTimePickerAdv1.Spacing = 5;
```

### VB.NET

```vb
Me.dateTimePickerAdv1.Spacing = 5
```

## RAG Annotations

<!-- tags: [syncfusion, windows forms, datetimepickeradv, date and time, formatting, spacing, customization] keywords: [format, custom format, spacing, date, time, text field, datetimepickeradv, windows forms] -->
```