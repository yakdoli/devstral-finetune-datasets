```html
<!-- 
 source: image
 domain: syncfusion-sdk
 task: pdf-ocr-to-markdown
 language: en
 source_filename: page_208.jpeg
 document_name: pdf
 page_number: 208
 page_id: pdf#page_208
 product: Syncfusion Winforms
 version: 11.4.0.26
 timestamp: 2025-08-09T07:36:29Z
 fidelity: lossless
-->

# Essential PDF

## Overview
- A custom schema defines the structure of customized information records.
- Use the customschema class to:
  - Define custom metadata files.
  - Add them to the PDF document.

## Content

### Defining a Custom Schema

Add the following code to define a custom schema.

```csharp
[C#]

//create a custom schema
CustomSchema cs = new CustomSchema(xml,"custom","http://www.syncfusion.com");
cs["Author"] = "Syncfusion";
cs["creationDate"] = DateTime.Now.ToString();
cs["DOCID"] = "SYNCSAM001";
```

The code snippet above illustrates the creation of a custom schema or first-level metadata field, `www.syncfusion.com`, which is a link. The second-level metadata fields under this link are `Author`, `creation date`, and `DocID`.

On running the code, the values assigned to these fields are reflected as data when expanding the first-level metadata field, as shown in the following screenshot.

## API Reference

- **Namespace**: Syncfusion
- **Class**: CustomSchema
- **Properties**:
  - `Author`: String representing the author of the document.
  - `creationDate`: String representing the date of creation of the document.
  - `DOCID`: String representing the document ID.

## Code Examples

The provided C# code demonstrates how to create and assign values to a custom schema in a PDF document using the `CustomSchema` class.

## Cross References

- See also: [Syncfusion PDF Documentation](https://www.syncfusion.com/documentation/pdf/net)

<!-- tags: [Syncfusion, PDF, CustomSchema, WinForms, Net, Essential PDF] keywords: [custom schema, metadata, PDF, document, Syncfusion, schema definition, C#] -->
```