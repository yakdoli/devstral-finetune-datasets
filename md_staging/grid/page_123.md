```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_123.jpeg
document_name: grid
page_number: 123
page_id: grid#page_123
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:40:04Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Describes the accessibility features supported by the Essential Grid component in Windows Forms.
- Highlights the key capabilities related to keyboard navigation, text editing, and operation independence.
- Details how the grid component ensures compatibility with accessibility features without disrupting other system components or attributes.

## Content

### Accessibility Support in Essential Grid

The following table outlines the criteria, supporting features, remarks, and explanations regarding the accessibility features of the Essential Grid component in Windows Forms.

| Criteria                                                                                                                                                   | Supporting Features | Remarks                                                                                                     | Explanations                                                                                                                                                                                                 |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|-------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| (a) When software is designed to run on a system that has a keyboard, product functions shall be executable from a keyboard where, the function itself or the result of performing a function can be discerned textually. | Fully Supported      | Essential Grid supports keyboard navigation and the editing of text.                                                          | Events can be handled in order to have all the keys to be suppressed and simulated. The events could be made to be dependent on the cell or over the grid.                                                                 |
| (b) Applications shall should not disrupt or disable activated features of other products that are identified as accessibility features, where those features are developed and documented according to industry standards. Applications also shall not disrupt or disable activated features of any operating system that are identified as accessibility features where the application programming interface for those accessibility features has been documented by the manufacturer of the operating system and is available to the product developer. | Fully Supported      | Essential Grid component can be placed independent to other control, so that no other products or items on the operating system could be disrupted or disabled. | Unless the grid is bound to the shared data source with external control, the grid does not affect the attributes over the other. Refreshing the form can also be specified within the bounds of the grid object.                                                                                          |

## API Reference (if applicable)
- This page does not contain specific API references but focuses on the functional accessibility features of the Essential Grid component.

## Code Examples (if applicable)
- No code examples are provided in this section. The document focuses on the functional support and compatibility of the grid with accessibility standards.

## RAG Annotations
<!-- tags: [Essential Grid, Windows Forms, Accessibility, Keyboard Navigation, Text Editing, Independence from Operating System Features] keywords: [keyboard navigation, text editing, accessibility features, activated features, shared data source, grid component, bound controls, independent functionality] -->
```