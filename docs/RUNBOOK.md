# Execution record and reproduction guide

The portal was used for live operations. These are documented steps, not an automatically deployed template. Use only an explicitly disposable lab account with approved cost coverage.

1. Verify subscription type, remaining credit, expiry, region and current regional prices. Preflight used an existing Free Trial; no upgrade or paid add-on was accepted.
2. Create a dedicated resource group and one Standard StorageV2 account, Hot LRS in North Europe. Disable anonymous blob access, require HTTPS and TLS 1.2, and enable seven-day blob and container soft delete. Keep versioning, change feed and other optional services off for this narrow exercise.
3. Select restricted public network access with default deny. Create the private `recovery-test` container through the management surface. The first contents-list request returned HTTP 403. Management access and data-plane reachability were therefore distinguishable in this run.
4. Add only the current lab client's IPv4 rule and remove the trusted-services bypass. Verify that the container's data-plane listing now succeeds with zero objects. Do not generalize this result to every source, identity or network path.
5. Attempt the prepared canary upload. In this run both file-picker attempts failed to provide a usable selection. Stop the content-recovery test and record it as not executed.
6. Delete the empty test container after confirming soft delete is enabled. Verify it disappears from the active-only view, then select the view including deleted containers and observe `Deleted`.
7. Choose Undelete and Save. Verify `recovery-test` returns as `Active`, with `Private` access and an Azure success notification. Portal last-modified time was 16 October 2026 04:36:03 Europe/Oslo (02:36:03 UTC).
8. Export the final account resource JSON, retaining a private original and publishing only selected sanitized fields. The blob-service retention values come from the separate portal overview, not this account-level JSON.
9. Check the dedicated group's inventory before cleanup: exactly the one lab storage account. Delete that group only and verify Azure success and an empty resource view. Preserve unrelated groups and the existing budget.

Microsoft guidance: [enable and manage container soft delete](https://learn.microsoft.com/en-us/azure/storage/blobs/soft-delete-container-enable) and [portal data authorization](https://learn.microsoft.com/en-us/azure/storage/blobs/authorize-data-operations-portal).

The operation timeline contains multi-hour quota/tool interruptions. It is not a recovery-time objective measurement. Container restoration success is supported by Azure's status and notification; restored file contents are not part of the evidence.
