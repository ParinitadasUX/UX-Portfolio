# Associate Mobile Case Study — Design System Guidelines

A reference for the editorial design system used to build the **Associate Mobile** case study (`associate-mobile.html`). Styles live in `assets/css/case-study.css` and are scoped to `.case-study-v`.

**Status:** Draft for review  
**Last updated:** June 2025  
**Reference implementation:** `associate-mobile.html`

---

## 1. Design philosophy

The Associate Mobile case study follows an **editorial, typography-led** approach — closer to a long-form article or design essay than a marketing landing page.

| Principle | What it means in practice |
|-----------|---------------------------|
| **Typography does the heavy lifting** | Hierarchy comes from font size, weight, and spacing — not color blocks or heavy decoration. |
| **Restrained color** | Near-monochrome palette. Color is used sparingly (HMW callout, quote accents, table icons). |
| **Flat, bordered surfaces** | Cards use `1px` borders and no drop shadows (except fanned quote cards). `border-radius: 0` on editorial components. |
| **Readable measure** | Body copy is capped at `--cs-text-max` (42rem / ~672px). |
| **Vertical rhythm** | Spacing is token-driven (`--cs-section`, `--cs-stack`) — not ad-hoc Bootstrap margins inside phases. |
| **Full-bleed moments** | Hero images and HMW callouts break out of the content column intentionally. |

---

## 2. File structure

```
associate-mobile.html          Page markup
assets/css/case-study.css      Editorial system (scoped to .case-study-v)
assets/css/style.css           Base theme + Bootstrap (loaded first)
```

### Page wrapper

```html
<body class="case-study-page">
  <section class="content case-study-v">
    <div class="container">
      <!-- content -->
    </div>
  </section>
</body>
```

- `case-study-page` — disables magic cursor and preloader.
- `case-study-v` — activates all design tokens and component styles.
- `cs-phase` — each major narrative topic (Overview, Problem, Solution, etc.).

### Fonts (Google Fonts)

Loaded in `associate-mobile.html`:

```html
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Mono&family=Geist:wght@300;400;500&family=Source+Serif+4:ital@0;1&display=swap" rel="stylesheet">
```

| Token | Family | Weights | Primary usage |
|-------|--------|---------|---------------|
| `--cs-body` | **Geist** | 300, 400, 500, 600 | All headings, body, UI, cards, captions |
| `--cs-meta` | **DM Mono** | 400 | Meta labels, nav links, numbered list prefixes |
| `--cs-quote` | **Source Serif 4** | 400 (italic) | Editorial pull quotes (`.cs-quote`) |
| `--cs-display` | **Bebas Neue** | — | Reserved for display moments (not used on Associate Mobile) |

> Full typography specs — sizes, line heights, weights, and examples — are in **§4 Typography**.  
> Card borders, padding, margins, and interactions — **§5 Card system**.

---

## 3. Design tokens

Defined on `.case-study-v` in `case-study.css`.

### Color

| Token | Value | Usage |
|-------|-------|-------|
| `--cs-text` | `#111111` | Primary text |
| `--cs-muted` | `#6b7280` | Secondary text, captions, descriptions |
| `--cs-border` | `#e8e8e8` | Card borders, dividers, image frames |
| `--cs-bg` | `#ffffff` | Page background |
| `--cs-surface` | `#fafafa` | Subtle fill (stat cards, table headers) |
| Overline gray | `#9ca3af` | Section overlines (`.cs-overline`) |
| HMW callout | `rgba(33, 150, 243, 1)` | Full-bleed “How might we” band |
| Highlight | `#ebedf0` | Inline emphasis (`.cs-highlight`) |
| Quote accent | `#007bff` | Opening quote mark on fanned cards |

### Layout

| Token | Desktop value | Purpose |
|-------|---------------|---------|
| `--cs-page-max` | `68rem` (~1088px) | Max content column width |
| `--cs-text-max` | `42rem` (~672px) | Max line length for prose |
| `--cs-gutter` | `clamp(1.5rem, 5vw, 3rem)` | Horizontal page padding |

### Spacing rhythm

| Token | Desktop value | Purpose |
|-------|---------------|---------|
| `--cs-section` | `clamp(6rem, 10vw, 8.5rem)` | Gap **between** major topics (`cs-phase`) |
| `--cs-stack` | `clamp(1.5rem, 3.125vw, 2.5rem)` | Gap **within** a phase (flex `gap`) |
| `--cs-head-gap` | `clamp(1.5rem, 3.125vw, 2.5rem)` | Section head → content spacing |
| `--cs-subsection` | `clamp(2.5rem, 5vw, 3.5rem)` | Sub-section breaks (validation notes) |

**Mobile (≤767px):** `--cs-section` becomes `clamp(4.5rem, 8vw, 6rem)`; `--cs-stack` and `--cs-head-gap` lock to `1.5rem`.

> **Note:** Global `section { padding: 130px 0 }` from `style.css` is overridden for `section.cs-phase` inside case studies. Section spacing is controlled by `--cs-section` margin-top instead.

---

## 4. Typography

Typography is the primary design tool on Associate Mobile. Hierarchy is built through **size, weight, and letter-spacing** — not color or decoration.

### 4.1 Base settings

Applied to `.case-study-v`:

| Property | Value |
|----------|-------|
| Font family | Geist (`--cs-body`) |
| Base size | `1.0625rem` (17px at 16px root) |
| Base weight | `300` (Light) |
| Base line-height | `1.65` |
| Base color | `#111111` (`--cs-text`) |
| Max line length | `42rem` / ~672px (`--cs-text-max`) |

