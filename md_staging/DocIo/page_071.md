```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_071.jpeg
document_name: DocIo
page_number: 071
page_id: DocIo#page_071
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:32:16Z
fidelity: lossless
-->

# DocumentProperty

The `DocumentProperty` class represents each custom document property.

## Public Methods

| Name          | Description                                          |
|---------------|------------------------------------------------------|
| Clone         | Clones itself.                                      |
| ToBool        | Converts value to Boolean.                          |
| ToByteArray   | Converts value to byte array.                       |
| ToDateTime    | Converts value to DateTime.                         |
| ToFloat       | Converts value to float.                            |
| ToInt         | Converts value to integer.                          |
| ToString      | Converts value to string.                           |

## Overview

- Demonstrates how to access and modify custom document properties.
- Includes examples for retrieving existing properties, setting their values, and adding new properties.

## Content

The following example illustrates how to get or set the existing custom document properties, and also how to add new custom document properties.

### Example Code: Accessing and Modifying Custom Document Properties

```csharp
[C#]
WordDocument doc = new WordDocument();
doc.Open( "DocumentProperties.doc" );

// Getting custom property value
int phoneNumber = doc.CustomDocumentProperties["Telephone number "].ToInt();

// Setting existent custom property value
doc.CustomDocumentProperties["Check by"].Value = "user name";

// Adding new custom property
DateTime completedDate = DateTime.Now;
doc.CustomDocumentProperties.Add( "Date completed", completedDate );
```

## API Reference

**Class**: DocumentProperty

### Public Methods

- **Clone**:
  - **Description**: Clones the current instance of the `DocumentProperty` class.

- **ToBool**:
  - **Description**: Converts the property value to a `Boolean` type.

- **ToByteArray**:
  - **Description**: Converts the property value to a `byte[]` array.

- **ToDateTime**:
  - **Description**: Converts the property value to a `DateTime` type.

- **ToFloat**:
  - **Description**: Converts the property value to a `float` type.

- **ToInt**:
  - **Description**: Converts the property value to an `integer` type.

- **ToString**:
  - **Description**: Converts the property value to a `string` type.

## Code Examples

The provided example demonstrates:
1. Opening a Word document with custom properties.
2. Retrieving an existing custom property value and converting it to an integer.
3. Setting the value of an existing custom property.
4. Adding a new custom property with a `DateTime` value.

This functionality is essential for working with document metadata in Syncfusion Winforms applications.

## Page-level Navigation/TOC (if applicable)

- [DocumentProperty]
  - Overview
  - Public Methods
  - Example Code

## Cross References

- See also: Related topics on custom document properties and Word document manipulation in Syncfusion Winforms documentation.

<!-- tags: [DocumentProperty, custom document properties, Syncfusion, WordDocument, Winforms, version: 11.4.0.26] keywords: [DocumentProperty, custom properties, WordDocument,module, control, api, 11.4.0.26] -->
```