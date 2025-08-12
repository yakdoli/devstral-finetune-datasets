```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_126.jpeg
document_name: edit
page_number: 126
page_id: edit#page_126
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:01:59Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

```csharp
// Resets selection.
this.editControl1.ResetSelection();
```

```vb.net
' Removes selection from text.
Me.editControl1.SelectionCancel()

' Resets selection.
Me.editControl1.ResetSelection()
```

## 4.5 Syntax Highlighting and Code Coloring

Essential Edit supports Syntax Highlighting and Code Coloring of some of the commonly used languages with the help of configuration files. It provides pre-defined configuration files for languages like SQL, Delphi or Pascal, HTML, VB.NET, XML, Java, VBScript, JScript and C#.

These configuration settings are made available in the `EditControl.Configurator.KnownLanguages` collection. The order of the languages in this collection is as follows: C#, Delphi, HTML, Java, JScript, Default Text, SQL, VB.NET, VBScript and XML.

### Pre-defined Configuration Files

You can set the Edit Control to use any of the pre-defined configuration settings by using the `ApplyConfiguration` method, as shown below.

**Example:**

```csharp
// Considering configuration settings for SQL as an example.
// Using the KnownLanguages enumerator.
this.editControl1.ApplyConfiguration(KnownLanguages.SQL);

// Using the file extension of the associated language.
this.editControl1.ApplyConfiguration(this.editControl1.Configurator.GetLanguage("sql") as IConfigLanguage);

// Using the associated index in the KnownLanguages collection.
```

## API Reference (if applicable)

- `ApplyConfiguration()` method:
  - **Parameters**:
    - `language`: KnownLanguages or IConfigLanguage.
  - **Description**: Applies the specified configuration settings to the Edit Control.

### Code Examples

- **Using KnownLanguages Enumerator**:
  ```csharp
  this.editControl1.ApplyConfiguration(KnownLanguages.SQL);
  ```

- **Using File Extension**:
  ```csharp
  this.editControl1.ApplyConfiguration(this.editControl1.Configurator.GetLanguage("sql") as IConfigLanguage);
  ```

<!-- tags: [syncfusion, winforms, essentialedit, syntaxhighlighting, codecoloring, applyconfiguration] keywords: [editcontrol, knownlanguages, text editor, multitext editor, code highlighting, c#, sql, pascal, html, vb.net, xml, java, vbscript, jscript] -->
```