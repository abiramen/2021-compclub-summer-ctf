#!/usr/bin/python3

# Made by someone at github.com/unswsecuritysociety. Not sure who, but SecSoc is awesome.

import yaml
import glob
import requests
import sys
import argparse
import os
from os.path import basename

class Markdown:
    def __init__(self, filename):
        with open(filename) as f:
            opening = False
            self.front_matter = ''
            self.content = ''
            for i in f:
                if i.rstrip() == '---' and not opening:
                    opening = True
                elif i.rstrip() == '---':
                    opening = False
                    break
                elif opening:
                    if i.rstrip() == '': continue
                    self.front_matter += i
                else: break

            # file ends before second delimiter
            if opening:
                self.content = self.front_matter

            for i in f:
                self.content += i
            self.content = self.content.strip()
            self.front_matter = yaml.safe_load(self.front_matter)

class Challenge:
    def __init__(self, folder):
        self.folder = folder
        # parse main challenge file
        md = Markdown(f'{folder}/challenge.md')

        self.name = md.front_matter['name']
        self.category = md.front_matter['category']
        self.value = md.front_matter['value']
        self.state = md.front_matter.get('state', 'visible')
        self.type = 'standard'

        self.tags = md.front_matter.get('tags', [])
        self.description = md.content
        if 'flags' in md.front_matter:
            self.flags = {'content': md.front_matter['flags'], 'data': None}
        else:
            self.flags = [{
                'content': md.front_matter['flag'],
                'data': md.front_matter.get('flag_case', None)
            }]

        # get filenames
        self.files = glob.glob(f'{folder}/files/*')

        # get hints
        self.hints = []
        for i in glob.glob(f'{folder}/hints/*.md'):
            hint_md = Markdown(i)
            self.hints.append({
                'cost': hint_md.front_matter['cost'],
                'hint': hint_md.content
            })

    def upload(self, s, ctfd_root):
        r = s.post(f'{ctfd_root}/challenges', json={
            'name': self.name,
            'category': self.category,
            'value': self.value,
            'state': self.state,
            'type': self.type,
            'description': self.description
            })

        res = r.json()
        if not res.get('success', False):
            raise IOException(f'Uploading challenge {self.name} failed')
        print(f'Challenge {self.name} added', file=sys.stderr)

        self.id = res['data']['id']

        # add flags
        for i in self.flags:
            # data: 'case_insensitive'
            r = s.post(f'{ctfd_root}/flags', json={
                'challenge': self.id,
                'content': i['content'],
                'data': i['data'],
                'type': 'static'
                })
            print(f'Flag for challenge {self.name} added', file=sys.stderr)

        # add hints if they exist
        for i in self.hints:
            r = s.post(f'{ctfd_root}/flags', json=i)
            print(f'Hint for challenge {self.name} added', file=sys.stderr)

        # add tags if they exist
        for i in self.hints:
            r = s.post(f'{ctfd_root}/tags', json={
                'challenge': self.id,
                'value': i
                })
            print(f'Tag for challenge {self.name} added', file=sys.stderr)

        # add files if they exist
        for i in self.files:
            r = s.post(f'{ctfd_root}/files', files={'file': open(i, 'rb')}, data={'challenge': self.id, 'type': 'challenge'})
            print(f'File for challenge {self.name} added', file=sys.stderr)
            if not res.get('success', False):
                raise IOException(f'Uploading files for challenge {self.name} failed')




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Upload challenges to CTFd.')
    parser.add_argument('ctfd_root', type=str, help='root url of ctfd site')
    parser.add_argument("--force", dest='force', action='store_true', help='wip: force overwriting challenges')
    parser.add_argument("--delta", dest='delta', action='store_true', help='only upload challenges which haven\'t been uploaded')
    args = parser.parse_args()

    ctfd_root = f'{args.ctfd_root}/api/v1'
    api_key = os.getenv("CTFD_TOKEN")

    # create request session
    s = requests.Session()
    s.headers.update({
        'authorization': f'Bearer {api_key}'
    })

    # get remote challenges (wip force)
    r = s.get(f'{ctfd_root}/challenges', headers={'content-type': 'application/json'})
    print(r.json(), file=sys.stderr)
    if not r.ok: sys.exit(1)

    # delta with log
    deployed = set()
    if args.delta:
        log = open('deploy-log.txt', 'r+')
        [deployed.add(i) for i in log.read().strip().split('\n')]
    else:
        log = open('deploy-log.txt', 'w')

    # read local challenges
    for i in glob.glob('*/*/_ctfd/'):
        chal = Challenge(i)
        if chal.folder in deployed: continue

        deployed.add(chal.folder)
        log.write(f'{chal.folder}\n')
        print(chal.folder)
        chal.upload(s, ctfd_root)

    print('All challenges uploaded!', file=sys.stderr)
