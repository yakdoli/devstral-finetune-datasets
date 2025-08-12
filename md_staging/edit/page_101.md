```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_101.jpeg
document_name: edit
page_number: 101
page_id: edit#page_101
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:00:26Z
fidelity: lossless
--> 

# Essential Edit for Windows Forms

## Overview

- Demonstrates automatic alignment of code braces in the Edit Control.
- Explains the AutoFormatting feature for code in the Edit Control.
- Discusses the `AutoIndentMode` property and its usage.

## Content

### Code Entry in Edit Control

Figure 32 illustrates code being entered into the Edit Control.

![Figure 32: Code is entered into the Edit Control](https://via.placeholder.com/600x400?text=Figure%2032)

The example shows a function definition written in C#.

### AutoFormatting in Edit Control

When the closing brace `}` is typed, it is automatically aligned with the opening brace, as shown in Figure 33.

#### AutoFormatting Demonstration

![Figure 33: AutoFormatting support for code in Edit Control](https://via.placeholder.com/600x400?text=Figure%2033)

### Note

The **AutoIndentMode** property for the Edit Control should be set to **Smart** for this purpose.

### AutoFormatter Interface

Essential Edit provides an extensible interface, **AutoFormatter**, which can be implemented to provide any kind of formatter for any desired language. This can be used to handle special scenarios, such as:

- XML or HTML text of the following format:
  ```html
  <abc>
    <xyz>
      ...
    </xyz>
  </abc>
  ```

  This should be formatted as follows:
  ```html
  <abc>
      <xyz>
          .
          .
          .
      </xyz>
  </abc>
  ```

## Page-level Navigation/TOC

- [Essential Edit for Windows Forms]
  - [Code Entry in Edit Control]
  - [AutoFormatting in Edit Control]
  - [AutoFormatter Interface]

## Cross References

- **AutoIndentMode**: Refer to the property documentation for more details.
- **AutoFormatter**: Explore the implementation guidelines for custom formatters.

## Final Notes

© 2013 Syncfusion. All rights reserved.

<!-- tags: [product, Syncfusion Windows Forms, AutoFormatting, AutoIndentMode, AutoFormatter] keywords: [C#, code formatting, braces alignment, extensible interface, XML, HTML, custom formatting, AutoFormatter implementation] -->
```