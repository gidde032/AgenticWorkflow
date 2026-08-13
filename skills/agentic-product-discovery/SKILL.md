---
name: agentic-product-discovery
description: >-
  Turn an uncertain product or feature idea into a ratified product-and-design
  contract before architecture and implementation. Use when deciding what to
  build; comparing existing software with a custom product; clarifying users,
  workflows, scope, value, requirements, and the capture of deferred ideas
  (their placement belongs to `agentic-project-memory`); shaping information
  architecture or interaction models; exploring UI directions, palettes,
  typography, density, navigation, components, or branding; iterating through
  visual mockups and synthesis rounds; or preserving approved product and design
  decisions for fresh agents. Routes rendering, image generation, system design,
  project bootstrap, and implementation to their owning skills.
---

# Agentic Product Discovery

Turn uncertainty into explicit decisions. End with a ratified contract another
agent can use without reconstructing the discovery conversation.

Worked examples and provenance: `examples.md`.

> Explore broadly enough to expose meaningful choices, then narrow deliberately
> until product behavior and visual direction are durable artifacts rather than
> memories in a chat.

---

## 1. Own the product question, not every downstream technique

Own:

- problem, audience, desired outcome, and current workflow;
- build-vs-buy and scope/value tradeoffs;
- product boundaries, requirements, workflows, and information architecture;
- experience principles and interaction direction;
- iterative visual and brand refinement;
- explicit decision states and deferred ideas; and
- the ratified handoff into specification and architecture.

Do not own implementation architecture, production UI code, or delivery. Use
the routing table in §7 as soon as another skill becomes the better specialist.
Discovery may produce wireframes, comparison panels, or prototypes as evidence,
but those artifacts answer a product or design question; they are not permission
to begin the build.

---

## 2. Choose the smallest useful discovery lane

| Lane | Use for | Expected shape |
|---|---|---|
| **Quick** | One bounded feature or a mostly settled direction | 1–2 question rounds, 2–3 options, short decision record |
| **Standard** | A new product or meaningful capability | Problem/workflow framing, options, interaction model, visual direction, ratified brief |
| **Deep** | Broad ecosystem product, uncertain audience, costly or irreversible choices | Research, build-vs-buy, several workflows, multiple design rounds, formal handoff |

If the user arrives with a complete approved specification, verify that the
critical choices are actually closed, record any remaining uncertainty, and
exit. Do not force discovery ceremony onto settled work.

---

## 3. The discovery loop

### Step 1 — Establish reality and the decision surface

Gather the existing artifacts first: notes, Markdown, screenshots, products,
repositories, workflows, constraints, prior decisions, and reference designs.
Separate current facts from aspirations.

State:

- who has the problem and what they do today;
- the outcome they want, independent of a proposed solution;
- hard constraints and privacy/cost requirements;
- decisions already made and their confidence;
- unknowns that materially change scope, architecture, or experience; and
- the next decision this conversation needs to make.

When alternatives, pricing, capabilities, or recommendations may have changed,
verify them with current primary sources. Compare real fit and switching cost,
not feature-list length.

### Step 2 — Ask questions in bounded, thematic rounds

Ask the smallest set that changes the next decision. Group questions by theme—
problem/workflow, scope, data, interaction, visual direction—not as one giant
intake form. After each round:

1. summarize what changed;
2. label assumptions and unresolved choices;
3. recommend a default with rationale; and
4. ask the user to select, synthesize, reject, or defer.

Follow `agentic-collaboration-cadence` for approval boundaries. The agent
proposes; the human ratifies product behavior and taste.

### Step 3 — Model the product before its screens

Describe the smallest coherent user journey, core objects, and information
hierarchy. Identify the product's main page or home state, primary actions,
navigation model, empty states, failure states, and future extension seams.

Keep early data and architecture language conceptual. Record what the product
must express or preserve; leave storage, framework, and service choices for
`system-design` or `architecture` after the behavior is stable.

