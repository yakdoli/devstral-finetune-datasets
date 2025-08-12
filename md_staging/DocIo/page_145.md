```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_145.jpeg
document_name: DocIo
page_number: 145
page_id: DocIo#page_145
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:37:27Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- Form Field ActiveX controls can only be preserved in doc and docx formats.
- ActiveX controls cannot be inserted using DocIO.
- Describes working with CheckBox form fields in Word documents.

## Content

### Form Field ActiveX Controls

Note that the Form Field ActiveX controls shown in the following screenshot can only be preserved in doc and docx formats and cannot be inserted by using DocIO.

![ActiveX Controls](./Figures/ActiveXControls.png)

**Figure 47:** ActiveX Controls

#### 4.4.1.2.4.1 CheckBox

The `WCheckBox` class represents a check box form field in the Word document. To add a check box to the Word document, click **Check Box Form Field** on the **Forms** toolbar.

![Forms Panel](./Figures/FormsPanel.png)

**Figure 48:** Forms Panel

The properties of a check box can be configured in the CheckBox Form Field Options dialog, as shown below:

![CheckBox Properties in MS Word](./Figures/CheckBoxPropertiesMSWord.png)

**Figure 49:** CheckBox Properties in MS Word

### CheckBox Properties in MS Word
- **Check box size**: Options include "Auto" or specifying a size "Exactly".
- **Default value**: Can be set to "Not checked" or "Checked".
- **Run macro on**: Entry and Exit options are available.
- **Field settings**: Includes bookmark naming.
- **Check box enabled**: Checked by default.
- **Calculate on exit**: Can be enabled or disabled.

### Additional Notes
- The `WCheckBox` object allows customization of check box form fields.
- The "Bookmark" property provides a unique identifier for the check box.

## RAG Annotations
<!-- tags: [docio, formfield, activexcontrols, wcheckbox, winforms, msword] keywords: [form field, activeX controls, check box, word document, doc, docx, wcheckbox class, form toolbar, form field options] -->
```