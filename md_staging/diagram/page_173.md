```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_173.jpeg
document_name: diagram
page_number: 173
page_id: diagram#page_173
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:19:40Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Explains how to use the HistoryManager in a Windows Forms application.
- Demonstrates categorically arranging nodes using layers in the diagram.
- Includes a sample diagram illustrating the use of layers.

```csharp
Me.diagram1.Model.HistoryManager.EndAtomicAction()
```

## Content

### 4.6.4 Layers

#### Overview
Layers are transparent sheets that can be added to the model, and the objects are added to it. Layers allow to categorically arrange a set of nodes onto the diagram.

#### Sample Layers

![Model Layers](#)
*Figure 108: Model Layers*

1. **Sign up Client**
   - New Client
   - Register
   - Client Account Info
   - Explain Data Entry Procedures
   - End
2. **Monthly Account Services**
   - Data Entry
   - Decision
   - Review
   - Needs Revising
   - Email Revisions
   - Evaluate Revisions
   - Decision
3. **Additional Services**
   - End
   - Decision
   - Taxes
   - Controller

## Sample Layers

---

```html
<!-- tags: [syncfusion, winforms, diagram, historymanager, layer, version:11.4.0.26] keywords: [essential diagram, windows forms, model layers, categorical arrangement, end atomic action, client registration, monthly account services] -->
``` 
```