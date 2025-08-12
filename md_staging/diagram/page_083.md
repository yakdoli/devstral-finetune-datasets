```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_083.jpeg
document_name: diagram
page_number: 083
page_id: diagram#page_083
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:11:47Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Provides a detailed look at the essential properties and behavior of symbols used in Windows Forms.
- Covers the process of customizing symbol settings using the Properties window.
- Explains how to save modified symbols into the symbol palette.

## Content

### Symbol4 Properties Overview
The properties window for "Symbol4" is shown in Figure 51. This window is divided into several categories, each detailing specific attributes of the symbol.

#### Appearance
- **BackgroundStyle**: `{Color [White], Type=Sl}`
- **LineStyle**: `{Width=1, Color [Black]}`
- **RenderingStyle**: `{Default}`
- **ShadowStyle**: `{False, Color [DimGray]}`

#### Behavior
- **BoundaryConstraintsE**: `True`
- **Header and Footer**: Not specified in detail
- **HeaderFooterData**: `Syncfusion.Windows.F` (unclear)

#### Layers
- **Layers**: `(Collection)`

#### Line Routing
- **BridgeStyle**: `Arc`
- **LineBridgeSize**: `16`
- **LineBridgingEnabled**: `False`
- **LineRoutingEnabled**: `False`

#### Logical Units
- **DocumentScale**: `1 px = 1 px`
- **DocumentSize**: `827 px; 1169 px`
- **MeasurementUnits**: `Pixel`

#### Miscellaneous
- **EnableSelectionListS**: `True`
- **LineRouter**: Not specified
- **LogicalSize**: `827 px; 1169 px`
- **MinimumSize**: `396.8504 px; 566.9291 px`
- **Name**: `Symbol4`
- **OptimizeLineBridging**: `False`
- **SizeToContent**: `False`

#### Saving the Modified Symbol
- After modifying the default settings, the symbol must be saved into the symbol palette.
- **Steps**:
  1. Go to the `File` menu.
  2. Click `Save`. 
  3. A `Save SymbolPalette` dialog will appear, as shown in the next screenshot.

### Figure: Properties Window

_Figure 51: Properties Window_

After modifying the default settings, we have to save this symbol into the symbol palette. Go to the `File` menu and click `Save`. A `Save SymbolPalette` dialog will appear as in the following screenshot.

## Code Examples

```xml
<!-- Example of Properties window setup XML configuration -->
<Syncfusion:Symbol Name="Symbol4" MinimumSize="396.8504,566.9291" SizeToContent="False" OptimizeLineBridging="False">
    <Appearance>
        <BackgroundStyle Type="Solid" Color="White" />
        <LineStyle Width="1" Color="Black" />
    </Appearance>
    <Behavior BoundaryConstraintsE="True" />
</Syncfusion:Symbol>
```

### Note
Ensure all custom settings are correctly reflected before saving the symbol to avoid any inconsistencies.

## Cross References
- See also: Symbol Customization Guide, Symbol Palette Management, Advanced Symbol Properties.

<!-- tags: [Syncfusion, Winforms, Diagram, Symbols, Properties, Save SymbolPalette, Symbol Palette] keywords: [Symbol4, Appearance, Behavior, Layers, Line Routing, Logical Units, Misc, Save, Symbol Palette, Customize] -->
```