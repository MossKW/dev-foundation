# Registry

**Status:** Draft

**Version:** 1.1

**Applies To:** dev-foundation

---

# Purpose

Registries provide shared platform state.

A registry stores platform capabilities and exposes registration and
lookup operations.

Registries do not coordinate execution.

---

# Responsibilities

A registry is responsible for:

- storing runtime state
- registering capabilities
- exposing lookup operations
- providing iteration over registered objects

Registries should remain simple.

---

# Design Principles

Registries own state.

Registries are passive.

Registries do not execute business logic.

Registries do not coordinate the runtime.

Managers provide behavior.

Runtime coordinates execution.

---

# Current Registries

The platform currently defines:

- CommandRegistry
- BlueprintRegistry

Future registries may include:

- PluginRegistry
- TemplateRegistry

---

# Ownership

Registries are owned by RuntimeContext.

```
Runtime
      │
      ▼
RuntimeContext
      │
      ▼
CommandRegistry

BlueprintRegistry
```

Registries should never own Runtime.

---

# Future Evolution

Additional registries may be introduced without modifying Runtime.

New registries should follow the same ownership and responsibility
rules.
