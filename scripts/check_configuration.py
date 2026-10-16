"""Offline verification of a sanitized snapshot. Makes no Azure requests."""
import argparse
import copy
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def check(account):
    p = account['properties']
    n = p['networkAcls']
    return {
        'standard_lrs': account['sku']['name'] == 'Standard_LRS',
        'storage_v2': account['kind'] == 'StorageV2',
        'north_europe': account['location'] == 'northeurope',
        'https_required': p['supportsHttpsTrafficOnly'] is True,
        'tls_1_2': p['minimumTlsVersion'] == 'TLS1_2',
        'anonymous_blob_access_disabled': p['allowBlobPublicAccess'] is False,
        'default_deny': n['defaultAction'] == 'Deny',
        'no_service_bypass': n['bypass'] == 'None',
        'single_redacted_client_rule': n['ipRules'] == [
            {'value': 'REDACTED_CLIENT_IPV4', 'action': 'Allow'}],
        'no_cross_tenant_replication': p['allowCrossTenantReplication'] is False,
        'microsoft_managed_blob_encryption': p['encryption']['keySource'] == 'Microsoft.Storage'
            and p['encryption']['services']['blob']['enabled'] is True,
        'no_private_endpoints': p['privateEndpointConnections'] == [],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--self-test', action='store_true')
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    data = json.loads((ROOT / 'evidence/account-final.sanitized.json').read_text())
    checks = check(data)
    mutations = {}
    if args.self_test:
        cases = [
            ('https_optional', ('properties', 'supportsHttpsTrafficOnly'), False, 'https_required'),
            ('anonymous_enabled', ('properties', 'allowBlobPublicAccess'), True, 'anonymous_blob_access_disabled'),
            ('default_allow', ('properties', 'networkAcls', 'defaultAction'), 'Allow', 'default_deny'),
            ('bypass_added', ('properties', 'networkAcls', 'bypass'), 'AzureServices', 'no_service_bypass'),
            ('extra_client', ('properties', 'networkAcls', 'ipRules'), [
                {'value': 'REDACTED_CLIENT_IPV4', 'action': 'Allow'},
                {'value': '192.0.2.1', 'action': 'Allow'}], 'single_redacted_client_rule'),
        ]
        for name, path, value, expected in cases:
            changed = copy.deepcopy(data)
            node = changed
            for key in path[:-1]:
                node = node[key]
            node[path[-1]] = value
            mutations[name] = check(changed)[expected] is False
    report = {'generatedAtUtc': datetime.now(timezone.utc).isoformat(),
              'mode': 'offline saved-configuration check; no Azure requests',
              'configurationChecks': checks, 'mutationsDetected': mutations,
              'passed': all(checks.values()) and all(mutations.values())}
    if args.report:
        args.report.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, indent=2))
    raise SystemExit(0 if report['passed'] else 1)


if __name__ == '__main__':
    main()
