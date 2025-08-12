```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_070.jpeg
document_name: DocIo
page_number: 070
page_id: DocIo#page_070
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:31:51Z
fidelity: lossless
-->

# Custom Tab in Document Properties Dialog Box

## Overview
- This page provides details about the custom tab in the document properties dialog box, which allows users to manage and modify custom properties within a document.
- It highlights the functionality of adding, modifying, and removing custom properties, as well as viewing them in a organized manner.

## Content

### Public Properties

| Name  | Description                            |
|-------|-----------------------------------------|
| Count | Gets count of the properties.          |

### Public Methods

| Name   | Description                          |
|--------|---------------------------------------|
| Add    | Adds a new custom property.          |
| Clone  | Clones itself.                       |
| Remove | Remove property specified by name.   |

## API Reference

### Properties

| Name  | Type                                   | Description                          | Default | Required |
|-------|----------------------------------------|---------------------------------------|---------|----------|
| Name  | String                                 | Gets or sets the name of the property. | None    | Yes      |
| Type  | String                                 | Gets the type of the property.       | None    | No       |
| Value | String                                 | Gets or sets the value of the property. | None    | No       |

### Methods

#### Add

- **Description**: Adds a new custom property to the collection.
- **Parameters**:
  - **Name**: Name of the property to add.
  - **Type**: Type of the property.
  - **Value**: Value of the property.
- **Returns**: None.
- **Exceptions**:
  - Thrown if a property with the same name already exists.

#### Clone

- **Description**: Creates a new custom properties object with the same properties as the current one.
- **Parameters**: None.
- **Returns**: A new instance of the custom properties object.
- **Exceptions**: None.

#### Remove

- **Description**: Removes a custom property specified by its name.
- **Parameters**:
  - **Name**: Name of the property to remove.
- **Returns**: None.
- **Exceptions**:
  - Thrown if the property does not exist.

## Code Examples

### Example 1: Adding a Custom Property

```csharp
// Assuming docProps is an object representing the custom properties collection
docProps.Add("My_Custom_Property", "Text", "Custom Value");
```

### Example 2: Removing a Custom Property

```csharp
docProps.Remove("My_Custom_Property");
```

## Page-level Navigation/TOC (if applicable)

- [Custom Tab in Document Properties Dialog Box](#custom-tab-in-document-properties-dialog-box)
  - [Public Properties](#public-properties)
  - [Public Methods](#public-methods)

## Cross References

- See also: [Document Properties Overview](#document-properties-overview), [Managing Document Properties](#managing-document-properties)

## RAG Annotations

<!-- tags: document properties, custom properties, document metadata, document properties dialog box, winforms, syncfusion-sdk keywords: custom, properties, add, remove, clone, document, metadata -->
```