All `h1–h6` inside `.case-study-v` are reset to **Geist** — overriding the portfolio theme’s default heading fonts.

### 4.2 Weight scale

| Weight | Name | Where it’s used |
|--------|------|-----------------|
| **300** | Light | Body copy, lede, descriptions, captions, HMW callout, solution principle |
| **400** | Regular | Page title, overlines, meta values, quote body |
| **500** | Medium | Section titles, subheadings, stat labels, quote authors, nav |
| **600** | Semibold | Dual-item titles, impact metrics (`strong`), constraint card titles, carousel lead |
| **700** | Bold | HMW callout emphasis (`strong`), bottleneck stat numbers (via Bootstrap) |

**Rule of thumb:** body stays light (300); hierarchy steps up in weight before jumping in size.

### 4.3 Letter-spacing

| Pattern | Value | Applied to |
|---------|-------|------------|
| Tight display | `−0.02em` | `.cs-title`, `.cs-section-title`, `.cs-heading`, `.cs-impact-summary`, HMW callout |
| Wide label | `0.14em` | `.cs-overline`, `.cs-quote-heading` |
| Meta label | `0.1em` | `.cs-eyebrow`, `.cs-meta-label`, `.case-study-quote-heading` |
| Nav / terms | `0.06–0.08em` | Navbar links, portfolio terms |
| Normal | `0` | Body, dual items, most card text |

Uppercase labels always pair wide tracking with small size — never track large headlines.

### 4.4 Type scale — full reference

Sizes shown at default `16px` root. Fluid values use `clamp(min, preferred, max)`.

#### Display & page level

| Class | Family | Size | Line-height | Weight | Tracking | Color | Example |
|-------|--------|------|-------------|--------|----------|-------|---------|
| `.cs-title` | Geist | `clamp(2.5rem, 6vw, 4.5rem)` → 40–72px | `1.05` | 400 | −0.02em | `--cs-text` | Associate Mobile Redesign |
| `.cs-eyebrow` | DM Mono | `0.72rem` → 11.5px | — | — | 0.1em, uppercase | `--cs-muted` | Enterprise · Mobile · Toshiba ELERA |

#### Section level

| Class | Family | Size | Line-height | Weight | Tracking | Color | Example |
|-------|--------|------|-------------|--------|----------|-------|---------|
| `.cs-overline` | Geist | `0.75rem` → 12px | `1.4` | 400 | 0.14em, uppercase | `#9ca3af` | Overview, Problem, Solution |
| `.cs-section-title` | Geist | `1.625rem` → 26px | `1.25` | 500 | −0.02em | `--cs-text` | A critical tool during peak-hour checkout |
| `.cs-heading` | Geist | `clamp(1.75rem, 3.5vw, 2.65rem)` → 28–42px | `1.15` | 500 | −0.02em | `--cs-text` | Larger in-section headlines |
| `.cs-subheading` | Geist | `clamp(1.15rem, 2vw, 1.35rem)` → 18–22px | `1.35` | 500 | — | `--cs-text` | Sub-section titles |

#### Body & prose

| Class | Family | Size | Line-height | Weight | Tracking | Color | Example |
|-------|--------|------|-------------|--------|----------|-------|---------|
| `.cs-lede` | Geist | `1.0625rem` → 17px | `1.65` | 300 | — | `--cs-text` | Hero intro paragraph |
| `.cs-body` | Geist | `1.0625rem` → 17px | `1.65` | 300 | — | `--cs-text` | Section body copy |
| `.cs-solution-principle` | Geist | `1.125rem` → 18px | `1.55` | 300 | — | `--cs-text` | Solution intro paragraph |
| `.cs-validation-note` | Geist | `1rem` → 16px | `1.55` | 300 | — | `--cs-text` | Research synthesis note |

#### Meta & links

| Class | Family | Size | Line-height | Weight | Tracking | Color | Example |
|-------|--------|------|-------------|--------|----------|-------|---------|
| `.cs-meta-label` | DM Mono | `0.68rem` → 11px | — | — | 0.1em, uppercase | `--cs-muted` | My role, Tools |
| `.cs-meta-value` | Geist | `0.95rem` → 15px | `1.45` | 400 | — | `--cs-text` | UX Research & Design |
| `.cs-meta-link` | Geist | `0.95rem` → 15px | — | 400 | — | `--cs-text` | View product → |

#### Lists & micro-items

| Class | Family | Size | Line-height | Weight | Tracking | Color | Example |
|-------|--------|------|-------------|--------|----------|-------|---------|
| `.cs-dual-item-title` | Geist | `1.0625rem` → 17px | `1.35` | 600 | — | `--cs-text` | Peak-hour speed |
| `.cs-dual-item-desc` | Geist | `1.0625rem` → 17px | `1.55` | 300 | — | `--cs-muted` | Speed up checkout and reduce walk-aways… |
| `.cs-dual-item-desc strong` | Geist | inherit | inherit | 600 | — | `--cs-text` | +43%, −58% |
| `.cs-takeaways-list li` | Geist | inherit (17px) | `1.5` | 300 | — | `--cs-text` | Key takeaway bullets |
| `.cs-insights li::before` | DM Mono | `0.85rem` → 14px | — | — | — | `--cs-muted` | 1/, 2/, 3/ |

