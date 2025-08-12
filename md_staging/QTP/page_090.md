```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_090.jpeg
document_name: QTP
page_number: 090
page_id: QTP#page_090
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:07:18Z
fidelity: lossless
-->

# Resizing Nodes in Diagram Control

## Overview
- Explains how to resize nodes in a diagram control using the `ResizeNode` function.
- Includes examples demonstrating the usage of `ResizeNode` in QTP.

## Content

### Method Description

Below is a table summarizing the method details:

| **Method Name** | **Description** | **Signature** | **Return Type** |
|------------------|------------------|---------------|------------------|
| **ResizeNode** | Resizes the node in diagram control. | public void ResizeNode(string name, float offsetX, float offsetY) | void |

### Applying ResizeNode in QTP

The following code examples illustrate how to resize the node size in the diagram control.

#### Code Example for Diagram Control

```csharp
[For Diagram Control]
SwfWindow("Simple Flow Diagram").SwfObject("diagram1").SelectNode("EllipseStart"
SwfWindow("Simple Flow Diagram").SwfObject("diagram1").ResizeNode("LineConnectror1",-42.467853,0.00000
```

### API Reference

#### Namespace: `DocuSyncfusionQuickTestProfessional`

##### Method: `ResizeNode`

**Signature:**
```csharp
public void ResizeNode(string name, float offsetX, float offsetY)
```

**Parameters:**
- **name:** Type - `string`  
  Description - The name of the node to resize.
- **offsetX:** Type - `float`  
  Description - The horizontal offset for resizing.
- **offsetY:** Type - `float`  
  Description - The vertical offset for resizing.

**Returns:**
- `void`

### Code Examples

#### Example 1: Resizing a Node in a Diagram Control

```csharp
// Selects a specific node in the diagram control
SwfWindow("Simple Flow Diagram").SwfObject("diagram1").SelectNode("EllipseStart"

// Resizes the selected node using specified offsets
SwfWindow("Simple Flow Diagram").SwfObject("diagram1").ResizeNode("LineConnectror1",-42.467853,0.00000
```

## Page-level Navigation/TOC (if applicable)
- Applying ResizeNode in QTP
- API Reference
- Code Examples

<!-- tags: [syncfusion, qtp, diagram control, resize node, code examples] keywords: [resize, node, diagram, qtp, method, signature, parameters, return, code example, swfwindow, flow diagram, ellipsetart, lineconnectror, offset] -->
```