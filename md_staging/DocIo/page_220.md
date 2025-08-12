```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_220.jpeg
document_name: DocIo
page_number: 220
page_id: DocIo#page_220
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:42:18Z
fidelity: lossless
-->

# Essential DocIO

```vb
para.ParagraphFormat.OutlineLevel = OutlineLevel.Level8
```

## Content

### Tabs

The **Tabs** class represents a tab collection within a paragraph. The **Tab** class represents a single tab within the tab collection.

#### Class Hierarchy

- **WParagraphFormat**
  - **Tabs**

#### Public Properties

| Name            | Description                                             |
|-----------------|---------------------------------------------------------|
| Justification   | Gets or sets the tab justification.                    |
| TabLeader       | Gets or sets the tab leader.                           |
| Position        | Gets or sets the tab position.                         |
| DeletePosition  | Gets or sets the Clear tab position.                   |

#### Public Methods

| Name                                         | Description                                                   |
|----------------------------------------------|---------------------------------------------------------------|
| AddTab()                                     | Adds default tab to the paragraph.                             |
| AddTab(float position)                      | Adds tab at the specified position.                            |
| AddTab(float position, TabJustification justification, TabLeader leader) | Adds tab at specified location with the specified tab justification and leader. |
| RemoveAt(int index)                         | Removes tab at specified index from the tab collection.        |

## Cross References

- See also: [4.4.2.4.1 Tabs]

<!-- tags: [tabs, paraformattabs, tabcollection, tabjustification, tableader, winforms] keywords: [paragraph format, outline level, tab properties, tab methods] -->
```