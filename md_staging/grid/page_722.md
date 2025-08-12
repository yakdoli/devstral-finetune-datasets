```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_722.jpeg
document_name: grid
page_number: 722
page_id: grid#page_722
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:38:28Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- TableOptions.GroupHeaderSectionHeight
- TableOptions.GroupFooterSectionHeight
- Group headers and footers can be populated by handling the QueryCellStyleInfo event wherein you can check for the Header / Footer cell type and provide the data.

## Content

### Group Header and Footer

Group headers and footers can be populated by handling the **QueryCellStyleInfo** event wherein you can check for the Header / Footer cell type and provide the data.

#### Figure 289: Group Header and Footer

![Group Header and Footer](289-group-header-footer.png "GroupHeader and Footer")

### GroupPreviewRows

The **GroupPreviewSection** is the suitable place when you want to display memo fields or add custom notes for a given group. It can be enabled by setting the `<GroupOptions>.ShowGroupPreview` property to `True`. You can adjust the size of the preview row through the `TableOptions.GroupPreviewSectionHeight` property. The QueryCellStyleInfo event can be used to populate the preview rows.

#### Figure 290: Group Preview Section

![Group Preview Section](290-group-preview-section.png "Group Preview Section")

### AddNew Records

Each group can optionally have an **AddNew** row where you can provide the values for a new record. Once a new record is entered, the record will be sorted into the existing record set and will be assigned a group's category automatically. The visibility of the **AddNewRecord** can be controlled through the following two boolean properties:

- `<GroupOptions>.ShowAddNewRecordBeforeDetails` - adds the **AddNew** row at the top of a group.
- `<GroupOptions>.ShowAddNewRecordAfterDetails` - adds the **AddNew** row at the bottom of a group.

<!-- tags: [product, module, control, api, version?] keywords: [k1, k2, ...] -->
```