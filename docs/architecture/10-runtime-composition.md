# Runtime Composition

**Status:** Draft

**Version:** 1.1

**Applies To:** dev-foundation

---

# Purpose

This document defines how the runtime is composed.

Unlike previous architecture documents, this specification describes
the runtime object graph and the ownership relationships between
runtime components.

The runtime composition serves as the implementation blueprint for the
platform core.

---

# Design Goals

The runtime should be:

- Simple
- Predictable
- Extensible
- Loosely Coupled
- Testable

The runtime coordinates services instead of implementing
domain-specific logic.

---

# Runtime Responsibilities

The Runtime coordinates platform execution.

Responsibilities include:

- startup
- shutdown
- plugin discovery
- capability registration
- validation
- command dispatch

The Runtime owns the execution lifecycle but does not own platform
state directly.

---

# Runtime Context

The Runtime owns a single RuntimeContext.

RuntimeContext contains the shared runtime state and long-lived
platform services.

```
Runtime
    │
    ▼
RuntimeContext
```

The RuntimeContext exists to prevent the Runtime from accumulating
large numbers of dependencies.

---

# RuntimeContext Responsibilities

RuntimeContext owns shared runtime objects.

Current responsibilities include:

- PluginManager
- CommandRegistry
- BlueprintRegistry
- Workspace

Future platform services should also be owned by the RuntimeContext.

The RuntimeContext does not coordinate execution.

---

# PluginManager

PluginManager is responsible for plugin behavior.

Responsibilities include:

- discovering plugins
- loading plugins
- validating plugins

PluginManager delegates discovery to PluginLoader.

```
PluginManager
        │
        ▼
PluginLoader
```

PluginManager provides behavior.

It does not own platform state.

---

# Registries

Registries are passive runtime objects.

Registries own platform state.

They do not coordinate execution.

Current registries include:

- CommandRegistry
- BlueprintRegistry

Future registries may include:

- PluginRegistry
- TemplateRegistry

Registries expose registration and lookup operations.

---

# Workspace

Workspace represents the active project environment.

Typical responsibilities include:

- project root
- template locations
- cache directory
- generated output

Workspace stores environment information only.

---

# Dispatcher

Dispatcher executes commands.

Responsibilities include:

- selecting commands
- invoking commands
- propagating runtime context

Dispatcher should not own runtime state.

---

# Object Graph

```
Application
      │
      ▼
Runtime
      │
      ▼
RuntimeContext
      │
 ┌────┼─────────────────────────────────────┐
 │    │                 │                  │
 ▼    ▼                 ▼                  ▼
PluginManager   CommandRegistry   BlueprintRegistry   Workspace
      │
      ▼
PluginLoader
```

Ownership always flows downward.

---

# Dependency Rules

Dependencies always point downward.

```
Application
      │
      ▼
Runtime
      │
      ▼
RuntimeContext
      │
      ▼
Shared Objects
```

The following rules apply.

Runtime owns RuntimeContext.

RuntimeContext owns managers and registries.

Managers provide behavior.

Registries own state.

Managers must not coordinate the platform.

Registries must not invoke Runtime.

Communication between runtime services should occur through Runtime.

---

# Lifecycle

Runtime executes the following sequence.

```
startup()

↓

discover plugins

↓

register capabilities

↓

validate

↓

dispatch

↓

shutdown()
```

Each phase should be independently testable.

---

# Future Evolution

The RuntimeContext is expected to grow over time.

Possible future runtime objects include:

- Configuration
- EventBus
- Cache
- Logger
- Metrics
- ServiceContainer
- TaskScheduler

New runtime objects should integrate through RuntimeContext without
changing existing ownership rules.

---

# Summary

The Runtime coordinates execution.

The RuntimeContext owns shared runtime objects.

Managers provide behavior.

Registries own state.

Business logic belongs to plugins.

This separation keeps the platform modular, testable, and extensible.
