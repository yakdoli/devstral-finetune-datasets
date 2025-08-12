```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_153.jpeg
document_name: tools
page_number: 153
page_id: tools#page_153
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:57:06Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Docking Manager Tasks Window

### Overview
- Explains the Docking Manager Tasks Window and its runtime features.
- Discusses options for configuring the appearance, behavior, and serialization of docking windows.

### Content

#### Figure 68: Docking Manager Tasks Window
The Docking Manager Tasks Window provides various options for customizing docking windows in Windows Forms.

##### Appearance
- **Dock Label Alignment Style**: Default
- **Dock Tab Alignment Style**: Left
- **Paint Borders**: Unchecked
- **Themes Enabled**: Unchecked

##### Behavior
- **Dock with Fill Style**: Unchecked
- **Disallow Floating**: Unchecked
- **Drag Provider Style**: VS2005
- **Docking Windows Visual Style**: Office2007
- **Image List**: Unspecified

##### Serialization
- **Docking Windows State Persist**: Unchecked

#### 3.4.3.4 RunTime Features

The following runtime features are discussed in this section.

##### 3.4.3.4.1 Browsing Key

DockingManager lets you specify the keyboard key combinations to tab through the docked controls. The property `BrowsingKey` of the docking manager provides modifiers like CTRL, SHIFT, ALT Keys, and keys like A, B, C, 0, 1, etc. The user can also provide a combination of modifiers and keys. Example: "CTRL + 0", as shown in the image below.

## Code Examples
The specific code for configuring the `BrowsingKey` property would look something like this:

```csharp
dockingManager1.BrowsingKey = "CTRL + 0";
```

This example demonstrates how to set the `BrowsingKey` to a combination of the `CTRL` key and the `0` key.

## Page-level Navigation/TOC
- 3.4.3.4 RunTime Features
  - 3.4.3.4.1 Browsing Key

## Cross References
See also:
- Document structure and control customization in Syncfusion Winforms.
- Additional runtime features for DockingManager.

<!-- tags: [DockingManager, Windows Forms, Essential Tools, Runtime Features, Browsing Key] keywords: [Docking Manager Tasks Window, BrowsingKey, Key combinations, Docked controls, CRT Key, Visual Style] -->
```