### Step 4 — Generate materially different options

Offer 2–5 labeled options only when they expose a real tradeoff. For each, state:

- defining idea;
- utility and user impact;
- scope and complexity;
- extensibility consequences;
- risks and reversibility; and
- the agent's recommendation.

Avoid fake variety: renamed versions of the same approach waste a decision
round. Avoid unlimited ideation: once one direction clearly wins, narrow.

### Step 5 — Run visual discovery as a controlled refinement process

Use this sequence for UI, brand, or interaction-heavy products. Read
`references/visual-refinement-worked-example.md` when running a visual
discovery lane.

1. **Set the visual brief.** Capture atmosphere, references, accessibility,
   density, contrast, platform, long-session comfort, and disliked defaults.
2. **Create a direction panel.** Show 3–5 named directions using comparable
   representative content. Make palette, typography, geometry, density,
   navigation, and signature element deliberately distinct.
3. **Select or synthesize.** Ask which direction supplies the base and which
   individual traits should be borrowed. Record the winning invariants.
4. **Refine controlled axes.** Change one or two axes per round—such as accent
   balance, typography, card shape, sidebar function, or logo silhouette—while
   preserving everything already approved.
5. **Report the design delta.** For every round state `preserved`, `changed`, and
   `still open`. Do not make the user rediscover what moved.
6. **Apply the direction system-wide.** Test the selected language across the
   main screen, secondary tabs, dense and empty states, forms, navigation,
   responsive layouts, and provider/status accents. Distinct structures may
   share one visual system.
7. **Refine identity separately.** For names, marks, and logos, test silhouette,
   orientation, geometry, small-size legibility, restrained color, monochrome,
   and icon variants before adding decorative detail.
8. **Ratify exact references.** Preserve final tokens, type roles, component
   rules, assets, screenshots/mockups, and rejected/deferred variants in durable
   files. "Use the version from the chat" is not a handoff.

Use real content wherever possible; generic placeholder copy can make otherwise
good directions look falsely interchangeable. Spend distinctiveness on one or
two signature ideas and keep supporting components disciplined.

### Step 6 — Maintain explicit decision state

Tag every consequential choice:

| State | Meaning |
|---|---|
| `PROPOSED` | Available for discussion; not authorized downstream |
| `SELECTED` | Preferred direction; refinement may still change it |
| `RATIFIED` | Approved source of truth for specification and implementation |
| `DEFERRED` | Intentionally postponed with trigger for reconsideration |
| `REJECTED` | Considered and declined; retain the rationale |
| `REOPENED` | A ratified decision is under review because new evidence appeared |

For each ratified or rejected decision, record date, rationale, affected
artifacts, and any evidence or reference. Never silently upgrade enthusiasm or
an agent recommendation into approval.

### Step 7 — Test coherence and stop

Before handoff, challenge the product from several angles:

- Can the target user complete the primary journey?
- Is the first usable version valuable rather than infrastructural?
- Do scope and data requirements agree with the promised experience?
- Do visual decisions hold across real screens and states?
- Are extensibility seams named without prebuilding speculative systems?
- Can a fresh agent distinguish ratified, proposed, and deferred work?

Stop discovery when all architecture-shaping product decisions are ratified or
explicitly deferred, the main journey is coherent, and the visual reference is
specific enough to implement. Discovery does not require eliminating every
future idea.

### Step 8 — Produce the handoff

Create or update durable project artifacts containing:

- problem, audience, outcomes, constraints, and success signals;
- current workflow and build-vs-buy conclusion when relevant;
- product scope, non-goals, requirements, and core journeys;
- conceptual objects, information architecture, and screen/state inventory;
- experience principles and ratified visual/design-system contract;
- decision register and deferred/rejected decisions;
- asset and reference manifest with stable paths;
- open architecture questions; and
- acceptance criteria for the first usable increment.

