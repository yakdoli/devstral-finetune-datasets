```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_159.jpeg
document_name: DocIo
page_number: 159
page_id: DocIo#page_159
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:37:52Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- Document variables are stored as part of a document or template and are useful for storing and retrieving information for future use.
- Essential DocIO provides support for working with document variables, allowing users to get or set variables by using either the variable name or index.
- These variables can be accessed, added, or removed easily through specific methods.

## Content

Document variables are stored as part of a document or template. Document variables store information about the document. These are useful for document automation because they allow the programmer to store information for future use. For example, some firms use document variables to store Client and Author information, for use in the footer or field code purposes.

### Working with Document Variables
Essential DocIO provides support to work with these document variables. You can get or set the variables by using the variable name or index.

#### Accessing Document Variables
Document variables are accessible through the `IDocument.Variables` property.

#### Adding and Removing Variables
Variables are added to the document by using the `IDocument.Variables.Add(string variableName, string variableValue)` method. Variables are removed from the document by using the `IDocument.Variables.Remove(string variableName)` method.

#### Inserting Document Variables
These fields could be referred to, in other parts of the document easily. For example, use the `IWParagraph.AppendField(string fieldName, FieldType type)` method, where the 1st argument is the name of the document field and the 2nd argument is `FieldType.FieldDocVariable`.

### Figure 55: Document Variable Field

- **Window Title**: Field
- **Main Section**:
  - **Field Types**: 
    - BidiOutline
    - Citation
    - Comments
    - Compare
    - CreateDate
    - Database
    - Date
    - DocProperty
    - DocVariable
    - EditTime
    - Eq
    - FileName
    - FileSize
    - Fill-in
    - GoToButton
    - GreetingLine
    - Hyperlink
    - If
  - **Field Properties**:
    - Name: "Var1"
  - **Field Options**: 
    - No field options available for this field
  - **Description**: Insert the value of the document variable named NAME
  - **Preserve Formatting During Updates**: Checked
- **Buttons**: OK, Cancel

## API Reference

### Methods for Managing Document Variables
- `IDocument.Variables.Add(string variableName, string variableValue)`
- `IDocument.Variables.Remove(string variableName)`
- `IWParagraph.AppendField(string fieldName, FieldType type)`

## Figure: Document Variable Field

The image showing the field configuration window provides a visual representation of how to manage document variables within a document. It includes various options for selecting the field type, naming the variable, and specifying the format for the variable.

## Cross References

See also:
- Documentation on document automation features in Essential DocIO
- Methods for inserting fields in documents

<!-- tags: [document variables, document automation, Essential DocIO, Syncfusion Winforms, version 11.4.0.26] keywords: [DocVariable, IDocument.Variables, IWParagraph.AppendField, document automation, document variables, document templates, field types, field options, preserve formatting] -->
```