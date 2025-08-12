```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_143.jpeg
document_name: DocIo
page_number: 143
page_id: DocIo#page_143
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:36:52Z
fidelity: lossless
-->

## Overview
- This page describes how to work with sequence fields and form fields in DocIO.
- It includes examples in C# and VB.NET for creating and configuring sequence fields.
- Details the properties of the `WFormField` class for handling form fields in MS Word.

## Content

### Sequence Field Configuration
The following examples demonstrate how to create and configure a sequence field in a document using both C# and VB.NET.

#### C#
```csharp
WSeqField field = (WSeqField)paragraph.AppendField("Sequence Field", FieldType.FieldSequence);
field.CaptionName = "Sequence Field";
field.NumberFormat = CaptionNumberingFormat.Alphabetic;
```

#### VB.NET
```vb
Dim field As WSeqField = CType(paragraph.AppendField("Sequence Field", FieldType.FieldSequence), WSeqField)
field.CaptionName = "Sequence Field"
field.NumberFormat = CaptionNumberingFormat.Alphabetic
```

### 4.4.1.2.4 Form Field

#### Overview of Form Fields
`WFormField` is the base abstract class for all form fields in DocIO (WCheckBox, WDropDownFormField, and WTextFormField). There are three types of form fields:

- **Text**: text form field
- **CheckBox**: check box form field
- **DropDown**: drop-down form field

#### Common Properties of Form Fields
The `WFormField` class holds all the common properties for the form fields. Below are the common properties:

- **CalculateOnExit**
- **Enabled**: defines whether the status bar form field is enabled.
- **FormFieldType**: defines the type of form field.
- **Help**: represents form field help.
- **MacroOnEnd**: defines the name of the macro to run on entry of form field.
- **MacroOnStart**: defines the name of the macro to run on start of form field.
- **Name**: represents the name of the form field.
- **StatusBarHelp**: represents the help to display in the status bar.

#### Inserting Form Fields
You can also insert these fields through the **Forms** toolbar in MS Word. The following screenshot illustrates a Forms toolbar in MS Word.

## API Reference
- **WSeqField**:
  - **CaptionName**: Sets the caption name of the sequence field.
  - **NumberFormat**: Sets the numbering format for the sequence field (e.g., `CaptionNumberingFormat.Alphabetic`).
- **WFormField**:
  - **CalculateOnExit**: Property to determine if calculations are to be performed when exiting the field.
  - **Enabled**: Property to define whether the form field is enabled in the status bar.
  - **FormFieldType**: Defines the type of the form field (e.g., Text, CheckBox, DropDown).
  - **Help**: Represents help text for the form field.
  - **MacroOnEnd**: Defines the macro to run on entry of the form field.
  - **MacroOnStart**: Defines the macro to run on start of the form field.
  - **Name**: Represents the name of the form field.
  - **StatusBarHelp**: Represents the help text to be displayed in the status bar.

## Code Examples

### C# Example
```csharp
WSeqField field = (WSeqField)paragraph.AppendField("Sequence Field", FieldType.FieldSequence);
field.CaptionName = "Sequence Field";
field.NumberFormat = CaptionNumberingFormat.Alphabetic;
```

### VB.NET Example
```vb
Dim field As WSeqField = CType(paragraph.AppendField("Sequence Field", FieldType.FieldSequence), WSeqField)
field.CaptionName = "Sequence Field"
field.NumberFormat = CaptionNumberingFormat.Alphabetic
```

## Cross References
- See also: [Page on Sequence Fields in DocIO]
- See also: [Page on Working with Forms in MS Word]

<!-- tags: [syncfusion, docio, winforms, sequence-field, form-field, wformfield, wseqfield, captionnumberingformat] keywords: [captionname, formfieldtype, macroonend, macroonstart, statusbarhelp, formfield, csharp, vb.net] -->
```