#### Stats & numbers

| Class | Family | Size | Line-height | Weight | Color | Example |
|-------|--------|------|-------------|--------|-------|---------|
| Bottleneck `h3` | Geist | `fs-3` / `fs-4` (Bootstrap) | — | Bold | `--cs-text` | 15–20%, $7.5–$20M |
| `.cs-research-stat strong` | Geist | `1.5rem` → 24px | `1.1` | 500 | `--cs-text` | 7, 43.3% |
| `.cs-research-stat span` | Geist | `0.88rem` → 14px | `1.4` | — | `--cs-muted` | User interviews and usability tests… |
| `.cs-stat strong` | Geist | `clamp(1.75rem, 3vw, 2.25rem)` | `1` | 500 | `--cs-text` | Stat card numbers |

#### Cards

| Class | Family | Size | Line-height | Weight | Color | Example |
|-------|--------|------|-------------|--------|-------|---------|
| `.cs-constraints-row h6` | Geist | `17px` | — | 600 | `--cs-text` | No new hardware |
| `.cs-constraints-row small` | Geist | `17px` | — | — | `--cs-muted` | Stores cannot afford… |
| `.heuristics-card-body h6` | Geist | `17px` | — | — | `--cs-text` | Visibility Issues |
| `.heuristics-badge` | Geist | `14px` | — | Bold | `#ffffff` on `#333` | 01, 02, 03, 04 |
| Bottleneck `h6.small` | Geist | Bootstrap `small` | — | Semibold, uppercase | `--cs-text` | Revenue at risk |

#### Quotes

| Class | Family | Size | Line-height | Weight | Style | Color | Example |
|-------|--------|------|-------------|--------|-------|-------|---------|
| `.cs-quote-heading` | Geist | `0.75rem` | — | 400 | uppercase | `#9ca3af` | What Associates Told Us |
| `.quote-text` | Geist | `0.9rem` → 14px | `1.5` | 400 | italic | `#2c3e50` | Quote body (fanned cards) |
| `.quote-text::before` | Serif | `2.5rem` → 40px | — | Bold | — | `#007bff` | Decorative opening “ |
| `.quote-author` | Geist | `0.85rem` → 14px | — | 500 | normal | `#6c757d` | Associate name |
| `blockquote.cs-quote` | Source Serif 4 | `clamp(1.1rem, 2vw, 1.35rem)` | `1.5` | 400 | italic | `--cs-text` | Flat pull quotes |

#### Captions & secondary

| Class | Family | Size | Line-height | Weight | Color | Example |
|-------|--------|------|-------------|--------|-------|---------|
| `.cs-figure-caption` | Geist | `0.88rem` → 14px | `1.45` | 300 | `--cs-muted` | Peak-hour floor checkout… |
| `.cs-figure-credit` | Geist | `0.78rem` → 12.5px | — | — | `--cs-muted` (85% opacity) | Image: Toshiba Global Commerce Solutions |
| `.cs-carousel-caption` | Geist | `0.95rem` → 15px | `1.45` | 300 | `--cs-muted` | Peak-hour flow. End-to-end checkout… |
| `.cs-carousel-caption strong` | Geist | inherit | inherit | 600 | `--cs-text` | Peak-hour flow |

#### Callouts & emphasis

| Class | Family | Size | Line-height | Weight | Color | Example |
|-------|--------|------|-------------|--------|-------|---------|
| `.cs-hmw .cs-callout p` | Geist | `clamp(1.875rem, 4vw, 2.5rem)` → 30–40px | `1.25` | 300 | `#111111` on blue band | How might we speed up checkout… |
| `.cs-hmw strong` | Geist | inherit | inherit | 700 | inherit | speed up checkout |
| `.cs-highlight` | Geist | inherit | inherit | 500 | `--cs-text` on `#ebedf0` | Inline highlighted phrase |

#### Navigation (case study pages)

| Element | Family | Size | Weight | Tracking |
|---------|--------|------|--------|----------|
| `.navbar-brand` | Geist | inherit | 500 | −0.02em |
| `.navbar-nav .nav-link` | DM Mono | `0.75rem` | 400 | 0.06em, uppercase |

#### Appendix table

| Element | Family | Size | Weight |
|---------|--------|------|--------|
| `thead th` | Geist | `0.875rem` → 14px | 600 |
| `tbody td` | Geist | inherit (17px) | inherit |
| Row `strong` | Geist | inherit | Bold |

### 4.5 Visual hierarchy (Associate Mobile)

```
cs-eyebrow          DM Mono · 11.5px · muted · uppercase · tracked
    ↓
cs-title            Geist · 40–72px · regular · tight
    ↓
cs-lede             Geist · 17px · light · 1.65 leading
    ↓
cs-meta-label       DM Mono · 11px · muted · uppercase
cs-meta-value       Geist · 15px · regular
    ↓
cs-overline         Geist · 12px · gray · uppercase · tracked
    ↓
cs-section-title    Geist · 26px · medium · tight
    ↓
cs-body             Geist · 17px · light · muted prose
    ↓
cs-dual-item-title  Geist · 17px · semibold
cs-dual-item-desc   Geist · 17px · light · muted
```

### 4.6 Emphasis patterns

