```markdown
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_033.jpeg
document_name: HTMLUI
page_number: 033
page_id: HTMLUI#page_033
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:04:29Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

## Overview
- Demonstrates the use of HTML documents as startup documents in HTMLUI.
- Explains how to create and track technical support incidents using "Direct-Trac" within the HTMLUI framework.

## Content

### Loading an HTML Document as the Startup Document

#### Figure 13: Loading an HTML document as the Startup Document
- The figure displays a window titled "HTMLUI" showing a startup document labeled "StartupDocument."
- The document contains the following:
  - A heading: **File Loaded At Startup**
  - Logos and text: **Track your Technical Support Incidents**
  - Subtext: **Direct-Trac enables you to create and track technical support incidents.**

### 4.1.1.1 Startup File Sample
#### Overview
- This sample demonstrates the implementation of a Startup Document using an HTML file in HTMLUI.
- Purpose: Showcasing how to configure and utilize HTML documents as the initial load content when an HTMLUI application starts.

## API Reference
- **Namespace:** Syncfusion.Windows.Forms.HTMLUI
- **Class:** HTMLUI
- **Properties:**
  - **StartupDocumentPath:** Specifies the path to the HTML file to be loaded as the startup document.

## Code Examples
```csharp
// Example: Setting the Startup Document
Syncfusion.Windows.Forms.HTMLUI.HTMLUI htmlUI = new Syncfusion.Windows.Forms.HTMLUI.HTMLUI();
htmlUI.StartupDocumentPath = "path-to-your-startup-document.html";
```

## Page-level Navigation/TOC
- **Figure 13:** Loading an HTML document as the Startup Document
- **4.1.1.1:** Startup File Sample

## Cross References
- For more details on HTMLUI properties and methods, see the HTMLUI API documentation.
- Refer to the section on configuring and customizing HTMLUI startup documents for additional guidance.

## RAG Annotations
<!-- tags: [syncfusion, winforms, htmlui, startup document, technical support incidents, direct-trac] keywords: [essential htmlui, startup document sample, loading html, technical incidents, direct-trac, startup file, windows forms, api reference, code examples] -->
```