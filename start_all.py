#!/usr/bin/env python3
"""Power on GNS3 nodes using the controller API (Python standard library only)."""

import argparse
import base64
import json
import os
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--server', default=os.getenv('GNS3_SERVER', 'http://localhost:3080'),
                        help='GNS3 controller URL (default: http://localhost:3080)')
    parser.add_argument('--api-version', choices=('v2', 'v3'), default='v2')
    parser.add_argument('--project', help='Start one project by exact name or UUID, opening it if needed')
    parser.add_argument('--list', action='store_true', help='List projects without starting nodes')
    args = parser.parse_args()
    headers = {'Content-Type': 'application/json'}
    token = os.getenv('GNS3_TOKEN')
    user = os.getenv('GNS3_USER')
    password = os.getenv('GNS3_PASSWORD', '')
    if token:
        headers['Authorization'] = f'Bearer {token}'
    elif user:
        credentials = base64.b64encode(f'{user}:{password}'.encode()).decode()
        headers['Authorization'] = f'Basic {credentials}'
    base = f'{args.server.rstrip("/")}/{args.api_version}'

    def request(path, method='GET'):
        req = Request(base + path, headers=headers, method=method,
                      data=b'{}' if method == 'POST' else None)
        try:
            with urlopen(req, timeout=120) as response:
                body = response.read()
                return json.loads(body) if body else None
        except HTTPError as error:
            raise RuntimeError(f'GNS3 returned HTTP {error.code} for {method} {path}. '
                               'Check the server URL, API version, and authentication.') from error
        except (URLError, TimeoutError) as error:
            raise RuntimeError(f'Cannot reach GNS3 at {args.server}: {error}. '
                               'Start the GNS3 server or set --server.') from error

    projects = request('/projects')
    if args.list:
        for project in projects:
            print(f'{project["project_id"]}  {project["name"]}  ({project["status"]})')
        return 0
    if args.project:
        selected = [p for p in projects if args.project in (p['name'], p['project_id'])]
        if len(selected) != 1:
            raise RuntimeError('Project not found or name is ambiguous. Use --list and select a UUID.')
    else:
        selected = [p for p in projects if p['status'] == 'opened']
        if not selected:
            raise RuntimeError('No open projects. Open your topology in GNS3 or use --project NAME.')

    failures = 0
    for project in selected:
        path = '/projects/' + quote(project['project_id'], safe='')
        try:
            if project['status'] != 'opened':
                request(path + '/open', 'POST')
            nodes = request(path + '/nodes')
            if not nodes:
                print(f'{project["name"]}: no nodes to start.')
                continue
            request(path + '/nodes/start', 'POST')
            nodes = request(path + '/nodes')
            failed = [n for n in nodes if n['status'] != 'started']
            print(f'{project["name"]}: {len(nodes) - len(failed)}/{len(nodes)} nodes started.')
            for node in failed:
                print(f'  {node["name"]}: {node["status"]}', file=sys.stderr)
            failures += bool(failed)
        except RuntimeError as error:
            failures += 1
            print(f'{project["name"]}: {error}', file=sys.stderr)
    return 1 if failures else 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (RuntimeError, ValueError, KeyError) as error:
        print(f'Error: {error}', file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        sys.exit(130)