| Need | Markup | Result |
|------|--------|--------|
| Metric or keyword in body | `<strong>+43%</strong>` | Weight 600, `--cs-text` color |
| Inline highlight | `<span class="cs-highlight">phrase</span>` | `#ebedf0` background, weight 500 |
| Muted supporting text | `.cs-dual-item-desc` or `<small class="text-muted">` | `--cs-muted` color |
| Link in body | `<a href="…">` | Default link styling from theme |
| Carousel lead phrase | `<strong>` inside `.cs-carousel-caption` | Semibold, flips to `--cs-text` |

Avoid bolding entire sentences. Reserve `600–700` weight for numbers, labels, and short phrases.

### 4.7 Typography by page section

| Section | Primary type classes |
|---------|---------------------|
| Hero | `.cs-eyebrow`, `.cs-title`, `.cs-lede` |
| Meta | `.cs-meta-label`, `.cs-meta-value`, `.cs-meta-link` |
| Goals + Impact | `.cs-section-title`, `.cs-overline`, `.cs-dual-item-title`, `.cs-dual-item-desc` |
| Overview | `.cs-overline`, `.cs-section-title`, `.cs-dual-item-*`, `.cs-figure-caption` |
| Problem | `.cs-section-title`, `.cs-body`, bottleneck `h3` / `h6` / `small` |
| User research | `.cs-body`, `.cs-research-stat`, `.cs-validation-note`, `.cs-quote-heading`, `.quote-text` |
| Insights | `.cs-overline`, `.cs-section-title`, `.heuristics-card-body h6`, `.cs-carousel-caption` |
| Define (HMW) | `.cs-overline`, `.cs-section-title`, `.cs-hmw .cs-callout p` |
| Constraints | `.cs-overline`, `.cs-section-title`, `.cs-constraint-card h6/small` |
| Solution | `.cs-overline`, `.cs-section-title`, `.cs-solution-principle`, `.cs-carousel-caption` |
| Appendix | `.cs-body`, table `th`/`td` with Bootstrap Icons |
| Takeaways | `.cs-takeaways-list`, `.cs-body` |

### 4.8 Responsive typography

Most type sizes are **fixed rem/px** — they don’t shrink on mobile. Exceptions:

| Class | Fluid behavior |
|-------|----------------|
| `.cs-title` | Scales 40px → 72px via `clamp` |
| `.cs-heading` | Scales 28px → 42px |
| `.cs-subheading` | Scales 18px → 22px |
| `.cs-hmw .cs-callout p` | Scales 30px → 40px |
| `.cs-stat strong` | Scales 28px → 36px |

Mobile dual-column items keep the same `1.0625rem` size — only layout stacks.

### 4.9 Typography do / don't

**Do**
- Use `.cs-overline` + `.cs-section-title` together for every phase
- Keep body at weight 300 for an editorial feel
- Use DM Mono only for meta/label contexts — not body paragraphs
- Cap prose width with `.cs-body` or `.cs-lede` (inherits `--cs-text-max`)

**Don't**
- Mix Bebas Neue into Associate Mobile content (breaks tone)
- Use `text-primary` or colored headings on new components
- Set custom `font-size` inline — add a class to `case-study.css` instead
- Use ALL CAPS without increased letter-spacing (overlines already handle this)

---

## 5. Card system

Associate Mobile uses **two card families**. Most content cards are flat and editorial; quote and heuristics cards are rounded and interactive.

### 5.1 Card families

| Family | Visual | Used for | Border radius | Shadow | Interaction |
|--------|--------|----------|---------------|--------|-------------|
| **Editorial flat** | `1px` border, no fill or light fill | Constraints, problem stats, research stats | `0` | None | None |
| **Interactive rounded** | `12px` radius, shadow, fill | Fanned quotes, heuristics findings | `12px` | Yes | Hover, click, carousel sync |

**Shared border token:** `--cs-border: #e8e8e8` — used on all editorial flat cards. Quote cards use a slightly cooler `#e9ecef`.

### 5.2 Master comparison

| Card type | Class | Border | Background | Padding | Gap between cards | Cursor |
|-----------|-------|--------|------------|---------|-------------------|--------|
| Problem / bottleneck | `.cs-bottleneck-row .cs-constraint-card` | `1px solid #e8e8e8` | Transparent | `1rem` / `1.5rem` (`p-3` / `p-md-4`) | `g-3` / `g-md-4` (1–1.5rem) | Default |
| Constraints | `.cs-constraints-row .cs-constraint-card` | `1px solid #e8e8e8` | Transparent | `1.25rem` | `g-3` (1rem) | Default |
| Research stats | `.cs-research-stat` | `1px solid #e8e8e8` | Transparent | `1.25rem` | `1rem` grid gap | Default |
| Fanned quotes | `.quote-horizontal-card` | `1px solid #e9ecef` | `#ffffff` | `1.5rem` | Overlapping (absolute) | Default |
| Heuristics | `.heuristics-card` | `2px solid transparent` → active `2px #2196f3` | `#f8f9fa` → active `#e3f2fd` | `1rem` (`p-3`) | `g-4` (1.5rem) | `pointer` |

---

### 5.3 Editorial flat cards

Default rules applied via `.cs-bottleneck-row` and `.cs-constraints-row`:

```css
border: 1px solid var(--cs-border);   /* #e8e8e8 */
border-radius: 0;
box-shadow: none;
background: unset;                    /* transparent */
text-align: left;
```

#### Problem / bottleneck cards

**Where:** Problem phase — revenue at risk, retailer scale, lost sales.

