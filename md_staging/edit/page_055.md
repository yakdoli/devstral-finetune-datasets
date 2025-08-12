```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_055.jpeg
document_name: edit
page_number: 055
page_id: edit#page_055
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:57:13Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

<lexem BeginBlock="/*" EndBlock="*/" Type="Comment" OnlyLocalSublexems="true" IsComplex="true" IsCollapsable="true" CollapseName="/*...*/" AllowTriggers="false">

The words to be replaced when the AutoReplace Triggers key is pressed can be defined by using the code given below.

### Code Example: AutoReplace Triggers

```csharp
this.editControl1.Language.AutoReplaceTriggers.AddRange(new AutoReplaceTrigger[] { new AutoReplaceTrigger("tis", "this"), new AutoReplaceTrigger("fro", "for") });
```

```vbnet
Me.editControl1.Language.AutoReplaceTriggers.AddRange({ New AutoReplaceTrigger("tis", "this"), New AutoReplaceTrigger("fro", "for") })
```

### Configuring AutoReplace Triggers in the Language Definition

The words to be replaced can also be defined within the language definition in the configuration file, as shown below.

```xml
<AutoReplaceTriggers>
    <AutoReplaceTrigger From ="tis" To ="this" />
    <AutoReplaceTrigger From ="itn" To ="int" />
</AutoReplaceTriggers>
```

#### See Also

- [AutoComplete Support](AutoComplete Support)

### 4.4 Text Visualization

The various text visualization features of Edit control is elaborated under the following topics:

#### 4.4.1 Text Navigation
***

© 2013 Syncfusion. All rights reserved.
```