```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_827.jpeg
document_name: tools
page_number: 827
page_id: tools#page_827
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:38:15Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Explains how to specify the `DataSource` for an `EditableList` control.
- Describes how to edit items in the list during runtime.
- Discusses the `EditableList` control's appearance and behavior settings.
- Lists the embedded controls of the `EditableList` control.

## Content

### Specifying the `DataSource`

The `DataSource` for the `EditableList` can be specified as follows:

```csharp
editableList1.ListBox.DataSource=<DataSource>
```

Otherwise, go to the property editor, expand the `ListBox` property of the `EditableList`, and then select `Items`. This `Items` property is editable like any other `Items` property.

#### Editing the List

The List can be edited in the following way during runtime:

1. Select the item you want to edit by clicking or by using the keyboard.
2. Click again. A `TextBox` appears where you can edit the text.
3. After editing, change the focus, and the list will get updated.

**Figure 527: Editing the List**

![Figure 527: Editing the List](https://ift.tt/3gKAM9m)

### 3.5.8.7.3.2

#### Appearance and Behavior Settings

This section discusses the complete appearance and behavior settings of the `EditableList` control.

### Embedded Controls

The `EditableList` control contains embedded controls such as `Button`, `TextBox`, and `ListBox`.

| **EditableList Embedded controls** | **Description** |
|----------------------------------|------------------|

## API Reference (if applicable)
- No specific API references are provided in this section.

## Code Examples (multi-language supported)
- No code examples are present in this section.

## Page-level Navigation/TOC (if applicable)
- None provided in this section.

---

<!-- tags: [Syncfusion Winforms, tools, editableList, appearance, behavior, embedded controls] keywords: [datasource, listbox, items property, text box, runtime editing, editableList control, appearance settings, behavior settings, embedded controls] -->
```