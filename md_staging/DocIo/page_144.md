```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_144.jpeg
document_name: DocIo
page_number: 144
page_id: DocIo#page_144
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:37:02Z
fidelity: lossless
-->

# WinForms Controls Overview

## Overview
- This page provides information on theForms Toolbar and its functionalities.
- It outlines the class hierarchy related to **WTextRange**, **WField**, and **WFormField**.
- The public properties associated with these classes are listed in a detailed table.

## Content

### Class Hierarchy

The class hierarchy is structured as follows:

- **WTextRange**
  - **WField**
    - **WFormField**

### Public Properties

The following table lists the public properties and their descriptions:

| Name             | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| CalculateOnExit  | Gets or sets calculate on exit property.                                  |
| Enabled          | Gets or sets Enabled property (true if form field enabled).              |
| EntityType       | Gets the type of the entity.                                              |
| FieldPattern     | Gets or sets field pattern.                                               |
| FieldType        | Gets or sets field type.                                                  |
| FieldValue       | Gets the field value.                                                     |
| FormFieldType    | Gets type of this form field.                                             |
| Help             | Gets or sets form field help.                                             |
| MacroOnEnd       | Gets or sets the name of macros on end.                                   |
| MacroOnStart     | Gets or sets the name of macros on start.                                 |
| Name             | Gets form field title name (bookmark name).                               |
| StatusBarHelp    | Gets or sets the status bar help.                                         |
| TextFormat       | Gets or sets regular text format.                                         |

## API Reference

### Properties

The public properties listed above can be used to manipulate and access various aspects of the **WFormField** class within the **Syncfusion Winforms** control.

### Code Examples

```csharp
// Example: Setting the calculate on exit property
WFormField formField = new WFormField();
formField.CalculateOnExit = true;

// Example: Getting the field value
string fieldValue = formField.FieldValue;

// Example: Setting the form field help
formField.Help = "Enter your details here.";
```

### Figures

- **Figure 46: Forms Toolbar**
  ![Forms Toolbar](image.png)

## Page-level Navigation/TOC (if applicable)
- This page provides detailed information about the Forms Toolbar and its public properties.
- Cross-references to other related sections or pages can be added as needed.

## Cross References
- This page is part of the broader **DocIO** documentation for the **Syncfusion Winforms** library.

## RAG Annotations
<!-- tags: WinForms, FormsToolbar, WTextRange, WField, WFormField, Module, Control, Properties, Version keywords: WTextRange, WField, WFormField, CalculateOnExit, Enabled, FieldType, FormFieldType, TextFieldFormat -->
```