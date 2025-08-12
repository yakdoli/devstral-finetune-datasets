```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_466.jpeg
document_name: tools
page_number: 466
page_id: tools#page_466
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:15:16Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview

- Unchecked state of the CheckBox demonstrated
- Formatting options for text fields in DateTimePickerAdv explained

## Content

### Text Field Formatting

**Format and CustomFormat properties** are used to format the text field. Below are the details:

#### DateTimePickerAdv Properties and Description

| **DateTimePickerAdv Properties** | **Description** |
|-----------------------------------|-----------------|
| **Format**                       | Gets or Sets the format of the picker. The options are,<br><br>* Long (default)<br>* Short<br>* Time<br>* Custom |
| **CustomFormat**                 | Specifies the custom format, when the Format is set to 'Custom'. For example, if you want to display 'March/2007', set CustomFormat to 'MMMM/yyyy'. |

### C#

```csharp
// Sets "Long" format for the text field
this.dateTimePickerAdv5.Format =
System.Windows.Forms.DateTimePickerFormat.Long;

// Sets "Short" format for the text field
this.dateTimePickerAdv5.Format =
System.Windows.Forms.DateTimePickerFormat.Short;

// Sets "Time" format for the text field
this.dateTimePickerAdv5.Format =
System.Windows.Forms.DateTimePickerFormat.Time;

// Sets custom format for the text field
this.dateTimePickerAdv5.Format =
```

## API Reference (if applicable)

- **Properties**: Format, CustomFormat
- **Enums**: DateTimePickerFormat

## Code Examples (multi-language supported)

- **C#**:
  ```csharp
  // Example of setting custom format
  this.dateTimePickerAdv5.Format =
  System.Windows.Forms.DateTimePickerFormat.Custom;
  this.dateTimePickerAdv5.CustomFormat = "MMMM/yyyy";
  ```

## RAG Annotations

<!-- tags: [windows forms, date time picker, formatting, custom format, unchecked checkbox] keywords: [DateTimePickerAdv, Format, CustomFormat, Long, Short, Time, Custom, C#, Text Field Formatting, CheckBox, Essentials] -->
```