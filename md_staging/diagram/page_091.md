```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_091.jpeg
document_name: diagram
page_number: 091
page_id: diagram#page_091
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:12:22Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- The document explains the Overview Control and discusses the Palette GroupBar and GroupView controls.
- Describes how users can drag-and-drop symbols onto a diagram using these controls.
- Explains the classification and maintenance of symbols through the use of GroupBar and GroupView.
- Lists properties and their descriptions for PaletteGroupBar and GroupView.

## Content

### 4.1.2 Palette GroupBar And GroupView

The Palette GroupBar control provides a way for users to drag-and-drop the symbols onto a diagram. It is based on the Syncfusion Essential Tools GroupBar control. Each symbol palette loaded in the PaletteGroupBar occupies a panel that can be selected by a bar button. The bar button is labeled with the name of the symbol palette. The symbols in the palette are shown as icons that can be dragged and dropped onto the diagram. This control allows users to add symbols to a palette, and save or load the palette whenever necessary. It provides a way to classify and maintain the symbols.

The PaletteGroupView control provides an easy way to serialize a symbol palette to and from the resource file of a form. At the design-time, users can attach a symbol palette to a PaletteGroupView control in a form. Selecting the PaletteGroupView, and clicking the Palette property in the Visual Studio .NET properties window, opens a standard Open File dialog, which allows the user to select a symbol palette file that has been created using the Symbol Designer.

The properties of the PaletteGroupBar and GroupView with their descriptions are given in the below table.

| Property    | Description                                   |
|-------------|-----------------------------------------------|
| BackColor   | Sets the background color of the component.  |

## Page-level Navigation/TOC (if applicable)
This section serves as an explanatory guide for the Palette GroupBar and GroupView, detailing their functionality and usage in maintaining and classifying symbols for diagrams, as well as their property settings.

## RAG Annotations
<!-- tags: [Windows Forms, Palette GroupBar, Palette GroupView, Syncfusion, Diagram, Symbol Palette] keywords: [drag-and-drop, diagrams, symbols, classification, maintenance, serialization, properties, designer] -->
```