| Property | Value |
|----------|-------|
| Wrapper | `.impact-problem-matrix.cs-bottleneck-row` |
| Row gap | `g-3` (16px) mobile · `g-md-4` (24px) desktop |
| Card padding | `p-3` = 1rem · `p-md-4` = 1.5rem at ≥768px |
| Card height | `h-100` — equal height per row |
| Layout | `flex-column justify-content-center` |
| Border | `1px solid #e8e8e8` (via CSS override) |
| Border radius | `0` |
| Shadow | None |
| Background | Transparent |
| Margins | None on card; phase spacing from `--cs-stack` |
| Interaction | None |

**Internal spacing:**
- `h3` stat number: `mb-2` (0.5rem) · `mb-md-3` (1rem) at desktop
- `h6` label: `mb-1` (0.25rem)
- `small` description: no extra margin

#### Constraints cards

**Where:** Constraints phase — No new hardware, Legacy system, Time pressure.

| Property | Value |
|----------|-------|
| Wrapper | `.row.g-3.cs-constraints-row` |
| Column layout | `col-md-4` — 3-up on desktop, stacked on mobile |
| Row/column gap | `g-3` = 1rem |
| Card padding | `1.25rem` (20px) all sides |
| Border | `1px solid #e8e8e8` |
| Border radius | `0` |
| Shadow | None |
| Background | Transparent |
| Text align | Left |
| Section head offset | Extra tight: `padding-bottom: calc(var(--cs-head-gap) - var(--cs-stack) - 1rem)` |
| Interaction | None |

**Internal spacing:**
- `h6` title → `small` description: `margin-bottom: 0.35rem` on title

#### Research stat cards

**Where:** User research phase — interview count, survey type, abandonment %.

| Property | Value |
|----------|-------|
| Wrapper | `.cs-research-stats` (CSS grid) |
| Grid | `repeat(auto-fit, minmax(11rem, 1fr))` |
| Gap | `1rem` |
| Card padding | `1.25rem` |
| Border | `1px solid #e8e8e8` |
| Border radius | `0` |
| Shadow | None |
| Background | Transparent |
| Interaction | None |

**Internal spacing:**
- `strong` value → `span` label: `margin-bottom: 0.35rem` on strong

---

### 5.4 Interactive rounded cards

#### Fanned quote cards

**Where:** User research — “What Associates Told Us”.

| Property | Default | Hover |
|----------|---------|-------|
| Size | `250×260px` (desktop) | Same |
| Border | `1px solid #e9ecef` | Same |
| Border radius | `12px` | Same |
| Background | `#ffffff` | `#ffffff` |
| Padding | `1.5rem` | Same |
| Shadow | `0 8px 25px rgba(0,0,0,0.1), 0 3px 10px rgba(0,0,0,0.05)` | `0 20px 40px rgba(0,0,0,0.2), 0 8px 20px rgba(0,0,0,0.1)` |
| Transform | Rotated ±15° / centered | `translateY(-15px) rotate(0deg) scale(1.05)` |
| Z-index | 1–4 (stacked) | `10` |
| Transition | `all 0.3s ease` | — |
| Cursor | Default | Default |

**Container (`.quote-horizontal-container`):**
- Padding: `2rem 0`
- Height: `300px` (desktop)
- Layout: Flex, cards absolutely positioned

**Mobile (≤767px):**
- Container: grid, 1 column, `gap: 1rem`, `height: auto`, `padding: 0`
- Cards: full width, `min-height: 180px`, no rotation, relative positioning

**Interaction:** CSS `:hover` only — no click action. Card straightens, lifts, and scales on hover.

#### Heuristics finding cards

**Where:** Insights phase — usability findings 01–04, synced to carousel.

| Property | Default | Hover (inactive) | Active (carousel-linked) | Click |
|----------|---------|------------------|--------------------------|-------|
| Border | `2px solid transparent` | — | `2px solid #2196f3` | — |
| Border radius | `12px` | Same | Same | — |
| Background | `#f8f9fa` | Same | `#e3f2fd` | — |
| Padding | `1rem` (`p-3`) | Same | Same | — |
| Shadow | None | `0 6px 20px rgba(0,0,0,0.15)` | `0 4px 12px rgba(33,150,243,0.3)` | — |
| Transform | `scale(1)` | `scale(1.05)` | `scale(1.02)` | `scale(0.95)` → `scale(1.02)` at 150ms |
| Cursor | `pointer` | `pointer` | `pointer` | `pointer` |
| Transition | `all 0.4s cubic-bezier(0.25, 0.8, 0.25, 1)` | — | — | — |

**Badge (`.heuristics-badge`):**

| Property | Default | Active |
|----------|---------|--------|
| Size | `40×40px` | Same |
| Shape | Circle (`border-radius: 50%`) | Same |
| Background | `#333` | `rgba(33, 150, 243, 1)` |
| Text | White, bold, `14px` | Same |
| Position | `top-0 start-0 translate-middle` (overlaps corner) | Same |
| Transform | `scale(1)` | `scale(1.1)` |
| Transition | `all 0.3s ease` | — |

**Card body (`.heuristics-card-body`):**
- `margin-top: 20px` (clears badge overlap)
- Title `h6`: `mb-2` (0.5rem), `17px`

**Row layout:** `row g-4 mb-4` — `1.5rem` gap between cards, 4 columns on `col-md-3`.

**Carousel sync logic** (inline JS in `associate-mobile.html`):

