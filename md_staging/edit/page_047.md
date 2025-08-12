```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_047.jpeg
document_name: edit
page_number: 047
page_id: edit#page_047
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:56:47Z
fidelity: lossless
-->

## Essential Edit for Windows Forms

### WinForms-specific conventions
- **C# Example**:
  ```csharp
  // Consider a scenario where configuration settings are being created dynamically in code.
  // Create a config lexem that belongs to a custom format.
  ConfigLexem configLex = new ConfigLexem("<%@", "%>", FormatType.Custom, false);

  // The actual regex can then be substituted with the lexical macro while defining the config lexem.
  // NameInConfig returns the name of the macro rounded with braces, like "{testmacro}".
  configLex.ContinueBlock = macro.NameInConfig;
  configLex.IsContinueRegex = true;
  ```

- **VB.NET Example**:
  ```vb
  ' Create and add a lexical macro to the EditControl.LexicalMacrosManager's collection.
  ' The Add method also returns the IMacro object associated with the lexical macro.
  Dim macro As IMacro = Me.EditControl.LexicalMacrosManager.Add("testMacro", ".+")

  ' Consider a scenario where configuration settings are being created dynamically in code.
  ' Create a config lexem that belongs to a custom format.
  Dim configLex As ConfigLexem = New ConfigLexem("<%@", "%>", FormatType.Custom, False)

  ' The actual regex can then be substituted with the lexical macro while defining the config lexem.
  ' NameInConfig returns name of the macro rounded with braces, like "{testmacro}".
  configLex.ContinueBlock = macro.NameInConfig
  configLex.IsContinueRegex = True
  ```

### See Also
- Language Elements

## Block Indent and Outdent
- This section discusses how to manage block indentation and outdenting in the Syncfusion Windows Forms controls.

<!-- tags: [configuration settings, lexical macros, config lexem, dynamic settings, block indentation, Windows Forms, edit control, lexical macros manager, custom format, indent, outdent] keywords: [lexical macro, config lexem, dynamic configuration, block indent, outdent, winforms, edit control, formatting] -->
```