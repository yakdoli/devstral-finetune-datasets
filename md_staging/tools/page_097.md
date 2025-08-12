```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_097.jpeg
document_name: tools
page_number: 097
page_id: tools#page_097
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:21:09Z
fidelity: lossless
-->

## Overview

- Explains the enhancement of the SkinManager to support Office 2010 themes in addition to Office 2007.
- Describes the serialization capabilities for saving and loading the layout state of a CommandBar object.
- Details the properties of CommandBarController for persistence support.
- Introduces the AppStateSerializer class for coordinating serialization behavior across multiple components.

## Content

### 3.3.3.8.5 Skin Manager Compatibility

Previously, the SkinManager supported only Office 2007 themes. Now the SkinManager will support Office 2010 themes for the following color schemes:

- Office 2010 Blue
- Office 2010 Black
- Office 2010 Silver

### 3.3.3.9 Serialization

The layout state of a CommandBar object can be saved and loaded in the formats given below.

- XML
- Binary Format
- Isolated Storage
- Windows Registry

#### Persistence Support

The CommandBarController provides support to save the persisted state of the CommandBar.

| CommandBarController Property | Description                                         |
| ----------------------------- | --------------------------------------------------- |
| PersistState                  | Specifies whether the application's CommandBar state should be persisted. |

##### Code Examples

[C#]

```csharp
this.commandBarController1.PersistState = true;
```

[VB.NET]

```vbnet
Me.commandBarController1.PersistState = True
```

#### AppStateSerializer class

The AppStateSerializer class provides a mechanism for coordinating the serialization behavior of multiple components.

## API Reference (if applicable)

### Properties

- **PersistState**
  - **Description:** Specifies whether the application's CommandBar state should be persisted.
  - **Type:** Boolean
  - **Default:** False

## Code Examples (multi-language supported)

Refer to the examples in the "Persistence Support" section for how to use the PersistState property in C# and VB.NET.

## Page-level Navigation/TOC (if applicable)

- **3.3.3.8.5 Skin Manager Compatibility**
- **3.3.3.9 Serialization**
  - Persistence Support
  - AppStateSerializer class

## Cross References

- This document provides details related to both the SkinManager and CommandBarController in Syncfusion Winforms, highlighting enhanced theme support and serialization capabilities.

<!-- tags: [Syncfusion Winforms, SkinManager, CommandBar, Serialize, AppStateSerializer] keywords: [Theme, Office 2010, Office 2007, CommandBar, Serialization, AppStateSerializer] -->
```