```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_262.jpeg
document_name: DocIo
page_number: 262
page_id: DocIo#page_262
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:44:51Z
fidelity: lossless
-->

# Essential DocIO

To perform Mail Merge

## Overview
- Open the Insert menu, point to Fields, and then click MergeField.
- Provide the merge field name, and the text to be inserted before and after the field.
- Note that the merge field name should match the field name of the data source.
- Mail merge operations are performed by the Execute or ExecuteGroup methods.

## Content

### Step 1: Insert Merge Field
1. Open the Insert menu, point to Fields, and then click MergeField.

#### Figure 78: Field Dialog Box
![Figure 78: Field Dialog Box](https://example.com/figure78.png)

### Step 2: Configure Merge Field
2. Provide the merge field name, and the text to be inserted before and after the field. Note that the merge field name should match the field name of the data source.

#### Figure 79: Merge field name Provided
![Figure 79: Merge field name Provided](https://example.com/figure79.png)

## Mail Merge Operations
Mail merge operations are performed by the Execute or ExecuteGroup methods. There are several overloads of these methods for different data sources.

## API Reference
### Methods
- **Execute**
- **ExecuteGroup**

<!-- tags: [syncfusion-sdk, winforms, docio, mailmerge, execute, executegroup] keywords: [mergefield, data source, field properties, field options, text formatting, preserve formatting] -->
```