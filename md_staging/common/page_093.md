```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_093.jpeg
document_name: common
page_number: 093
page_id: common#page_093
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:03:59Z
fidelity: lossless
-->

## Overview
- This section explains the configuration of controls in the Toolbox and introduces the Multi-Target Manager utility in Syncfusion WinForms.
- Guides users on reseting the toolbox if the installed controls are not properly reflected and outlines the utility's limitations based on framework versions.
- Explains the utility of using Multi-Target Manager in Visual Studio 2008 and its role in managing multiple framework versions.

## Content

### Toolbox Configuration

The Syncfusion Toolbox Installer ensures the correct configuration of controls in the Toolbox. Here is an information window indicating successful configuration:

**Figure 86: Information**

**Note:**
- You need to reset the toolbox if the installed controls are not reflected properly in the Toolbox.
- This tool will configure only the controls which are located under Installed Location] \Assemblies \ [Framework version].

### **1.13.6 Multi-Target Manager**

#### Overview
MultiTarget Manager helps in managing multiple .NET frameworks in your Visual Studio 2008 project, i.e., switching between multiple frameworks.

**Note:**
This is not essential for VS 2010 because Common Language Runtime (CLR) is different for both the 3.5 and 4.0 frameworks. VS 2010 selects the required .NET framework assembly for the corresponding projects. 3.5 and 4.0 are the only frameworks configured; the MultiTarget Manager utility allows you to work on framework 2.0 with VS 2010.

#### When to Use Multi-Target Manager?
When Essential Studio is installed in a machine comprising both 2.0 and 3.5 frameworks, then by default the target framework is set to 3.5 and the following registry entry AssemblyFoldersEx is also set to 3.5 assemblies. You can use the Multi-Target Manager to change the target framework to 2.0.

#### Registry Key
The registry key involved is:

```
HKLM\Software\Microsoft\.NetFramework\v2.0.50727\AssemblyFoldersEx\Syncfusion Essential Studio 3.5
```

#### Launching MultiTarget Manager
1. Open the Syncfusion Dashboard.
2. Click Utilities > Assembly Management.
3. Click the **Launch** button for Multi-Target Manager.

## References
- [Syncfusion Documentation]
- [Visual Studio 2008 and 2010 Frameworks]
- [Multi-Target Manager Usage]

<!-- tags: [syncfusion, winforms, multiframe, toolbox, multi-target] keywords: [syncfusion winforms, multiframe support, toolbox configuration, vs2008, vs2010, multitargeting, assembly management] -->
```