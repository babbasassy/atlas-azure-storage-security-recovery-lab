# Cost controls and cleanup

Only the existing USD 200 Azure Free Trial was authorized. No own-money spend, Pay-As-You-Go conversion, spending-limit removal, Marketplace item, paid Defender plan or paid backup service was introduced. Budget alerts are notifications, not a hard cap.

## Preflight estimate

The Microsoft Retail Prices API was queried on 15 October 2026 for USD consumption prices, North Europe, General Block Blob v2, Hot LRS. The complete response contained nine meter/tier rows. Selected planning rates:

| Allowance | Price used | Estimated USD |
|---|---|---:|
| 1 GB-month storage | 0.022 per GB-month | 0.0220 |
| 1,000 writes | 0.05 per 10,000 | 0.0050 |
| 1,000 list/create operations | 0.05 per 10,000 | 0.0050 |
| 1,000 reads | 0.004 per 10,000 | 0.0004 |
| 1,000 other operations | 0.004 per 10,000 | 0.0004 |
| 1 GB outbound bandwidth, free allowance ignored | 0.087 per GB | 0.0870 |
| **Conservative planned scenario** | | **0.1198** |

This was a planning estimate, not a bill or enforced limit. No canary data was uploaded. Transaction charges and delayed reporting still prevent a final zero-cost claim. Microsoft documents no activation fee for [container soft delete](https://learn.microsoft.com/en-us/azure/storage/blobs/soft-delete-container-overview), while retained data remains billable.

Sources: [Retail Prices API](https://learn.microsoft.com/en-us/rest/api/cost-management/retail-prices/azure-retail-prices), [bandwidth pricing](https://azure.microsoft.com/en-us/pricing/details/bandwidth/), [Free Trial terms](https://azure.microsoft.com/en-us/pricing/offers/ms-azr-0044p/). Recheck them before reproducing the lab.

## Cleanup and schedule deviation

- Account created: 15 October 2026 at 16:30:17 UTC.
- Intended target: remove resources during the same work session.
- Actual deviation: quota/tool interruptions left the empty account present overnight. Only the empty test container and the service-created `$logs` container were observed; no test payload was uploaded. The account's existence spanned about ten hours.
- Final group inventory: one storage account, `statlasrecovery261015`, in `rg-atlas-storage-20261015`.
- Cleanup confirmed at observation time **16 October 2026 02:41:23 UTC**: Azure reported `Deleted resource group rg-atlas-storage-20261015`; the resource view showed `Showing 0 of 0`.
- No unrelated group was deleted. `NetworkWatcherRG` was not assumed to belong to this lab.
- Post-cleanup portal: trial active; credit displayed as **NOK 1,904.17**, expiry **29 October 2026**, 13 days remaining, month-to-date cost **NOK 0.00**. This is the portal's localized, provisional view, not a new credit purchase or a final invoice.

The failure to meet the same-session target is recorded explicitly. Future resource-bearing exercises should reserve cleanup capacity before starting, stop optional diagnostics when completion becomes uncertain, and prioritize deletion before publication or further project work. No ongoing storage resource is required to reproduce the local evidence checks.