| Carousel slide | Cards highlighted |
|----------------|-------------------|
| Slide 0 | Cards 01 & 02 |
| Slide 1 | Card 03 |
| Slide 2 | Card 04 |

**Click behavior:** Card click navigates carousel to linked slide. Cards 0–1 → slide 0; card 2 → slide 1; card 3 → slide 2.

---

### 5.5 Surfaces that look like cards (not bordered boxes)

| Surface | Border | Background | Padding | Interaction |
|---------|--------|------------|---------|-------------|
| HMW callout (`.cs-hmw .cs-callout`) | None | `rgba(33, 150, 243, 1)` blue | `clamp(1.75rem, 4vw, 2.5rem)` vertical · horizontal aligns to page gutter | None |
| Generic callout (`.p-4.bg-light.rounded-3.text-start`) | `1px solid #e8e8e8` | `#fafafa` | `1.75rem` | None |
| Appendix table (`.modern-table`) | `1px solid #e8e8e8` outer | Header `#fafafa` | Cell `1rem 1.25rem` | None |

---

### 5.6 Spacing around card groups

| Group | Margin above | Margin below | Notes |
|-------|--------------|--------------|-------|
| Bottleneck row | From `--cs-stack` in phase | From `--cs-stack` | Follows `.cs-body` paragraph |
| Constraints row | Tighter section head padding | From `--cs-stack` | Head gap reduced by `1rem` |
| Research stats | From `--cs-stack` | Chart grid `mt-2` below | — |
| Quote container | `clamp(1.25rem, 2.5vw, 1.75rem)` on `.cs-quotes-classic` | Validation note uses `--cs-subsection` | — |
| Heuristics row | From `--cs-stack` | Carousel follows in same phase | `mb-4` normalized to 0 in phase |

Bootstrap `mt-*` / `mb-*` inside `.cs-phase` are zeroed out — **card group spacing comes from the phase flex `gap` (`--cs-stack`)**, not card margins.

---

### 5.7 Card design rules

**Do**
- Use `1px solid var(--cs-border)` for new editorial/stat cards
- Keep editorial cards square (`border-radius: 0`) and shadowless
- Use `g-3` or `g-4` row gaps for card grids
- Left-align text in editorial cards
- Reserve rounded corners + shadow for interactive or quote content only

**Don't**
- Mix `12px` radius on editorial constraint/stat cards
- Add icons to constraints cards without a strong scanability reason
- Use Bootstrap `shadow-sm`, `bg-light`, or `text-primary` on new cards — existing markup is overridden but new cards should use system classes
- Rely on card `margin-bottom` for vertical rhythm — use `--cs-stack` on the parent phase

---

### 5.8 Card interaction summary

| Card | Hover | Click | Keyboard | Linked content |
|------|-------|-------|----------|----------------|
| Bottleneck | — | — | — | — |
| Constraints | — | — | — | — |
| Research stats | — | — | — | — |
| Fanned quotes | Lift, straighten, scale 1.05 | — | — | — |
| Heuristics | Scale 1.05 + shadow (if inactive) | Navigate carousel + press animation | Not implemented | Heuristics carousel + caption |

---

## 6. Page anatomy

Associate Mobile follows this narrative structure. Each block is a `<section class="cs-phase">` unless noted.

```
┌─────────────────────────────────────────┐
│  Hero (.cs-hero)                        │
│  Eyebrow + Title + Lede                 │
├─────────────────────────────────────────┤
│  Meta grid (.cs-meta-grid)              │
│  View product link (.cs-meta-link)      │
├─────────────────────────────────────────┤
│  Full-bleed hero image (.cs-bleed)      │
├─────────────────────────────────────────┤
│  PHASE: Goals + Impact (.cs-dual-column)│
│  PHASE: Overview (.cs-overview-layout)  │
│  PHASE: Problem (.cs-bottleneck-row)    │
│  PHASE: User research                   │
│  PHASE: Insights (.cs-heuristics-classic)│
│  PHASE: Define (.cs-hmw)                │
│  PHASE: Constraints (.cs-constraints-row)│
│  PHASE: Solution (carousel)             │
│  PHASE: Appendix (.cs-appendix)         │
│  PHASE: Key takeaways                   │
└─────────────────────────────────────────┘
```

### Standard phase pattern

```html
<section class="cs-phase">
  <div class="cs-section-head">
    <p class="cs-overline">Topic label</p>
    <h2 class="cs-section-title">Section headline</h2>
  </div>
  <!-- phase content -->
</section>
```

- `.cs-section-head` removes bottom margin from the title; spacing to content is handled by `--cs-stack` on the phase flex container.
- Avoid Bootstrap `mt-*` / `mb-*` inside phases — they are normalized to `0` by the system.

---

## 7. Components

### 6.1 Hero

```html
<header class="cs-hero">
  <p class="cs-eyebrow">Enterprise · Mobile · Toshiba ELERA</p>
  <h1 class="cs-title">Associate Mobile Redesign</h1>
  <p class="cs-lede">…</p>
</header>
```

### 6.2 Meta grid

Project metadata in a bordered grid. Labels in DM Mono uppercase; values in Geist.

```html
<div class="cs-meta-grid">
  <div>
    <div class="cs-meta-label">My role</div>
    <div class="cs-meta-value">UX Research &amp; Design</div>
  </div>
  <!-- repeat -->
</div>
<a class="cs-meta-link" href="…">View product <i class="bi bi-arrow-right-short"></i></a>
```

