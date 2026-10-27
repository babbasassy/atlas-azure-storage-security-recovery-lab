# Azure lab closeout — 26 October 2026

A read-only portal review at approximately **19:25–19:33 UTC on 26 October** confirmed that the four disposable ATLAS resource groups were absent. This review covers the earlier SOC, Policy, Network and Storage labs. Documentation was completed on 27 October after an interruption; the observations below are from 26 October.

| Check | Actual observation |
|---|---|
| Resource groups | Subscription list showed 1 of 1: the pre-existing `NetworkWatcherRG` only |
| All resources | All types/regions/groups showed 1 of 1: `NetworkWatcher_northeurope` only |
| Own lab groups | `rg-atlas-soc-20261010`, `rg-atlas-policy-20261012`, `rg-atlas-network-20261014` and `rg-atlas-storage-20261015` absent |
| Activity-log export | Subscription diagnostic settings showed **No diagnostic settings defined** |

No deletion was required during this review. The pre-existing Network Watcher resource was preserved. No Azure resources, log exports or permissions were changed. No further Azure deployments are needed for the remaining local portfolio work.

The original Storage limits still apply: the recovered container was empty; file upload failed and no blob/file restoration was demonstrated. An interruption previously left the empty account allocated for about ten hours before confirmed deletion on 16 October. See the [original cost and cleanup record](COST-AND-CLEANUP.md).

## Evidence and boundaries

These are transcribed technical observations from the authenticated Azure portal, checked against the existing private account/subscription record. Private screenshots and accessibility snapshots were retained for the resource inventory and diagnostic settings. Account identifiers, billing/credit details and unredacted portal captures are excluded from this public repository.

This closeout verifies the observed absence of the owned labs and subscription activity-log export at that time. It is not a new Azure lab, a tenant-wide security audit, or a claim that another user's retained resources were reviewed or removed. Local/synthetic cyber projects continue without new cloud resource creation.
