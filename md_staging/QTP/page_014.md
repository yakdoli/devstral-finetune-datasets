```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_014.jpeg
document_name: QTP
page_number: 014
page_id: QTP#page_014
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:02:01Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview
- The installation process of Syncfusion Essential QTP has been completed.
- Describes the configuration process involving the swfconfig file and how it maps Syncfusion controls to their corresponding custom server libraries.

## Content

### 2.1.2 Configuration
An XML file in QTP called **swfconfig** is the configuration file located at `(Installed location of Essential QuickTest Professional)\<version-2.0, 3.5, or 4.0>\swfconfig`, which contains all the mapping information for QTP to recognize Syncfusion controls. In **swfconfig**, the controls are mapped to their corresponding custom server libraries (Essential QuickTest Professional DLLs) by giving the fully qualified name of the DLL.

**Note:** The fully qualified name is the name of the file mentioned with its complete path.

Any event that is triggered while working with a Syncfusion control, either by the user or the program activity, will be handled by the corresponding method in the custom library (DLL) given as the `<DllName>` tag under the `<Control>` tag.

An XML file can be configured in one of two ways, automatically or manually.

#### 2.1.2.1 Automatic Configuration
This section provides the details about the configuration of the swfconfig file using the SwfConfigUtility. Refer to the Utility section of this document.

## API Reference (if applicable)

## Code Examples (multi-language supported)

## Page-level Navigation/TOC (if applicable)

## Cross References
- See also: `Syncfusion Essential QTP`
- `swfconfig` file mapping

## RAG Annotations
<!-- tags: [Syncfusion, Winforms, QTP, swfconfig, version-11.4.0.26, Essential QuickTest Professional, configuration] keywords: [essential, qtp, configfile, dllmapping, swfconfig] -->
```
```