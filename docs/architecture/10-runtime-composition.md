# Runtime Composition

**Status:** Draft

**Version:** 1.0

**Applies To:** dev-foundation

---

# Purpose

This document defines how the runtime is composed.

Unlike previous documents that define responsibilities and contracts,
this document specifies how the runtime object graph is organized and
how runtime services collaborate during execution.

The runtime composition acts as the blueprint for the implementation.

---

# Design Goals

The runtime should be:

- Simple
- Predictable
- Extensible
- Testable
- Loosely coupled

The runtime should coordinate services instead of implementing
business logic.

---

# Runtime Responsibilities

The Runtime is responsible for coordinating platform execution.

It owns the execution lifecycle and orchestrates all runtime services.

The Runtime should never implement domain-specific behavior.

Responsibilities include:

- startup
- shutdown
- plugin discovery
- capability registration
- validation
- command dispatch

---

# Runtime Context

The Runtime owns a single RuntimeContext.

The RuntimeContext contains long-lived runtime services shared across
the platform.

The Runtime itself should avoid holding many independent service
instances directly.

Instead:

```
Runtime
    │
    ▼
RuntimeContext
```

---

# RuntimeContext Responsibilities

RuntimeContext is responsible for owning platform services.

Typical responsibilities include:

- Plugin management
- Registry access
- Workspace information
- Configuration
- Shared metadata

The RuntimeContext should not contain business logic.

---

# Managers

Managers encapsulate reusable platform services.

Each manager has a single responsibility.

Managers never coordinate the platform.

Only the Runtime coordinates execution.

---

## PluginManager

Responsible for:

- discovering plugins
- loading plugins
- validating plugins

The PluginManager delegates low-level discovery to PluginLoader.

```
PluginManager
        │
        ▼
PluginLoader
```

---

## RegistryManager

Responsible for runtime registries.

Possible registries include:

- Commands
- Plugins
- Blueprints

The RegistryManager owns registry state.

---

## Workspace

Workspace represents the active project environment.

Responsibilities include:

- project root
- templates
- cache
- generated output

Workspace is independent from Runtime execution.

---

# Dispatcher

The Dispatcher is responsible for executing commands.

Responsibilities include:

- selecting commands
- invoking commands
- propagating execution context

The Dispatcher should not own platform state.

---

# Object Graph

The runtime object graph is shown below.

```
Application
      │
      ▼
Runtime
      │
      ▼
RuntimeContext
      │
 ┌────┼───────────────┐
 │    │               │
 ▼    ▼               ▼
Plugin Registry   Workspace
Manager Manager
      │
      ▼
PluginLoader
```

Only Runtime owns RuntimeContext.

Managers do not own each other.

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
Managers
```

Managers should never reference Runtime.

Managers should not depend on one another unless explicitly required.

Communication between managers should occur through Runtime or
RuntimeContext.

---

# Lifecycle

Runtime executes services in the following order.

```
startup()

↓

discover plugins

↓

load plugins

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

The RuntimeContext is expected to grow as the platform evolves.

Possible future services include:

- ConfigurationManager
- EventBus
- ServiceContainer
- TaskScheduler
- CacheManager
- Logger
- Metrics

Adding new services should not require changes to existing managers.

---

# Summary

The Runtime coordinates execution.

The RuntimeContext owns runtime services.

Managers own individual responsibilities.

Business logic belongs to plugins.

This separation keeps the platform small, extensible, and maintainable.
