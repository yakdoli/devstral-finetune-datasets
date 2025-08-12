```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_148.jpeg
document_name: diagram
page_number: 148
page_id: diagram#page_148
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:15:51Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Content

### Hierarchical Tree Layouts

#### Figure 85: Top-to-Bottom Hierarchical Tree Layout

![Top-to-Bottom Hierarchical Tree Layout](figures/Figure85.png)

#### Figure 86: Bottom-to-Top Hierarchical Tree Layout

![Bottom-to-Top Hierarchical Tree Layout](figures/Figure86.png)

### 4.5.1.6 Graph Layout Manager

The `GraphLayoutManager` is an abstract base class that can be used for implementing layout managers for diagrams composed primarily of nodes forming connected graphs. The `GraphLayoutManager` implements the infrastructure for initializing, validating, and creating the diagram graph by enumerating the diagram model's child nodes. It also enables positioning diagram nodes using the layout strategies provided by specialized directed tree layout managers that derive from it.

The event of the `Graph Layout Manager` class and its description is given below:

| Event                | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| PreferredLayout Event | Event provides the application a chance to customize the layout of the diagram. |

**Programmatically, it is implemented as follows.**
```csharp

```

## Page-level Navigation/TOC (if applicable)
- Hierarchical Tree Layouts
  - Top-to-Bottom Hierarchical Tree Layout
  - Bottom-to-Top Hierarchical Tree Layout
- 4.5.1.6 Graph Layout Manager
  - Overview and Features
  - Event Details
  - Implementation

## Code Examples (multi-language supported)
```csharp
// Example code snippet for customizing layout
Diagram.LayoutManager = new CustomLayoutManager();
Diagram.LayoutManager.PreferredLayout += (sender, args) =>
{
    // Implement custom layout logic here
};
```

## RAG Annotations
<!-- tags: [Syncfusion, Winforms, Diagram, Graph Layout Manager, Hierarchical Tree Layout] keywords: [top-to-bottom layout, bottom-to-top layout, preferred layout event, directed tree layout, custom layout] -->
```