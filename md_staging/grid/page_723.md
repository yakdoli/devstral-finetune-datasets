```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_723.jpeg
document_name: grid
page_number: 723
page_id: grid#page_723
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:36:09Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Explains the functionality of adding new rows in a grid.
- Describes the GroupCaptionSection and its properties to control the display of captions.
- Provides details on available token formats for `<GroupOptions>.CaptionText`.

## Content

### GroupCaptionSection

This section within a group provides a caption bar above the column headers. The GroupCaptionRows are unbound rows created to combine records into a group. By default, they display the group category and the number of items in that group. The following properties can be used to control the display:

- `<GroupOptions>.ShowCaption`: Enables the display of the caption section; True by default.
- `<GroupOptions>.CaptionText`: Used to get/set the caption text.

![AddNew Rows](#fig291)<br>
**Figure 291: AddNew Rows**

**Figure 292: Group Caption Section**<br>
![Group Caption Section](#fig292)<br>

### CaptionText Tokens

The following table lists the available token formats for `<GroupOptions>.CaptionText`:

| Token             | Description                                                                                                     |
|-------------------|-----------------------------------------------------------------------------------------------------------------|
| `{TableName}`     | Displays the `CaptionSection.ParentTableDescriptor.Name`.                                                         |
| `{CategoryName}`  | Displays the `CaptionSection.ParentGroup.Name`.                                                         |
| `{CategoryCaption}` | Displays the Header Text of the column that this group belongs to.                                              |

## References
- See also: [Syncfusion Winforms Documentation](#syncfusion-docs)

<!-- tags: [grid, windows forms, add new rows, group caption section, caption text, token formats] -->
```