- Top/bottom border: `1px solid var(--cs-border)`
- Grid: `repeat(auto-fit, minmax(9rem, 1fr))`

### 6.3 Full-bleed media

```html
<figure class="cs-bleed portfolio-content items">
  <img src="…" alt="…">
</figure>
```

- Breaks to `100vw`, centered with negative margins
- Top margin: `clamp(2.5rem, 5vw, 4rem)`

### 6.4 Goals + Impact dual column

Two columns of stacked micro-items. On mobile, columns stack with a top border separator.

```html
<div class="cs-dual-column row g-4 g-lg-5">
  <div class="col-12 col-md-6">
    <p class="cs-overline">Goals</p>
    <div class="cs-dual-items">
      <div class="cs-dual-item">
        <h3 class="cs-dual-item-title">Title</h3>
        <p class="cs-dual-item-desc">Description</p>
      </div>
    </div>
  </div>
</div>
```

- Item gap: `1.75rem`
- Impact metrics use `<strong>` inside `.cs-dual-item-desc` for emphasis

### 6.5 Overview layout

Three micro-items in a row (desktop) + full-width figure below.

```html
<div class="cs-overview-layout">
  <div class="cs-dual-items cs-overview-items">…</div>
  <figure class="cs-overview-figure">
    <img src="…" alt="…">
    <figcaption class="cs-figure-caption">
      Caption text. <span class="cs-figure-credit">Image: Source</span>
    </figcaption>
  </figure>
</div>
```

- Overview items: 3-column grid at `≥768px`, gap `1.75rem 2rem`
- Images: `1px` border, no border-radius

### 6.6 Problem / bottleneck stat cards

Large numbers as visual anchors. Editorial flat style (no shadow, no radius). **Full specs: §5.3**

```html
<div class="impact-problem-matrix row g-3 g-md-4 cs-bottleneck-row">
  <div class="col-6 col-lg-3">
    <div class="p-3 p-md-4 h-100 cs-constraint-card">
      <h3 class="mb-2 mb-md-3 fw-bold fs-3">15–20%</h3>
      <h6 class="mb-1 small fw-semibold text-uppercase">Revenue at risk</h6>
      <small class="text-muted">Description</small>
    </div>
  </div>
</div>
```

- `.cs-bottleneck-row` forces left-aligned, border-only cards
- Primary Bootstrap color on numbers is overridden to `--cs-text`
- **Border:** `1px #e8e8e8` · **Padding:** `1rem` / `1.5rem` · **Gap:** `g-3` / `g-md-4` · **Interaction:** none

### 6.7 Research stats

Compact bordered stat blocks in an auto-fit grid. **Full specs: §5.3**

```html
<div class="cs-research-stats">
  <div class="cs-research-stat">
    <strong>7</strong>
    <span>Label text</span>
  </div>
</div>
```

- Strong: `1.5rem`, weight 500
- Span: `0.88rem`, muted
- **Border:** `1px #e8e8e8` · **Padding:** `1.25rem` · **Grid gap:** `1rem` · **Interaction:** none

### 6.8 Fanned quote cards (Associate Mobile signature)

Used in User Research for associate quotes. Interactive hover lifts and straightens cards. **Full specs: §5.4**

```html
<div class="cs-quotes-classic">
  <h5 class="cs-quote-heading mb-4">What Associates Told Us</h5>
  <div class="quote-horizontal-container">
    <div class="quote-horizontal-card">…</div>
  </div>
</div>
```

| Property | Value |
|----------|-------|
| Card size | 250×260px (desktop) |
| Border | `1px solid #e9ecef`, radius `12px` |
| Shadow | Layered soft shadow |
| Layout | Absolute, rotated ±15° / centered |
| Quote text | `0.9rem`, italic, clamped to 4 lines |
| Accent | Blue opening quote mark (`#007bff`) |
| Mobile | Stacks vertically, no rotation |

### 6.9 Heuristics finding cards

Numbered insight cards linked to a carousel. **Full specs: §5.4**

```html
<section class="cs-phase cs-heuristics-classic">
  <div class="heuristics-card">
    <div class="heuristics-badge">01</div>
    <div class="heuristics-card-body">
      <h6 class="mb-2">Visibility Issues</h6>
      <small class="text-muted">Critical notifications hidden</small>
    </div>
  </div>
</section>
```

| Property | Value |
|----------|-------|
| Background | `#f8f9fa` |
| Border radius | `12px` (exception to flat editorial rule) |
| Badge | 40px circle, `#333` background, white text |
| Card title | `17px` |
| Interaction | Click navigates carousel; hover scale 1.05; active state blue border `#2196f3` |

### 6.10 HMW callout (full-bleed)

```html
<div class="cs-hmw">
  <div class="cs-callout">
    <p>How might we <strong>speed up checkout</strong>…</p>
  </div>
</div>
```

- Full viewport width, blue background
- Text: `clamp(1.875rem, 4vw, 2.5rem)`, weight 300
- Strong tags: weight 700, no highlight background

### 6.11 Constraints cards

Minimal bordered text cards. **No icons** by design. **Full specs: §5.3**

```html
<div class="row g-3 cs-constraints-row">
  <div class="col-md-4">
    <div class="cs-constraint-card">
      <h6>No new hardware</h6>
      <small>Stores cannot afford another fixed-lane POS.</small>
    </div>
  </div>
</div>
```

