# Platform

**Status:** Draft

**Version:** 1.0

**Applies To:** dev-foundation

---

## Purpose

`dev-foundation` is the core platform for building reusable developer
tools.

It provides the runtime, extension system, and shared infrastructure
required by plugins.

The platform remains minimal, extensible, and independent of
domain-specific implementations.

---

## Vision

Build a stable and extensible platform where developer tools are
implemented as reusable plugins instead of standalone applications.

The platform should encourage consistency, code reuse, and long-term
maintainability across the ecosystem.

---

## Responsibilities

The platform provides shared infrastructure, including:

- Plugin discovery and loading
- Runtime lifecycle
- Command registration
- Blueprint registration
- Template management
- Project generation
- Shared platform services

---

## Non-Responsibilities

The platform does **not** implement domain-specific functionality.

Examples include:

- Documentation rendering
- PDF generation
- Docker integration
- FastAPI project logic
- Language-specific generators
- External CLI tools

These responsibilities belong to plugins or external engines.

---

## Core Principles

### Platform First

The platform evolves before plugins.

Common infrastructure should be implemented in the platform before
being reused by plugins.

---

### Minimal Core

Only shared infrastructure belongs in the platform.

Business-specific logic should remain outside the core.

---

### Extensible by Default

New capabilities should be added through plugins whenever possible.

The platform should expose extension points instead of accumulating
features.

---

### Separation of Responsibilities

The platform provides infrastructure.

Plugins provide domain-specific functionality.

External engines perform specialized work.

---

### Convention over Configuration

Prefer consistent conventions before introducing additional
configuration.

A predictable platform is easier to understand and maintain.

---

### Testability

Every public component should be independently testable.

Architecture should encourage isolated unit testing.

---

## Architecture Layers

The ecosystem is organized into three logical layers.

Each layer has a single responsibility and communicates through
well-defined platform contracts.

### Platform

Provides reusable infrastructure.

Components include:

- Runtime
- Registry
- Plugin API
- Blueprint API
- Command API
- Template Engine

---

### Plugins

Plugins extend the platform by implementing domain-specific
functionality.

Examples:

- dev-docbuildr
- dev-fastapi
- Future official plugins
- Third-party plugins

---

### Engines

Plugins may integrate with external engines to perform specialized
work.

Examples:

- docbuildr
- FastAPI
- Docker
- MkDocs

---

## Ecosystem

```text
                 +----------------------+
                 |    dev-foundation    |
                 +----------------------+
                  Runtime / Registries
                           │
                   Platform Contracts
                           │
        ┌──────────────────┴──────────────────┐
        │                                     │
 Official Plugins                    Third-party Plugins
        │                                     │
   dev-docbuildr                     community plugins
        │
   External Engines
        │
 docbuildr / FastAPI / Docker / MkDocs
```

---

## Design Rule

A feature belongs to the platform only if it provides reusable
infrastructure.

If a feature can be implemented as a plugin, it should not be added
to the platform core.

The platform should remain small and stable while plugins evolve
independently.

Platform APIs should remain stable so that plugins rarely require
changes when the platform evolves.

---

## Terminology

**Platform**

: The shared infrastructure that powers the ecosystem.

**Plugin**

: An extension loaded by the platform to provide additional
functionality.

**Blueprint**

: A reusable project definition used during project generation.

**Generator**

: A component responsible for generating project files.

**Engine**

: An external implementation used by plugins to perform specialized
tasks.

**Platform Contract**

: A stable interface that defines how plugins interact with the
platform.

---

## Future Evolution

The platform is designed to support multiple official and third-party
plugins without requiring changes to the core runtime.

Whenever possible, new capabilities should be introduced by extending
existing platform contracts instead of modifying existing behavior.

Maintaining backward compatibility is preferred to introducing
breaking changes.

Platform contracts should evolve through extension rather than
replacement whenever practical.
