# Visual refinement — worked reference

Read this reference when a product needs iterative UI or identity discovery.
Use it as evidence for the *shape* of the process, not as a palette or style
template for unrelated products.

## Contents

1. Starting conditions
2. Refinement sequence
3. What made the process work
4. Portable round template
5. What not to generalize

## 1. Starting conditions

The reference product was a local-first personal productivity dashboard with
broad product goals but no settled visual system. The user wanted a dark-first
interface, comfortable for long sessions, compact but not sterile, extensible
over time, and recognizably its own product rather than a generic Kanban clone.

The visual process did not attempt to solve every axis at once. It moved from
atmosphere to system, then from system to components, and finally from product
UI to brand identity.

## 2. Refinement sequence

### Atmosphere and palette

Several named palette directions were compared. The user selected aubergine for
its atmosphere while borrowing the contrast and accent discipline of another
direction. The chosen family was then narrowed:

1. Start from aubergine.
2. Smoke and mute it for extended viewing.
3. Increase lavender's role in the accents and general scheme.
4. Prefer teal over copper as the primary supporting accent.
5. Reserve copper for Claude/Anthropic semantics and mint for Codex semantics.

The important pattern is **base direction → synthesis → controlled accent
rebalance**, not the specific colors.

### Typography, density, and geometry

The user compared one direction's typography and card shape against another's
muted compactness. The result synthesized those traits rather than choosing a
whole mockup unchanged. Descriptive copy was deprioritized relative to compact
operational information. IBM Plex was then selected from focused typography
previews.

This round isolated:

- type personality;
- information density;
- card geometry;
- hierarchy; and
- how much secondary description deserved space.

### Navigation and component coherence

Feedback on the sidebar and headers became concrete changes:

- remove the unattractive control-desk identity;
- rename the product and settle its capitalization;
- condense navigation and remove decorative bullet points;
- make all tabs share the dashboard's crisp outlines and coloration while
  preserving their different information structures;
- expand project cards into wider, information-rich operational rows; and
- fill unused sidebar depth with useful context rather than decoration.

Several sidebar-function concepts were compared; one was selected as the
context-oriented lower panel. This is evidence that spatial leftovers should be
resolved through product utility, not ornamental filler.

### Identity and logo

Logo exploration started from user-provided fishhook references. Early concepts
were rejected as too busy. The process then narrowed around these invariants:

- keep the settled capitalization of the product name;
- use an almost exact hook silhouette in place of one letterform;
- orient it so that letter still reads correctly;
- contain the color within the mark rather than scattering accent effects;
- vary the hook shape slightly between finalists; and
- test a synthesis of two promising concepts before ratifying the final option.

The final direction emerged through silhouette and geometry refinement, not
through adding detail. Small and large lockups were preserved for later use.

## 3. What made the process work

### Named options

Every comparison used stable labels. The user could say “C,” “D,” or “combine B
and D” without ambiguity. Labels also made rejected directions durable.

### Synthesis was allowed

The user was never forced to choose one entire concept. Typography from one,
density from another, and accent treatment from a third could become an explicit
new direction.

### Approved invariants accumulated

Later rounds did not reopen dark-first, aubergine atmosphere, restrained
contrast, or compactness without cause. Each approval reduced the active design
surface.

### One or two variables changed per refinement

Requests such as “more lavender,” “teal over copper,” “use Plex,” “turn the hook
around,” and “vary the hook shape” were interpretable because the rest of the
concept remained stable.

### Product-wide coherence followed local selection

Once the global language was approved, tabs and components were brought into
the same crisp system while retaining their functional differences. A visual
system is not identical page structure.

### Decisions became durable artifacts

The final work included exact tokens, component rules, typography, logo assets,
screen references, and documentation. Without that step, the apparent design
would still depend on the original conversation.

## 4. Portable round template

Use this compact structure for each visual round:

```markdown
## Round <N>: <axis being decided>

### Fixed invariants
- <already approved rule>

### Options
- A — <defining difference and tradeoff>
- B — <defining difference and tradeoff>
- C — <defining difference and tradeoff>

### Recommendation
<Preferred direction and why it fits the product.>

### User decision
State: PROPOSED | SELECTED | RATIFIED | DEFERRED | REJECTED
Choice or synthesis: <...>

### Design delta for the next round
- Preserved: <...>
- Changed: <...>
- Still open: <...>
```

## 5. What not to generalize

- Do not reuse smoked aubergine, lavender, teal, Plex, compact ledger cards, or
  nautical imagery merely because they succeeded here.
- Do not require a logo process for internal tools that do not need identity.
- Do not make every feature wait for visual exploration when the Quick lane is
  enough.
- Do not treat subjective preference as universal design evidence.
- Do generalize the narrowing mechanics: labeled alternatives, synthesis,
  cumulative invariants, controlled deltas, system-wide application, and durable
  ratification.