| Property | Value |
|----------|-------|
| Border | `1px solid var(--cs-border)` |
| Padding | `1.25rem` |
| Title (`h6`) | `17px`, weight 600 |
| Description (`small`) | `17px`, muted |
| Background | None (transparent) |

### 6.12 Solution carousel

```html
<div id="solutionCarousel" class="carousel slide cs-solution-carousel">
  <!-- Bootstrap carousel -->
</div>
<p class="cs-carousel-caption">
  <strong>Peak-hour flow</strong>. Description text.
</p>
```

- Media max-height: `500px`, `object-fit: cover`
- Controls: 50px circular buttons, `rgba(0,0,0,0.5)` background
- Caption: centered, muted; bold lead phrase in `--cs-text`

### 6.13 Appendix comparison table

Icons used here (Bootstrap Icons) — the one place icons appear prominently.

```html
<section class="cs-phase cs-appendix">
  <table class="table modern-table">…</table>
</section>
```

- Flat table: no outer radius, `1px` border
- Header: `--cs-surface` background
- Row dividers: `1px solid var(--cs-border)`

### 6.14 Key takeaways

```html
<ul class="cs-takeaways-list">
  <li>Takeaway with <strong>metrics</strong>.</li>
</ul>
<p class="cs-body">Closing reflection.</p>
```

- Simple disc list, max-width `--cs-text-max`
- Item spacing: `0.75rem`

### 6.15 Inline highlight

```html
<span class="cs-highlight">highlighted phrase</span>
```

- Background `#ebedf0`, padding `0.15rem 0.4rem`, radius `3px`
- Prefer this over inline `style` attributes in new content

### 6.16 Validation note

Divider + centered reflection between research sections.

```html
<p class="cs-validation-note">…</p>
```

- Top border, padding-top from `--cs-stack`
- Margin-top: `--cs-subsection`

---

## 8. Spacing rules (do / don't)

### Do

- Wrap each topic in `<section class="cs-phase">`
- Use `.cs-section-head` + `.cs-overline` + `.cs-section-title` for topic headers
- Let `--cs-section` control distance between topics
- Use `.cs-body` for paragraph copy
- Use `.cs-highlight` or `<strong>` for emphasis

### Don't

- Add Bootstrap `mt-5` / `mb-4` inside phases (normalized to 0)
- Use `border-radius` or `box-shadow` on new editorial cards
- Use colorful Bootstrap utility classes (`text-primary`, `bg-light`) on new components — existing ones are overridden but new markup should use system classes
- Add icons to constraint cards unless there's a clear scanability need
- Use em dashes in body copy if plain punctuation reads cleaner

---

## 9. Responsive behavior

| Breakpoint | Key changes |
|------------|-------------|
| `≤767px` | Tighter gutters; dual columns stack with border separator; quote cards stack flat; stat row → single column; meta grid → 2 columns |
| `≥768px` | Overview items → 3-column grid; dual column side-by-side |

---

## 10. Associate Mobile vs. shared system

`case-study.css` is shared with **Security Suite** and future case studies. Associate Mobile–specific patterns:

| Pattern | Class modifier | Notes |
|---------|----------------|-------|
| Fanned quotes | `.cs-quotes-classic` | Associate Mobile only |
| Heuristics cards | `.cs-heuristics-classic` | Associate Mobile only |
| Flat pull quotes | `.cs-quotes-grid` | Security Suite pattern |
| HMW callout | `.cs-hmw` | Used on Associate Mobile |
| Constraints row | `.cs-constraints-row` | Associate Mobile only |
| Results cards | `.results-card` | Security Suite |

When adding a new case study, reuse tokens and phase structure; only add page-specific modifiers if the narrative needs a unique pattern.

---

## 11. Quick reference — CSS variables

```css
.case-study-v {
  --cs-body: "Geist", system-ui, -apple-system, sans-serif;
  --cs-meta: "DM Mono", ui-monospace, monospace;
  --cs-quote: "Source Serif 4", Georgia, serif;

  --cs-text: #111111;
  --cs-muted: #6b7280;
  --cs-border: #e8e8e8;
  --cs-bg: #ffffff;
  --cs-surface: #fafafa;

  --cs-section: clamp(6rem, 10vw, 8.5rem);
  --cs-stack: clamp(1.5rem, 3.125vw, 2.5rem);
  --cs-head-gap: clamp(1.5rem, 3.125vw, 2.5rem);
  --cs-subsection: clamp(2.5rem, 5vw, 3.5rem);
  --cs-gutter: clamp(1.5rem, 5vw, 3rem);
  --cs-text-max: 42rem;
  --cs-page-max: 68rem;
}
```

---

## 12. Open questions for review

Use this section to capture decisions as you review:

- [ ] Is `--cs-section` spacing (96–136px desktop) the right rhythm between topics?
- [ ] Should heuristics cards keep `12px` radius while editorial cards stay square?
- [ ] Unify quote card border `#e9ecef` with system token `#e8e8e8`?
- [ ] Move heuristics interaction styles from inline JS to CSS classes?
- [ ] Should constraint card title/description stay equal at `17px`, or should titles be larger?
- [ ] Should fanned quote cards be simplified to flat editorial quotes for consistency?
- [ ] Remove em dash in Constraints card copy (“ELERA—no” → comma or rewrite)?
- [ ] Add `.gitignore` entries for `.bak` and large `.mov` assets?

---

*Generated from `assets/css/case-study.css` and `associate-mobile.html`.*
