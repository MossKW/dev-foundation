# Engineering Principles

> Build once. Reuse forever.

These principles define how software projects are designed, developed, tested, and maintained. They are intended to be stable over time and apply to every project built on Dev Foundation.

---

## 1. Build Once, Reuse Forever

Every reusable solution should be designed to outlive a single project.

---

## 2. Standards Before Tools

Choose engineering standards first.
Tools are selected to support those standards, not define them.

---

## 3. Convention Over Configuration

Projects should follow the same structure whenever possible.

Consistency is more valuable than customization.

---

## 4. Automation by Default

Any task performed repeatedly should eventually become a command or script.

---

## 5. Local == CI == Release

A project that passes locally should pass in CI.

A project that passes CI should always be releasable.

---

## 6. Documentation Is Part of the Product

Documentation is not optional.

README, architecture documents, guides, and ADRs are part of the product itself.

---

## 7. Every Decision Has a Reason

Important engineering decisions must be documented.

Future developers should understand not only *what* was chosen, but *why*.

---

## 8. Optimize Developer Experience

Development tools should reduce cognitive load.

Good tooling saves more time than clever code.

---

## 9. Small, Incremental Changes

Small commits.

Small pull requests.

Continuous improvement.

---

## 10. Design for the Next Project

Design systems that benefit future projects, not only the current one.

---

## 11. Foundation Before Features

Whenever implementing a new feature, first ask:

"Does this belong in the project, or in the foundation?"

Reusable functionality belongs in the foundation.

Project-specific functionality belongs in the project.
