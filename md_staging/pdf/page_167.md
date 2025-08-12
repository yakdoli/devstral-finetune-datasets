```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_167.jpeg
document_name: pdf
page_number: 167
page_id: pdf#page_167
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:35:15Z
fidelity: lossless
-->

## Overview

- This page explains the unordered list marker representation using the `PdfUnorderedMarker` class and the supported marker styles via the `PdfUnorderedMarkerStyle` class.
- It discusses how to use custom styles like `CustomString`, `CustomImage`, and `CustomTemplate`.
- The section on drawing lists covers various `Draw` overloads for rendering lists on pages.
- Events for list rendering are detailed, along with the needed namespaces for working with lists.
- The interactive features section outlines how user interaction can be implemented in Essential PDF.

## Content

### Unordered List Marker Representation

**Unordered list has an unordered marker that is represented by the `PdfUnorderedMarker` class. Unordered marker has the marker style represented by the `PdfUnorderedMarkerStyle` class. The following marker styles are supported:**

- None
- Disk
- Square
- Asterisk
- Circle
- CustomString
- CustomImage
- CustomTemplate

**Default list marker has Disk style.**

To use the `CustomString`, `CustomImage` or `CustomTemplate` style, you must set the `Text`, `Image` or `Template` property of the `PdfUnorderedMarker` class respectively.

#### Drawing Lists

**There are a lot of `Draw` overloads that enable you to draw lists on a series of pages or on a `PdfGraphics` page.**

#### Events

**Each list raises the following four events:**

- `BeginPageLayout` event is raised when the list starts layouting on page
- `EndPageLayout` event is raised when the list completes layouting on the page
- `BeginItemLayout` event is raised when the item starts layouting
- `EndItemLayout` event is raised when the item completes layouting

**Note:** You should add the `Syncfusion.Pdf.List` namespace to work with lists.

### 4.1.3 Interactive Features

This section demonstrates various user interactive features and how it can be implemented with Essential PDF. It includes the following topics.

## API Reference (if applicable)
- None listed in this extracted content.

## Code Examples (if applicable)
- No code examples provided in this section.

## Page-level Navigation/TOC (if applicable)
- 4.1.3 Interactive Features

## Cross References
- None listed in this extracted content.

## RAG Annotations
<!-- tags: [pdf, unordered marker, marker style, custom strings, custom image, custom template, drawing lists, events, interactive features, syncfusion] keywords: [unordered list, PdfUnorderedMarker, PdfUnorderedMarkerStyle, Disk style, CustomString, CustomImage, CustomTemplate, Draw, BeginPageLayout, EndPageLayout, BeginItemLayout, EndItemLayout, Syncfusion.Pdf.List namespace, user interactive features] -->
```