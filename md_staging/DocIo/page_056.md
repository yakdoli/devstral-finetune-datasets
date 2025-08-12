```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_056.jpeg
document_name: DocIo
page_number: 056
page_id: DocIo#page_056
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:31:32Z
fidelity: lossless
-->

## Overview

- This page provides an introduction to the basic concepts and features of Essential DocIO, including an overview of the DLS entities.
- It explains the simplified hierarchy of WordDocument components within Microsoft Word documents.
- Reference to Class Reference documentation for comprehensive information on classes is provided.

## Content

### 4 Concepts and Features

This tutorial illustrates how to get started with Essential DocIO. It will give you a basic introduction to the concepts you need to know before getting started with the product, and some tips and ideas on how to implement DocIO in your projects. Each category under this section explains about the various DLS entities of DocIO.

**Note:** Refer to the Class Reference documentation for comprehensive information on the classes.

This section covers information on the following:

#### 4.1 Basic Concepts

Object model of Microsoft Word document is dendritic. WordDocument is the root of such a tree. Base, simplified hierarchy of document content can be shown as follows.

![Figure 22: Object Model of Word Document](https://via.placeholder.com/400x200?text=Figure+22%3A+Object+Model+of+Word+Document)

WordDocument and the rest of the nodes in such a tree (which are containers for content: text or graphics), are inherited from the abstract class, Entity. This class has the `EntityType` property, which defines the type of the node. Such an approach gives an opportunity to generalize the work with the nodes of the WordDocument tree.

<!-- tags: [docio, worddocument, objectmodel, dendritic, worddocumenthierarchy, entityType] keywords: [essential docio, basic concepts, dendritic structure, word document, inheritance, generalization] -->
```