```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_131.jpeg
document_name: DocIo
page_number: 131
page_id: DocIo#page_131
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:36:11Z
fidelity: lossless
-->

# ParagraphItem Class Hierarchy

## Overview
- This page provides a detailed look at the class hierarchy of the ParagraphItem abstract class in the "Essential DocIO."
- It includes various abstract and concrete classes that inherit from ParagraphItem.
- The figure illustrates the hierarchical structure and relationships among different classes.

## Content

### Class Hierarchy Diagram
The diagram below represents the hierarchical structure of the ParagraphItem class. It includes various concrete and abstract classes that inherit from ParagraphItem.

```plaintext
ParagraphItem
├── WComment
├── WFieldMark
├── WFootnote
├── WPicture
├── WSymbol
├── WTextBox
├── Break
├── Watermark
│   ├── PictureWatermark
│   └── TextWatermark
├── WTextRange
│   └── WField
│       ├── WMergeField
│       └── WFormField
│           ├── WCheckBox
│           ├── WTextFormField
│           └── WDropDownFormField
```

### Legend
- **Abstract** classes are represented in purple.
- **Class** names are represented in gray.

## Public Property

| Name       | Description                                       |
|------------|---------------------------------------------------|
| [unclear]                       | [unclear]                       |

## Page-level Navigation/TOC
- The page describes the ParagraphItem class hierarchy and its associated properties.

## Cross References
- For more information on related classes and functions, refer to the [ParagrahItem Class](#ParagrahItem_Class) and its subclasses.

## RAG Annotations
<!-- tags: [DocIO, ParagraphItem, ClassHierarchy, WComment, WFieldMark, WFootnote, WPicture, WSymbol, WTextBox, Break, Watermark, WTextRange, WField, WMergeField, WFormField, WCheckBox, WTextFormField, WDropDownFormField] keywords: [ParagraphItem, hierarchy, class, abstract, concrete, WComment, WFieldMark, WFootnote, WPicture, WSymbol, WTextBox, Break, Watermark, WTextRange, WField, WMergeField, WFormField, WCheckBox, WTextFormField, WDropDownFormField, publicproperty] -->
```