Then route to `agentic-project-bootstrap` for the formal spec and phased plan, or
directly to `system-design`/`architecture` when the workflow is already stood up.
Implementation begins only after the contract is ratified.

---

## 4. Design artifact quality bar

A durable design handoff names exact choices, not adjectives alone:

- color tokens with roles and contrast intent;
- typography families, roles, weights, scale, and spacing behavior;
- layout density, grid, radii, borders, shadows, and responsive behavior;
- navigation and component anatomy;
- interactive, loading, empty, error, disabled, and focus states;
- brand/logo source assets and required variants;
- screen-specific exceptions and the invariant system beneath them; and
- approved reference images or mockups with stable locations.

If an artifact cannot tell a fresh implementer what must remain unchanged, it
is still inspiration, not specification.

---

## 5. Failure patterns

- **Premature architecture.** Choosing databases or frameworks before the user
  journey is stable turns implementation preference into product constraint.
- **Premature convergence.** Presenting one polished option hides tradeoffs and
  invites vague approval.
- **Endless option generation.** Exploration without narrowing avoids the hard
  work of choosing.
- **Uncontrolled visual drift.** Changing palette, type, layout, and content at
  once makes feedback uninterpretable.
- **Transcript as source of truth.** Fresh agents cannot reliably reconstruct
  dozens of incremental approvals.
- **Prototype becomes production by accident.** A discovery artifact proves a
  choice; it does not automatically satisfy implementation quality.
- **Extensibility theater.** Name seams and contracts now; do not build plugin,
  event, or orchestration infrastructure before a real integration needs it.
- **Generic design vocabulary.** "Modern," "clean," and "professional" are not
  decisions. Translate them into observable visual and interaction rules.

---

## 6. Discovery completion checklist

- [ ] Problem, audience, current workflow, and desired outcome are explicit.
- [ ] Existing-software fit was assessed when relevant.
- [ ] Scope, non-goals, first usable increment, and deferred ideas are separate.
- [ ] Main journey, objects, information architecture, and states are coherent.
- [ ] Material options and tradeoffs were surfaced before convergence.
- [ ] Visual direction was compared, refined in controlled rounds, and applied
      across representative screens.
- [ ] Every consequential decision has an explicit state.
- [ ] Ratified assets and design rules live at stable paths.
- [ ] Open architecture questions are identified without being pre-decided.
- [ ] A fresh agent can begin specification without reading the discovery chat.

---

## 7. Routing map

Route instead of duplicating specialist technique:

| Need | Route to |
|---|---|
| Distinctive aesthetic direction, typography, layout, UI critique, or production frontend work | `frontend-design` when available |
| Raster concepts, logo exploration, or image edits | `imagegen` when available |
| Interactive comparison panels, diagrams, wireframes, or small design labs | `visualize` when available |
| Current alternatives, pricing, capabilities, or recommendations | Web research with primary/current sources |
| Architecture, data model, APIs, services, and technology choices | `system-design` or `architecture` |
| Approval checkpoints and judgment-sensitive pauses | `agentic-collaboration-cadence` |
| Durable handoffs and decision-memory placement | `agentic-project-memory` |
| Formal spec, gates, phases, and day-one workflow | `agentic-project-bootstrap` |
| Phase sequencing after the specification exists | `agentic-phase-workflow` |
| Delegation, work packets, integration, and implementation acceptance | `agentic-implementation-orchestration` |

If an optional specialist skill is unavailable, continue with the smallest
useful text, wireframe, or reference artifact and disclose the limitation.

## When NOT to use this skill

- The product contract is already ratified and the question is architectural.
- The task is implementation against an approved specification.
- The user wants only a code review, debug session, or production hardening pass.
- The request is a small visual correction with no unresolved product or design
  choice; route directly to the relevant design/implementation skill.

## Provenance

Worked examples, evidence boundaries, and maintenance triggers: `examples.md`.
