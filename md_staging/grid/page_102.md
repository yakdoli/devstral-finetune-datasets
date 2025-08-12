```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_102.jpeg
document_name: grid
page_number: 102
page_id: grid#page_102
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:24:09Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview

- Virtual Grid setup for Windows Forms projects.
- Instructions on customizing properties and initializing the Virtual Grid.
- Step-by-step guide tailored for C# users.

## Content

### By Design (Virtual Grid)

#### Virtual Grid on Form

Figure 64: Virtual Grid on Form

2. Customize the other properties such as **BorderStyle**, and so on.

#### Initializing the Virtual Grid

**3.1.5.3 Initializing the Virtual Grid**

To initialize the Virtual Grid added to your application:

1. Double-click the form's background so that a handler for the form's load event is added to your code.
2. Add an `ExternalData` member to your form with the code given below.

```csharp
// Add an external data member.
private ExternalData _extData;
```

```vb
' Add an external data member.
Dim _extData As ExternalData
```

## Page-level Navigation/TOC (if applicable)

### WinForms-specific Conventions

- Treat control names, namespaces, and types exactly.
- Distinguish design-time vs runtime features.

## Cross References

See also:  
- [Design-Time Features in WinForms](#)
- [Grid Initialization and Customization](#)

### RAG Annotations

<!-- tags: [virtual-grid, winforms, form-design, initialization] keywords: [external data member, BorderStyle, handler, load event, form customization] -->
```