# AI Memory

## Things I Learned
- How APIs work
- Git basics
- Debugging Python errors

## Common Mistakes
- Forgetting to activate virtual environments
- Missing imports

## Preferred Tools
- VS Code
- Python
- GitHub

## Things That Help Me Learn
- Step-by-step explanations
- Small experiments

## Session History
- Date: 2026-03-07
- Task completed: Built and refined `drills/complete_or_fix/cafe-site.html` with semantic sections, menu content, about details, contact info, and footer.
- What was learned: Internal anchor navigation (`#id` links), clean section structure, and incremental improvement through review cycles.
- Follow-up focus: Link an external stylesheet and add basic CSS layout/typography rules.

- Date: 2026-03-07
- Task completed: Linked `cafe-site.css` to HTML and added foundational styles (reset, list bullet removal, section spacing).
- What was learned: How external stylesheets connect to HTML and how base CSS rules improve layout readability.
- Follow-up focus: Style navigation layout (horizontal links with spacing) and add simple header/footer styling.

- Date: 2026-03-07
- Task completed: Applied hero/card styling concepts including gradient overlay, box shadow, shorthand padding, and container positioning.
- What was learned: Complex CSS becomes manageable when tested one property at a time instead of memorizing full blocks.
- Follow-up focus: Rebuild the same layout from scratch in a short practice pass without copying.

- Date: 2026-03-08
- Task completed: Added mobile-nav toggle markup (`#menu-toggle`) and accessibility state attributes (`aria-controls`, `aria-expanded`) to the cafe site nav.
- What was learned: UI state in JavaScript should be mirrored with semantic accessibility attributes, not only visual classes.
- Follow-up focus: Add CSS hidden/visible behavior for the nav list and then wire JS click toggling.

- Date: 2026-03-08
- Task completed: Implemented working JS nav toggle with `classList.toggle("open")` and synchronized `aria-expanded` state.
- What was learned: The return value of `classList.toggle()` can drive accessibility attributes directly and avoid duplicate state bugs.
- Follow-up focus: Add responsive breakpoint behavior so nav stays visible on desktop and toggles on mobile only.

- Date: 2026-03-29
- Task completed: Finished pandas practice drill with totals, groupby summaries, sorting, and highest-revenue item.
- What was learned: Grouping by category and summarizing with sum() plus idxmax() to find top values.
- Follow-up focus: Practice sort_values() on full DataFrames vs grouped Series to understand output shapes.
