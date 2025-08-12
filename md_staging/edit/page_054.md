```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_054.jpeg
document_name: edit
page_number: 054
page_id: edit#page_054
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:57:16Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- Explains how to enable and configure AutoReplace Triggers in the Essential Edit control for Windows Forms.
- Demonstrates the correction of mistyped tokens in real-time using AutoReplace Triggers.
- Provides code examples in C# and VB.NET for enabling AutoReplace Triggers.
- Details the configuration of triggers within the language settings using the `TriggersActivators` attribute.

## Content

### AutoReplace Triggers in Action

When typing `'` and mistyping "fro," the incorrect token is replaced with the correct token "for" as shown in **Figure 13**.

![Figure 13: After typing `'` the incorrect token "fro" is replaced with the correct token "for"](image.png)

### Enabling AutoReplace Triggers

To enable AutoReplace Triggers, use the `UseAutoreplaceTriggers` property as demonstrated below.

#### Code Examples

- **C#**
  ```csharp
  // Enables AutoReplace Triggers.
  this.editControl.UseAutoreplaceTriggers = true;
  ```

- **VB.NET**
  ```vb
  ' Enables AutoReplace Triggers.
  Me.editControl.UseAutoreplaceTriggers = True
  ```

### Defining Keys for AutoReplace Triggers

The keys used as AutoReplace Triggers are defined using the `TriggersActivators` attribute of the language in the configuration file, as shown below:

```xml
<ConfigLanguage name ="C#" Known ="Csharp" StartComment ="/" 
TriggersActivators =" ;.()" >
```

### Trigger Validity in Lexical States

Triggers can be flagged as valid only within specific lexical states. For example, you can prevent a trigger from firing within a comment by using the `AllowTriggers` attribute, as shown below.

```xml
<ConfigLanguage name ="C#" Known ="Csharp" StartComment ="/" 
TriggersActivators =" ;.()" >
```

Triggers can be flagged as valid only within the specific lexical states. For example, you can set a trigger not to fire, if it is in a comment within a language, by using the `AllowTriggers` attribute, as shown below.

## Page-level Navigation/TOC
- AutoReplace Triggers in Action
- Enabling AutoReplace Triggers
- Defining Keys for AutoReplace Triggers
- Trigger Validity in Lexical States

<!-- tags: [Syncfusion Winforms, AutoReplace Triggers, Edit, Configuration, Language, TriggersActivators, AllowTriggers, C#, VB.NET, version 11.4.0.26] keywords: [AutoReplace, Triggers, Enable, Define, Lexical States, C#, VB.NET] -->
```